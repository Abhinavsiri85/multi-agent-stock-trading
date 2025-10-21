from crewai import Task
from agents.trader_agent import trader_agent

trade_descision = Task(
    agent=trader_agent,
    description=("Use live market data and stock performance indicators for {stock} to make a strategic trading decision."
    "Assess keey factors such as current price, daily change percentage, volume trends, and recent momentum."
    "Based on your analysis, reccomend wether to **Buy**, **Sell**, or **Hold, the stock."),
    expected_output=("A clear and confident trading reccomendation (Buy/ Sell/ Hold), supported by:/n" \
    "- Current stock price and daily change\n" 
    "- Volume and market activity observations\n" \
    "- Justification for the trading action based on technical signals or risk-reward outlook"
    )
)