# ---------------------------------------------
# import package to read json
# ---------------------------------------------
import json

# ---------------------------------------------
#  write function to load file and parse json
# ---------------------------------------------
def readJson(file):
    with open(file) as p:
        return json.load(p) 

# ---------------------------------------------
#  call 'readJson', load salaries
# ---------------------------------------------
salaries = readJson('./data.json')

# ---------------------------------------------
#  print all salaries
# ---------------------------------------------
print(salaries)

# ---------------------------------------------
# loop through list, only print salary field
# ---------------------------------------------
for salary in salaries['data']:
   print(float(salary[18]))

# ---------------------------------------------
#  add all salaries
# ---------------------------------------------