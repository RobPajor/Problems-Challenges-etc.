## V.1.1.0 Code now fulfills all requirements and works for 6 digit numbers, Codewars kata has been passed

numberDict = {0:"zero", 1: "one", 2: "two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11: "eleven",
       12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
       18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50:"fifty", 60: "sixty", 70:"seventy",
       80: "eighty", 90: "ninety"}

def number2words(n):
    
    if len(str(n)) == 0:
        return None
    
    if len(str(n)) == 1:
        return numberDict[n]
    
    if len(str(n)) == 2:
        return lenght_two(n)
    
    if len(str(n)) == 3:
        return length_three(n)
    
    if len(str(n)) == 4:
        return length_four(n)
    
    if len(str(n)) == 5:
        return length_five(n)
    
    if len(str(n)) == 6:
        return lenght_six(n)

          
def lenght_two(n):
    if n == 0:
        return ""
    numberString = str(n)
    sol = ""
    if n < 20:
        return numberDict[n]
    sol = sol + numberDict[int(numberString[0] + "0")]
    if numberString[1] != "0" and numberString[0] != "0" and n > 20:
        sol += "-" + numberDict[int(numberString[1])]
    return sol

def length_three(n):
    if n == 0:
        return ""
    
    numberString = str(n)
    
    if len(numberString) < 3:
        return lenght_two(n)
    
    
    if lenght_two(int(numberString[1:3])) != "":
        hundreds = numberDict[int(numberString[0])] + " hundred " + lenght_two(int(numberString[1:3]))
    if lenght_two(int(numberString[1:3])) == "":
        hundreds = numberDict[int(numberString[0])] + " hundred" + lenght_two(int(numberString[1:3]))
    return hundreds

def length_four(n):
    numberString = str(n)
    if length_three(int(numberString[1:4])) != "":
        thousands = numberDict[int(numberString[0])] + " thousand " + length_three(int(numberString[1:4]))
    else:
        thousands = numberDict[int(numberString[0])] + " thousand"
    return thousands

def length_five(n):
    numberString = str(n)
    if length_three(int(numberString[2:5])) != "":
        tenThousands = lenght_two(int(numberString[0:2])) + " thousand " + length_three(int(numberString[2:5]))
    else:
        tenThousands = lenght_two(int(numberString[0:2])) + "thousand"
    return tenThousands

def lenght_six(n):
    numberString = str(n)
    if length_three(int(numberString[3:6])) != "":
        hundredThousands = length_three(int(numberString[0:3])) + " thousand " + length_three(int(numberString[3:6]))
    else:
        hundredThousands = length_three(int(numberString[0:3])) + "thousand"
    return hundredThousands

