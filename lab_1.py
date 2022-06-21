
#input
percentage = 0.20
adult_t = 0
adult_price = 6.00
child_t = 0
child_price = 3.00
#output
gross_box_profit = (adult_t * adult_price) + (child_t * child_price)
net_box = gross_box_profit * percentage
theater_gross = gross_box_profit - net_box

def main():    
    movie_name = input("What's is the movie name? ")
    adult_t = int(input ("How many adults tickets were sold? "))
    child_t = int (input ("How many child tickets were sold? "))
    gross_box_profit = (adult_t * adult_price) + (child_t * child_price)
    net_box = gross_box_profit * percentage
    theater_gross = gross_box_profit - net_box
    print ("Movie name: ", movie_name)
    print("Adult Tickets Sold: ", adult_t)
    print("Child Tickets Sold: ", child_t)
    print("Gross Box Office Profit: ", gross_box_profit)
    print("Net Box Office Profit: ", net_box)
    print("Amount Paid to Movie Co", theater_gross)
main()