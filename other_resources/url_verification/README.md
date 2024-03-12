# 2-step verification for verifying a website's contents before scraping

Credits: [@Sshubam](https://github.com/Sshubam)

This repository contains a simple 2-step verification process for verifying a website's contents before scraping. 

## Functionality

1. **User Authentication**: Users can register and login to the website, using Firebase Authentication.
2. **Website verification**: Users will be displayed an IFRAME of a random website for verification.
3. **Feedback**: Users can provide feedback on the website's contents, including a "accept" or "reject" tab where they categorize the website into a categoary such as "news", "blog", "e-commerce", etc. or provide a reason for rejection.The feedback is stored in a Firebase Firestore database along with the metadata.


## Pre-requisites
1. **Google Cloud Account**: The dashboard uses [Google Cloud](https://console.cloud.google.com/) Firestore to store feedback data. You will need to have a Google Cloud account and a Firestore database to run the dashboard.
2. **Firebase Project**: The dashboard uses [Firebase authentication](https://firebase.google.com/docs/auth) to authenticate users. You will need to have a Firebase project and a service account key to run the dashboard.
3. **Service Account Key**: The dashboard uses a service account key to authenticate with Google Cloud Firestore. You will need to have a service account key to run the dashboard.
4. **Google Cloud SDK**: If you want to deploy the dashboard to the [Google Cloud App Engine](https://cloud.google.com/appengine/?hl=en), you will need to have the Google Cloud SDK installed on your machine.
5. **Anaconda** : The dashboard is built using the Streamlit framework. You will need to have Anaconda installed on your machine to run the dashboard.
6. **Docker**: The dashboard can be run in a Docker container. You will need to have Docker installed on your machine to run the dashboard in a container.

<br>

## Setup

To run the application, you will need to have a Firebase service account key. This key should be stored in the root directory as `serviceAccountKey.json`.

```bash
docker build -t <target-name> . 
docker run <target-name> 
```

If you want to deploy to the Google cloud App engine, install the [gcloud cli](https://cloud.google.com/sdk/docs/install) and run the following command:

```bash
gcloud app deploy
```

Akter to run the app locally, run the following command:

```bash
conda create -n url_verification python=3.9
conda activate url_verification

pip install -r requirements.txt
streamlit run app.py
```
<br>
Getting <span style="color:red">DefaultCredentialsError</span> ?

<br>

You need to set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the service account key. You can do this by running the following command:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/serviceAccountKey.json"
```
