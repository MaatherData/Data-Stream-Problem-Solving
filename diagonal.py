rows= int(input(' pls enter number of rows: '))
columns= rows

matrix= []

print(' Enter the entries rowwise, seperated by spaces: ')

for x in range(rows):
    row_input= input(f'Enter row { x + 1}: ')
    row_values= row_input.split()
    row= [int(value) for value in raw_values]
    matrix.append(row)
    
print('The matrix is: ')
for raw in matrix:
    for value in raw:
        print(value, end=' ')
    print()
    
''' First diagonal'''
for i in range(rows):
    print(matrix[i][i], end=' ')
    
''' Second diagonal'''
for i in range(rows):
    print(matrix[i][rows-1-i], end=' ')
    
first_sum= 0
second_sum= 0

for i in range(rows):
    first_sum += matrix[i][i]
    second_sum += matrix[i][rows-1-i]
    
print('The diagnoal is: ', abs(first_sum - second_sum))
    