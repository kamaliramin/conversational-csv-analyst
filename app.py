import streamlit as st
import os
from dotenv import load_dotenv
import ui_components
import utils
import agent_handler
import matplotlib.pyplot as plt
import pandas as pd
import re

# Set page config
st.set_page_config(page_title="تحلیلگر داده هوش مصنوعی", layout="wide")

# Load custom CSS
utils.load_css("assets/style.css")

st.title("🤖 هوش مصنوعی تحلیلگر داده")

# Load environment variables
load_dotenv()

# Check for Google API Key
if not os.getenv("GOOGLE_API_KEY"):
    st.error("لطفاً کلید API گوگل خود را در فایل .env تنظیم کنید.")
    st.stop()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent" not in st.session_state:
    st.session_state.agent = None
if "data" not in st.session_state:
    st.session_state.data = None

# Render sidebar
uploaded_file = ui_components.render_sidebar()

# Main content area
if uploaded_file is None:
    st.info("لطفاً برای شروع، یک فایل CSV یا Excel از نوار کناری بارگذاری کنید.")
else:
    df = utils.load_data(uploaded_file)
    if df is not None:
        st.session_state.data = df
        with st.container():
            st.success(f"فایل '{uploaded_file.name}' با موفقیت بارگذاری شد!")
            st.info(f"فایل شامل {len(df)} ردیف و {len(df.columns)} ستون است.")
            st.dataframe(df)
        st.session_state.agent = agent_handler.create_agent(df)

st.divider()

# Render chat history
ui_components.render_chat_history(st.session_state.messages)

# Chat input
if prompt := st.chat_input("سوالی در مورد داده‌های خود بپرسید...", disabled=st.session_state.agent is None):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("در حال پردازش..."):
            try:
                response = st.session_state.agent.run(prompt)
                
                # Check if the response contains a python code block for plotting
                code_match = re.search(r"```python\n(.*?)```", response, re.DOTALL)
                
                if code_match:
                    code_to_execute = code_match.group(1).strip()
                    try:
                        df = st.session_state.data
                        exec(code_to_execute, globals(), {'df': df, 'plt': plt})
                        fig = plt.gcf()
                        st.pyplot(fig)
                        plt.clf()
                        # Display any text that was outside the code block
                        text_response = response.replace(f"```python\n{code_to_execute}\n```", "").strip()
                        if not text_response:
                             text_response = "در اینجا نمودار درخواستی شما نمایش داده شده است."
                        st.markdown(text_response)
                        st.session_state.messages.append({"role": "assistant", "content": text_response})
                        # Also add the plot to the history? For now, just text.
                    except Exception as exec_error:
                        st.error(f"متاسفانه در تولید نمودار خطایی رخ داد: {exec_error}")
                        st.session_state.messages.append({"role": "assistant", "content": f"خطا در کد: {exec_error}"})
                else:
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})

            except Exception as e:
                error_message = f"خطایی رخ داد: {e}"
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})
