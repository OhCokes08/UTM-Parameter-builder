import streamlit as st
import pandas as pd

utm_params = ["Campaign", "Term", "Content","Ref","id"]

st.title("URL Builder with UTM Parameters")
st.subheader("blah blah blah blah")

st.text_input("Enter Base URL", key = "base_url")
st.subheader("Select your additional UTM parameters")
st.subheader("Select your required Parameters")
st.checkbox(label = "Campaign", value = False, key = "campaign_param")
st.checkbox(label = "Term", value = False, key = "term_param")
st.checkbox(label = "Content", value = False, key = "content_param")
st.checkbox(label = "Ref", value = False, key = "ref_param")
st.checkbox(label = "id", value = False, key = "id")
