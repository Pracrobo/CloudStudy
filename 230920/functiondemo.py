# lambda function
# BASH 
def calc_sum() :             # 함수 헤더 : 함수 정의
    sum = 0                  # 함수의 바디
    for i in range(1, 101):  # 함수의 바디
        sum += i             # 함수의 바디
    
    print(f'sum =  {sum}')   # 함수의 바디
    
calc_sum()  # 함수의 호출, Call by Name
calc_sum() 
calc_sum() 
