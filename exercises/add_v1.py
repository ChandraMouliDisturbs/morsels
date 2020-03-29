'''
Problem statement can be found at bottom 
'''

def flat_matrix(matrixes):
    if len(set([len(matrix)for matrix in matrixes])) != 1:
        raise ValueError("Given matrices are not the same size.")
    return [row  for matrix in matrixes for row in matrix]

def add(*matrixes) :
    flatten_matrix = flat_matrix(matrixes)
    matrixes_size = len(matrixes)
    cols = len(matrixes[0])
    row_sizes = [len(elem) for elem in flatten_matrix]
    if len(set(row_sizes)) !=1 :
        raise ValueError("Given matrices are not the same size.")
    row_size = set(row_sizes).pop()
    indices   = [i for i in range(0, matrixes_size*cols, cols) ]
    out = []
    for col in range(cols):
        catch_fish = []
        for i in range(0, row_size):
            catch_fish.append(sum([flatten_matrix[index+col][i] for index in indices]))
        out.append(catch_fish)
    return out


# matrix1 = [[1, 9], [7, 3],  [7, 3]]
# matrix2 = [[5, -4], [3, 3],  [7, 3]]
# matrix3 = [[2, 3], [-3, 1],  [7, 3]]
# add(matrix1, matrix2, matrix3)
# m1 = [[6, 6], [3, 1]]
# m2 = [[1, 2], [3, 4], [5, 6]]
# m3 = [[6, 6], [3, 1, 2]]
# add(m1,m2)

'''
Hey! ✨

I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
Try to solve this exercise without using any third-party libraries (without using pandas for example).

Before attempting any bonuses, I'd like you to put some effort into figuring out the clearest and most idiomatic way to solve this problem. If you're using indexes to loop, take a look at the first hint.

There are two bonuses this week.

Bonus 1

For the first bonus, modify your add function to accept and "add" any number of lists-of-lists. ✔️

>>> matrix1 = [[1, 9], [7, 3]]
>>> matrix2 = [[5, -4], [3, 3]]
>>> matrix3 = [[2, 3], [-3, 1]]
>>> add(matrix1, matrix2, matrix3)
[[8, 8], [7, 7]]
Bonus 2

For the second bonus, make sure your add function raises a ValueError if the given lists-of-lists aren't all the same shape. ✔️

>>> add([[1, 9], [7, 3]], [[1, 2], [3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "add.py", line 10, in add
    raise ValueError("Given matrices are not the same size.")
ValueError: Given matrices are not the same size.
'''
