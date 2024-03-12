import json
import os
import random
import requests
import firebase_admin
import streamlit as st
from firebase_admin import firestore, credentials, auth
import os


#Set your environment variable to the path of your service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key2.json"

st.set_page_config(page_title="Setu", page_icon="favicon-32x32.ico", layout="wide")

#Enter the path to your service account key
cred = credentials.Certificate("./key2.json")

try:
    app = firebase_admin.initialize_app(cred)
except:
    pass

db = firestore.Client(project="setu-dashboard")


if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = None


def get_doc():

    #Languages mapping
    languages = [
        "gujarati",
        "oriya",
        "dogri",
        "punjabi",
        "malayalam",
        "hindi",
        "manipuri",
        "konkani",
        "urdu",
        "telugu",
        "maithili",
        "sanskrit",
        "assamese",
        "kashmiri",
        "english",
        "kannada",
        "tamil",
        "sindhi",
        "santhali",
        "marathi",
        "nepali",
        "bodo",
        "bengali",
    ]

    random_language = random.choice(languages)


    #Language document count
    lang_count_dict = {
        "gujarati": 5000,
        "oriya": 5000,
        "dogri": 12,
        "punjabi": 5000,
        "malayalam": 5000,
        "hindi": 5000,
        "manipuri": 882,
        "konkani": 5000,
        "urdu": 5000,
        "telugu": 5000,
        "maithili": 5000,
        "sanskrit": 5000,
        "assamese": 5000,
        "kashmiri": 2,
        "english": 5000,
        "kannada": 5000,
        "tamil": 5000,
        "sindhi": 5000,
        "santhali": 110,
        "marathi": 5000,
        "nepali": 5000,
        "bodo": 2930,
        "bengali": 5000,
    }


    random_idx = random.randint(1, lang_count_dict[random_language])



    try:
        done_docs = (
            db.collection(f"{random_language}_submissions")
            .document("docs_done")
            .get()
            .to_dict()["idx_done"]
        )
    except:
        done_docs = []
        db.collection(f"{random_language}_submissions").document("docs_done").set(
            {"idx_done": []}
        )



    if random_idx in done_docs:
        while random_idx in done_docs:
            random_idx = random.randint(0, lang_count_dict[random_language] - 1)
    print("*************")
    print(random_idx)
    print(random_language)
    doc = (
        db.collection("data")
        .document(random_language)
        .collection(f"index_{random_idx}")
        .get()[0]
        .to_dict()
    )



    text = doc["text"]
    doc_id = doc["doc_id"]
    url = doc["url"]
    uncleaned_text = doc["uncleaned_text"]
    source = doc["source"]
    language = doc["language"]
    lid = doc["LID"]

    return (
        lid,
        random_idx,
        text,
        doc_id,
        url,
        uncleaned_text,
        source,
        language,
        doc,
        done_docs,
    )



def get_doc_pdf(lang: str):
    """
    Randomly selects a PDF document from a specified language 
    collection and returns its information if it has not been already returned in a previous attempt.
    """

    # Initialize language document count
    lang_count_dict_pdf = {
        "gujarati": 5000,
        "oriya": 5000,
        "dogri": 5000,
        "punjabi": 5000,
        "malayalam": 5000,
        "hindi": 5000,
        "manipuri": 5000,
        "konkani": 5000,
        "urdu": 5000,
        "telugu": 5000,
        "maithili": 5000,
        "sanskrit": 5000,
        "assamese": 5000,
        "kashmiri": 5000,
        "english": 5000,
        "kannada": 5000,
        "tamil": 5000,
        "sindhi": 5000,
        "santhali": 5000,
        "marathi": 5000,
        "nepali": 5000,
        "bodo": 5000,
        "bengali": 5000,
    }
    # Generate random index
    random_idx = random.randint(1, lang_count_dict_pdf[lang])

    # Get list of processed documents
    pdf_done_docs = (
        db.collection(f"{lang}_pdf_submissions")
        .document("docs_done")
        .get()
        .to_dict()["idx_done"]
    )

    # Ensure the selected document is not processed
    if random_idx in pdf_done_docs:
        while random_idx in pdf_done_docs:
            random_idx = random.randint(1, lang_count_dict_pdf[lang] - 1)

    print("*************")
    print(f"PDF_RANDOM_IDX : {random_idx}")
    print(lang)
    # Get document data
    pdf_doc = (
        db.collection("pdf_data")
        .document(lang)
        .collection(f"index_{random_idx}")
        .get()[0]
        .to_dict()
    )

    # Unpack document data
    text = pdf_doc["text"]
    doc_id = pdf_doc["doc_id"]
    url = pdf_doc["url"]
    id = pdf_doc["id"]
    uncleaned_text = pdf_doc["uncleaned_text"]
    source = pdf_doc["source"]
    language = pdf_doc["language"]
    pdf_name = pdf_doc["pdf_name"]
    page_no = pdf_doc["page_no"]

    return (
        random_idx,
        page_no,
        text,
        id,
        doc_id,
        url,
        uncleaned_text,
        source,
        language,
        pdf_name,
        pdf_done_docs,
    )

