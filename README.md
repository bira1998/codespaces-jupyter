Always-On AI Agent
An AI-powered autonomous agent built using Python, LangChain, LangGraph, and Ollama. The project demonstrates AI planning, memory management, human approval, task execution, and scheduled automation.

Features
AI Planning: Generates step-by-step plans using Llama 3.2. 
Long-Term Memory: Stores and retrieves user preferences using SQLite.
Human Approval: Requests user approval before executing tasks.
Tool Execution: Uses custom Python tools to save tasks and create notes.
Workflow Management: Uses LangGraph to manage the agent workflow.
Weekly Scheduler: Runs the agent every Monday at 9:00 AM IST.
Error Handling: Handles runtime errors using Python try-except.
Tech Stack
Python 3.12
LangChain
LangGraph
Ollama
Llama 3.2
SQLite
APScheduler
Project Structure
always-on-ai-agent/
│
├── agent.py
├── memory.py
├── tools.py
├── scheduler.py
├── agent_memory.db
├── agent_notes/
└── README.md
Installation
Clone the repository.
Create and activate a Python virtual environment.
Install the required packages:
pip install langchain langgraph langchain-ollama apscheduler
Install and start Ollama.
Download the model:
ollama pull llama3.2
Run the Agent
python agent.py
Run the Scheduler
python scheduler.py
The scheduler is configured to run every Monday at 9:00 AM IST.

Learning Objectives
This project demonstrates practical implementation of Agentic AI concepts, including planning, memory, human-in-the-loop approval, tool integration, workflow orchestration, and scheduled execution.

Author
Rohit Biradar
