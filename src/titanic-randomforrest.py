from sklearn.ensemble import RandomForestClassifier
import pandas as pd 




if __name__ ==  "__main__" : 
    print("Hello Random Forest")

    train_data = pd.read_csv("src/train.csv")
    test_data = pd.read_csv("src/test.csv")
    # print(train_data.head())
    # print(f"{ train_data.columns}")
    # print(f"{ train_data.info()}")

    y = train_data["Survived"]
    print(y.head())

    features = ["Pclass", "Sex", "SibSp", "Parch"]
    X = pd.get_dummies(train_data[features])
    X_test = pd.get_dummies(test_data[features])

    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
    model.fit(X, y)
    predictions = model.predict(X_test)

    output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
    print(f"{ output.head(10)}")