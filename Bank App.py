files = open("Transaction Log.txt", "w")

print("Enter your PIN to continue")
password = int(input("PIN: "))

files.write("Card Holder:\tL. Mbula \n")
files.write("PIN:\t" + str(password)+"\n")

yes = "1"
no = "2"
bal = 10000

if password == 10846:
    print("\nWelcome, Mr. L. Mbula\n")
    print("Would you like to make a transaction?\n 1. Yes\n 2. No")

transaction = int(input())

if transaction == 1:
    print("Would you like to make a Deposit, Withdrawal, or Check balance \n 1. Deposit\n 2. Withdrawal \n 3. Check Balance")
    option = int(input())
    if option == 1:
        print("Enter the amount to Deposit: ")
        deposit = float(input("R"))
        new_bal = bal + deposit
                
        files.write("Money In:\t" + str(deposit)+"\n");            
        files.write("Balance:\t" + str(new_bal)+"\n")
                
        print('R', deposit , "has been deposited into your account succesfully \nAnd your Current Balance is: R", new_bal)

    elif option == 2:
        print("Enter the amount you want to withdraw: ")
        withdraw = float(input("R"))
        new_bal = bal - withdraw
                
        files.write("Money Out:\t" + str(withdraw)+"\n")
        files.write("Balance:\t" + str(new_bal))
                
        print("\n""R",-withdraw, "has been deducted from your account succesfully\nAnd your Current Balance is: R", round(new_bal, 2))

    elif option == 3:
        print("Your Current Balance: \nR", bal)

    elif option > 3:
        print("Sorry, you've entered an invalid number!")
        files.write("You provided an invalid input")    
        
    else:            
        print("\n You provided an invalid input")
        files.write("You provided an invalid input")
                
else:
    print("Thank you for your time, please take your card!")
    files.write("The transactions were cancelled")
    
files.close()