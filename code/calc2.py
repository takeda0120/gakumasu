import yaml

with open("code/data.yml", "r") as yml:
    data = yaml.safe_load(yml)



rank = str(input(">>>"))

maxmin = data["cost"][rank]
print(maxmin)
