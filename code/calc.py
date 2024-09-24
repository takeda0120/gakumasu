import yaml

with open("code/data.yml", "r") as yml:
    data = yaml.safe_load(yml)
    
def last(score):
    score = int(score)
    if score >= 1770:
        score = 1800
        return score
    elif 0 <= score < 1770:
        score += 30
        return score
    
def hard(rank,para):
    ax = para
    print(ax)
    if 5000 * 0.3 > ax:#1500
        x = ax / 0.3

    elif 5000 * 0.3 + 5000 * 0.15 > ax:#2250
        x = (ax - 5000 * 0.3 + 5000 * 0.15) / 0.15

    elif 5000 * 0.3 + 5000 * 0.15 + 10000 * 0.08 > ax:#3050
        x = (ax - 5000 * 0.3 - 5000 * 0.15 + 10000 * 0.08) / 0.08

    elif 5000 * 0.3 + 5000 * 0.15 + 10000 * 0.08 + 10000 * 0.04 > ax:#3450
        x = (ax - 5000 * 0.3 - 5000 * 0.15 - 10000 * 0.08 + 20000 * 0.04) / 0.04

    elif 5000 * 0.3 + 5000 * 0.15 + 10000 * 0.08 + 10000 * 0.04 + 10000 * 0.02 > ax:
        x = (ax - 5000 * 0.3 - 5000 * 0.15 - 10000 * 0.08 - 10000 * 0.04 + 30000 * 0.02) / 0.02
   
    else:
        x = (ax - 5000 * 0.3 - 5000 * 0.15 - 10000 * 0.08 - 10000 * 0.04 - 10000 * 0.02 + 40000 * 0.01) / 0.01
    return int(x)

p_Vo, p_Da, p_Vis = input("半角{vocal,dance,vis}>>>").split(",")
#p_Vo, p_Da, p_Vis = 1500, 1200, 1000
sum_para = last(p_Vo) + last(p_Da) + last(p_Vis)
all_1 = sum_para * 2.3 + 1700
needs = {
    "S+": int(data["rank"]["S+"] - all_1),
    "S": int(data["rank"]["S"] - all_1),
    "A+": int(data["rank"]["A+"] - all_1),
    "A": int(data["rank"]["A"] - all_1)
}
#print(needs)
#1000,1000,1000

needsp = {
    "S+": hard("S+",int(data["rank"]["S+"] - all_1)),
    "S": hard("S",int(data["rank"]["S"] - all_1)),
    "A+": hard("A+",int(data["rank"]["A+"] - all_1)),
    "A": hard("A",int(data["rank"]["A"] - all_1))
}
print(needsp)