
# %% Loading environment variables
from typing import Annotated
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    Field,
)
from libs.langchain_nodes.basic_tool_node import BasicToolNode
from libs.settings import settings
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from IPython.display import Image, display
from langgraph.prebuilt import create_react_agent
from libs.langchain_tools.kql import execute_kql_query

class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]