#Addition function 
def add_func ():
    val_1 = int(input("What is the first integer value?"))
    val_2 = int(input("What is the second integer value?"))

    sum_val = val_1 + val_2

    usr_choice = input("Would you like to add another integer value to this sum? (Y/N)")
    
    while usr_choice != "Y" and usr_choice != "y" and usr_choice != "N" and usr_choice != "n":
        usr_choice = input(" (ಠ_ಠ) Please make a valid selection... (Y/N)") #User input error prevention

    while usr_choice != "n" and usr_choice != "N": #Option of adding additional values selected by user
        val_3 = int(input("What is this value?"))
        sum_val += val_3
        usr_choice = input("Would you like to add another integer value to this sum? (Y/N)")

    print("The sum of these values is " + str(sum_val) + ".")

#Subtraction function
def subtr_func ():
    val_1 = int(input("What is the integer minuend? (The number being diminished)"))
    val_2 = int(input("What is the integer subtrahend? (The part subtracted)"))

    dif_val = val_1 - val_2

    usr_choice = input("Would you like to subtract another integer value from this difference? (Y/N)")
    
    while usr_choice != "Y" and usr_choice != "y" and usr_choice != "N" and usr_choice != "n": #User input error prevention
        usr_choice = input(" (ಠ_ಠ) Please make a valid selection... (Y/N)")

    while usr_choice != "n" and usr_choice != "N": #Option of subtracting additional values selected by user
        val_3 = int(input("What is this value?"))
        dif_val -= val_3
        usr_choice = input("Would you like to subtract another integer value from this difference? (Y/N)")

    print("The difference of these values is " + str(dif_val) + ".")

#Multiplication function
def multi_func ():
    val_1 = int(input("What is the first integer value?"))
    val_2 = int(input("What is the second integer value?"))

    prod_val = val_1 * val_2

    usr_choice = input("Would you like to multiply this product by another integer value? (Y/N)")
    
    while usr_choice != "Y" and usr_choice != "y" and usr_choice != "N" and usr_choice != "n": #User input error prevention
        usr_choice = input(" (ಠ_ಠ) Please make a valid selection... (Y/N)")

    while usr_choice != "n" and usr_choice != "N": #Option of multiplying additional values selected by user
        val_3 = int(input("What is this value?"))
        prod_val *= val_3
        usr_choice = input("Would you like to multiply this product by another integer value? (Y/N)")

    print("The product of these values is " + str(prod_val) + ".") 

#Division function
def div_func ():
    val_1 = int(input("What is the dividend? (Number being divided)"))
    val_2 = int(input("What is the divisor? (Number to divide by)"))

    quot_val = val_1 // val_2
    rem_val = val_1 % val_2

    usr_choice = input("Would you like to divide this quotient by another integer value? (Y/N)")
    
    while usr_choice != "Y" and usr_choice != "y" and usr_choice != "N" and usr_choice != "n": #User input error prevention
        usr_choice = input(" (ಠ_ಠ) Please make a valid selection... (Y/N)")

    while usr_choice != "n" and usr_choice != "N": #Option of dividing additional values selected by user
        val_3 = int(input("What is this value?"))
        rem_val = quot_val % val_3
        quot_val //= val_3
        
        usr_choice = input("Would you like to divide this quotient by another integer value? (Y/N)")
    if rem_val == 0:
        print("The quotient of these values is " + str(quot_val) + ".")
    else:
        print("The quotient of these values is " + str(quot_val) + " and " + str(rem_val) + "/" + str(val_3))

#Calculator interface
oper_pick = input("Please choose an operation (1-4): \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n")

while oper_pick != "1" and oper_pick != "2" and oper_pick != "3" and oper_pick != "4": #User input error prevention
        usr_choice = input(" (ಠ_ಠ) Please make a valid selection... (1, 2, 3 or 4)")

if oper_pick == "1":
    add_func()
elif oper_pick == "2":
    subtr_func()
elif oper_pick == "3":
    multi_func()
else:
    div_func()