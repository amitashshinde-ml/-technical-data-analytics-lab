import  pandas as pd
from etl.extract import retail_extract

def transform_stores(feature_df,sales_df,stores_df):

    dim_store = stores_df.drop_duplicates().reset_index(drop=True)

    sales_df["Date"] = pd.to_datetime(sales_df["Date"],dayfirst=True)
    dim_date=sales_df[['Date','IsHoliday']]
    dim_date['year']= dim_date['Date'].dt.year
    dim_date['month'] = dim_date['Date'].dt.month
    dim_date['week'] =  dim_date['Date'].dt.isocalendar().week.astype(int)

    feature_df["Date"] = pd.to_datetime(feature_df["Date"])
    MarkDown1_clmns = ['MarkDown1','MarkDown2','MarkDown3','MarkDown4','MarkDown5']
    feature_df=feature_df.drop(columns=MarkDown1_clmns, errors='igonre')
    dim_feature = feature_df.drop_duplicates().reset_index(drop=True)

    fact_sales=sales_df.copy()

    def col_lower(df):
        df.columns=df.columns.str.lower()
        return df

    dim_date=col_lower(dim_date)
    dim_feature=col_lower(dim_feature)
    dim_store=col_lower(dim_store)
    fact_sales = col_lower(fact_sales)

    return fact_sales,dim_store,dim_feature,dim_date