def register_user(email, password, display_name):
    """
    Registers a new user in the system using email, password and display name.
    """
    try:
        user = auth.create_user(
            email=email, password=password, display_name=display_name
        )
        st.success(f"Successfully registered user {display_name} with email {email} !")
        db.collection("users").document(f"{username}").set(
            {"n_done": 0, "doc_ids_done": [], "pdf_doc_ids_done": []}
        )
        return user

    except Exception as e:
        st.error(e)
        return None


def login_user(email, password):
    """
    Logs in an existing user using email and password.
    """
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyB9z1dFQ-LfOkMQ0r3wcwl_bVbYiT-B-bc"
    payload = {"email": email, "password": password, "returnSecureToken": True}
    response = requests.post(url, data=json.dumps(payload)).text

    return response


if st.session_state["authentication_status"] == True:
    db_user_info = db.collection("users").document(f"{st.session_state['username']}")
    user_info = db_user_info.get().to_dict()

    (
        lid,
        random_idx,
        text,
        doc_id,
        url,
        uncleaned_text,
        source,
        language,
        _,
        pdf_done_docs,
    ) = get_doc()
    try:
        done_docs = (
            db.collection(f"{language}_submissions")
            .document("docs_done")
            .get()
            .to_dict()["idx_done"]
        )
    except:
        db.collection(f"{language}_submissions").document("docs_done").set(
            {"idx_done": []}
        )
        done_docs = []

    try:
        done_docs_ids = (
            db.collection(f"{language}_submissions")
            .document("docs_done")
            .get()
            .to_dict()["doc_ids"]
        )

    except:
        db.collection(f"{language}_submissions").document("docs_done").set(
            {"doc_ids": []}
        )
        done_docs_ids = []

    try:
        pdf_done_docs_ids = (
            db.collection(f"pdf_docs_info")
            .document("docs_done")
            .get()
            .to_dict()["doc_ids"]
        )
        print("TRYING PDF DONE DOCS IDS")   
    except:
        db.collection(f"pdf_docs_info").document("docs_done").set(
            {"doc_ids": []}
        )
        pdf_done_docs_ids = []
        print("EXCEPT PDF DONE DOCS IDS")

    user_doc_ids = user_info["doc_ids_done"]

    st.markdown(
        "<h1 style='text-align: center;'>Welcome to the Setu Dashboard 📈</h1>",
        unsafe_allow_html=True,
    )
    st.write(" ")

    url_page, pdf_page = st.tabs(["URL 🔗", "PDF 📄"])

    st.write(" ")
    st.write(" ")

    with url_page:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write(f'Logged in as **{st.session_state["username"]}**!')
        st.write(
            f'You have completed {user_info["n_done"]} documents'
        )

        st.header(f"Website")
        styled_link = f'<a href="{url}" style="text-decoration: none; color: #0078D4; font-size: 18px;">{f"{url}"}</a>'
        st.markdown(styled_link, unsafe_allow_html=True)

        st.components.v1.iframe(f"{url}", height=1000, scrolling=True)
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.header("Extracted Text")
            st.json({"uncleaned_text": uncleaned_text})

        with col2:
            st.header("Filtered Text")
            st.json({"filtered_text": text})

        st.text(" ")
        st.text(" ")
        st.text(" ")

        st.caption("Document metadata")
        st.json(
            {
                "indicLID_lang": lid,
                "doc_id": doc_id,
                "url": url,
                "source": source,
                "language": language,
            }
        )

        # button to get next document
        next_doc = st.button("Next document")
        if next_doc:
            st.experimental_rerun()

        st.markdown("# User feedback 📜")
        with st.form(key="feedback_form", clear_on_submit=True):
            tab1, tab2, tab3, tab4 = st.tabs(
                [
                    "LID",
                    "Trafilatura verification",
                    "Filtering stage",
                    "Overall Remarks",
                ]
            )

            with tab1:
                st.markdown("## Is LID correct?")
                cols = st.columns(2)
                with cols[0]:
                    lid_yes = st.checkbox("Yes", key="lid_yes")
                with cols[1]:
                    lid_no = st.checkbox("No", key="lid_no")
                lid_reason = st.text_area(
                    "Reason for the above answer", key="lid_reason"
                )

            with tab2:
                st.markdown("## Trafilatura verification")
                st.markdown("#### 1. Is the text extracted by Trafilatura correct?")
                cols = st.columns(2)
                with cols[0]:
                    trafilatura_yes = st.checkbox("Yes", key="trafilatura_yes")
                with cols[1]:
                    trafilatura_no = st.checkbox("No", key="trafilatura_no")
                trafilatura_reason = st.text_input(
                    "Reason for the above answer", key="trafilatura_reason"
                )

                st.markdown("#### 2. Menu items properly removed ?")
                cols = st.columns(2)
                with cols[0]:
                    menu_yes = st.checkbox("Yes", key="menu_yes")
                with cols[1]:
                    menu_no = st.checkbox("No", key="menu_no")
                menu_reason = st.text_input(
                    "Reason for the above answer", key="menu_reason"
                )

                st.markdown("#### 3. Is the main text properly extracted ?")
                cols = st.columns(2)
                with cols[0]:
                    main_text_yes = st.checkbox("Yes", key="main_text_yes")
                with cols[1]:
                    main_text_no = st.checkbox("No", key="main_text_no")
                main_text_reason = st.text_input(
                    "Reason for the above answer", key="main_text_reason"
                )

                st.markdown("#### 4. Are headers and footers properly removed ?")
                cols = st.columns(2)
                with cols[0]:
                    headers_yes = st.checkbox("Yes", key="headers_yes")
                with cols[1]:
                    headers_no = st.checkbox("No", key="headers_no")
                headers_reason = st.text_input(
                    "Reason for the above answer", key="headers_reason"
                )

            with tab3:
                st.markdown("## Filtering stage")

                st.markdown(
                    "#### 1. Is the useless text removed in filtered text like menu items?"
                )
                cols = st.columns(2)
                with cols[0]:
                    filtering_yes = st.checkbox("Yes", key="filtering_yes")
                with cols[1]:
                    filtering_no = st.checkbox("No", key="filtering_no")
                filtering_reason = st.text_input(
                    "Reason for the above answer", key="filtering_reason"
                )

                st.markdown(
                    "#### 2. Is any useful content being removed in the cleaned document?"
                )
                cols = st.columns(2)
                with cols[0]:
                    useful_content_yes = st.checkbox("Yes", key="useful_content_yes")
                with cols[1]:
                    useful_content_no = st.checkbox("No", key="useful_content_no")
                useful_content_reason = st.text_input(
                    "Reason for the above answer", key="useful_content_reason"
                )

                st.markdown(
                    "#### 3. Rank the cleanliness of the document on a scale of 1-5"
                )
                rank = st.slider("Rank", min_value=1, max_value=5, key="rank")

            with tab4:
                st.markdown("## Overall remarks")
                st.text_area("Remarks", key="remarks")

                submit_button = st.form_submit_button(label="Submit", disabled=False)

            
            
            if submit_button:
                submit_info = {
                    "given_by": st.session_state["username"],
                    "indicLID_lang": lid,
                    "doc_id": doc_id,
                    "url": url,
                    "source": source,
                    "language": language,
                    "LID_correct": {
                        "option": "yes" if lid_yes else "no",
                        "remark": lid_reason,
                    },
                    "trafilatura_verification": {
                        "extraction_performed_properly": {
                            "option": "yes" if trafilatura_yes else "no",
                            "remark": trafilatura_reason,
                        },
                        "menu_items_removed": {
                            "option": "yes" if menu_yes else "no",
                            "remark": menu_reason,
                        },
                        "main_text_proper": {
                            "option": "yes" if main_text_yes else "no",
                            "remark": main_text_reason,
                        },
                        "header_footer_removed": {
                            "option": "yes" if headers_yes else "no",
                            "remark": headers_reason,
                        },
                    },
                    "filtering_stage": {
                        "useless_text_removed": {
                            "option": "yes" if filtering_yes else "no",
                            "remark": filtering_reason,
                        },
                        "useful_text_removed": {
                            "option": "yes" if useful_content_yes else "no",
                            "remark": useful_content_reason,
                        },
                        "cleanliness_rank": rank,
                    },
                    "overall_remark": st.session_state["remarks"],
                }

                db.collection("feedback").document(f"{doc_id}").set(submit_info)
                db_user_info.update({"n_done": user_info["n_done"] + 1})

                print(done_docs)
                print(random_idx)

                done_docs.append(random_idx)
                done_docs_ids.append(doc_id)
                db.collection(f"{language}_submissions").document("docs_done").update(
                    {"idx_done": done_docs, "doc_ids": done_docs_ids}
                )

                db.collection("docs_info").document("docs_done").update(
                    {"doc_ids": done_docs_ids}
                )

                user_doc_ids.append(doc_id)
                db_user_info.update({"doc_ids_done": user_doc_ids})

                st.success("Feedback submitted successfully!")
                import time

                with st.spinner("Loading next document...please wait"):
                    time.sleep(3)
                st.experimental_rerun()

    
    
    with pdf_page:
        options = st.multiselect(
            "Choose your preferred Language ",
            [
                "assamese",
                "bengali",
                "gujarati",
                "hindi",
                "kannada",
                "malayalam",
                "marathi",
                "oriya",
                "punjabi",
                "sanskrit",
                "tamil",
                "telugu",
                "urdu",
            ],
            max_selections=1,
        )
        if len(options) == 0:
            st.warning("Please select a language")

        if len(options) == 1:
            (
                pdf_random_idx,
                pdf_page_no,
                pdf_text,
                pdf_id,
                pdf_doc_id,
                pdf_url,
                pdf_uncleaned_text,
                pdf_source,
                pdf_lang,
                pdf_name,
                _,
            ) = get_doc_pdf(options[0])

            print(f"PDF_RANDOM_IDX_INSIDE : {pdf_random_idx}")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write(f'Logged in as **{st.session_state["username"]}**!')
            st.write(
                f'You have completed {user_info["n_done"]} documents'
            )


            st.link_button("PDF Link", pdf_url)
            st.text(f"Page No: {pdf_page_no}")
            

            col2, col3 = st.columns(2, gap="large")

            with col2:
                st.header("Extracted Text")
                st.json({"uncleaned_text": pdf_uncleaned_text})

            with col3:
                st.header("Filtered Text")
                st.json({"filtered_text": pdf_text})

            st.text(" ")
            st.text(" ")
            st.text(" ")

            st.caption("Document metadata")
            st.json(
                {
                    "pdf_language": pdf_lang,
                    "pdf_name": pdf_name,
                    "page_no": pdf_page_no,
                    "pdf_url": pdf_url,
                    "pdf_source": pdf_source,
                    "pdf_doc_id": pdf_doc_id,
                }
            )

            # button to get next document
            next_doc = st.button("Next document", key="next_doc_pdf")
            if next_doc:
                st.experimental_rerun()

            st.markdown("# User feedback (PDF) 📜")
            with st.form(key="feedback_form_pdf", clear_on_submit=True):
                tab1, tab2, tab3 = st.tabs(
                    ["LID", "Filtering stage", "Overall Remarks"]
                )

                with tab1:
                    st.markdown("## Is LID correct?")
                    cols = st.columns(2)
                    with cols[0]:
                        pdf_lid_yes = st.checkbox("Yes", key="pdf_lid_yes")
                    with cols[1]:
                        pdf_lid_no = st.checkbox("No", key="pdf_lid_no")
                    pdf_lid_reason = st.text_area(
                        "Reason for the above answer", key="pdf_lid_reason"
                    )

                with tab2:
                    st.markdown("## Filtering stage")

                    st.markdown(
                        "#### 1. Is the useless text removed in filtered text like menu items?"
                    )
                    cols = st.columns(2)
                    with cols[0]:
                        pdf_filtering_yes = st.checkbox("Yes", key="pdf_filtering_yes")
                    with cols[1]:
                        pdf_filtering_no = st.checkbox("No", key="pdf_filtering_no")
                    pdf_filtering_reason = st.text_input(
                        "Reason for the above answer", key="pdf_filtering_reason"
                    )

                    st.markdown(
                        "#### 2. Is any useful content being removed in the cleaned document?"
                    )
                    cols = st.columns(2)
                    with cols[0]:
                        pdf_useful_content_yes = st.checkbox(
                            "Yes", key="pdf_useful_content_yes"
                        )
                    with cols[1]:
                        pdf_useful_content_no = st.checkbox(
                            "No", key="pdf_useful_content_no"
                        )
                    pdf_useful_content_reason = st.text_input(
                        "Reason for the above answer", key="pdf_useful_content_reason"
                    )

                    st.markdown(
                        "#### 3. Rank the cleanliness of the document on a scale of 1-5"
                    )
                    pdf_rank = st.slider(
                        "Rank", min_value=1, max_value=5, key="pdf_rank"
                    )

                with tab3:
                    st.markdown("## Overall remarks")
                    overall_pdf_remarks = st.text_area("Remarks", key="pdf_remarks")

                    pdf_submit_button = st.form_submit_button(
                        label="Submit", disabled=False
                    )

                if pdf_submit_button:
                    pdf_submit_info = {
                        "given_by": st.session_state["username"],
                        "doc_id": pdf_doc_id,
                        "id": pdf_id,
                        "url": pdf_url,
                        "source": pdf_source,
                        "language": pdf_lang,
                        "LID_correct": {
                            "option": "yes" if lid_yes else "no",
                            "remark": lid_reason,
                        },
                        "filtering_stage": {
                            "useless_text_removed": {
                                "option": "yes" if pdf_filtering_yes else "no",
                                "remark": pdf_filtering_reason,
                            },
                            "useful_text_removed": {
                                "option": "yes" if pdf_useful_content_yes else "no",
                                "remark": pdf_useful_content_reason,
                            },
                            "cleanliness_rank": pdf_rank,
                        },
                        "overall_remark": overall_pdf_remarks,
                    }

                    db.collection("pdf_feedback").document(f"{pdf_doc_id}").set(
                        pdf_submit_info
                    )
                    db_user_info.update({"n_done": user_info["n_done"] + 1})

                    print(f"PDF DONE DOCS:{pdf_done_docs}")
                    print(pdf_random_idx)
                    # try:
                    pdf_done_docs = (
                        db.collection(f"{pdf_lang}_pdf_submissions")
                        .document("docs_done")
                        .get()
                        .to_dict()["idx_done"]
                    )
                    print(f"PDF DONE DOCS FINAL:{pdf_done_docs}") 
                    print(f"PDF DONE DOCS:{pdf_done_docs}")
                    pdf_done_docs.append(pdf_random_idx)
                    print(f"PDF DONE DOCS:{pdf_done_docs}")

                    pdf_done_docs_ids.append(pdf_doc_id)
                    print(f"PDF DONE DOCS IDS:{pdf_done_docs_ids}")

                    print(f"PDF DONE DOCS FOR LANG:{pdf_done_docs}")
                    db.collection(f"{pdf_lang}_pdf_submissions").document(
                        "docs_done"
                    ).update({"idx_done": pdf_done_docs})

                    db.collection("pdf_docs_info").document("docs_done").update(
                        {"doc_ids": pdf_done_docs_ids}
                    )
                    try:
                        lang_doc_ids = db.collection(f"{pdf_lang}_pdf_submissions").document(
                            "docs_done"
                        ).get().to_dict()["doc_ids"]

                        lang_doc_ids.append(pdf_doc_id)
                        db.collection(f"{pdf_lang}_pdf_submissions").document(
                            "docs_done"
                        ).update({"doc_ids": lang_doc_ids, "idx_done": pdf_done_docs})

                    except:

                        db.collection(f"{pdf_lang}_pdf_submissions").document(
                            "docs_done"
                        ).set({"doc_ids": [pdf_doc_id]})


                    try:
                        pdf_user_doc_ids = user_info["pdf_doc_ids_done"]
                    except:
                        pdf_user_doc_ids = []
                        db_user_info.set({"pdf_doc_ids_done": []})

                    pdf_user_doc_ids.append(pdf_doc_id)
                    db_user_info.update({"pdf_doc_ids_done": pdf_user_doc_ids})

                    st.success("Feedback submitted successfully for this PDF!")
                    import time

                    with st.spinner("Loading next document...please wait"):
                        time.sleep(3)
                    st.experimental_rerun()
        pass



elif st.session_state["authentication_status"] is None:
    col1, col2, col3 = st.columns(3)

    with col2:
        st.markdown("# Login to the Setu Dashboard")
        with st.form(key="login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submit_button = st.form_submit_button(label="Login", disabled=False)

            if submit_button:
                try:
                    auth_user = eval(
                        login_user(email, password).replace("true", "True")
                    )
                    print(auth_user)

                    if auth_user["registered"] == True:
                        st.session_state["authentication_status"] = True
                        print(st.session_state["authentication_status"])
                        st.session_state["username"] = auth_user["displayName"]
                        st.experimental_rerun()

                    else:
                        st.error("Error logging in")

                except Exception as e:
                    st.error(f"Username/password is incorrect")

        st.warning("Please enter your email and password")

        register = st.button("Register")

        if register:
            st.session_state["register"] = True
            st.session_state["authentication_status"] = False
            st.experimental_rerun()


elif st.session_state["register"]:
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("# Register to Setu Dashboard")
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
            st.experimental_rerun()

        if submit_button:
            user = register_user(email, password, username)
