import streamlit as st
import time


st.set_page_config(page_title="For My Dearest", page_icon="❤️")


st.markdown("""
    <style>
    .main {
        background-color: #fff0f3;
    }
    .romantic-text {
        color: #c9184a;
        font-family: 'Georgia', serif;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown("<h1 class='romantic-text'>To My Better Half 💖</h1>", unsafe_allow_html=True)


st.write("") 
st.markdown("<h3 style='text-align: center; color: #4a4a4a;'>Every moment with you is like a beautiful dream come true.</h3>", unsafe_allow_html=True)


if st.button('Click here for a surprise 🎁'):
    st.balloons() 
    time.sleep(1)
    st.snow() 
    st.markdown("""
        <div style="background-color: #ffb3c1; padding: 20px; border-radius: 15px; text-align: center;">
            <h2 style="color: white;">I Love You More Than Words Can Say!</h2>
            <p style="color: white; font-size: 18px;">
                You are the melody to my heart and the light in my life.<br>
                I'll be right by your side, forever and always.
            </p>
        </div>
    """, unsafe_allow_html=True)


st.write("")
st.write("My love for you:")
love_bar = st.progress(0)
for p in range(100):
    time.sleep(0.01)
    love_bar.progress(p + 1)
st.write("✨ 100% Infinite Love ✨")


with st.sidebar:
    st.title("From Your Girl 💌")
    st.write("You are my favorite person in the entire world.")
    st.image("https://cdn-icons-png.flaticon.com/512/833/833472.png", width=100) 