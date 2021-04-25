import random
database = {
    7549124946: ['oluwatobi' , 'olubunmi' , 'olujas1@gmail.com' , 'zuri_56', 5000]
} 


def init():

    
    print("Welcome to Zuri Guaranty Trust Bank")

    haveAccount = int(input("Do you have an account with us: 1 (Yes) 2 (No) \n"))

    if (haveAccount == 1):
        login()

    elif (haveAccount == 2):
        register() 

    else:
        print("You have selected an invalid option") 

        init()  


def login():
    print("***** Login *****")

    accountNumberGenerated = int(input("Please enter your account number\n"))
    password = input("Please enter your password \n")
    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberGenerated):
            if(userDetails[3] == password):
                bankOperation(userDetails)
        else:
            print("Sorry, you have entered an invalid account number or password or probably details not stored in our database ")
            login()
                    

                    



def register():
    print ("****** Register ******")
    email = input("Enter your email address \n")
    firstName = input("What is your first name? \n")
    lastName = input("What is your last name? \n")
    password = input("Create a password \n") 

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ firstName, lastName, email, password]
    print("Your account has been created")
    print("*************************************")
    print(f" Your account number is: {accountNumber}")
    print(" Make sure you keep it safe")
    print("*************************************")
    login() 


def bankOperation(user):
    print(f" Welcome { user[0]} {user[1]} ")
    


    selectedOption = int (input ("What would you like to do? (1) Check Balance (2) Deposit (3) Withdraw (4) Logout (5) Exit \n"))


    if(selectedOption == 1):
        checkBalance(user)  
     
    elif(selectedOption == 2):
        depositOperation(user)

    elif(selectedOption == 3):
        withdrawalOperation(user)

    elif(selectedOption == 4):
        Logout()

    elif(selectedOption == 5):
        init()

    else:
        print("Invalid option selected")
        bankOperation(user) 



def secondBankOperation(user):
    print(f" Dear, { user[0]} {user[1]} ")
    


    selectedOption = int (input ("Would you like to perform other operations? (1) Check Balance (2) Deposit (3) Withdraw (4) Logout (5) Exit \n"))


    if(selectedOption == 1):
        checkBalance(user)  
     
    elif(selectedOption == 2):
        depositOperation(user)

    elif(selectedOption == 3):
        withdrawalOperation(user)

    elif(selectedOption == 4):
        Logout()

    elif(selectedOption == 5):
        init()

    else:
        print("Invalid option selected")
        bankOperation(user) 


def checkBalance(user):
    print(f" Your current balance is { user[4] } ")
    secondBankOperation(user)()
    

           
def withdrawalOperation(user):
    checkBalance(user)()
    
    userWithdraw= int(input("How much would you like to withdraw? \n"))

    print('****Please take your cash****')
    secondBankOperation(user)()
     


def depositOperation(user):
    deposit_amount = int(input("please enter deposit amount \n"))

    print(f"{deposit_amount} is credited to your account")
    secondBankOperation(user)()

   
def generationAccountNumber():

    return random.randrange(1111111111 , 9999999999)  



def Logout():
    login()
    
    
  
# print (generationAccountNumber())

init()