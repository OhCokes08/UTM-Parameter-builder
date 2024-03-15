import streamlit as st
import pandas as pd

utm_sources = ['eloqua','email', 'adwords', 'ads','facebok', 'twitter','instagram','linkedin', 'bing','google','duckduckgo', 'eloqua']
utm_mediums = ['social','socialmedia','social-media','display', 'email','paid-social','paid_social','ppc-social','search','cpc','ppc','paid']

def link_creation(base_url, utm_source, utm_medium, utm_campaign, utm_content, utm_term, utm_id, utm_ref):
    utm_params = []
    if utm_source:
        utm_params.append(f"utm_source={utm_sources}")
    if utm_medium:
        utm_params.append(f"utm_medium={utm_mediums}")
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
    return f"{base_url}?{utm_params_str}"

def main():
    st.title("URL Builder with UTM Parameters")
    st.subheader("blah blah blah blah")

    with st.form("utm_creator",clear_on_submit=False):
        base_url = st.text_input("Enter Base URL", key = "base_url")
        st.subheader("Select your source and medium")
        col1, col2 = st.columns(2)
        with col1:
            utm_source = st.multiselect("Source", options = utm_sources, max_selections=1)

        with col2:
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
            st.code(utm_url)

if __name__ == "__main__":
    main()






