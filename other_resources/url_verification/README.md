# URL Verification Portal

Credits: [@Sshubam](https://github.com/Sshubam)

This contains the code for creating a simple portal for verifying a website's contents before scraping. 

<p align="left">
  <img src="https://github.com/AI4Bharat/IndicLLMSuite/assets/31161768/6ad272ed-142b-4b62-af48-8b268405eb38" alt="Reject" width="45%" />
  <img src="https://github.com/AI4Bharat/IndicLLMSuite/assets/31161768/b697dfda-57e0-44b6-a3e0-ce48987d34d4" alt="Accept" width="45%" /> 
</p>




## Functionality

1. **User Authentication**: Users can register and login to the website, using Firebase Authentication.
2. **Website verification**: Users will be displayed a random website for verification.
3. **Feedback**: The Users have to verify the website for quality and either accept or reject it with an appropriate reason.


## Pre-requisites
1. **Google Cloud Account**: The dashboard uses [Google Cloud](https://console.cloud.google.com/) Firestore to store feedback data. You will need to have a Google Cloud account and a Firestore database to run the dashboard.
2. **Firebase Project**: The dashboard uses [Firebase authentication](https://firebase.google.com/docs/auth) to authenticate users. You will need to have a Firebase project and a service account key to run the dashboard.
4. **Google Cloud SDK**: If you want to deploy the dashboard to the [Google Cloud App Engine](https://cloud.google.com/appengine/?hl=en), you will need to have the Google Cloud SDK installed on your machine.
5. **Streamlit** : The dashboard is built using the Streamlit framework. You will need to have Streamlit installed on your environment to run the dashboard.
6. **Docker** (Optional) : The dashboard can be run as a Docker container. You will need to have Docker installed on your machine to run the dashboard in a container.

<br>

## Setup

To run the application, you will need to have a Firebase service account key. This key should be stored in the `base` directory as `serviceAccountKey.json`.

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
