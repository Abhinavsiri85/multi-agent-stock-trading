from crewai import Agent, LLM

from tools.stock_research_tool import get_stock_price

llm = LLM(
    model="groq/llama-3.3-70B-versatile",
    temperature=0.0
)

analyst_agent = Agent(
    role= "Financial Market Analyst",
    goal=("Perform in-depth evaluations of publicly traded stocks using real-time data,"
    "identyfying trends, performance insights, and key financial signals to support decision-making"),
    backstory= ("You are a veteran financial analyst with deep expertise in interepreting stock market data,"
    "technical trends, and fundamental analysis. You speacialize in well structured reports that evaluate stock"
    "perfomance using live market indicators"),
    llm=llm, 
    tools=[get_stock_price],
    verbose=True
)