#destiney cardenas
#10/2024


def grn_or_org():
    answer = input("Green(1) or Orange(2)? ")
    if answer.lower() == "green" or answer == "1":
        print('You are a Scaliene Triangle')
        return True
    elif answer.lower() == "orange" or answer == "2":
        print("You are a Square")
        return True
    else:
        print("Please enter a valid response")
def blu_or_sil():
    answer = input("Blue(1) or Silver(2)? ")
    if answer.lower() == "blue" or answer == "1":
        print('You are a Rhombus')
        return True
    elif answer.lower() == "silver" or answer == "2":
        print("You are a Dodecahedron")
        return True
    else:
        print("Please enter a valid response")
        return False
def sam_or_red():
    answer = input("Salmon(1) or Red(2)? ")
    if answer.lower() == "salmon" or answer == "1":
        print('You are a Trapezoid')
        return True
    elif answer.lower() == "red" or answer == "2":
        print("You are an Octagon")
        return True
    else:
        print("Please enter a valid response")
        return False
def tan_or_gol():
    answer = input("Tan(1) or Gold(2)? ")
    if answer.lower() == "tan" or answer == "1":
        print('You are a Cone')
        return True
    elif answer.lower() == "gold" or answer == "2":
        print("You are a Star")
        return True
    else:
        print("Please enter a valid response")
        return False
def chi_or_coo():
    answer = input("Chips(1) or Cookies(2) ")
    if answer.lower() == "chips" or answer == "1":
        go = False
        while go == False:
            go = grn_or_org()
    elif answer.lower() == "cookies" or answer == "2":
        go = False
        while go == False:
            go = blu_or_sil()
    else:
        print("Please enter a valid response")
        return False
def buf_or_sth():
    answer = input("Buffet(1) or Steakhouse(2) ")
    if answer.lower() == "buffet" or answer == "1":
        go = False
        while go == False:
            go = sam_or_red()
    elif answer.lower() == "steakhouse" or answer == "2":
        go = False
        while go == False:
            go = tan_or_gol()
    else:
        print("Please enter a valid response")
        return False
def mod_or_ret():
    answer = input("Modern(1) or Retro(2 )")
    if answer.lower() == "modern" or answer == "1":
        go = False
        while go == False:
            go = chi_or_coo()
    elif answer.lower() == "retro" or answer == "2":
        go = False
        while go == False:
            go = buf_or_sth()
    else:
        print("Please enter a valid response")
        return False
def questions():
    go = False
    while go == False:
        go = mod_or_ret()

#main
questions()
