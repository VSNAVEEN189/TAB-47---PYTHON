a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"a = {a} -> {bin(a)}")
print(f"b = {b} -> {bin(b)}")

and_result = a & b
print(f"a & b = {and_result} -> {bin(and_result)}")

or_result = a | b
print(f"a | b = {or_result} -> {bin(or_result)}")

xor_result = a ^ b
print(f"a ^ b = {xor_result} -> {bin(xor_result)}")

left_result = a << 1
print(f"a << 1 = {left_result} -> {bin(left_result)}")

right_result = a >> 1
print(f"a >> 1 = {right_result} -> {bin(right_result)}")