#This program is made by Bryan Liem. This program simply prints information about irises in different ways,
#including tables that seperate the table into three based on species number, finding the max, min, average, and standard deviation of the values,
#and comparing the three seperated tables to the original full min data to see if each value is greater than the full min data.

#Imports the necessary modules, with matplotlib.pyplot for creating the graph
#and numpy to create the storage of the data.
import matplotlib.pyplot as plt
import numpy as np

#A function that prints an entire clean array with five columns.
def printData(array):
    for row in array:
        j = 0
#Prints each individual piece of data in a specific format per row. The newline statement ensure that the next row is printed in the next line.
        while j < len(row):
            print(f'   {row[j]:.2f}   ', end='')
            j += 1
        print()

#A function that prints an entire array row with four columns.
def printDataStats(array):
    for row in array:
        print(f'   {row:.2f}   ', end='')


#A function that compares an array's index with iris_min's index, provided an array and an index number,
#Which then prints 1 if the value of the array's index is larger than the value of the iris_min's index and 0 otherwise.
def compareMin(array, index):
    if array[index] > iris_min[index]:
        print('    1     ', end='')
    else:
        print('    0     ', end='')

#Opens iris.txt and sets the iris array with the data from the file, using "," as the delimiter.
#The code also skips the first line of the text file.
iris = np.genfromtxt('iris.txt', skip_header=1, delimiter=',', dtype='float')

#Prints the original RAW data.
print('Original RAW Data:\n')
print(iris)

#Deletes the fifth column in the iris array.
iris = np.delete(iris, 4, 1)

#Opens iris.txt and sets the header array with the headings from the file, using "," as the delimiter and autostripping.
#The code gets the headers by removing the last 30 lines of the text file, which leaves with only the headers.
header = np.genfromtxt('iris.txt', skip_footer=30, delimiter=',', autostrip=True, dtype='str')

#Deletes the fifth column in the header array to allign with the width of the iris array.
header = np.delete(header, 4)

#Prints the cleaned data by printing headers and then using the printData() function to print the iris data.
print('\n\nCleaned Data:')
for i in header:
    print(f'{i:.9}', end=' ')
print()
printData(iris)

#Prints three statements about the shape, dimensions, and the size of the iris array.
print(f'\nThe shape of the array is {iris.shape}')
print(f'The dimensions of the array are: {iris.ndim}')
print(f'The size of the array is: {iris.size}')

#Create three seperate iris arrays using the species number of the iris array.
iris1 = np.vsplit(iris, 3)[0]
iris2 = np.vsplit(iris, 3)[1]
iris3 = np.vsplit(iris, 3)[2]

#Prints headers and the iris1 data using the printData() function.
print('\nArray for Species 1:')
for i in header:
    print(f'{i:.9}', end=' ')
print()
printData(iris1)

#Prints headers and the iris2 data using the printData() function.
print('\nArray for Species 2:')
for i in header:
    print(f'{i:.9}', end=' ')
print()
printData(iris2)

#Prints headers and the iris3 data using the printData() function.
print('\nArray for Species 3:')
for i in header:
    print(f'{i:.9}', end=' ')
print()
printData(iris3)

#Using iris as a reference, uses the largest values of the array to create iris_max.
iris_max = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
j = 0
while j < 5:
    iris_max[j] = np.max(iris[0:30, j])
    j += 1

#Using iris as a reference, uses the smallest values of the array to create iris_min.
iris_min = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
j = 0
while j < 5:
    iris_min[j] = np.min(iris[0:30, j])
    j += 1

#Using iris as a reference, uses the averages of the values of the array to create iris_avg.
iris_avg = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
j = 0
while j < 5:
    iris_avg[j] = np.average(iris[0:30, j])
    j += 1

#Using iris as a reference, uses the standard deviations of the values of the array to create iris_std.
iris_std = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
j = 0
while j < 5:
    iris_std[j] = np.std(iris[0:30, j])
    j += 1

#Prints headers and the data from the iris_max, iris_min, iris_avg, and iris_std arrays using the printDataStats() function.
print('\nFull Data Set Statistics')
print('    ', end='')
for i in header:
    print(f'{i:.9}', end=' ')
print('\nMAX:', end='')
printDataStats(iris_max)
print('\nMIN:', end='')
printDataStats(iris_min)
print('\nAVG:', end='')
printDataStats(iris_avg)
print('\nSTD:', end='')
printDataStats(iris_std)

#Using iris1 as a reference, uses the largest values of the array to create iris_max1.
iris_max1 = np.array([0.0, 0.0, 0.0, 0.0])
j = 0
while j < 4:
    iris_max1[j] = np.max(iris1[0:10, j])
    j += 1

#Using iris1 as a reference, uses the smallest values of the array to create iris_min1.
iris_min1 = np.array([0.0, 0.0, 0.0, 0.0])
j = 0
while j < 4:
    iris_min1[j] = np.min(iris1[0:10, j])
    j += 1

#Using iris1 as a reference, uses the averages of the values of the array to create iris_avg1.
iris_avg1 = np.array([0.0, 0.0, 0.0, 0.0])
j = 0
while j < 4:
    iris_avg1[j] = np.average(iris1[0:10, j])
    j += 1

