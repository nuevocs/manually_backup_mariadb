from sqlalchemy import create_engine, MetaData
import tomllib
import pandas as pd

with open(".env.toml", mode="rb") as fp:
    config = tomllib.load(fp)

user = config["db"]["mariadb"]["user"]
password = config["db"]["mariadb"]["pw"]
host = config["db"]["mariadb"]["host"]
port = config["db"]["mariadb"]["port"]
dbname = config["db"]["mariadb"]["db_name"]

db_url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}?charset=utf8mb4'

engine = create_engine(db_url)
meta = MetaData()
meta.reflect(bind=engine)
print(list(meta.tables.keys()))  # Print table names available in a database


def df_from_dbtable(table_name: str, engine_func):
    sql_statement = f"SELECT * from {table_name}"
    df = pd.read_sql_query(sql=sql_statement, con=engine_func)
    df.to_csv(f"{table_name}.csv", index=False)
    print(df)


# df_from_dbtable("table_name", engine)
