

total_hits = 0
total_bat = 0
total_bases = 0
single = 1
double = 2
triples = 3
batting_avg = total_hits / total_bat
slugging_avg = total_bases / total_bat
k = 0
while (k < 3):
    print("Fill in the data for player #", K +1)
    single_total = int (input("How many singles? "))
    double_total = int (input("How many doubles? "))
    triple_total = int (input("How many doubles? "))
    home_run = int (input("How many home run? "))
    time_bat = int (input ("How many times at bat? "))
    total_bases = (single_total * single) + (double * double_total) + (triple_total * triples)
    
    k = k + 1

