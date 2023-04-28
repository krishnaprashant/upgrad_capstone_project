import joblib
import pandas as pd

# load model
model = joblib.load("credit_card_model")

# load list of trasactions
transactions = pd.read_csv("transactions.csv").iloc[:, 1:]
result = []
for index,transaction in transactions.iterrows():
    result.append(model.predict([list(transaction)])[0])
transactions['result'] = result
# dump output of csv
transactions.to_csv("result.csv")