n1 = int(input("輸入數字A:"))
n2 = int(input("輸入數字B:"))
op = input("輸入一個四則運算符號(加+,減-,乘*,除/,整除//):")

if op == "+" :
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/": 
    print(n1/n2)
elif op == "//":
    print(n1//n2)
    
else:
    print("符號輸入錯誤")