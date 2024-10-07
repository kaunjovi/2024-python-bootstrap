import pandas as pd 

print(f"Pandas version { pd.__version__}")

if __name__ == "__main__" : 
    print(f"Hello.")
    
    train_data = pd.read_csv("src/train.csv")


    print(f"Train data")
    print(f"Shape = {train_data.shape}")
    print(f"Columns = {train_data.columns}")
    print("Info =============")
    print(f"{train_data.info()}")
    
    print("Describe ========")
    print(f"{ train_data.describe()}")
    print(f"{ train_data.describe(include=["object", "bool"])}")

    print("Head ========")
    print(f"{ train_data.head() }")

