from airflow.decorators import dag, task
from airflow.models import Variable
from airflow.utils.dates import days_ago

from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from google.cloud import storage

from io import BytesIO
from datetime import timedelta

# Constants
SHAREPOINT_SITE = "https://liveeduisegiunl.sharepoint.com/sites/sadeeqapps"
FOLDER_PATH = "/sites/sadeeqapps/Shared Documents/flat_files"
GCS_BUCKET = "sharepoint_source"
GCS_PREFIX = "input_folder"
PROJECT_ID = "sadeeq-demo-01"

@dag(
    dag_id="sharepoint_files_transfer",
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
    tags=["sharepoint", "gcs", "composer3"],
    default_args={
        "retries": 1,
        "retry_delay": timedelta(minutes=5)
    },
)
def sharepoint_to_gcs_dag():

    @task()
    def transfer_files():
        # Load SharePoint credentials from Airflow environment variables
        username = Variable.get("sharepoint_username")
        password = Variable.get("sharepoint_password")

        # Authenticate with SharePoint
        ctx = ClientContext(SHAREPOINT_SITE).with_credentials(
            UserCredential(username, password)
        )
        folder = ctx.web.get_folder_by_server_relative_url(FOLDER_PATH)
        files = folder.files
        ctx.load(files)
        ctx.execute_query()

        if not files:
            raise Exception("No files found in SharePoint folder.")

        # Set up GCS client
        gcs_client = storage.Client(project=PROJECT_ID)
        bucket = gcs_client.bucket(GCS_BUCKET)

        # Process each file
        for file in files:
            file_name = file.properties["Name"]
            file_url = f"{FOLDER_PATH}/{file_name}"

            # Download file to memory
            buffer = BytesIO()
            ctx.web.get_file_by_server_relative_url(file_url).download(buffer).execute_query()

            # Upload to GCS
            blob_path = f"{GCS_PREFIX}/{file_name}"
            blob = bucket.blob(blob_path)
            blob.upload_from_file(buffer, rewind=True)

            print(f"✅ Uploaded: {file_name} to gs://{GCS_BUCKET}/{blob_path}")

    transfer_files()

sharepoint_to_gcs_dag()
