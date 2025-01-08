import streamlit as st
from translator import translate_ar_to_en
from image_generator import generate_image

st.title("Arabic to Image Generator")

arabic_text = st.text_input("Enter Arabic text:")
if st.button("Generate"):
    if arabic_text:
        english_translation = translate_ar_to_en(arabic_text)
        st.write(f"Translated Text: {english_translation}")
        generate_image(english_translation, "generated_image.png")
        st.image("generated_image.png")
    else:
        st.error("Please enter Arabic text.")
