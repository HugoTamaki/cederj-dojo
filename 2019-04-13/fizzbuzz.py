
def fizz_buzz(num):
    fb = ""
    if num % 3 == 0:
        fb += "Fizz"
    if num % 5 == 0:
        fb += "Buzz"
    return fb or num


    # if  num % 3 != 0 and num % 5 != 0:
    #     return num
    # elif num % 3 == 0 and num % 5 == 0 :
    #     return "FizzBuzz"
    # elif  num % 3 == 0:
    #     return "Fizz"
    # elif num % 5 == 0 :
    #     return "Buzz"
