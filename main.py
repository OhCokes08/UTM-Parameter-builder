import streamlit as st
import pandas as pd

utm_sources = ["eloqua","email", "adwords", "ads","facebok", "twitter","instagram","linkedin", "bing","google","duckduckgo", "eloqua"]
utm_mediums = ["social","socialmedia","social-media","display", "email","paid-social","paid_social","ppc-social","search","cpc","ppc","paid"]
st.title("URL Builder with UTM Parameters")
st.subheader("blah blah blah blah")

st.text_input("Enter Base URL", key = "base_url")
st.subheader("Select your source and medium")
col1, col2 = st.columns(2)
with col1:
    st.multiselect("Source", options = utm_sources, max_selections=1)

with col2:
    st.multiselect("Medium", options= utm_mediums, max_selections=1)

st.subheader("Select your additional UTM parameters")
col3, col4 = st.columns(2)
with col3:
    st.checkbox(label = "Campaign", value = False, key = "campaign_param")
    st.checkbox(label = "Term", value = False, key = "term_param")
    st.checkbox(label = "Content", value = False, key = "content_param")
    st.checkbox(label = "Ref", value = False, key = "ref_param")
    st.checkbox(label = "id", value = False, key = "id")
with col4:
    st.text_input("Enter Campaign Identifier", key = "campaign_input")
    st.text_input("Enter Term Identifier", key = "term_input")
    st.text_input("Enter Content Identifier", key = "content_input")
    st.text_input("Enter Ref Identifier", key = "ref_input")
    st.text_input("Enter ID Identifier", key = "id_input")

st.button("Create Link", key = "runit", on_click=None)

st.text_area("Final URL", key= "final_url")

def link_creation(base_url):
    pass