from sqlalchemy import  create_engine
import psycopg2

def load_data(fact_sales,dim_store,dim_feature,dim_date):
    dbname = 'retail_db'
    db_host= 'localhost'
    db_port=5432
    db_pass ='DB123'
    db_user= 'postgres'

    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{dbname}')

    dim_store.to_sql('dim_store', engine, schema='public',if_exists='replace', index= False )
    fact_sales.to_sql('fact_sales', engine, schema='public', if_exists='replace', index=False)
    dim_feature.to_sql('dim_feature', engine, schema='public', if_exists='replace', index=False)
    dim_date.to_sql('dim_date', engine, schema='public', if_exists='replace', index=False)

    print('Data Loaded')