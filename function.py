
# Global Variable
n=2
def main ():
    # Variable declaration
    a=b=c=d=0
    # collect input from user
    # value 3, 6, 7
    a = int (input ("please enter value # 1: "))
    b = int (input ("please enter value # 2: "))
    c = int (input ("please enter value # 3: "))
    # call function Dallas
    d = Dallas (a, b, c)
    # Output
    print (a, b, c, d)
    # end of main
#function
def Dallas (r, s, t):
    # Local variable
    x=0
    # Calculation
    x = r + s * t + n
    return (x)
main()

    