# sharepoint-to-gcs.py
Using Cloud Composer (Apache Airflow) to pull blob files (e.g csv) from Sharepoint File System into Google Cloud Storage (GCS)
---
Here is my Sharepoint Site. Notice the folder named "flat_files", and it contents:
<img width="2055" alt="image" src="https://github.com/user-attachments/assets/eaa59373-c300-454e-9fb6-667c8cb51461" />


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

#
