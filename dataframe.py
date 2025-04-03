import pandas as pd
import yaml

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print("Initial DF", df.loc[1])

print(" #### NEXT ####")

### JSON ###
jsondf = pd.read_json("PandaJsonSample.json")
jsondf.info()
print("JSON: ", jsondf.to_string())

#print("Colories Collumn Of 5th Row: ", jsondf.loc[5]['Calories'])

print(" #### NEXT ####")
### Bad Data Excersices 
# Calories is missing row 0 & 3rd is NaN
jsondf2 = pd.read_json("PandaJsonSampleBadData.json").dropna()
#print("Colories Collumn Of 5th Row: ", jsondf2)

# Row 1 & 2 are duplicates
jsondf3 = pd.read_json("PandaJsonSampleBadData.json").dropna().drop_duplicates()
#print("Drop one of the duplicates: ", jsondf3)

print(" #### NEXT ####")
# Dates are wrong
df = pd.read_json("PandaJsonSampleBadDate.json")
df2 = df[df['Dates']!="0000/12/19"]
#print("DF2: ", df2['Dates'].loc[0])
df2['Dates'] = pd.to_datetime(df2['Dates'])
#print("Dates: ", df2.to_string())

#### YAML ####
print(" #### NEXT YAML ####")

## TODO: This does not work correctly?
d = yaml.safe_load('Employee.yaml')
print("Data: ", d)
#testdf = pd.DataFrame(d)
#print(testdf.to_string())


yaml_data_correct = """
- name: Apple
  price: 1.0
- name: Banana
  price: 0.5
"""

yamldf = pd.DataFrame(yaml.safe_load(yaml_data_correct))
yml = yamldf[yamldf['name'] == 'Apple']
print(yml.to_string())




