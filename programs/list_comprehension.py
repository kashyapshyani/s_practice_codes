h_letters = []

# for letter in 'human':
#     h_letters.append(letter)
h_letters = [x if x%2==0 else "Odd" for x in range(20)]
print(h_letters)



matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)

# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Nested List Comprehension to flatten a given 2-D matrix
flatten_matrix = [val for sublist in matrix for val in sublist]

print(flatten_matrix)
