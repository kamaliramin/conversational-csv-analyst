import streamlit as st

def render_sidebar():
    """
    Renders the sidebar of the Streamlit application.

    Returns:
        A Streamlit UploadedFile object.
    """
    st.sidebar.title("تنظیمات")
    st.sidebar.divider()
    st.sidebar.header("بارگذاری داده‌ها")
    uploaded_file = st.sidebar.file_uploader("یک فایل CSV یا Excel انتخاب کنید", type=["csv", "xlsx", "xls"], label_visibility="collapsed")
    
    st.sidebar.divider()
    
    with st.sidebar.expander("نمونه سوالات (برای مشاهده کلیک کنید)"):
        st.info(
            """
            - چند ردیف در مجموعه داده وجود دارد؟
            - نام ستون‌ها چیست؟
            - ۵ ردیف اول را به من نشان بده.
            - میانگین مقدار یک ستون خاص چقدر است؟
            - یک هیستوگرام برای یک ستون خاص رسم کن.
            """
        )
    return uploaded_file

def render_chat_history(messages):
    """
    Renders the chat history with avatars.

    Args:
        messages: A list of messages from the session state.
    """
    for message in messages:
        avatar = "👤" if message["role"] == "user" else "🤖"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])
