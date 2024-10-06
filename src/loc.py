import pandas as pd 

if __name__ == "__main__" : 

    # Creating the DataFrame
    df = pd.DataFrame({"A":[12, 4, 5, None, 1],
        "B":[7, 2, 54, 3, None],
        "C":[20, 16, 11, 3, 8],
        "D":[14, 3, None, 2, 6]})
    
    print(f"Data frame : {df}")

    a = df.loc[:, "A"]
    print(f"Data frame : {a}")