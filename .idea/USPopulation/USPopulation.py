#This program is made by Bryan Liem. This program creates a line graph
#Imports the necessary modules, with matplotlib.pyplot for creating the graph
#and numpy to create the storage of the data.
import matplotlib.pyplot as plt
import numpy as np

#Tries to run the code below and if fails, gives an error message.
try:

#Opens USPopulation.txt and sets the table data with the data from the file.
    with open('USPopulation.txt', 'r') as file:
        data = np.genfromtxt('USPopulation.txt', dtype=int)

#Defines the minuend and the subtrahend, which is used to find the difference in the change of populations.
#This data is stored in the difference array.
    minuend = np.array(data[1:len(data)], dtype=int)
    subtrahend = np.array(data[0:len(data)-1], dtype=int)
    difference = minuend - subtrahend

#Grabs the largest and smallest values in the difference array.
    largestIncrease = max(difference)
    smallestIncrease = min(difference)

#Grabs the average of values of the difference array by diving the sum of all of the values of the
#difference array and divides it by the amount of values the difference array has.
    average = sum(difference) / len(difference)

#Defines the indices for the largest and smallest values in the difference array.
    largestIncreaseIndex = np.argwhere(difference == largestIncrease)
    smallestIncreaseIndex = np.argwhere(difference == smallestIncrease)

#Which then is immediately converted into integers for use later.
    largestIncreaseIndex = int(largestIncreaseIndex[0][0])
    smallestIncreaseIndex = int(smallestIncreaseIndex[0][0])
    
#Defines the years range from 1951 to 1990.
    years = np.arange(1951, 1991, 1)

#Uses the indicies for the largest and smallest values to find the associated year with the values.
    largestYears = years[largestIncreaseIndex]
    smallestYears = years[smallestIncreaseIndex]

#Prints the average change, largest increase, and the smallest increase of the population.
    print(f'Average change is {average:.2f}')
    print(f'Largest increase in population {largestIncrease} in year {largestYears}')
    print(f'Smallest increase in population {smallestIncrease} in year {smallestYears}')

#Creates the line chart with the years and difference arrays, along with adjusting the lline graphs's labels, title, markers, and color.
    plt.plot(years, difference, color='#00BFBF', marker='o')
    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.title('US Population Change')

#Displays the finished line chart.
    plt.show()

#Gives an error message if the code above fails to work due to the file being missing, variable assignment not working, etc.
except:
    print('There was an error in trying to open USPopulation.txt, calculating data, or creating the line graph.')
