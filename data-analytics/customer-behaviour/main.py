from etl.extract import customer_behaviour_extract
from etl.transform import transform_data
from etl.load import load_data

def main():
    df= customer_behaviour_extract()
    df = transform_data(df)
    load_data(df)


if __name__=="__main__":
    main()