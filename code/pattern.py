from itertools import combinations

f = open("data2.txt", "w")

dl = []

def sum_dict_combinations(input_dict):
    results = {}
    
    # 全てのキーのリストを取得
    keys = list(input_dict.keys())
    for combo in combinations(keys, 5):
        combo_sum = sum(input_dict[key] for key in combo)
        combo_str = ','.join(sorted(combo))  # キーを文字列として結合し、ソート
        results[combo_sum] = results.get(combo_sum, []) + [combo_str]
    
    # 1から全てのキーの数までの組み合わせを考える
    # n = 6
    # for r in range(1,n):
    #     for combo in combinations(keys, r):
    #         combo_sum = sum(input_dict[key] for key in combo)
    #         combo_str = ','.join(sorted(combo))  # キーを文字列として結合し、ソート
    #         results[combo_sum] = results.get(combo_sum, []) + [combo_str]
    
    return results

# 使用例
allp = {
    "01LR": 30,#低銀
    "03R": 45,#銀
    "05LSR": 75,#低金
    "07SR": 105,#金
    "09SSR": 150,#虹
    "11SU": 96,#サポ
    "02pLR": 39,#低銀+
    "04pR": 60,#銀+
    "06pLSR": 102,#低金+
    "08pSR": 141,#金+
    "10pSSR": 204,#虹色+
    "12pSU": 126,#サポ+
}

result = sum_dict_combinations(allp)

# 結果を表示
Smax = 642
Amin = 441
for total, combos in result.items():
    for combo in combos:
        if Amin <= total <= Smax:
            dl.append([total]+[combo])
            #print(f"{total}[{combo}],")
            s = str(total) + combo + "," + "\n"  # 改行を追加
            f.write(s)

f.close()
#print(dl)
#print(dl[0][1].split(","))
#print(len(dl))
tc = 0
for lis in dl:
    check_p = 0
    check = lis[1].split(",")
    check_p += check.count("11SU")
    check_p += check.count("12pSU")
    if check_p > 1:
        dl.remove(lis)
        #print("サポカが2枚検出されました")
        tc += 1
#print(tc)
#print(len(dl))
#print(dl)
fdl = []
for s in dl:
    #print(s)
    a = s[1]
    #print(a.split(","))
    A = a.split(",")
    TEXT = ""
    for c in range(len(A)):
        b = A[c]
        B = b.replace("01LR", "低銀").replace("02pLR", "低銀+").replace("03R","高銀").replace("04pR", "高銀+").replace("05LSR", "低金").replace("06pLSR", "低金+").replace("07SR", "金").replace("08pSR", "金+").replace("09SSR", "虹").replace("10pSSR", "虹+").replace("11SU", "サポカ").replace("12pSU", "サポカ+")
        #print(B)
        TEXT += B
        if c != len(A)-1:
            TEXT += ","
    fdl.append([s[0],[TEXT]])
    #print(TEXT)

    #a.replace("01LR", "低銀").replace("02pLR", "低銀+").replace("03R","高銀").replace("04pR", "高銀+").replace("05LSR", "低金").replace("06pLSR", "低銀+").replace("07SR", "金").replace("08pSR", "金+").replace("09SSR", "虹").replace("10pSSR", "虹+").replace("11SU", "サポカ").replace("12psU", "サポカ+")
    #fdl.append(s[0],a)
print(fdl)