#calculate the multiplication and sum of two numbers
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
if num1 * num2 <= 1000:
    print(num1 * num2)
else:
    print(num1 + num2)
    

#print the sum of current number and a previous number
print("printing current and previous number sum in a range(10)")
prev_num = 0
for i in range(1,11):
    x_sum = prev_num + i
    print("Current Number" , i, "Previous Number", prev_num, "Sum: ", x_sum)
    prev_num =  i


#print character present at an even index number
word = input("Enter word:")
print("original string:", word)
size = len(word)
print("Printing only even index chars")
for i in range(0, size - 1,2): #range(start,end,step)
    print("index[", i, "]", word[i])


#remove first n characters from a string
def remove_chars(word, n):
    print("original string: ", word)
    x = word[n:] #this string splicing s[start:end:step]. s[7:] -> character from index 7 to end. s[:5] -> character from start up to index 5. s[::2] -> every second character. s[1:8:3] -> every thrid character from index 1 to 8
    return x
print("removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))


#check if the first and last numbe rof a list are same
def first_last_same(numberlist):
    print("given list:", numberlist)
    
    first_num = numberlist[0] #access list first value
    last_num = numberlist[-1] #access list last value and for second last value can use -2
    
    if first_num == last_num:
        return True
    else:
        return False

number_x = [10,20,30,40,50,10]
number_y = [75, 65, 35, 75, 30]

print("result is", first_last_same(number_x))
print("result is", first_last_same(number_y))


#display number divisible by 5
num_list = [10,20,33,46,55]
print("given list is ", num_list)
print("divisible by 5")
for i in num_list:
    if i % 5 == 0:
        print(i)
    
#find the number of occurrences of substring in a string
str_x = input("enter your sentence: ")
word = input("enter a word you want to count: ")
times = str_x.count(word)
print(word, "appeared ", times, "times")


#print the pattern
for i in range(6):
    for j in range(i): #inner loop controls how many times the outer loop's i value is printed. range(1) → j = 0 (only one iteration).
        print(i, end=" ")
    print("\n")
    

#check palindrome number
def pallindrome(number):
    print("original number", number)
    original_number = number
    
    rev_num = 0
    while number > 0:
        remainder = number % 10
        rev_num = (rev_num * 10) + remainder
        number = number // 10
    
    if original_number == rev_num:
        print("given number pallindrome")
    else:
        print("given number not pallindrome")

pallindrome(121)
pallindrome(123)


#merge two lists using the following condition
list1 = [10,20,25,30,35]
list2= [40,45,60,75,90]

result_list = []

for n in list1:
    if n % 2 != 0:
        result_list.append(n)
        
for n in list2:
    if n % 2 == 0:
        result_list.append(n)

print("result list", result_list)


#get each digit from a number in reverse order
num = 7536
print("given number", num)
while num > 0:
    digit = num % 10
    num = num // 10
    print(digit, end=" ")
    
    
#calculate income tax
income = int(input("Enter your income: "))
tax_pay = 0
print("Given Income", income)

if income <= 10000:
    tax_pay = 0
elif income <= 20000:
    x = income - 10000
    tax_pay = x * 10/100
else:
    tax_pay = 0
    
    tax_pay = 10000 * 10/100
    
    tax_pay += (income - 20000) * 20 / 100
 
print("total tax to pay", tax_pay)


#print multiplication table from 1 to 10
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end=" ")
    print("\t\t")
    
    
#print a downward half-pyramid pattern of stars
for i in range(6, 0, -1):
    for j in range(0, i, -1):
        print("*", end=" ")
    print(" ")
    
#get an int value of base raises to power of exponent
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to power of", exp, "is: ", result)

exponent(2,5)
