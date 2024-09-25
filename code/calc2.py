import yaml

with open("code/data.yml", "r") as yml:
    data = yaml.safe_load(yml)

cc = 5

rank = str(input(">>>"))

maxmin = data["cost"][rank]
print(maxmin)

cd = data["card2"].values()
print(cd,type(cd))
for i in cd.values():
    print(i)


