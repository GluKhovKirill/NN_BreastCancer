import requests
import pandas as pd
import json


df = pd.read_csv('validate.csv').drop("Unnamed: 0", axis=1) # Read csv
y, X = df['diagnosis'], df.drop('diagnosis', axis=1) # Split X & y

#Post request to Flask app
resp = requests.post('http://127.0.0.1:4862', 
                     data={'X_rows': json.dumps([list(i) for i in X.values])})
if resp: # OK 200
    ans=json.loads(resp.text)
else:
    ans = []
    print("Err. Wrong response.")

# Calculate accuracy (and MAE) of the model
c=0
for pred, real in zip(ans, y):
    if pred == real: 
        c += 1
accuracy = round(100*c/len(y), 2)

print(f"Accuracy:\t{accuracy}%\nMAE:\t\t{round(100-accuracy, 3)}%")