from pprint import pprint

#get user integer input
userInt = int(input("Enter a number: "))
#btwn 0 and number: add if divisble by 3 == Fizz
fizzieList = [0]
for number in range(1, (userInt + 1)):
    if number % 3 == 0 and number %5 == 0:
        fizzieList.append("FizzBuzz")
    elif number % 3 == 0:
        fizzieList.append("Fizz")
    elif number %5 == 0:
        fizzieList.append("Buzz")
    else:
        fizzieList.append(number)

#if / by 5 Buzz
# if /3 and /5 FizzBuzz
# if neither add just number to list
for item in fizzieList:
    print(f"{item}")

total=0
fizzCount = 0
buzzCount = 0
fizzBuzzCount = 0
#loop over list and print each element
#print sum of all numbers
#add count of Fizz, Buzz, and FizzBuzz
for num in fizzieList:
    if type(num) == int:
        total = num + total
    elif num == "Fizz":
        fizzCount = fizzCount + 1
    elif num == "Buzz":
        buzzCount = buzzCount + 1
    else:
        fizzBuzzCount = fizzBuzzCount + 1

print(f"Total of Integers is :  {total} \n Fizz: {fizzCount} \n Buzz: {buzzCount} \n FizzBuzz: {fizzBuzzCount}")