#7. Program to find Greatest Common Divisor of two numbers.
num1 = int(input("Enter First number: "))
num2 = int(input("Enter second number: "))

if num2 > num1:
    min = num1
else:
    min = num2
#as per number line concept (0,1,2......m, n) iterate till the min number of the given two numbers by the user 
# as the min number cant be divided by a greater number than that.
# so i keeps updating until the final dividing number is found of which the remainder of the division is 0.  
#That number i itself is the highest comman factor or Greatest comman divisor
for i in range(1, min+1):
    if num1%i == 0 and num2%i==0:
        hcf = i

print(f"The GCD/HCF of these two numbers is {hcf}")