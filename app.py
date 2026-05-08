import streamlit as st
from modules.ai_engine import ask_sara
from modules.memory import add_preference
from modules.feedback import load_logs
from modules.insights import generate_insights


st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main {
    background-color: #0B0F19;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid rgba(255,255,255,0.05);
}

.stTextInput input {
    background-color: #1F2937 !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 14px !important;
}

.stButton button {
    background-color: #2563EB;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.6rem 1rem;
    font-weight: 500;
}

.response-card {
    background: #111827;
    padding: 24px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.05);
    margin-top: 20px;
}

.small-label {
    color: #9CA3AF;
    font-size: 0.9rem;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown(
    """
    <h1 style='font-size: 3rem; margin-bottom:0;'>
    SARA
    </h1>

    <p style='color: #9CA3AF; font-size: 1.1rem; margin-top:0;'>
    Smart Adaptive Response Assistant
    </p>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Memory Entries",
        len(load_logs())
    )

with col2:
    st.metric(
        "Personalization",
        f"{min(len(load_logs()) * 10, 100)}%"
    )

with col3:
    st.metric(
        "Assistant Status",
        "Active"
    )

st.markdown("### Ask SARA")

query = st.text_input(
    "",
    placeholder="Ask SARA anything..."
)

if st.button("Send"):

    if query:

        with st.spinner("Thinking..."):

            response = ask_sara(query)

            st.session_state["response"] = response
# =========================
# SIDEBAR
# =========================
with st.sidebar:

    st.markdown("## ✨ SARA")

    st.caption("Built around you")

    st.markdown("---")

    st.markdown("### Quick Actions")

    if st.button("Plan My Day"):
        st.session_state["response"] = ask_sara(
            "Create a productive plan for my day."
        )

    if st.button("Outfit Suggestion"):
        st.session_state["response"] = ask_sara(
            "Suggest an outfit for today."
        )

    if st.button("Meal Suggestion"):
        st.session_state["response"] = ask_sara(
            "Suggest healthy vegetarian meals."
        )

    st.markdown("---")

    st.markdown("### Teach SARA")

    preference_type = st.text_input("Type")

    preference_value = st.text_input("Value")

    if st.button("Save"):

        add_preference(
            preference_type,
            preference_value
        )

        st.success("Saved")

# =========================
# RESPONSE SECTION
# =========================

if "response" in st.session_state:

    st.markdown(
        f"""
        <div class="response-card">

        <div class="small-label">
        SARA RESPONSE
        </div>

        <br>

        {st.session_state["response"]}

        </div>
        """,
        unsafe_allow_html=True
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


**You:** {log['query']}

**SARA:** {log['response']}

---
"""
        )

else:

    st.info("No activity yet.")