

row = ['_'] * 3
print(row)
# board = [row] * 3
# print(board)
# board[0][0] = 'x'
# print(board)

board = [['_'] * 3 for _ in range(3)]
print(board)

board[0][0] = 'x'
print(board)

z = ('one', 'two', 'three')
for item in z:
    print(item)

print(type(z))