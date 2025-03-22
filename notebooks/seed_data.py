# ruff: noqa: E402

# %%
# import sys
from pathlib import Path
import kagglehub
import shutil
from libs.settings import settings
import libs.paths as Paths
from libs.db_consts import DbConsts
from libs.kusto_client import get_client

# Download latest version
path = kagglehub.dataset_download("mmohaiminulislam/ecommerce-data-analysis")
print("Path to dataset files:", path)

# %%
Paths.KUSTO_DATA_FILES_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

print(f"Emptying {Paths.KUSTO_DATA_FILES_CSV_PATH.absolute()}")
shutil.rmtree(Paths.KUSTO_DATA_FILES_CSV_PATH, ignore_errors=True)

print(f"Moving {path} to {Paths.KUSTO_DATA_FILES_CSV_PATH.absolute()}")
Path(path).rename(Paths.KUSTO_DATA_FILES_CSV_PATH.absolute())

# %%
client = get_client()

# %%

# empty the table
client.execute_mgmt(
    DbConsts.name,
    f"""
  .clear table {DbConsts.customer_table} data
""",
)

# %%
client.execute_mgmt(
    DbConsts.name,
    f"""
  .ingest into table {DbConsts.customer_table} (@"{Paths.CONTAINER_KUSTO_DATA_FILES_CSV_ITEM_PATH.absolute()}")
""",
)
# %%
response = client.execute_query(
    DbConsts.name,
    f"""
  {DbConsts.customer_table}
""",
)
for row in response.primary_results[0]:
    print(row[0], " ", row["ItemName"])
# %%
