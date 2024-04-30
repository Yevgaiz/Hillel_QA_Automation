matrix = [['a', 'c', 'e', 'g'],
          ['f', 'b', 'a', 'h'],
          ['a', 'n', 'k', 'e'],
          ['e', 'l', 'i', 'r'],
          ['e', 'l', 'i', 't']]


horizontally_matrix = []
for i in range(len(matrix[0])):
    horizontally_row = []
    for row in matrix:
        horizontally_row.append(row[i])
    horizontally_matrix.append(horizontally_row)
# print(horizontally_matrix)

for row in horizontally_matrix:
    row.sort()
# print(horizontally_matrix)

sorted_matrix = []
for i in range(len(horizontally_matrix[0])):
    sorted_row = []
    for row in horizontally_matrix:
        sorted_row.append(row[i])
    sorted_matrix.append(sorted_row)


for row in sorted_matrix:
    print(row)