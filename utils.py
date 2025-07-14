import pandas as pd
import streamlit as st
import os

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_data(uploaded_file):
    """
    Safely loads a CSV or Excel file into a Pandas DataFrame.

    Args:
        uploaded_file: A Streamlit UploadedFile object.

    Returns:
        A Pandas DataFrame if successful, otherwise None.
    """
    if uploaded_file is not None:
        try:
            # Get the file extension
            name, extension = os.path.splitext(uploaded_file.name)
            if extension == '.csv':
                return pd.read_csv(uploaded_file)
            elif extension in ['.xls', '.xlsx']:
                return pd.read_excel(uploaded_file)
            else:
                st.error(f"فرمت فایل پشتیبانی نمی‌شود: {extension}")
                return None
        except Exception as e:
            st.error(f"خطا در خواندن فایل: {e}")
            return None
    return None
