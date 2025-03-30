import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

#print("Row", df.loc[0])

### JSON ###
jsondf = pd.read_json("PandaJsonSample.json")
#print("JSON: ", jsondf.head(3))

print("Colories Collumn Of 5th Row: ", jsondf.loc[5]['Calories'])

### Bad Data
# Calories is missing row 0 & 3rd is NaN
jsondf2 = pd.read_json("PandaJsonSampleBadData.json").dropna()
print("Colories Collumn Of 5th Row: ", jsondf2)

# Row 1 & 2 are duplicates
jsondf3 = pd.read_json("PandaJsonSampleBadData.json").dropna().drop_duplicates()
print("Drop one of the duplicates: ", jsondf3)