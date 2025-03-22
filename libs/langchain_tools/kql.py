from langchain_core.tools import tool
from libs.kusto_client import get_client


@tool
def execute_kql_query(query: str) -> dict:
    """
    This function is a tool that can be used to execute Kusto queries.
    """
    data = None
    with get_client() as client:
        response = client.execute(None, query)
        data = response.primary_results[0].to_dict()
    return data
