import  pandas as pd

def retail_extract():
    feature_df= pd.read_csv("E:\\Python Code\\technical-data-analytics-lab\\etl-and-data-pipelines\\Retail Data ETL\\data\\Features_dataset.csv")
    print("Feature Dataframe")
    print(feature_df.head(2))
    print(feature_df.dtypes)

    sales_df=pd.read_csv("E:\\Python Code\\technical-data-analytics-lab\\etl-and-data-pipelines\\Retail Data ETL\\data\\sales_dataset.csv")
    print("Sales Dataframe")
    print(sales_df.head(2))
    print(sales_df.dtypes)

    stores_df=pd.read_csv("E:\\Python Code\\technical-data-analytics-lab\\etl-and-data-pipelines\\Retail Data ETL\\data\\stores_dataset.csv")
    print("Stores Dataframe")
    print(stores_df.head(2))
    print(stores_df.dtypes)

    return feature_df,sales_df,stores_df
