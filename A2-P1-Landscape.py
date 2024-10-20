#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #:     W0239497
#Student Name:  Chauntel Smith

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Welcome message $ charge info 
    print("Welcome, to the Landscape Calculator! \nAll projects have a base charge of $1000 as well as projects over 5000sf have an additonal charge of $500\nplease enter your information below.")
    #user imput values
    hNumber = int(input("Enter house number: "))
    length = float(input("Enter propty depth (feet): "))
    width = float(input("Enter property width (feet): "))
    #variables
    sirfaceArea = length * width
    sirfaceCharge = 1000
    grassPSF = 0
    #calculate sirface area cost
    if sirfaceArea >=5000:
        sirfaceCharge = 1500
    #tree input
    treeNum = int(input("Trees are an additonal $100\nEnter number of trees you would like to add: "))
    #grass type input
    grassType =input("Grass types we offer are Fescue $0.05, Bentgrass $0.02, Campus $0.01\nPlease enter the name of your chosen grass type: ")
    if grassType.lower() == "fescue":
        grassPSF = 0.05
    elif grassType.lower() == "bentgrass":
        grassPSF = 0.02
    elif grassType.lower() == "campus":
        grassPSF = 0.01
    else:
        print("You have entered an invalid grass type, please start again.")
    #math variables
    grassCost = grassPSF * sirfaceArea
    treeCost = treeNum * 100
    TotalCost = grassCost + treeCost + sirfaceCharge
    #Total outcome
    print("\nTotal cost for house {0} is: ${1}\nDepth: {2}\nWidth: {3}\nGrass Type: {4}\nNumber of trees: {5}".format(hNumber,TotalCost,(int(length)),(int(width)),grassType,treeNum))
    # YOUR CODE ENDS HERE

main()