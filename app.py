import streamlit as st
from captcha.image import ImageCaptcha
import random
import string
from PIL import Image

# CAPTCHA yaratish funksiyasi
def generate_captcha():
    image_captcha = ImageCaptcha(width=280, height=90)
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    image = image_captcha.generate_image(captcha_text)
    return captcha_text, image

# CAPTCHA tekshirish funksiyasi
def verify_captcha(user_input, actual_captcha):
    return user_input.strip().upper() == actual_captcha

# CAPTCHA holatini saqlash
if "captcha_text" not in st.session_state:
    st.session_state["captcha_text"], st.session_state["captcha_image"] = generate_captcha()

# Interfeys
st.title("Botlarni aniqlash")
st.write("Quyidagi CAPTCHA matnini kiriting:")

# CAPTCHA-ni ko'rsatish
st.image(st.session_state["captcha_image"], caption="CAPTCHA")

# CAPTCHA-ni yangilash tugmasi
if st.button("CAPTCHA-ni almashtirish"):
    st.session_state["captcha_text"], st.session_state["captcha_image"] = generate_captcha()

# Foydalanuvchi kiritishi
captcha_input = st.text_input("CAPTCHA-ni kiriting:")

# Tekshirish
if captcha_input:
    if verify_captcha(captcha_input, st.session_state["captcha_text"]):
        st.success("CAPTCHA to'g'ri!")
    else:
        st.error("CAPTCHA noto'g'ri! Iltimos, qaytadan urinib ko‘ring.")


# import streamlit as st
# import random
# import string
# from captcha.image import ImageCaptcha
# from io import BytesIO
# from PIL import Image

# # CAPTCHA yaratish funksiyasi
# def generate_captcha():
#     image_captcha = ImageCaptcha(width=280, height=90)
#     captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
#     image = image_captcha.generate_image(captcha_text)
#     return captcha_text, image

# # CAPTCHA tekshirish funksiyasi
# def verify_captcha(user_input, actual_captcha):
#     return user_input.strip().upper() == actual_captcha

# # Interfeys
# st.title("CAPTCHA Tekshiruvi")
# st.write("Quyidagi CAPTCHA-ni kiriting")

# # CAPTCHA yaratish
# captcha_text, captcha_image = generate_captcha()
# st.image(captcha_image, caption="CAPTCHA matnini kiriting")
# captcha_input = st.text_input("CAPTCHA-ni kiriting:")

# # CAPTCHA tasdiqlash
# if st.button("Tekshirish"):
#     if not captcha_input:
#         st.warning("Iltimos, CAPTCHA-ni kiriting!")
#     elif not verify_captcha(captcha_input, captcha_text):
#         st.error("CAPTCHA noto‘g‘ri! Iltimos, qaytadan urinib ko‘ring.")
#     else:
#         st.success("CAPTCHA to‘g‘ri kiritildi!")
