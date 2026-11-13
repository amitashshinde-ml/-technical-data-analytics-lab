from sqlalchemy import  create_engine
from sqlalchemy.engine import URL
import psycopg2
import os
from dotenv import load_dotenv


def load_data(fact_sales,dim_store,dim_feature,dim_date):
    load_dotenv()
    dbname =os.getenv("dbname")
    db_host= os.getenv("db_host")
    db_port=os.getenv("db_port")
    db_pass =os.getenv("db_pass")
    db_user= os.getenv("db_user")


    connection_url = URL.create(
        drivername="postgresql+psycopg2",
        username=db_user,
        password=db_pass,
        host=db_host,
        port=int(db_port),
        database=dbname
    )

    engine = create_engine(connection_url)
    dim_store.to_sql('dim_store', engine, schema='public',if_exists='replace', index= False )
    fact_sales.to_sql('fact_sales', engine, schema='public', if_exists='replace', index=False)
    dim_feature.to_sql('dim_feature', engine, schema='public', if_exists='replace', index=False)
    dim_date.to_sql('dim_date', engine, schema='public', if_exists='replace', index=False)

    print('Data Loaded')