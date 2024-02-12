try:
    print(x)
except:
    print("NameError occurred")

try:
    num1 = 20
    num2 = 0
    print(num1 / num2)

except:
    print("ZeroDivisionError Occurred")



# User-defined function
try:
    def sum(first, second):
        return first + second

except:
    print("Exception occurred")
finally:
    print("success")





print(sum(10,20))
