from agents import build_read_agent,build_search_agent,writer_chain,critic_chain
def run_research_pipeline(topic:str)->dict:
    state={}
    print("search agent is working")
    search_agent=build_search_agent()
    search_result=search_agent.invoke(
        {
            "messages":[("user",f"find reliable information about the following Topics:{topic}")]
        }
    )
    state["search_results"]=search_result["messages"][-1].content
    print(state["search_results"])

    reader_agent=build_read_agent()
    reader_result=reader_agent.invoke(
        {
            "messages":[("user",f"based on the search results {state['search_results']} about {topic} pick the most important and useful url and scrape it")]
        }
    )
    state["scraped_content"]=reader_result["messages"][-1].content
    print(state["scraped_content"])

    research_combined = (
    f"Search Results:\n{state['search_results']}\n\n"
    f"Scraped Content:\n{state['scraped_content']}"
)
           
    state["report"]=writer_chain.invoke({
        "topic":topic,
        "research":research_combined
    })
    print(state['report'])

    state["feedback"]=critic_chain.invoke({"report":state['report']})
    print(state['feedback'])
    return state
if __name__=="__main__":
    topic=input("Enter a research topic:")
    run_research_pipeline(topic)
        