# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "fcf89326-2a8b-441b-b112-f4f93c595ef6"
FLOW_ID = "aa60726e-2393-48df-af40-91849b01f117"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "tutor" # The endpoint name of the flow

def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title('Rafi TutorsPlan Tutor Chat')
    st.header("Your Students: Rafi, Zubair, Rabbi, Ihan, Umm Honey")
    st.header("Write a STUDENT'S NAME to get their recommended SYLLABUS")
    message = st.text_area("Message", placeholder = "Write a student name... ")
    
    if st.button("Run Flow"):
          if not message.strip():
               st.error("Please enter a message")
               return

          try:
               with st.spinner("Running flow..."):
                    response = run_flow(message)
               
               response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
               st.markdown(response)
          except Exception as e:
               st.error(str(e))

if __name__ == "__main__":
    main()
