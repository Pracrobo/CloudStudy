# lambda function
# BASH 
def calc_sum(start, end) :   #Parameter, 매개변수  # 함수 헤더 : 함수 정의
    sum = 0                                  # 함수의 바디
    for i in range(start, end+1):                  # 함수의 바디
        sum += i
        
    return sum # 함수의 끝

start = 50
end = 70
result = calc_sum(start, end)

print("%d 부터 %d까지의 합은 %d입니다." %(start,end, result))
# print("%d 부터 %d까지의 합은 %d입니다." %(start, end, calc_sum(start,end)))
#   # argument, 인수, 인자, call by value
