# def show_points(p, a, b):
#     return[(x,y) for x in range(p) for y in range(p) if (y*y - (x*x*x + a*x + b)) % p ==0]
# a = show_points(23,1,4)
# print(a)
# print(len(a))
list = [i for i in range(1,23)]
byg = []                    #用于存放本原根
List = []                   #用于存放遍历元素的测试集合
for i in list:
    key = 0                 #key清零
    for j in range(1,22):
        k = i**j % 23        #每个数1-20次方mod23
        if k==1 and j!=23:   #判断中途是否出现1，出现则证明不是本原根
            key = 1          #key = 1 用于标志该元素非本原根
            break
        elif k in List:
            key = 1
            break
        else:
            List.append(k)
    if key == 0:
        byg.append(i)
    List = []               #List初始化，以待下一轮迭代
print("23的本原根：" , byg)

