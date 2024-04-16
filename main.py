import datetime as dt
import csv
import streamlit as st
import pandas as pd


utm_sources = ["eloqua","email", "adwords", "ads","facebook", "twitter","instagram","linkedin", "bing","google","duckduckgo", "eloqua"]
utm_mediums = ["social","socialmedia","social-media","display", "email","paid-social","paid_social","ppc-social","search","cpc","ppc","paid"]

def link_creation(base_url, utm_source, utm_medium, utm_campaign, utm_content, utm_term, utm_id, utm_ref):
    utm_params = []
    if utm_source:
        utm_params.append(f"utm_source={','.join(utm_source)}")
    if utm_medium:
        utm_params.append(f"utm_medium={','.join(utm_medium)}")
    if utm_campaign:
        utm_params.append(f"utm_campaign={utm_campaign}")
    if utm_content:
        utm_params.append(f"utm_content={utm_content}")
    if utm_term:
        utm_params.append(f"utm_term={utm_term}")
    if utm_ref:
        utm_params.append(f"utm_ref={utm_ref}")
    if utm_id:
        utm_params.append(f"utm_id={utm_id}")

    utm_params_str = "&".join(utm_params)
    return f"{base_url}/?{utm_params_str}"

def link_save(url, doc = "tracking_links.csv"):
    time = dt.datetime.now()
    date = time.strftime("%d-%m-%Y")
    link = url
    with open(doc, mode = 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date,link])

def main():
    st.image('https://static.vecteezy.com/system/resources/previews/000/176/200/original/vector-abstract-company-logo-template-design-illustration.jpg',use_column_width= True)
    col1, col2 = st.columns(2)
    with col1:
        st.title("RX URL Builder with UTM Parameters")
    with col2:
        st.subheader("blah blah blah blah")

    with st.form("utm_creator",clear_on_submit=False):
        base_url = st.text_input("Enter Base URL", key = "base_url")
        st.subheader("Select your source and medium")
        col3, col4 = st.columns(2)
        with col3:
            utm_source = st.multiselect("Source", options = utm_sources, max_selections=1)

        with col4:
            utm_medium = st.multiselect("Medium", options= utm_mediums, max_selections=1)

        st.subheader("Select your additional UTM parameters")
        utm_campaign = st.text_input("Enter Campaign Identifier", key = "campaign_input")
        utm_term = st.text_input("Enter Term Identifier", key = "term_input")
        utm_content = st.text_input("Enter Content Identifier", key = "content_input")
        utm_ref = st.text_input("Enter Ref Identifier", key = "ref_input")
        utm_id = st.text_input("Enter ID Identifier", key = "id_input")

        submitted = st.form_submit_button('Build URL')

        if submitted and base_url:
            utm_url = link_creation(base_url, utm_source, utm_medium, utm_campaign, utm_term, utm_content, utm_ref, utm_id)
            st.success('Your UTM URL is:')
            print(utm_url)
            st.code(utm_url)
            link_save(utm_url)

if __name__ == "__main__":
    main()






