import json
import random

with open('config/data.json') as data_file:
    data = data_file.read()
    data2 = json.loads(data)
print(random.choice(data2['knugenLinks']))
