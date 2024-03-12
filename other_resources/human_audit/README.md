# Setu Dashboard ⚒️: 2-step verification for Setu pipeline outputs

This repository contains the code for the setu dashboard. The dashboard is a web application that allows users to provide feedback on the outputs of the Setu Data cleaning pipeline. The dashboard is built using the [Streamlit](https://streamlit.io/) framework.

<br>

## Functionality

1. **Feedback**: Users can provide feedback on the outputs of the Setu data cleaning pipeline via a form. The feedback is stored in a Firestore database.
2. **Data Visualization**: The dashboard provides visualizations of the feedback data. The visualizations include:
    - The Webpage which was scraped, alongside the filtered text
    - The PDF's extracted and filtered text
3. **User Authentication**: The dashboard uses Firebase authentication to authenticate users. Only authenticated users can provide feedback, user-wise feedback is stored in the database.

<br>

## Pre-requisites
1. **Google Cloud Account**: The dashboard uses [Google Cloud](https://console.cloud.google.com/) Firestore to store feedback data. You will need to have a Google Cloud account and a Firestore database to run the dashboard.
2. **Firebase Project**: The dashboard uses [Firebase authentication](https://firebase.google.com/docs/auth) to authenticate users. You will need to have a Firebase project and a service account key to run the dashboard.
3. **Service Account Key**: The dashboard uses a service account key to authenticate with Google Cloud Firestore. You will need to have a service account key to run the dashboard.
4. **Google Cloud SDK**: If you want to deploy the dashboard to the [Google Cloud App Engine](https://cloud.google.com/appengine/?hl=en), you will need to have the Google Cloud SDK installed on your machine.
5. **Anaconda** : The dashboard is built using the Streamlit framework. You will need to have Anaconda installed on your machine to run the dashboard.
6. **Docker**: The dashboard can be run in a Docker container. You will need to have Docker installed on your machine to run the dashboard in a container.

<br>

## Setup

To run the dashboard, you will need to have a Firebase service account key. This key should be stored in the `setu-dashboard` directory as `serviceAccountKey.json`.

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
conda create -n setu_dashboard python=3.9
conda activate setu_dashboard

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
