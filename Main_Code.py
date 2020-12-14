import pickle
from coffee import Coffee


intro = "\nWelcome to the EOQ Calculator prepared by Nitya, Divya and Holly"
mainmenu = "\nMain Menu:\nA)dd to an existing file \nL)oad a file and view results \nP)rint current results \nR)eset and perform new EOQ calculations \nS)ave current calculations to a file \nQ)uit:\n"
question = "Enter q to quit and display the results or the name of the coffee to continue\n"
nofile = "\nThe file doesn't exist\n"
nocalc = "\nThere are no calculations to display\nLoad a file or perform new calculations\n"
noact = "\nThere are no accounts to display\nLoad a file or add new accounts\n"

def validate(vString):
    """ This function validates the inputs to be non-negative numeric values"""
    while True: 
        try: 
            if float(vString) >= 0:
                vString = int(float(vString))
                break
            else: 
                vString = input("Negative values are not accepted. Please provide a positive value:\n")
        except ValueError:
            vString = input("Non-numeric values are not accepted. Please provide a numeric value:\n")
    return vString

def newBrand(inputList):
    brand = str(input("Please enter the Brand: "))
    d = int(validate(input("Please enter Demand: ")))
    c = int(validate(input("Please enter Unit Cost: ")))
    coffee = Coffee(brand, d, c)
    inputList.append(coffee)
    printObjects(inputList)
    return inputList



def printObjects(inputList): #displays the results of eoq calcs a user performed for various brands of coffee
#for each coffee stored in coffeeObjects, it displays brand, cost, demand, order q, total cost, cycle length
    total = 0
    print("*********\n\nThe Results of EOQ Calculations\n\n*********")
    print('{0:15} {1:15} {2:15} {3:15} {4:15} {5:15}'.format("Name", "C($)", "Demand", "Q(lbs)", "TAC($)", "T(weeks)"))
    for i in inputList:
        print(i)
    print("\nIf you purchase all of the coffee, you will need space to hold  lbs. of coffee.\n")
        
    
    
def load_data(filename="accountObjects"):
    """ Load the objects stored in file using the pickle module and creates a list of objects """
    # Open file to read
    accountObjects = pickle.load(open(filename, 'rb'))# Read the objects directly from the file and create a list of objects. No need to call the constructor. This time I'm returning the list. So that you can see the different use. Make sure look at the main for the calls to this function. 
    return accountObjects
        
def store_data(inputList, filename = 'accountObjects'):
    """ Allows the user to store data in a list to the text file named filename. """
    pickle.dump(inputList, open(filename, 'wb')) # Dump the objects on the list to a file 
    
    
    
def main():
    
    database = []
    done = False
    accountObjects = database
    while not done:
        cmd = input(mainmenu)       
        if cmd.lower() == 'a':
            try:               
                newBrand(accountObjects)
            except NameError: 
                print(noact)
                
        elif cmd.lower() == 's':
            try:
                filename = input('Enter a filename. Hit enter key for the default file (accountObjects):')
                if filename:                                            # Checks to see if filename is given
                    store_data(accountObjects, filename)
                else:
                    store_data(accountObjects)                          # Uses the default if filename is not given
            except Exception as e:      # Fails if accountObjects list cannot be found or filename is not acceptable
                print(e)                # Print the exception
                print(noact)
                input("Hit enter to go to the main menu\n")
                
        elif cmd.lower() == 'p':
            try:
                printObjects(accountObjects)
            except UnboundLocalError: 
                print(nocalc)
                input("Hit enter to go to the main menu\n")               
            except: pass
        elif cmd.lower() == 'r':
                dataList = []
                try:               
                    newBrand(accountObjects)
                except NameError: 
                    print(noact)                
        elif cmd.lower() == 'l':
            while True:
                try:
                    filename = input('Enter a filename. Hit enter key for the default file (accountObjects):')
                    if filename: 
                        accountObjects = load_data(filename)           # Checks to see if filename is given
                    else:
                        accountObjects = load_data()                    # Uses the default if filename is not given
                    break
                except FileNotFoundError:                               # Fails if accountObjects file cannot be found
                    print(nofile)
            printObjects(accountObjects)
            
        elif cmd.lower() == 'q':
            done = True
        
if __name__ == '__main__':
      main()