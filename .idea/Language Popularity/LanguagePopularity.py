#This program is made by Bryan Liem. This program creates a bar graph from a given txt file.
#Imports the necessary modules, with matplotlib.pyplot for creating the graph and
#and numpy to create the storage of the data.
import matplotlib.pyplot as plt
import numpy as np

#Tries to run the code below and if fails, gives an error message.
try:
    
#Opens languages.txt and sets the table data with the data from the file as an array of strings.
#Uses the "," as the delimiter.
    table = np.genfromtxt('languages.txt', dtype=str, delimiter=',')

#Sets the label and data array with the labels and data from the table respectively.
#The vaues of the data array are also converted to int.
    label = np.array(table[0])
    data = np.array(table[1], dtype=int)
    
#Creates the bar chart with the label and data lists, along with adjusting the bar graphs's labels, title, width, and color.
    plt.bar(label, data, width=0.5, color='maroon')
    plt.xlabel('Languages')
    plt.ylabel('Popularity')
    plt.title('Computer Languages')

#Displays the finished bar chart.
    plt.show()

except:
    
#Gives an error message if the code above fails to work due to the file being missing, variable assignment not working, etc.
    print('There was an error in trying to open languages.txt or creating the bar graph.')

