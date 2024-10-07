import pandas as pd 

if __name__ == "__main__" : 
    print(f"Hello from house. Pandas version : {pd.__version__}")
    melbourne_data = pd.read_csv("src/data/melb_data.csv")
    
    print(f"{ melbourne_data.head()}")


    # print(f"{ melbourne_data.shape}")
    # 21 columns. Cant see them with head. 

    print(f"{ melbourne_data.describe()}")
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

