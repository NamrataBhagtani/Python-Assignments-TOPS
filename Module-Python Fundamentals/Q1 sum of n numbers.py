#  Write a python program to sum of the first n positive integers.
#Method to find the sum of integers with variable range

# num1 = int(input("Enter the first number"))

# num2 = int(input("Enter the last number"))

# sum = (num2*(num1 + num2))/2

# print(sum)

#Method to find the sum of integers having range starting from 1 to n
def total_sum(num):
    sum_t = 0
    for i in range(1, num+1):
    
        sum_t += i
        # i = i+1
        # if sum == num+1:
        #     print(sum)
    return sum_t

num = int(input("Enter the number: "))        
sum_n = total_sum(num)
print(f"The sum of first n positive numbers is {sum_n}")
    
