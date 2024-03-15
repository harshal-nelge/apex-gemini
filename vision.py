from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

print(os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key="AIzaSyD-l11_8FKSih3yJScgkgWq0EYomo979ck")
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])

    else:
        response=model.generate_content(image)
    return response.text


st.set_page_config(page_title="Description Extractor")

st.header("Gemini Application")
input=st.text_input("enter instruction: ",key="input")

uploaded_file = st.file_uploader("choose an image", type=["jpg", "jpeg", "png"])
image=""

if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption="Uploaded image", use_column_width=True)


submit=st.button("generate")

if submit:

  response=get_gemini_response(input,image)
  st.subheader("The response is")
  st.write(response)