#Using iris1 as a reference, uses the standard deviations of the values of the array to create iris_std1.
iris_std1 = np.array([0.0, 0.0, 0.0, 0.0])
j = 0
while j < len(iris_std1):
    iris_std1[j] = np.std(iris1[0:10, j])
    j += 1

#Prints headers and the data from the iris_max1, iris_min1, iris_avg1, and iris_std1 arrays using the printDataStats() function.
print('\n\nSpecies 1 Statistics')
print('    ', end='')
for i in header:
    if i != header[4]:
        print(f'{i:.9}', end=' ')
print('\nMAX:', end='')
printDataStats(iris_max1)
print('\nMIN:', end='')
printDataStats(iris_min1)
print('\nAVG:', end='')
printDataStats(iris_avg1)
print('\nSTD:', end='')
printDataStats(iris_std1)

#Using iris2 as a reference, uses the largest values of the array to create iris_max2.
iris_max2 = np.array([0.0, 0.0, 0.0, 0.0])
j = 0
while j < 4:
    iris_max2[j] = np.max(iris2[0:10, j])
    j += 1

#Using iris2 as a reference, uses the smallest values of the array to create iris_min2.
iris_min2 = np.array([0.0, 0.0, 0.0, 0.0])
j = 0
while j < 4:
    iris_min2[j] = np.min(iris2[0:10, j])
    j += 1
#Using iris2 as a reference, uses the averages of the values of the array to create iris_avg2.
iris_avg2 = np.array([0.0, 0.0, 0.0, 0.0])
j = 0
while j < 4:
    iris_avg2[j] = np.average(iris2[0:10, j])
    j += 1
#Using iris2 as a reference, uses the standard deviations of the values of the array to create iris_std2.
iris_std2 = np.array([0.0, 0.0, 0.0, 0.0])
j = 0
while j < 4:
    iris_std2[j] = np.std(iris2[0:10, j])
    j += 1
    
#Prints headers and the data from the iris_max2, iris_min2, iris_avg2, and iris_std2 arrays using the printDataStats() function.
print('\n\nSpecies 2 Statistics')
print('    ', end='')
for i in header:
    if i != header[4]:
        print(f'{i:.9}', end=' ')
print('\nMAX:', end='')
printDataStats(iris_max2)
print('\nMIN:', end='')
printDataStats(iris_min2)
print('\nAVG:', end='')
printDataStats(iris_avg2)
print('\nSTD:', end='')
printDataStats(iris_std2)

#Using iris3 as a reference, uses the largest values of the array to create iris_max3.
iris_max3 = np.array([0.0, 0.0, 0.0, 0.0])
j = 0
while j < 4:
    iris_max3[j] = np.max(iris3[0:10, j])
    j += 1
#Using iris3 as a reference, uses the smallest values of the array to create iris_min3.
iris_min3 = np.array([0.0, 0.0, 0.0, 0.0])
j = 0
while j < 4:
    iris_min3[j] = np.min(iris3[0:10, j])
    j += 1
#Using iris3 as a reference, uses the averages of the values of the array to create iris_avg3.
iris_avg3 = np.array([0.0, 0.0, 0.0, 0.0])
j = 0
while j < 4:
    iris_avg3[j] = np.average(iris3[0:10, j])
    j += 1
#Using iris3 as a reference, uses the standard deviations of the values of the array to create iris_std3.
iris_std3 = np.array([0.0, 0.0, 0.0, 0.0])
j = 0
while j < 4:
    iris_std3[j] = np.std(iris3[0:10, j])
    j += 1
    
#Prints headers and the data from the iris_max3, iris_min3, iris_avg3, and iris_std3 arrays using the printDataStats() function.
print('\n\nSpecies 3 Statistics')
print('    ', end='')
for i in header:
    if i != header[4]:
        print(f'{i:.9}', end=' ')
print('\nMAX:', end='')
printDataStats(iris_max3)
print('\nMIN:', end='')
printDataStats(iris_min3)
print('\nAVG:', end='')
printDataStats(iris_avg3)
print('\nSTD:', end='')
printDataStats(iris_std3)

#Prints the heading that compared min species category with full data.
print('\n\nCatagories - compare min species category w/ full data (1 = >)')
print('              Species1  Species2  Species3')

#Print the header "sepal len" and uses compareMin() to compare the each min species category with full data.
print(f'{header[0]:.9}     ', end='')
compareMin(iris_min1, 0)
compareMin(iris_min2, 0)
compareMin(iris_min3, 0)

#Print the header "sepal wid" and uses compareMin() to compare the each min species category with full data.
print(f'\n{header[1]:.9}     ', end='')
compareMin(iris_min1, 1)
compareMin(iris_min2, 1)
compareMin(iris_min3, 1)

#Print the header "petal len" and uses compareMin() to compare the each min species category with full data.
print(f'\n{header[2]:.9}     ', end='')
compareMin(iris_min1, 2)
compareMin(iris_min2, 2)
compareMin(iris_min3, 2)

#Print the header "petal wid" and uses compareMin() to compare the each min species category with full data.
print(f'\n{header[3]:.9}     ', end='')
compareMin(iris_min1, 3)
compareMin(iris_min2, 3)
compareMin(iris_min3, 3)
