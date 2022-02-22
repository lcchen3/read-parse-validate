# -------------------------------------
# import package to read json
# import package to walk file system
# -------------------------------------
import json
import glob #be able to use specified patterns

# -----------------------------------
#  list all files
# -----------------------------------
pattern = './data/*/*.json' #inside data, just grab json files

data = []
for file in glob.glob(pattern):
    data.append(file) #append into something called data

print(data)
# -----------------------------------
#  loop through files, parse json
# -----------------------------------
def readJson(file):
    with open(file) as p:
        return json.load(p)

for file in data:
    banana = readJson(file) #don't want to change source file
    print(banana)