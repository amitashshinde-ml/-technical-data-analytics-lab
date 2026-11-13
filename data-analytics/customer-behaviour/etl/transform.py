import pandas as pd
from IPython.terminal import pt_inputhooks


def transform_data(customer_beh_df):
    customer_beh_df["New_Review_Rating"] = customer_beh_df.groupby("Category")['Review Rating'].transform(
        lambda x: x.fillna(x.median()))

    customer_beh_df.columns = customer_beh_df.columns.str.lower()
    customer_beh_df.columns = customer_beh_df.columns.str.replace(' ', '_')
    customer_beh_df.columns = customer_beh_df.columns.str.replace('(', '')
    customer_beh_df.columns = customer_beh_df.columns.str.replace(')', '')

    labels = ['Young Adults', 'Adults', 'Middle Ages', 'Senior']
    customer_beh_df['age_group'] = pd.qcut(customer_beh_df['age'], q=4, labels=labels)

    frequency_mapping = {'Fortnightly': 14, 'Weekly': 7, 'Annually': 365, 'Quarterly': 90, 'Bi-Weekly': 14,
                         'Monthly': 30, 'Every 3 Months': 90}
    customer_beh_df["frequency_of_purchases_days"] = customer_beh_df["frequency_of_purchases"].map(frequency_mapping)

    customer_beh_df = customer_beh_df.drop('promo_code_used', axis=1)

    print('Data cleansed...')

    return customer_beh_df