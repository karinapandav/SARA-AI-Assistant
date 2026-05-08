import streamlit as st
from modules.ai_engine import ask_sara
from modules.memory import add_preference
from modules.feedback import load_logs

st.set_page_config(
    page_title="SARA",
    layout="wide"
)

# =========================
# HEADER
# =========================

st.title("SARA — Smart Adaptive Response Assistant")
st.caption("Built around you.")
st.info(
    "SARA learns from your preferences, habits, and interactions to become more personalized over time."
)
# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.header("SARA Dashboard")

    st.markdown("---")

    st.subheader("Quick Actions")

    if st.button("Plan My Day"):

        response = ask_sara(
            "Create a productive and balanced daily plan for me."
        )

        st.session_state["response"] = response

    if st.button("👗 Outfit Suggestion"):

        response = ask_sara(
            "Suggest an outfit for my day."
        )

        st.session_state["response"] = response

    if st.button("Meal Suggestion"):

        response = ask_sara(
            "Suggest vegetarian meals for weight gain."
        )

        st.session_state["response"] = response

    st.markdown("---")

    st.subheader("Teach SARA")

    preference_type = st.text_input("Preference Type")
    preference_value = st.text_input("Preference Value")

    if st.button("Save Preference"):

        add_preference(
            preference_type,
            preference_value
        )

        st.success("SARA learned something new!")

# =========================
# MAIN CHAT
# =========================

st.subheader("Talk to SARA")

query = st.text_input(
    "Ask anything..."
)

if st.button("Send"):

    with st.spinner("SARA is thinking..."):

        response = ask_sara(query)

        st.session_state["response"] = response

# =========================
# RESPONSE SECTION
# =========================

if "response" in st.session_state:

    st.markdown("### SARA Response")

    st.success(
        st.session_state["response"]
    )

# =========================
# RECENT ACTIVITY
# =========================

st.markdown("---")

st.subheader("Recent Activity")

logs = load_logs()

recent_logs = logs[-5:]

if recent_logs:

    for log in reversed(recent_logs):

        st.markdown(
            f"""
** {log['time']}**

**You:** {log['query']}

**SARA:** {log['response']}

---
"""
        )

else:

    st.info("No activity yet.")