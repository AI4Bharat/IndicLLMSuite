import json
import random
import requests
import firebase_admin
import streamlit as st
from datetime import datetime
from firebase_admin import firestore, credentials, auth
import os 

# initialize authentication with Firebase
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "url_verification_key.json"
cred = credentials.Certificate("url_verification_key.json")


def initialize_app():
    try:
        app = firebase_admin.initialize_app(cred)
    except:
        pass



# initialize Firestore client
db = firestore.Client(project="setu-dashboard", database="url-verification")



# configure Streamlit webpage
st.set_page_config(page_title="URL Validator System", page_icon=":link:", layout="wide")



# create session variables if they don't exist
if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = None
if "username" not in st.session_state:
    st.session_state["username"] = None



def register_user(email, password, display_name):
    """
    This function is for registering a user given an email, password and username
    """
    try:
        check_user_exists = db.collection("users").document(display_name).get().to_dict()

        if check_user_exists == None:
            # if user does not exist, create one
            user = auth.create_user(email=email, password=password, display_name=display_name)
            st.success(f"Successfully registered user {display_name} with email {email} !")
            return user

        if check_user_exists != None:
            # if user already exists, then return an error
            st.error("Username already exists")
            return None

    except Exception as e:
        st.error(f"{e}, if you have already registered on **Setu Dashboard**, please login")
        return None



def login_user(email, password):
    """
    This function logs in a user given an email and password
    """
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyB9z1dFQ-LfOkMQ0r3wcwl_bVbYiT-B-bc"
    payload = {"email": email, "password": password, "returnSecureToken": True}
    response = requests.post(url, data=json.dumps(payload)).text
    return response




