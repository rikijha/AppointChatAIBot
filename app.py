from google_auth import *
from tools.calendar_function import get_calender_list
from agent import run_agent_executor
import streamlit as st



if __name__ == '__main__':
    st.title("Appoint Scheduler AI Bot")

    if 'code' in st.query_params and 'email' not in st.session_state:
        get_user()

    if 'email' not in st.session_state:
        with st.sidebar:
            st.title("Please login into google account to use the bot")
            st.write(get_login_str(), unsafe_allow_html=True)

    if 'email' in st.session_state:
        st.header(f'''Welcome {st.session_state['email']}''')
        calendars = get_calender_list()
        value = st.selectbox('Please select type of google calendar', options=calendars.keys(), format_func=lambda x: calendars[x])
        user_question = st.text_input("Ask or create appoints on your calendar")
        if user_question:
            st.write("Reply: ", run_agent_executor(user_question, value))


