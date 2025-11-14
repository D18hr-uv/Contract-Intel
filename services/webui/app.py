import streamlit as st
import requests
import time

# Define the API endpoints
API_UPLOAD_URL = "http://localhost:8000/upload"
API_TASK_STATUS_URL = "http://localhost:8000/tasks/{task_id}"

st.title("Contract Intelligence & Compliance Platform")

uploaded_file = st.file_uploader("Upload a contract document", type=["pdf", "docx"])

if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)

    # Send the file to the API for processing
    with st.spinner("Processing document..."):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        response = requests.post(API_UPLOAD_URL, files=files)

        if response.status_code == 200:
            task_id = response.json().get("task_id")
            st.write("Document processing started with task ID:", task_id)

            # Poll for the result
            while True:
                task_response = requests.get(API_TASK_STATUS_URL.format(task_id=task_id))
                if task_response.status_code == 200:
                    task_data = task_response.json()
                    if task_data["status"] == "SUCCESS":
                        st.success("Document processing complete!")

                        # Display the risk analysis
                        risk_analysis = task_data.get("result", {}).get("risk_analysis", {})
                        if risk_analysis:
                            st.subheader("Risk Analysis")
                            st.write("Risk Score:", risk_analysis.get("risk_score"))
                            st.write("Risk Level:", risk_analysis.get("risk_level"))

                            st.subheader("Reasons for Risk Assessment")
                            for reason in risk_analysis.get("reasons", []):
                                st.write("- ", reason)
                        else:
                            st.error("Could not retrieve risk analysis.")
                        break
                    elif task_data["status"] == "FAILURE":
                        st.error("Document processing failed.")
                        break
                else:
                    st.error("Failed to get task status.")
                    break

                time.sleep(2)  # Wait for 2 seconds before polling again
        else:
            st.error("Failed to upload file.")
