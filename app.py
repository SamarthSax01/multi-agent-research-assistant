import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    layout="wide"
)

# Header
st.title("Multi-Agent Research Assistant")

st.markdown("""
This AI system performs autonomous research using multiple specialized agents.

**Workflow**

Search Agent → Reader Agent → Writer Agent → Critic Agent
""")

# Sidebar
with st.sidebar:
    st.header("Architecture")

    st.markdown("""
    **Search Agent**
    - Searches live web data using Tavily

    **Reader Agent**
    - Reads and extracts webpage content

    **Writer Agent**
    - Generates structured research report

    **Critic Agent**
    - Evaluates report quality
    """)

    st.divider()

    st.markdown("""
    **Tech Stack**

    - LangChain
    - Mistral AI
    - Tavily Search
    - BeautifulSoup
    - Streamlit
    """)

# Input Section
topic = st.text_input(
    "Research Topic",
    placeholder="Artificial Intelligence"
)

if st.button("Generate Research Report", use_container_width=True):

    if not topic:
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("Running Multi-Agent Research Pipeline..."):
        result = run_research_pipeline(topic)

    st.success("Research Complete")

    # Report Section
    st.header("Research Report")

    st.markdown(result["report"])

    # Feedback Section
    st.header("Critic Evaluation")

    with st.container(border=True):
        st.markdown(result["feedback"])

    # Agent Outputs
    st.header("Agent Outputs")

    with st.expander("Search Agent Results"):
        st.write(result["search_results"])

    with st.expander("Reader Agent Extracted Content"):
        st.write(result["scraped_content"])

    # Download Button
    st.download_button(
        label="Download Research Report",
        data=result["report"],
        file_name=f"{topic}_report.txt",
        mime="text/plain"
    )