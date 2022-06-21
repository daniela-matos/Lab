
def main():
    k=0
    while (k<3):
        print ("Please enter values for house # ", k+1, "?")
        house_price = int (input ("How much is the house? "))
        fuel_cost_annual = int (input("How much is the fuel cost? "))
        tax_rate = float (input("How much is the tax? "))
        period = 5
        house_total_cost = float ((house_price * tax_rate) + (fuel_cost_annual * period) + house_price)
        k = k +1
        print("The total house cost for house", k, "for", period, "years is: $",house_total_cost)
main()



    