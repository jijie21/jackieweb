import streamlit as st
from PIL import Image

st.title('This is a Jackie')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')

# Load the image
image = Image.open('./IMG_0969.JPG')

# Display the image
st.image(image)