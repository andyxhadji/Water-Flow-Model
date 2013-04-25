Water-Flow-Model (Python)
=========================

Creates ppm file of dimensions specified containing open and closed blocks. Water is poured from the top and its flow can be visualized.

percolation.py

When the program runs, you will be prompted to open an existing file or not.
If you respond with 'y', you will be asked to input the name of the input file.
The input file is expected to have the dimension in the first line, then 
the first row of the array in the second line, with a space in between each number,
and so on.
If you respond with 'n', you will then be asked if you want an array generated randomly.

If you respond with 'yes', you will then be prompted to input the dimensions of the array.
After that, you will be shown your random array and a boolean value indicated whether
or not the array percolates.
If you respond with 'n', you will be asked the name of a text file you want to output.
After this, you will be asked to input the dimensions of the array.
Next, you will input 1's and 0's with spaces in between for each row as indicated by 
the dimensions you included. Make sure to put the correct number of 1's and 0's in each row.
Then you will be asked to input the name of the input file. 
Finally, a boolean value will tell you if the system percolates or not.

An output ppm file called "flow" will be outputted in the same folder as the program.
If displayed, this file will show the flow, indicated by columbia blue.

The number of row/columns you input will be used to calculate a plot that displays the
percolation probability vs the probability of a vacant site. The plot is saved as a jpg
in the folder of the program.

IMPORTANT: The program will take about 8 minutes to run, to create an output of the plot.

menu()

The menu function returns the array generated from functions which are ran
after input from the user.

array_to_file()

Creates a blank array NxN to a file. A new text file is opened with a name decided by
the user and each line is written one by one as the user inputs them. The loop ends
when the rows equal N, the value inputted by the user.

array_from_file()

Creates a blank array from a file, will work with txt files already present or 
ones made from the previous function. The lines are read to first find the dimensions
and then an empty matrix is made. As each line of the text file is read, it is inserted
into the array. After it is inserted, the previous line is deleted. Then the array is
converted into boolean, and the file is closed.

output_array()

The array is ran through this and outputted with vacant and full sites, depending
on the current boolean values. The first two rows are first checked and their values
are changed depending on if the value above the current index in the iteration of the
for loop is true or false. Then the next rows are changed one by one, each time 
comparing the values to the row above it.

VVV UPDATE VVV

It checks if an element in original array contains a False value 
next to a True value in the changed array, and changed the value
which has the same position as the False(in the original array)
except in the changed array, regardless of whether it's current
value is True or False.



percolation()

This functions outputs a boolean value indicating if the array percolates, by 
checking the last row and looking for a true value.


random_array()

This function uses a function from numpy to generate an array with values randomly
assigned from 0-1. The user is asked to input a probability, and numbers in the array
less than this value are set to zero, and greater than are set to 1.

visualize()

This function outputs a ppm file showing the flow. The size of the image is the same 
everytime, the only difference is that the blocks representing each element in the 
flow array is a different size depending on how many you have. The function creates a
new text file called flow, and inputs the first 3 rows of the ppm file. Then it compares
the original array to the final array. If the original is false and the new is true, there
is flow and a line of columbia blue pixels is drawn. The length of the line is dependent
on the total number of elements in a row of the array. If both are false, a brown line is
drawn. If the first is true and the second is false, a red line is drawn. These lines are
repeated going down until the block is finished, which is dependant on the number of 
elements in a column of the array.

plot()

This function makes random arrays and finds the probability of an array pecolating at each
probability of a vacant site, starting at .01 and finishing at 1.00, with a step of .01.
At each probability of a vacant site, the probability of an array percolating is calculated
using 50 random arrays, and finding how many of the 50 percolate. The Pylab library is used 
to plot the two arrays, and it take about 2 minutes for the plot to complete.
