def fibonacci(num):
    series = [0]
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while counter <= num :
        counter = counter + 1 
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        series.append(sum)
    print(f"The fibonacci series of {num} numbers is {series}")
    
num = int(input('Enter the number to generate Fibonacci series: '))
fibonacci(num)    