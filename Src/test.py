#coding:utf-8

ab = ["1,2","2","3","4"]

for i in range(len(ab)):
    t = ab[i].split(",")
    t[0] = [5]
    ab[i].split(".")[0] = 5

print(ab)
