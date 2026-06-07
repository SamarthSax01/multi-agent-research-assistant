import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Multi-Agent Research Assistant")

st.markdown(
    """
    Enter a research topic and let the AI:
    - Search the web
    - Read relevant sources
    - Generate a report
    - Critique the report
    """
)

topic = st.text_input(
    "Enter Research Topic",
    placeholder="Artificial Intelligence"
)

if st.button("Generate Research Report"):

    if not topic:
        st.warning("Please enter a topic.")
        st.stop()

    with st.spinner("Researching..."):

        result = run_research_pipeline(topic)

    st.success("Research Complete!")

    st.subheader("Search Results")

    st.text_area(
        "Search Results",
        result["search_results"],
        height=250
    )

    st.subheader("Scraped Content")

    st.text_area(
        "Scraped Content",
        result["scraped_content"],
        height=250
    )

    st.subheader("Research Report")

    st.markdown(result["report"])

    st.subheader("Critic Feedback")

    st.markdown(result["feedback"])