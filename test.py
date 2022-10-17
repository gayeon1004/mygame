import mod1

# 두 수를 입력 받게 만들고
num1 = int(input("첫번째 수 입력:")) #문자로 입력되기 때문에 숫자로 변경
num2 = int(input("두번째 수 입력:")) #문자로 입력되기 때문에 숫자로 변경
# 메뉴 1. 더하기 2. 빼기
print("1. 더하기 2. 빼기")
num = int(input('선택:'))
# 만약에 1를 누르면 두수의 더한 결과값
if num == 1:
    result = mod1.add(num1, num2)
# 만약에 2를 누루면 두수의 뺀 결과값
elif num == 2:
    result = mod1.sub(num1, num2)
# 출력되게 해보자
print('결과값:', result)