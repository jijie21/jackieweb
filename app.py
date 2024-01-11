import streamlit as st
from PIL import Image

st.title('This is a Jackie')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')

# Load the image
image = Image.open('/Users/jieji/Library/Mobile Documents/com~apple~CloudDocs/UW Winter 2024/TECHIN510/Lab 1/IMG_0969.JPG')

# Display the image
st.image(image)