
# Global Variable

n=10
def main ():
    # Variable declaration
    num = 0
    avg = 0.0
    sumx = 0
    k = 0
    # using a loop to collect input from user
    while (k < 10):
        num = int (input ("Please enter a number: "))
        # add number to sumx
        sumx = sumx + num
        # increment k
        k = k + 1
    # compute average (outside the loop)
    avg = sumx/n
    # print sum and average
    print ("Sum =    ", sumx)
    print ("Average =    ", avg)    
    # hold screen
    dummy = input ("Press any key to continue")
main ()

    
        

