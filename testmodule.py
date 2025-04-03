# A module with some dummy data to test importing it

personList = [
    {
        "name": "Abhinav",
        "lname": "Yadav",
    }, 
    {
        "name": "ACE",
        "lname": "BASE",
    }
]

def iterateOverMe(itrObj):
    for i in itrObj:
        print("Value: ", i)

def iterateOverDict(dict):
    for key in dict:
        print("Key: ", key, " Value: ", dict[key])

def iterateOverPersonList():
    for person in personList:
        print(person["name"], " ", person["lname"])


def generatorTemp():
    for person in personList:
        yield person


def generatorTemp2():
    return (person for person in personList)