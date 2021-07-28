import streamlit as st
import pytesseract
from PIL import Image
st.title("Optical character Recognition")
img=st.sidebar.file_uploader("choose an Image")
if img is not None:
  img_read=Image.open(img)
  st.image(img,caption='uploaded Image')
  if st.button('Predict'):
    op=pytesseract.image_to_string(img_read)
    st.write(op)
