from sqlalchemy import  create_engine
from sqlalchemy.engine import URL
import psycopg2
import os
from dotenv import load_dotenv

def load_data(customer_beh_df):
    load_dotenv()
    dbname = os.getenv("dbname")
    db_host = os.getenv("db_host")
    db_port = os.getenv("db_port")
    db_pass = os.getenv("db_pass")
    db_user = os.getenv("db_user")

    connection_url = URL.create(
        drivername="postgresql+psycopg2",
        username=db_user,
        password=db_pass,
        host=db_host,
        port=int(db_port),
        database=dbname
    )

    engine = create_engine(connection_url)
    print(customer_beh_df.head(5))
    customer_beh_df.to_sql('customer_behaviour', engine, schema='public', if_exists='replace', index=False)

    print('Data loaded to database')



