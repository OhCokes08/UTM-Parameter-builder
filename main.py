import streamlit as st
import pandas as pd

utm_params = ["Campaign", "Term", "Content","Ref","id"]

st.title("URL Builder with UTM Parameters")
st.subheader("blah blah blah blah")

st.text_input("Enter Base URL", key = "base_url")

st.subheader("Select your additional UTM parameters")
col1, col2 = st.columns(2)
with col1:
    st.checkbox(label = "Campaign", value = False, key = "campaign_param")
    st.checkbox(label = "Term", value = False, key = "term_param")
    st.checkbox(label = "Content", value = False, key = "content_param")
    st.checkbox(label = "Ref", value = False, key = "ref_param")
    st.checkbox(label = "id", value = False, key = "id")
with col2:
    st.text_input("Enter Campaign Identifier", key = "campaign_input")
    st.text_input("Enter Term Identifier", key = "term_input")
    st.text_input("Enter Content Identifier", key = "content_input")
    st.text_input("Enter Ref Identifier", key = "ref_input")
    st.text_input("Enter ID Identifier", key = "id_input")
