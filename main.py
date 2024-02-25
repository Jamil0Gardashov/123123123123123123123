import logging
logging.basicConfig(level=logging.DEBUG , filename="logss.txt" , filemode="w")
try:
    a = int(input())
    b = int(input())
    vibor = input("+ - * /")
    if vibor == "+":
        result = a + b
    elif vibor == "-":
        result = a - b
    elif vibor == "*":
        result = a * b
    elif vibor == "/":
        result = a / b

    print(result)
except :
    logging.error("Error")
