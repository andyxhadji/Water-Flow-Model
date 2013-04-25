#***********************************************
#Percolation_v2.py
#Percolation module
#Finds if a given or generated array percolates
#Andreas Hadjigeorgiou - ahh2131
#Assignment 5 
#***********************************************
import numpy
import math
import pylab

def main():
    B = menu()
    D = copy_array(B)
    C = output_array(B)
    J = percolation(C)
    print J
    visualize(D, C)
    plot()
    
# menu asking to create a file or open a file
def menu():
    input = raw_input("Would you like to open an existing file?(y/n)")
    if input == 'y':
        B = array_from_file()
        
    if input == 'n':#ask to make your own array or to generate one
        input2 = raw_input("Would you like an array to be made for you?(y/n)")
        if input2 == 'n':
            array_to_file()
            B = array_from_file()
        else:
            B = random_array()
    return B
       
# create a blank array N x N to a file

def array_to_file():
    file_name = raw_input("What would you like to name your file? (add .txt)")
    outfile = open(file_name, 'w')#create text file
    dimen = raw_input("How many columns/rows are in your array? (1 number)")
    outfile.write(str(dimen)+ '\n')
    for x in range(0, int(dimen)):#user inputs numbers per row
        line = raw_input("Enter row of numbers separated by a space.")
        line = line + '\n'
        outfile.write(str(line))
    outfile.close() 

#create a blank array from a file
def array_from_file():
    input_file = raw_input("What is the name of input file?(add .txt)")
    infile = open(input_file, 'r')#open file
    
    global N
    N = int(infile.readline()) #read the first line to find size of array
    A = numpy.zeros((N, N))# empty matrix
    
    for x in range(0, N): #replaces empty matrix rows with int arrays from file
        temp1 = infile.readline()
        str_temp1 = temp1.split()
        int_temp1 = [int(item) for item in str_temp1]
        A = numpy.insert(A, [x], int_temp1, axis = 0)#insert row
        A = numpy.delete(A, [x+1], axis = 0)#delete row
    A = A.astype(bool)#convert to boolean
    infile.close()#close file
    return A      
    
# Take array from file and output with vacant/full sites
def output_array(B):
    E = numpy.zeros((N, N))
    for r in range (0, N):
        for t in range (0, N):
            E[r, t] = B[r, t]
    E = E.astype(bool)
    check = 2
    for x in range(1, N):      
        for y in range(0, N):#change first two rows to full/vacant
            if x == 1:
                if B[x, y] == False and B[x-1, y] == False:
                    B[x, y] = True
                    B[x-1, y] = True
                    #compares original array to changing array in order to
                    #determine if any other element in the row is also True
                    again = 'y'
                    w = 1
                    if (y-w) >= 0:
                        while again == 'y':
                            if E[x, y-w] == False:
                                B[x, y-w] = True
                                if y-(w + 1) >= 0:
                                    w = w + 1
                                else:
                                    again = 'n'
                            else:
                                again = 'n'                                                               
                elif B[x, y] == False and B[x-1, y] == True:
                    B[x-1, y] = False
                    B[x, y] = False
                    
                elif B[x, y] == True and B[x-1, y] == True:
                    B[x, y] = False
                    B[x-1, y] = False
                elif B[x, y] == True and B[x-1, y] == False:
                    B[x-1, y] = False
                    B[x, y] = False
            #everytime a row is made into open/vacant sites, next if statement
            #checks if there are any values which are adjacent to a True value
            #in the changed array, by comparing it to the original array.
            if x == check :              
                for u in range(0, N-1):
                    if E[(check-1), u+1] == False and B[(check-1), u] == True:
                        B[(check-1), u+1] = True
                check = check + 1
            if x != 1:#compare two rows at a time, change second row only
                if B[x, y] == False and B[x-1, y] == False:
                    B[x, y] = False
                elif B[x, y] == False and B[x-1, y] == True:
                    B[x, y] = True
                    again = 'y'
                    w = 1
                    if y-w >= 0:
                        while again == 'y':
                            if E[x, y-w] == False:                           
                                B[x, y-w] = True
                                if y-(w+1) >=0:
                                    w = w + 1
                                else:
                                    again = 'n'
                            else:
                                again = 'n'
                elif B[x, y] == True and B[x-1, y] == True:
                    B[x, y] = False
                elif B[x, y] == True and B[x-1, y] == False:
                    B[x, y] = False
    return B

#Output a boolean indicating percolation
def percolation(C):
    J = 0
    for y in range(0, N):#check last row for any True values
        if C[N-1, y] == True:
            J = True
            break;
    if J != True:
        J = False
    return J

