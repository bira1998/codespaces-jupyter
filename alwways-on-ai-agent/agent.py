import traceback
from memory import remember, recall

from tools import TOOLS
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model ="llama3.2",
    base_url="http://localhost:11434"
)


# 1. Agent ki memory/state
class AgentState(TypedDict):
    goal: str
    plan: list
    results: list
    status: str


# 2. Planning function
def plan_task(state):

    goal = state["goal"]

    print("\nAI Planning Started...")

    prompt = f"""
    You are an intelligent AI agent.

    User Goal: {goal}

    Create a clear step-by-step execution plan.
    Give only 3 to 5 steps.
    """

    response = llm.invoke(prompt)

    steps = response.content.split("\n")

    steps = [
        step.strip()
        for step in steps
        if step.strip()
    ]

    print("AI Generated Plan:")
    for step in steps:
        print(step)

    return {
        "plan": steps,
        "status": "planned"
    }


# 3. Execution function
def execute_task(state):
    results = []

    goal = state["goal"]

    print("\nChecking Agent Memory...")

    memories = recall("user-001")

    print("Previous Memories:", memories)
    
    print("MY SAVED PREFERENCE:", memories.get("preference", "No memory found"))

    print("\nAI Execution Started...")
    
    approval = input(
       "\nDo you approve this task? (yes/no): "
    )

    if approval.lower() != "yes":
        print("Task rejected by user.")
        return {
        "results": ["Task rejected"],
        "status": "rejected"
    }

    TOOLS["save_task"](goal)

    for step in state["plan"]:
        print("Executing:", step)

        results.append("Completed: " + step)

    TOOLS["create_note"](
        "weekly_report.txt",
        "\n".join(results)
    )

    return {
        "results": results,
        "status": "completed"
    }

# 4. Create AI Agent workflow
builder = StateGraph(AgentState)

builder.add_node("planner", plan_task)
builder.add_node("executor", execute_task)

builder.add_edge(START, "planner")
builder.add_edge("planner", "executor")
builder.add_edge("executor", END)

# 5. Compile agent
agent = builder.compile()


# 6. Give agent a goal
try:
    result = agent.invoke({
        "goal": "Prepare a weekly AI research report",
        "plan": [],
        "results": [],
        "status": "started"
    })

    print("\nFINAL RESULT")
    print(result)

except Exception as e:
    print("\nAgent Error:", e)
    traceback.print_exc()


# 7. Display result

