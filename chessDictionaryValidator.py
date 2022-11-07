theBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop','5h': 'bqueen', '3e': 'wking',
            '1a': 'bpawn', '2a': 'bpawn', '3a': 'bpawn', '4a': 'bpawn', '5a': 'bpawn',
            '6a': 'bpawn', '7a': 'bdragon', '8a': 'wbishop', '5b': 'bpawn'}

def isValidChessBoard(board):
    pieceCount = {}
    validX = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    validY = ['1', '2', '3', '4', '5', '6', '7', '8']
    validPieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    #count number of pieces
    for v in board.values():
        pieceCount.setdefault(v,0)
        pieceCount[v] += 1
    print (pieceCount)

    #check for one white king and one black king
    if pieceCount.get('wking',0) !=1 or pieceCount.get('bking',0) != 1:
        print('Incorrect number of kings!')
        return False
    print ('Number of white kings: ' + str(pieceCount.get('wking')))
    print ('Number of black kings: ' + str(pieceCount.get('bking')))

    #count total number of pieces on each side and for invalid colors
    whitePieces = 0
    blackPieces = 0
    for color in board.values():
        if color[0] == 'w':
            whitePieces += 1
            #if whitePieces > 16:
                #print ('Too many white pieces!')
                #return False
        elif color[0] == 'b':
            blackPieces +=1
            #if blackPieces > 16:
                #print ('Too many black pieces!')
                #return False
        else:
            print ('Incorrect color!')
            errorValue = list(board.values()).index(color)
            errorSpace = list(board.keys())[errorValue]
            print('Error at ' + str(errorSpace) + ': ' + color + '.')
            return False
    print('Number of white pieces: ' + str(whitePieces))
    print('Number of black pieces: ' + str(blackPieces))
    if whitePieces > 16 or blackPieces > 16:
        print ('Too many pieces on one side!')

    #verifies that all pieces on the board are validPieces
    for piece in board.values():
        if piece[1:] not in validPieces:
            print ('Invalid pieces!')
            return False
    else:
        print ('All pieces valid.')

    #counts number of pawns
    if pieceCount.setdefault('wpawn',0) > 8 or pieceCount.setdefault('bpawn',0) > 8:
        print ('Too many pawns!')
        return False
    else:
        print ('At most 8 pawns on either side.')

    #checks piece placement validity
    for x in board.keys():
        if x[1] not in validX:
            print ('X-axis out of bounds!')
            return False
    for y in board.keys():
        if y[0] not in validY:
            print ('Y-axis out of bounds!')
            return False
    else:
        print ('All pieces in bounds.')
        #print ('white: ' + str(whitePieces) + ', black: ' + str(blackPieces))
        return True

#Output
if isValidChessBoard(theBoard):
    print('Board is valid!')
else:
    print('Board is invalid!')
