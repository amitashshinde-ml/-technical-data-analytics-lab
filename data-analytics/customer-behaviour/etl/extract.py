import pandas as pd

def customer_behaviour_extract():

    customer_beh_df = pd.read_csv(
        "E:\\Python Code\\technical-data-analytics-lab\\data-analytics\\customer-behaviour\\data\\customer_shopping_behavior.csv")

    print('Customer behaviour data')
    print(customer_beh_df.head(5))

    return customer_beh_df

