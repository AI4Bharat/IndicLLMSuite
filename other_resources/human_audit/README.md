# Setu Audit ⚒️: Portal for Data Audit

This contains the code for the setu dashboard. The dashboard is a [Streamlit](https://streamlit.io/) based web application that allows users to audit cleaned Web and PDF extracted documents.

![Setu-audit](https://github.com/AI4Bharat/IndicLLMSuite/assets/31161768/f457aec8-01a2-41a1-bff0-fc41922bccdb)


<br>

## Functionality

1. **Feedback**: Users can provide feedback on the cleaned document. The feedback is stored in a Firestore database.
2. **Data Visualization**: The dashboard provides one stop visualization for ease. The visualizations include:
    - The Webpage which was scraped, alongside the extracted and cleaned text
    - The PDF's extracted and cleaned text
3. **User Authentication**: The dashboard uses Firebase authentication to authenticate users. Only authenticated users can provide feedback.

<br>

## Pre-requisites
1. **Google Cloud Account**: The dashboard uses [Google Cloud](https://console.cloud.google.com/) Firestore to store feedback data. You will need to have a Google Cloud account and a Firestore database to run the dashboard.
2. **Firebase Project**: The dashboard uses [Firebase authentication](https://firebase.google.com/docs/auth) to authenticate users. You will need to have a Firebase project and a service account key to run the dashboard.
4. **Google Cloud SDK**: If you want to deploy the dashboard to the [Google Cloud App Engine](https://cloud.google.com/appengine/?hl=en), you will need to install the Google Cloud SDK installed on your machine.
5. **Streamlit** : The dashboard is built using the Streamlit framework.
6. **Docker** (Optional): The dashboard can be run in a Docker container. You will need to have Docker installed on your machine to run the dashboard in a container.

<br>

## Setup

To run the dashboard, you will need to have a Firebase service account key. This key should be stored in the `base` directory as `serviceAccountKey.json`.

```bash
docker build -t <target-name> . 
docker run <target-name> 
```

If you want to deploy to the Google cloud App engine, install the [gcloud cli](https://cloud.google.com/sdk/docs/install) and run the following command:

```bash
gcloud app deploy
```

To run the app locally, run the following command:

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
