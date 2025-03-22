from pathlib import Path

# Path to Kusto data files
KUSTO_DATA_FILES_CSV_PATH = Path.cwd() / ".local/kustodata/files/csvs"
KUSTO_DATA_DBS_PATH = Path.cwd() / ".local/kustodata/dbs"

#
CONTAINER_KUSTO_DATA_FILES_CSV_PATH = Path("/kustodata/files/csvs")
CONTAINER_KUSTO_DATA_FILES_CSV_ITEM_PATH = Path("/kustodata/files/csvs/item_dim.csv")