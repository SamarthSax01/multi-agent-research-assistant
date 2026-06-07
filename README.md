# Multi-Agent Research Assistant

## Overview

Multi-Agent Research Assistant is an agentic AI system that autonomously researches a user-provided topic using multiple specialized AI agents.

Instead of relying solely on a language model's internal knowledge, the system performs live web search, extracts information from relevant web pages, generates a structured research report, and evaluates the report through a dedicated critic component.

The project demonstrates the use of multi-agent workflows, tool integration, web search, web scraping, and automated report generation.

---

## Architecture

User Topic
    ↓
Search Agent
    ↓
Tavily Search API
    ↓
Search Results Stored in Shared State
    ↓
Reader Agent
    ↓
BeautifulSoup Web Scraper
    ↓
Scraped Content Stored in Shared State
    ↓
Writer Chain
    ↓
Research Report
    ↓
Critic Chain
    ↓
Feedback and Evaluation
    ↓
Final Output

---

## Features

- Live web search using Tavily API
- Multi-agent architecture
- Autonomous information gathering
- Web scraping using BeautifulSoup
- Shared state management between agents
- Research report generation
- Automated report evaluation and feedback
- Streamlit user interface
- Modular and extensible design

---

## Tech Stack

### AI / LLM

- Mistral AI
- LangChain

### Search & Retrieval

- Tavily Search API

### Web Scraping

- BeautifulSoup4
- Requests

### Frontend

- Streamlit

### Backend

- Python

---

## Project Workflow

### Search Agent

The Search Agent receives a research topic and performs live web search using Tavily.

Responsibilities:

- Search the web
- Find relevant sources
- Retrieve titles, URLs and snippets

---

### Reader Agent

The Reader Agent selects relevant URLs and extracts webpage content.

Responsibilities:

- Access web pages
- Remove unnecessary HTML elements
- Extract clean textual content

---

### Writer Chain

The Writer component transforms the collected information into a structured research report.

Report Sections:

- Introduction
- Key Findings
- Conclusion
- Sources

---

### Critic Chain

The Critic reviews the generated report and provides:

- Numerical score
- Strengths
- Areas of improvement
- Overall verdict

---

## Installation

### Clone Repository

```bash
git clone https://github.com/SamarthSax01/multi-agent-research-assistant.git

cd multi-agent-research-assistant
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Example Use Cases

- Technology Research
- Market Research
- Industry Analysis
- Academic Topic Exploration
- Current Affairs Research

---

## Future Improvements

- LangGraph orchestration
- Multi-source article aggregation
- Source ranking and credibility scoring
- PDF report export
- Citation generation
- Report refinement using critic feedback
- Multi-modal research capabilities

---

## Author

Samarth Saxena