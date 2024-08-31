import math

board = []
tiles = {i for i in range(64)}
for _ in range(8):
    board.append(input())
for row in range(8):
    for column in range(8):
        if board[row][column] == "R":
            tile = row * 8 + column
            tiles.discard(tile)
            pointer = tile + 1
            while pointer // 8 == tile // 8 and board[pointer//8][pointer%8] == '*':
                tiles.discard(pointer)
                pointer += 1
            pointer = tile - 1
            while pointer // 8 == tile // 8 and board[pointer // 8][pointer % 8] == '*':
                tiles.discard(pointer)
                pointer -= 1
            pointer = tile + 8
            while pointer % 8 == tile % 8 and pointer < 64 and board[pointer // 8][pointer % 8] == '*':
                tiles.discard(pointer)
                pointer += 8
            pointer = tile - 8
            while pointer % 8 == tile % 8 and pointer > -1 and board[pointer // 8][pointer % 8] == '*':
                tiles.discard(pointer)
                pointer -= 8
        elif board[row][column] == "B":
            tiles.discard(8 * row + column)
            pointerRow = row + 1
            pointerColumn = column + 1
            while pointerRow < 8 and pointerColumn < 8 and board[pointerRow][pointerColumn] == '*':
                tiles.discard(pointerRow * 8 + pointerColumn)
                pointerRow += 1
                pointerColumn += 1
            pointerRow = row - 1
            pointerColumn = column - 1
            while pointerRow > -1 and pointerColumn > -1 and board[pointerRow][pointerColumn] == '*':
                tiles.discard(pointerRow * 8 + pointerColumn)
                pointerRow -= 1
                pointerColumn -= 1
            pointerRow = row + 1
            pointerColumn = column - 1
            while pointerRow < 8 and pointerColumn > -1 and board[pointerRow][pointerColumn] == '*':
                tiles.discard(pointerRow * 8 + pointerColumn)
                pointerRow += 1
                pointerColumn -= 1
            pointerRow = row - 1
            pointerColumn = column + 1
            while pointerRow > -1 and pointerColumn < 8 and board[pointerRow][pointerColumn] == '*':
                tiles.discard(pointerRow * 8 + pointerColumn)
                pointerRow -= 1
                pointerColumn += 1
print(len(tiles))
