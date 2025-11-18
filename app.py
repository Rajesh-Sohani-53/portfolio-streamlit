import streamlit as st
def app():
    st.markdown("""
    <div class="hero">
        <h1 class="hero-title">Hi, I'm <span>Rajesh Ravi Sohani</span></h1>
        <p class="hero-sub">AI/ML • RAG Systems • IoT • Java • Full Stack Engineering</p>

        <div class="hero-anim"></div>

        <p class="hero-desc">
            I build intelligent systems using Generative AI, embeddings, vector databases,
            and IoT devices. Currently developing a full Document-QA System using RAG.
        </p>
    </div>
    """, unsafe_allow_html=True)