# Generates a NxN boolean array of open/blocked sites
def random_array():
    p = input("Input the probability that a site will be open. (0-1)")
    global N
    N = input("Enter the row/column of the array.")
    A = numpy.random.rand(N, N)# creates an array N x N containing numbers 0-1
    for x in range(0, N):
        for y in range(0, N):#change numbers to 0 or 1 depending on probability
            if A[x, y] <= p:
                A[x, y] = 0
            else:
                A[x, y] = 1
    return A

def visualize(B, C):
    #creates a ppm file showing the flow
    flow_file = open('flow.ppm', 'w')
    length_block = int(math.floor(1000/N))
    flow_file.write('P3' + '\n')
    flow_file.write(str(N*length_block))
    flow_file.write(' ')
    flow_file.write(str(N*length_block) + '\n')
    flow_file.write('255' + '\n')
    #makes blocks of the elements in the array one line at a time,
    #outputting each line to the ppm file as a color, depending
    #on the comparison between the original and final array.
    for y in range (0, N):
        for w in range(0, length_block):
            for z in range(0, N):
                if B[y, z] == False and C[y, z] == True:
                    flow_file.write((length_block) * "117 178 221 ")
                if B[y, z] == False and C[y, z] == False:
                    flow_file.write((length_block) * "75 56 56 ")
                if B[y, z] == True and C[y, z] == False:
                    flow_file.write((length_block) * "170 21 26 ")
    flow_file.close()
    
def copy_array(B):
    #creates a copy of array B
    E = numpy.zeros((N, N))
    for r in range (0, N):
        for t in range (0, N):
            E[r, t] = B[r, t]
    E = E.astype(bool)
    return E

def plot():
    #creates an array of the probability of percolation and plots it
    #versus the probability of a vacant site.
    qe = numpy.arange(0, 1.0, .01, dtype=float)
    p = 0.4
    k = 0.0
    qw = numpy.zeros(100)
    while p <=.8:
        for w in range(0, 999):
            #each probability is calculated using 100 random arrays
            B = numpy.random.rand(N, N)
            for q in range(0, N):
                for z in range(0, N):
                    if B[q, z] <= p:
                        B[q, z] = 0
                    else:
                        B[q, z] = 1
            E = numpy.zeros((N, N))
            for r in range (0, N):
                for t in range (0, N):
                    E[r, t] = B[r, t]
            E = E.astype(bool)
            check = 2
            for x in range(1, N):      
                for y in range(0, N):
                    if x == 1:
                        if B[x, y] == False and B[x-1, y] == False:
                            B[x, y] = True
                            B[x-1, y] = True
                            again = 'y'
                            w = 1
                            if (y-w) >= 0:
                                while again == 'y':
                                    if E[x, y-w] == False:
                                        B[x, y-w] = True
                                        if y-(w + 1) >= 0:
                                            w = w + 1
                                        else:
                                            again = 'n'
                                    else:
                                        again = 'n'                                                               
                        elif B[x, y] == False and B[x-1, y] == True:
                            B[x-1, y] = False
                            B[x, y] = False
                            
                        elif B[x, y] == True and B[x-1, y] == True:
                            B[x, y] = False
                            B[x-1, y] = False
                        elif B[x, y] == True and B[x-1, y] == False:
                            B[x-1, y] = False
                            B[x, y] = False
                    if x == check :              
                        for u in range(0, N-1):
                            if E[(check-1), u+1] == False and B[(check-1), u] == True:
                                B[(check-1), u+1] = True
                        check = check + 1
                    if x != 1:
                        if B[x, y] == False and B[x-1, y] == False:
                            B[x, y] = False
                        elif B[x, y] == False and B[x-1, y] == True:
                            B[x, y] = True
                            again = 'y'
                            w = 1
                            if y-w >= 0:
                                while again == 'y':
                                    if E[x, y-w] == False:                           
                                        B[x, y-w] = True
                                        if y-(w+1) >=0:
                                            w = w + 1
                                        else:
                                            again = 'n'
                                    else:
                                        again = 'n'
                        elif B[x, y] == True and B[x-1, y] == True:
                            B[x, y] = False
                        elif B[x, y] == True and B[x-1, y] == False:
                            B[x, y] = False





            
            J = 0
            for q in range(0, N):#check last row for any True values
                if B[N-1, q] == True:
                    k = k + 1.0
                    break;
        qw[p*100] = k/1000
        k = 0
        p = p + .01
    while p > .8 and p <= 1.0:
        qw[p*100] = 1.0
        p = p + .01
        #pylab library is used to plot the two arrays
    pylab.plot(qe, qw)
    pylab.xlabel('Vacancy Probabiliy')
    pylab.ylabel('Percolation Probability')
    pylab.title('Vacancy Probability Vs. Percolation Probability')
    pylab.grid(True)
    pylab.savefig('percolation_plot')
    pylab.show()
        
            
                    
    

