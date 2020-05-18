decimal=int(input("Enter a decimal number"))

def convert(number):
    romans = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,'V': 5, 'IV': 4, 'I': 1}
    result=""

    for roman in romans.keys():
        while number >= romans[roman]:
            result += roman
            number -= romans[roman]
    return result

print(convert(decimal))
