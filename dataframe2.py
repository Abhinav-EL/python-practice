import pandas as pd

#### NEXT Replace ####
rdf = pd.DataFrame({"Student1":['OK','Awful','Acceptable'], 
                   "Student2":['Perfect','Awful','OK'], 
                   "Student3":['Acceptable','Perfect','Poor']})

rdf = rdf.replace({'OK': 'A', 'Awful': 'F', 'Acceptable': 'C', 'Perfect': 'A+', 'Poor': 'D'})
#print("Replaced DF: ", rdf)

#### Splitting ####
df = pd.DataFrame({"Age": [34, 22, 19], 
                   "PlusOne":[0,0,1], 
                   "Ticket":["23:44:55", "66:77:88", "43:68:05 56:34:12"]})

# Inspect your DataFrame `df`
#print(df)
# Series

series = pd.Series(df['Age'])
#print("Series: ", series)
#print("Series Apply Double: ", series.apply(lambda x:x * 2))
#print("Serries Map: ", series.map(lambda x: x*2))


#### PIVOT ####
# Construct the DataFrame
products = pd.DataFrame({'category': ['Cleaning', 'Cleaning', 'Entertainment', 'Entertainment', 'Tech', 'Tech'],
                       'store': ['Walmart', 'Dia', 'Walmart', 'Fnac', 'Dia','Walmart'],
                       'price':[11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
                       'testscore': [4, 3, 5, 7, 5, 8]})

#print( products)

pivotedProducts = products.pivot(index='category', columns='store', values='price')
#print( pivotedProducts)

### MELT ###
people = pd.DataFrame({'FirstName' : ['John', 'Jane'],
                       'LastName' : ['Doe', 'Austen'],
                       'BloodType' : ['A-', 'B+'],
                       'Weight' : [90, 64]})

print(people)
print(pd.melt(people, id_vars=['FirstName', 'LastName'], var_name='measurements'))

#for index, row in people.iterrows():
#    print("FName: ", row['FirstName'], "LName: ", row['LastName'], " Index: ",index)