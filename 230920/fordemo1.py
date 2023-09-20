count, line = 0, 1
for i in range(65, 91) :
    if line % 2 == 1 : print(chr(i), end = '\t')
    else : print(chr(i+32), end = '\t')
    count += 1 # 5개면 줄바꿈
        if count % 5 == 0 : 
            print()
            line += 1
print()

# i : 관례적으로 쓰임, Interating
# 숫자를 글자로 만드는 
# 65 ~ 90 : 대문자 A-Z
# 97 ~ 122 : 소문자 a-z
#대문자와 소문자 차이 32
