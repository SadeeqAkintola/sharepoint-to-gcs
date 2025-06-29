# sharepoint-to-gcs.py
Using Cloud Composer (Apache Airflow) to pull blob files (e.g csv) from Sharepoint File System into Google Cloud Storage (GCS)
---
Here is my Sharepoint Site. Notice the folder named "flat_files", and it contents:
<img width="2055" alt="image" src="https://github.com/user-attachments/assets/eaa59373-c300-454e-9fb6-667c8cb51461" />

## Set up the destination folder on Google Cloud Storage: _sharepoint_source --> input_folder_:
<img width="2055" alt="image" src="https://github.com/user-attachments/assets/670e3363-6335-4eab-99e4-93ab9765b1f5" />

## Setting up Apache Airflow on Google Cloud Composer...
<img width="2055" alt="image" src="https://github.com/user-attachments/assets/fbc08c86-6a14-471c-85c3-2130f1b2c12e" />

## What you see once your environment has been provisioned 
<img width="2055" alt="image" src="https://github.com/user-attachments/assets/827384a1-d649-4dcf-a7bc-19bccca37e02" />

## Install the neccessary packages on Cloud Composer: _office365-rest-python-client_ and _google-cloud-storage_
<img width="2055" alt="image" src="https://github.com/user-attachments/assets/eac4a585-154c-41bd-b0f5-3e37e83e6bb2" />

## Open the Dag Folder and place the _sharepoint-to-gcs.py_ file:
<img width="2055" alt="image" src="https://github.com/user-attachments/assets/a28c8b31-c462-4ef2-90b9-f01a2d325d17" />

Wait for a few minutes for the file to be available on the Airflow UI.

## Launch the Airflow UI:
<img width="2055" alt="image" src="https://github.com/user-attachments/assets/f006a298-309d-4630-b15b-88fb4e03fcd0" />

## In the Airflow UI, under Admin >> Variables, store your Sharepoint site credentials such as Username/email and password. This will be stored securely for the airflow dag to consume at runtime:
<img width="2055" alt="image" src="https://github.com/user-attachments/assets/1eac4686-a977-41a8-97f6-a0ed22c223b6" />


## Click on the _sharepoint-to-gcs_ dag and run the dag:
<img width="2055" alt="image" src="https://github.com/user-attachments/assets/0eb7ddbb-6757-489b-bb3a-0e1aec4b3953" />

## When the dag run is successful, you will see the files already pushed into the gcs bucket (input folder):
<img width="2055" alt="image" src="https://github.com/user-attachments/assets/5c8051a9-38d0-4336-adcc-c883f49d38d3" />

---

# End.
