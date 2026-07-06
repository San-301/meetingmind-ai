from tools.file_parser import extract_text
from agents.coordinator import CoordinatorAgent
from tools.pdf_tool import generate_pdf
import streamlit as st

# ---------------------------------------
# Streamlit Configuration
# ---------------------------------------
st.set_page_config(
    page_title="🧠 MeetingMind AI",
    layout="wide"
)

# ---------------------------------------
# Sidebar
# ---------------------------------------
with st.sidebar:
    st.title("🧠 MeetingMind AI")
    st.markdown("### AI Meeting Assistant")

    st.markdown("---")

    st.success("📄 Meeting Summary")
    st.success("✅ Decision Extraction")
    st.success("📋 Action Items")
    st.success("📧 Email Generator")
    st.success("📅 Schedule Planner")
    st.success("📄 PDF Report")

    st.markdown("---")
    st.info("Powered by Google Gemini")

# ---------------------------------------
# Cache
# ---------------------------------------
@st.cache_data
def analyze_cached(transcript):
    coordinator = CoordinatorAgent()
    return coordinator.process_meeting(transcript)

# ---------------------------------------
# Header
# ---------------------------------------
st.title("🧠 MeetingMind AI")
st.caption("AI-powered Multi-Agent Meeting Assistant")

uploaded_file = st.file_uploader(
    "📂 Upload Meeting Document",
    type=["txt", "pdf", "docx", "mp3", "wav", "m4a"]
)

# ---------------------------------------
# Main Logic
# ---------------------------------------
if uploaded_file:

    result = extract_text(uploaded_file)

    # Audio placeholder
    if isinstance(result, str) and result.endswith((".mp3", ".wav", ".m4a")):
        st.info("🎤 Audio transcription support will be added in the next version.")

    else:

        try:
            with st.spinner("🤖 AI is analyzing your meeting..."):
                results = analyze_cached(result)

        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

        # ---------------------------------------
        # Metrics
        # ---------------------------------------
        decisions_list = results.get("decisions", [])

        if (
            len(decisions_list) == 1
            and decisions_list[0].lower() == "no decisions identified."
        ):
            decisions = 0
        else:
            decisions = len(decisions_list)

        actions = len(results.get("action_items", []))

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📌 Decisions", decisions)

        with col2:
            st.metric("📋 Tasks", actions)

        with col3:
            st.metric("✅ Status", "Completed")

        st.divider()

        # ---------------------------------------
        # Tabs
        # ---------------------------------------
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📄 Summary",
            "✅ Decisions",
            "📋 Action Items",
            "📧 Email",
            "📅 Schedule"
        ])

        with tab1:
            st.write(results.get("summary", "No summary available."))

        with tab2:
            decisions = results.get("decisions", [])

            if (
                len(decisions) == 1
                and decisions[0].lower() == "no decisions identified."
            ):
                st.info("No decisions were identified in this meeting.")
            else:
                for decision in decisions:
                    st.markdown(f"• {decision}")
                    
        with tab3:
            st.table(results.get("action_items", []))

        with tab4:
            st.write(results.get("email", "No email generated."))

        with tab5:
            st.write(results.get("schedule", "No schedule generated."))

        st.divider()

        # ---------------------------------------
        # Download Report
        # ---------------------------------------
        pdf_path = generate_pdf(results)

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="📄 Download Meeting Report",
                data=pdf_file,
                file_name="MeetingMind_Report.pdf",
                mime="application/pdf"
            )