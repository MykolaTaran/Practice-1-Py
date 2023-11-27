a = int (input ("Enter a: "))
while (a < 1 or a > 100):
    a = int(input ("Enter a: "))
b = int(input ("Enter b: "))
while (b < 1 or b > 100):
    b = int (input ("Enter again: "))
if a < b:
    r = ((a * b - 2) / a)
elif a==b:
    r = a + 25
else:
    r = a / b + 1
print("Result: ",r)