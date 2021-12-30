dict = {"яблоко" : "красное", "банан" : "желтый", "лимон" : "желтый"}
for i in dict.items():
    print(i)

del(dict["банан"])
print(dict)