# If the user is authenticated
if st.session_state["authentication_status"] == True:
    try:
        # Retrieve user data from database
        user_data = db.collection("users").document(st.session_state["username"]).get().to_dict()

        # Get the total number of verified URLs by the user
        total_links_done = user_data["n_urls_verified"]

    except:
        # If user data is not found, set default data in the database for the user
        user_data = db.collection("users").document(st.session_state["username"]).set({"n_urls_verified": 0, "url_ids_verified": []})

        # Reset the total number of verified URLs
        total_links_done = 0

    
    
    print(st.session_state["username"])
    st.title("URL Validator System :link:")
    st.markdown(
        f"Welcome **{st.session_state['username']}**! You have verified **{total_links_done}** URLs so far."
    )
    st.write("")


    #Language mapping
    lang_map = {
        "Hindi": "hi",
        "Assamese": "as",
        "Bengali": "bn",
        "Gujarati": "gu",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Marathi": "mr",
        "Nepali": "ne",
        "Odia": "or",
        "Punjabi": "pa",
        "Sanskrit": "sa",
        "Telugu": "te",
        "Urdu": "ur",
        "Tamil": "ta",
        "Sindhi": "sd",
    }


    #Language count
    count_dict = {
        "sa": 107,
        "hi": 600,
        "gu": 600,
        "sd": 600,
        "mr": 600,
        "as": 271,
        "te": 600,
        "ur": 600,
        "ta": 600,
        "bn": 600,
        "or": 600,
        "ml": 600,
        "ne": 600,
        "kn": 600,
        "pa": 600,
    }


    #Language list
    lang_list = [
        "Assamese",
        "Bengali",
        "Gujarati",
        "Kannada",
        "Malayalam",
        "Marathi",
        "Nepali",
        "Odia",
        "Hindi",
        "Punjabi",
        "Sanskrit",
        "Tamil",
        "Telugu",
        "Urdu",
        "Sindhi",
    ]


    selected_lang = "sangraha_v2"

    urls_info = db.collection("urls_info").document("urls_done").get().to_dict()
    done_url_ids = urls_info["url_ids"]

    random_idx = random.randint(0, 472)

    url_id = f"{selected_lang}_{random_idx}"
    lang_done_flag = False


    try:
        if url_id in done_url_ids:
            with st.spinner("Finding URLs to validate..."):
                while url_id in done_url_ids:
                    random_idx = random.randint(0, 472)
                    url_id = f"{selected_lang}_{random_idx}"

    except:

        try:
            if url_id in done_url_ids:
                with st.spinner("Finding URLs to validate..."):
                    while url_id in done_url_ids:
                        random_lang = random.choice(lang_list)
                        selected_lang = lang_map[random_lang]
                        lang_count = count_dict[selected_lang]
                        random_idx = random.randint(0, lang_count)
                        url_id = f"{selected_lang}_{random_idx}"

        except:
            lang_done_flag = True
            st.error(
                "No more urls to validate in this language. Please select another language."
            )

    if lang_done_flag != True:
        print(f"URL ID: {url_id}")
        fetched_url = db.collection("urls").document(url_id).get().to_dict()
        print(fetched_url)
        url = fetched_url["url"]

        styled_link = f'<a href="{url}" style="text-decoration: none; color: #ss; font-height: 100px;">{f"{url}"}</a>'

        print(fetched_url)
        url = fetched_url["url"]
        st.markdown(
            """
                ### Website to validate
                """
        )
        st.markdown(styled_link, unsafe_allow_html=True)
        st.caption("doc metadata")
        st.write(fetched_url)
        st.write("")
        st.write("")

        st.markdown(
            """
                    ### Feedback Section
                    """
        )
        st.write("")
        tab1, tab2 = st.tabs(["Accept", "Reject"])

        with tab1:
            with st.form(key="accept_form", clear_on_submit=True):
                st.markdown("""#### What is the category of this website ? """)
                st.caption("Select one of the below options")

                st.write("")

                goverment = st.checkbox("Government")
                education = st.checkbox("Education")
                news = st.checkbox("News")
                blog = st.checkbox("Blog")
                shopping = st.checkbox("Shopping")
                religion = st.checkbox("Religion/Spirituality")

                others_accept = st.text_input(
                    "Other Categories (if none of the above)", key="others_accept"
                )
                st.divider()
                lang_dropdown = st.selectbox(
                    "Select the language of the website",
                    [
                        "Assamese",
                        "Bengali",
                        "Gujarati",
                        "Kannada",
                        "Malayalam",
                        "Marathi",
                        "Nepali",
                        "Odia",
                        "Hindi",
                        "Punjabi",
                        "Sanskrit",
                        "Tamil",
                        "Telugu",
                        "Urdu",
                        "Sindhi",
                    ],
                    index=None,
                )

                st.write("")

                accept_form = st.form_submit_button("Submit")

                feedback_accept = None

                if goverment:
                    feedback_accept = {"accept": "Government"}
                elif education:
                    feedback_accept = {"accept": "Education"}
                elif news:
                    feedback_accept = {"accept": "News"}
                elif blog:
                    feedback_accept = {"accept": "Blog"}
                elif shopping:
                    feedback_accept = {"accept": "Shopping"}
                elif religion:
                    feedback_accept = {"accept": "Religion/Spirituality"}
                elif others_accept:
                    feedback_accept = {"accept": others_accept}

                if accept_form:
                    if feedback_accept is not None and lang_dropdown is not None:
                        accept_feedback_dict = feedback_accept
                        done_url_ids.append(url_id)

                        user_done_urls = (
                            db.collection("users")
                            .document(st.session_state["username"])
                            .get()
                            .to_dict()["url_ids_verified"]
                        )
                        user_done_urls.append(url_id)

                        db.collection("urls_info").document("urls_done").update(
                            {"url_ids": done_url_ids}
                        )

                        db.collection("urls").document(url_id).set(
                            {
                                "feedback": accept_feedback_dict,
                                "verified": "True",
                                "url": url,
                                "submitted_by": st.session_state["username"],
                                "timestamp": datetime.now(),
                                "language": lang_dropdown,
                            }
                        )

                        db.collection("users").document(
                            st.session_state["username"]
                        ).update(
                            {
                                "n_urls_verified": total_links_done + 1,
                                "url_ids_verified": user_done_urls,
                            }
                        )

                        with st.spinner("Loading New task..."):
                            import time

                            time.sleep(2)
                            st.success("URL Accepted Successfully")
                            st.rerun()
                    else:
                        st.warning(
                            "Please select a category and the language of the website ⚠️"
                        )


        with tab2:
            with st.form(key="reject_form", clear_on_submit=True):
                st.markdown("""#### What is the reason for rejection ? """)
                st.caption("Select one of the below options")

                st.write("")

                not_loading = st.checkbox("Website not loading")
                mtc = st.checkbox("Machine Translated Content")
                nil = st.checkbox(
                    "Non Indic Language content (like chinese, french, etc)"
                )
                ac = st.checkbox("Adult Content")

                others_reject = st.text_input(
                    "Other Reasons (if none of the above)", key="others_reject"
                )

                st.write("")

                reject_form = st.form_submit_button("Submit")

                feedback_reject = None

                if not_loading:
                    feedback_reject = {"reject": "Website not loading"}
                elif mtc:
                    feedback_reject = {"reject": "Machine Translated Content"}
                elif ac:
                    feedback_reject = {"reject": "Adult Content"}
                elif others_reject:
                    feedback_reject = {"reject": others_reject}

                if reject_form:
                    if feedback_reject is not None:
                        reject_feedback_dict = feedback_reject
                        done_url_ids.append(url_id)

                        user_done_urls = (
                            db.collection("users")
                            .document(st.session_state["username"])
                            .get()
                            .to_dict()["url_ids_verified"]
                        )
                        user_done_urls.append(url_id)

                        db.collection("urls_info").document("urls_done").update(
                            {"url_ids": done_url_ids}
                        )

                        db.collection("urls").document(url_id).set(
                            {
                                "feedback": reject_feedback_dict,
                                "verified": "True",
                                "url": url,
                                "submitted_by": st.session_state["username"],
                                "timestamp": datetime.now(),
                            }
                        )

                        db.collection("users").document(st.session_state["username"]).update(
                            {"n_urls_verified": total_links_done + 1, "url_ids_verified": user_done_urls}
                        )

                        with st.spinner("Loading New task..."):

                            time.sleep(2)
                            st.success("URL Accepted Successfully")
                            st.rerun()
                    else:
                        st.warning("Please select a reason for rejection ⚠️")



