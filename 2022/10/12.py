# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked by Amazon.
# 
# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

def print_matrix(matrix, x0, y0, x1, y1):
    if x0 >= x1 or y0 >= y1:
        return

    for x in range(x0, x1):
        print(matrix[y0][x])

    for y in range(y0+1, y1-1):
        print(matrix[y][x1-1])

    for x in range(x1-1, x0, -1):
        print(matrix[y1-1][x])

    for y in range(y1-1, y0, -1):
        print(matrix[y][x0])

    print_matrix(matrix, x0+1, y0+1, x1-1, y1-1)

matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

print_matrix(matrix, 0, 0, len(matrix[0]), len(matrix))
