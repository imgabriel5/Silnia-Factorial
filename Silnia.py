# Napisz funkcję liczącą silnię dla podanej przez użytkownika w argumencie liczby.
# Write a function that counts the factorial for the number given by the user.
def factorial(L):
    if L == 0:
        return 1
    else:
        return L * factorial(L-1)
print(factorial(5))
print('------------------------------------------------------------------------------------------------------')
def power(number):
    if number == 0:
        return 1

    return number * power(number - 1)
print(power(5))