elif st.session_state["authentication_status"] is None:
    # If the user is not authenticated
    col1, col2, col3 = st.columns(3)

    with col2:
        st.markdown("# Login to URL Verification :link:")
        with st.form(key="login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submit_button = st.form_submit_button(label="Login", disabled=False)

            if submit_button:
                try:
                    auth_user = eval(
                        login_user(email, password).replace("true", "True")
                    )
                    st.session_state["username"] = auth_user["displayName"]
                    print(auth_user)

                    if auth_user["registered"] == True:
                        st.session_state["authentication_status"] = True
                        print(st.session_state["authentication_status"])
                        st.session_state["username"] = auth_user["displayName"]
                        st.rerun()

                    else:
                        st.error("Error logging in")

                except Exception as e:
                    st.error(f"Username/password is incorrect")

        st.warning("Please enter your email and password")

        register = st.button("Register")

        if register:
            st.session_state["register"] = True
            st.session_state["authentication_status"] = False
            st.rerun()



elif st.session_state["register"]:
    # If the user has navigated to the register page
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("# Register to  URL Verification :link:")
        with st.form(key="register_form"):
            username = st.text_input("Username")
            email = st.text_input("Email")
            password = st.text_input(
                "Password",
                type="password",
                help="Password must be at least 6 characters long",
            )

            submit_button = st.form_submit_button(label="Register", disabled=False)

        st.text(" ")
        st.text(" ")

        back_to_login = st.button("Back to login")

        if back_to_login:
            st.session_state["register"] = False
            st.session_state["authentication_status"] = None
            st.rerun()

        if submit_button:
            user = register_user(email, password, username)
