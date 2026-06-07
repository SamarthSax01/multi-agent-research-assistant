from langchain.tools import tool
import requests #for web scraping AND BEAUTIFULSOUP
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os 
from dotenv import load_dotenv
load_dotenv()

tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
@tool
def web_search(query : str) ->str:
    """ Search the web for reliable info on a topic and returns
    title url and basic info
    """
    results =tavily.search(query=query,max_results=5)
    out=[]
    for r in results['results']:
        out.append(
            f"Title:{r['title']} \n URL:{r['url']} \n Snippet:{r['content'][:300]}\n"
        )
    return "\n......\n".join(out)


# Now what we are doing is that we are going to use BeautifulSoup bcz the llm is not capable to 
# read the url and give content which we get from the search agent therefore we use BeautifulSoup
# So the Flow is like URL by using requests.get then use html parser tha is now call the beautiful soup 
# then remove the unwanted content and then finally get the text by get.text and then except so and so if error
@tool
def read_webpage(url: str) ->str:
    """ scrape and return clean texr and data from a url"""
    try:
        response=requests.get(url,timeout=10)
        soup=BeautifulSoup(response.text,"html.parser")
        for tag in soup(["script","style"]):
            tag.decompose()
            # MEANS KI JO JO HTML ME UNDER SCRIPT HOGA LIKE <SCRIPT .... <SCRIPT AUR SAME WITH SYLE 
            # TO YE CONTENT KO DISCARD KR DIYA DECOMPOSE KR DIYA KYUKI YE NI CHYE LLM KO SIRF KAM KA BHJO
        text=soup.get_text(separator=" ",strip=True)[:3000]
        return text
    except Exception as e:
        return "ERROR FETCHING THE URL"    
    