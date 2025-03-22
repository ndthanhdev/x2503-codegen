# ruff: noqa: E402
# %% Loading environment variables
from typing import Annotated
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    Field,
)
from langgraph.prebuilt import ToolNode, tools_condition
from libs.langchain_state import State
from libs.settings import settings
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict
from langchain_core.tools import tool
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from IPython.display import Image, display
from langgraph.prebuilt import create_react_agent
from libs.langchain_tools.kql import execute_kql_query

# %% Creating tools

# %% Creating LLMs
llm = ChatOpenAI(
    api_key=settings.open_ai_key,
    model="o1",
)
# %% Agents
agent = llm.bind_tools([execute_kql_query])


# %% Nodes
def chatbot(state: State):
    return {"messages": [agent.invoke(state["messages"])]}

tool_node = ToolNode(tools=[execute_kql_query])
# %% Edges


# %% Build graph
graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
# Any time a tool is called, we return to the chatbot to decide the next step
graph_builder.add_edge("tools", "chatbot")
graph_builder.set_entry_point("chatbot")
graph = graph_builder.compile()
# Any time a tool is called, we return to the chatbot to decide the next step
graph = graph_builder.compile()

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass
# %%
def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break

# %%
