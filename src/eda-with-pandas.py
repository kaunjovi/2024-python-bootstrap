import pandas as pd 

def explore_data(csv = "src/telecom_churn.csv") : 
    print("Hello world. Exploratory Data Analysis") 
    
    telecom_data = pd.read_csv( csv)

    # start by just having a look 
    print(f"{ telecom_data.head() }")
    # You knew you were to get the top 10 rows. 
    # But, you have not got all the columns. Have you. 
    # Check what is the rows and columns of this dataset. 
    # print(f"{ telecom_data.shape }")

    # Fine. So now you know there are n number of columns. 
    # What are their names? 
    # print(f"{ telecom_data.columns }")

    # Knowning names is not enough. 
    # You need to know what is the type of data that they have boolean, object etc. 
    print(f"{ telecom_data.info() }")


    # print(f"{ telecom_data.describe() }")
    # print(f"{ telecom_data.describe( include=["bool"]) }")
    # print(f"{ telecom_data.describe( include=["object"]) }")

    # print(f"{ telecom_data["state"].value_counts() }")
    # print(f"{ telecom_data["international plan"].value_counts() }")
    
    # print(f"{ telecom_data["churn"].value_counts() }")
    # print(f"{ telecom_data["churn"].head() }")

    # What are average values of numerical features for churned users?
    # print(f"{telecom_data[ telecom_data["churn"]=="TRUE"].mean()}") 

    print(f"account length : { telecom_data[ telecom_data["churn"] == 'False']["account length"].mean()}")


if __name__ == "__main__" : 
    explore_data() 

