import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

def load_data( filtered = True) : 
    data = pd.read_csv("src/data/melb_data.csv")  
    print(f"{ data.columns }")
    if filtered == True : 
        return data.dropna(axis=0) 
    else : 
        return data 

def extract_X_y( data ) : 
    y = melb_data.Price
    features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
    X = melb_data[features]
    return X, y

def calculate_mae(max_leaf_nodes, train_X, val_X, train_y, val_Y) : 
    model = DecisionTreeRegressor( max_leaf_nodes = max_leaf_nodes ) 
    model.fit(train_X, train_y)
    predictions = model.predict(val_X)
    mae = mean_absolute_error(val_Y, predictions)
    print(f"Leaf nodes [{max_leaf_nodes}],  MAE [{ mae }]")
    return mae 

if __name__ == "__main__" : 

    # print(f"Panda version : {pd.__version__}")

    # load data
    # melb_data = load_data(False) # 13580 rows 
    melb_data = load_data() # 6195 rows, filtered, dropna  
    print(f"Shape : {melb_data.shape}")

    # extract X (features) and y (the value you would like to predict)
    # y = ground truth 
    X, y = extract_X_y( melb_data)

    # split training and verification data
    train_X, val_X, train_y, val_Y = train_test_split( X, y, random_state = 1 )

    # Use training data to train a model. 
    # Predict the output using that model. 
    # Check how far apart on average your predictions to real answer is (MAE)
    model = DecisionTreeRegressor( max_leaf_nodes = 5 ) 
    model.fit(train_X, train_y)
    predictions = model.predict(val_X)
    mae = mean_absolute_error(val_Y, predictions)
    print(f"MAE [{ mae }]")


    # compare MAE to find the best fitment 
    for leaf_nodes in [5,50,500, 5000, 5] : 
        calculate_mae(leaf_nodes, train_X, val_X, train_y, val_Y)
    
