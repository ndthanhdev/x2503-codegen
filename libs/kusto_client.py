from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from libs.settings import settings

def get_client():
    """
    Get a KustoClient instance initialized with the connection string from settings.
    
    Returns:
        KustoClient: An initialized Kusto client
    """
    return KustoClient(
        KustoConnectionStringBuilder.with_no_authentication(settings.kql_connection_string)
    )
