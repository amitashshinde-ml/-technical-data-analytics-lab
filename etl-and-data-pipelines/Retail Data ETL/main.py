from etl.extract import retail_extract
from etl.load import load_data
from etl.transform import transform_stores

def run_pipeline():
    print('*************pipeline started*****************')
    feature_df, sales_df, stores_df = retail_extract()
    fact_sales, dim_store, dim_feature, dim_date = transform_stores(feature_df, sales_df, stores_df)
    load_data(fact_sales, dim_store, dim_feature, dim_date)

    print('Pipeline complete')

if __name__=="__main__":
    run_pipeline()