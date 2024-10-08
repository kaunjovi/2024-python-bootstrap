import pandas as pd 
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


if __name__ == "__main__" : 
    print(f"Hello from house. Pandas version : {pd.__version__}")
    melbourne_data = pd.read_csv("src/data/melb_data.csv")
    
    print(f"{ melbourne_data.head()}")


    # print(f"{ melbourne_data.shape}")
    # 21 columns. Cant see them with head. 

    print(f"{ melbourne_data.describe()}")

    # Works in Jupyter. How to in py file. 
    # pd.DataFrame.hist(melbourne_data, 'YearBuilt')

    # even this is not fitting the screen. Will have to find a way to download. 

    # Picking just one column. 
    # Rooms         Price 
    # count  13580.000000 -- rows with non missing values. 
    # mean       2.937997 -- average 
    # std        0.955748 -- standard deviation 
    # min        1.000000 
    # 25%        2.000000 
    # 50%        3.000000 
    # 75%        3.000000 
    # max       10.000000 

    # print(f"{ melbourne_data.columns}")
    # Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG',
    #    'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
    #    'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude',
    #    'Longtitude', 'Regionname', 'Propertycount'],
    #   dtype='object')


    # print(f"{ melbourne_data.info()}")
     #   Column         Non-Null Count  Dtype  
    # ---  ------         --------------  -----  
    # 0   Suburb         13580 non-null  object 
    # 1   Address        13580 non-null  object 
    # 2   Rooms          13580 non-null  int64  
    # 3   Type           13580 non-null  object 
    # 4   Price          13580 non-null  float64
    # 5   Method         13580 non-null  object 
    # 6   SellerG        13580 non-null  object 
    # 7   Date           13580 non-null  object 
    # 8   Distance       13580 non-null  float64
    # 9   Postcode       13580 non-null  float64
    # 10  Bedroom2       13580 non-null  float64
    # 11  Bathroom       13580 non-null  float64
    # 12  Car            13518 non-null  float64
    # 13  Landsize       13580 non-null  float64
    # 14  BuildingArea   7130 non-null   float64
    # 15  YearBuilt      8205 non-null   float64
    # 16  CouncilArea    12211 non-null  object 
    # 17  Lattitude      13580 non-null  float64
    # 18  Longtitude     13580 non-null  float64
    # 19  Regionname     13580 non-null  object 
    # 20  Propertycount  13580 non-null  float64
    # dtypes: float64(12), int64(1), object(8)

    # dropna drops missing values (think of na as "not available")
    # why did 13,580 go down to 6,196
    melbourne_data = melbourne_data.dropna(axis=0)
    print(f"{ melbourne_data.info()}")

    # #   Column         Non-Null Count  Dtype  
    # ---  ------         --------------  -----  
    # 0   Suburb         6196 non-null   object 
    # 1   Address        6196 non-null   object 
    # 2   Rooms          6196 non-null   int64  
    # 3   Type           6196 non-null   object 
    # 4   Price          6196 non-null   float64
    # 5   Method         6196 non-null   object 
    # 6   SellerG        6196 non-null   object 
    # 7   Date           6196 non-null   object 
    # 8   Distance       6196 non-null   float64
    # 9   Postcode       6196 non-null   float64
    # 10  Bedroom2       6196 non-null   float64
    # 11  Bathroom       6196 non-null   float64
    # 12  Car            6196 non-null   float64
    # 13  Landsize       6196 non-null   float64
    # 14  BuildingArea   6196 non-null   float64
    # 15  YearBuilt      6196 non-null   float64
    # 16  CouncilArea    6196 non-null   object 
    # 17  Lattitude      6196 non-null   float64
    # 18  Longtitude     6196 non-null   float64
    # 19  Regionname     6196 non-null   object 
    # 20  Propertycount  6196 non-null   float64
    # dtypes: float64(12), int64(1), object(8)
    # memory usage: 1.0+ MB

    # y is generally predicition data 
    y = melbourne_data.Price 
    # print(f"{ y.head() }")

    # X is the training data, by convention 
    features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    X = melbourne_data[features]
    print(f"{X.head()}")
    print(f"{ X.describe() }")

    melbourne_model = DecisionTreeRegressor(random_state=1)
    melbourne_model.fit(X, y)
    # At this point the model should have an opinion. 
    # Let's check

    print(f"{melbourne_model.predict( X.head() )}") 

    predicitions = melbourne_model.predict( X)
    print(f"MAE = {mean_absolute_error ( predicitions, y )}")






