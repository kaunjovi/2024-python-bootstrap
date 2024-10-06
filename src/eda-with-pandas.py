import pandas as pd 

def explore_data(csv = "src/telecom_churn.csv") : 
    print("Hello world. Exploratory Data Analysis") 
    
    telecom_data = pd.read_csv( csv)

    print(f"{ telecom_data.head() }")
    print(f"{ telecom_data.shape }")
    print(f"{ telecom_data.columns }")
    print(f"{ telecom_data.info() }")
    print(f"{ telecom_data.describe() }")
    
    print(f"{ telecom_data.describe( include=["bool"]) }")
    print(f"{ telecom_data.describe( include=["object"]) }")

    print(f"{ telecom_data["state"].value_counts() }")

if __name__ == "__main__" : 
    explore_data() 

