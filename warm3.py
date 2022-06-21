


n=2
def main():
    # Variable declaration
    a=b=c=d=e=f=0
    i=0
    # File declaration
    infile=open('data.txt','r')
    outfile=open('outdata.txt','w')
    # Use a loop to read from the data file
    while(i < 2):
        # Yank data set
        templist=infile.readline().strip('\n').split(',')
        a=int(templist[0])
        b=int(templist[1])
        c=int(templist[2])
        d=int(templist[3])
        e=int(templist[4])
        # Sum the data
        sumx=a+b+c+d+e+f
        # Print output to screen
        print(a,b,c,d,e,f,sumx)
        # Print the data set to the output file
        outfile.write(str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(e) + " " +str(sumx)+'\n')
        # Increment iterator
        i=i+1
    # Close file
    infile.close()
    outfile.close()
main()
