# 1,2,3,4,5
# list_ = [1,2,3,4,5]
# for in list_ :
#     pass

# for num in[1,2,3,4,5] : 
#     print(num, end = '\t')
# print()
count = 0
for num in range(1, 101):
    if num % 7 == 0 :
        print(num, end  = '\t')
        count += 1
        if count % 5 == 0 :
            print()
print()