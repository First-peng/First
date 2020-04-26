# -*- coding: UTF-8 -*-
print("\n\t欢迎光临Python商城!!!\n")

go_shopping = True  #False or True
cart = []

dict_1 = {'aaa' : 6688,'bbb' : 1488,'ccc' : 80,'aaaabbbb' : 100}     #字典{键值对}
products = [('华为',6688),('wine',1488),('Book',80),('MateBook',100)]   #列表[元祖]

str_1 = "<商品列表>"
print(str_1.center(46,"-"))

num_2 = 0
for name_into,price_into in dict_1.items():
    num_2 += 1
    # print(name_into,price_into)
    # print("\t%d、%s\t\t￥%s"% (products.index(name_into) + 1 , name_into[0], name_into[1]))
    # print("\t%d、%s\t\t%s"% (num_2, name_into, price_into))
    print("\t{}、{:<10}\t￥{}".format(num_2,name_into,price_into))
print("\t5、退出")
print("-"*50)

if go_shopping:
    print("买!")
else:
    print("不买!")

while go_shopping:
    try:
        num = int(input('请输入商品编号[1/2/3/4/5]: \t>>>'))
        if num >= 6 or num < 1:
            print('商品不存在!!!')
        elif 5 == num:
            break
        else:
            if num in cart:
                print('该商品已在购物车')
            else:
                print('添加商品成功')
                cart.append(num)
    except:
        break