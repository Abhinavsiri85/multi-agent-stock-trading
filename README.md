# Multi Agent Stock Trading

## Overview
This project demonstrates a multi-agent system for stock market analysis and trading decisions using the CrewAI framework. The system defines specialized agents that work together to analyze stock performance and propose trading actions. The project integrates real-time financial data from Yahoo Finance via a custom research tool.

## Key Features
- Multi-agent collaboration using CrewAI  
- Real-time stock data retrieval through Yahoo Finance  
- Modular design with clear separation between agents, tasks, and tools  
- Extendable framework for new financial analysis or AI tools  

## Technologies Used
- Python 3.13  
- CrewAI  
- yFinance  
- OpenAI API (via CrewAI integration)  
- Pydantic  

## Project Structure
AI_Agents/
│
├── agents/
│ ├── analyst_agent.py # Defines the Analyst Agent responsible for stock analysis
│ └── trader_agent.py # Defines the Trader Agent responsible for trade decisions
│
├── tasks/
│ ├── analyze_task.py # Task for analyzing stock performance
│ └── trade_task.py # Task for making trading decisions
│
├── tools/
│ └── stock_research_tool.py # Tool to fetch stock data from Yahoo Finance
│
├── crew.py # Assembles agents and tasks into a working CrewAI pipeline
├── main.py # Entry point to execute the multi-agent trading system
├── requirements.txt # Python dependencies
├── env_template.txt # Example of environment variable setup
└── .gitignore # Git ignore configuration

##Components
Analyst Agent
  - Focuses on analyzing current stock market conditions, including price, percentage change, and volatility.

Trader Agent
  - Uses insights from the Analyst Agent to make trading decisions such as buy, hold, or sell.

Stock Research Tool
  - Custom tool that connects to Yahoo Finance to fetch stock prices and market data.

Crew Configuration
  - The crew.py file brings all components together, defining how agents collaborate to complete tasks.
