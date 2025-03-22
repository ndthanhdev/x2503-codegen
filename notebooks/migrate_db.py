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


# %%
client = get_client()


# %%
client.execute_mgmt(
    None,
    f"""
  .create database {DbConsts.name} persist (
    @"/kustodata/dbs/{DbConsts.name}/md",
    @"/kustodata/dbs/{DbConsts.name}/data"
    )
""",
)
# %%
# item_key,item_name,desc,unit_price,man_country,supplier,unit
# I00001,A&W Root Beer - 12 oz cans,a. Beverage - Soda,11.5,Netherlands,Bolsius Boxmeer,cans
client.execute_mgmt(
    DbConsts.name,
    f"""
  .create table {DbConsts.customer_table} (
    ItemKey:string,
    ItemName:string,
    Description:string,
    UnitPrice:real,
    ManufacturerCountry:string,
    Supplier:string,
    Unit:string
  )
""",
)

# %%
