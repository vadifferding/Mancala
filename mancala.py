import sys

import urllib.request

#[0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
    
def main():
        board = createboard()
        
        x = 1
        printBoard(board)
        print('\n')
        

        gameOver = False  # boolean variable!
##        while not gameOver:
##                a = input('enter num player1: fisdt ask: ')
##                
##                get move for player 1
##                do move for player 1
##                if validMove for player 2:  # call your isGameOver function here to see
##                        get move for player 2
##                        do move for player 2
##                        gameover = not valudMove for Player1
##        else:
##                gameOver = True


             
        a = input("Enter a move for player 1:  ")
        print('\n')
 #       if isGameOver(board, 1) == True:
#                print('overrrrr')
                
        while legalMove(board, a, 1) == False:
                a = input('Enter a move for player 1: ')
        while legalMove(board, a, 1) == True and gameOver == False:
               # print(a)
                print('\n')
                printBoard(checkP1(board, a))
                print('\n')
                if isGameOver(board, 2) == True:
                        return scoreCounter(board)
                        
                if isGameOver(board, 2) ==False:
                        
                        b = input('Enter a move for player 2: ')
                        print('\n')
                        b = int(b)
 #               print(board[b])
##                while legalMove(board, b, 2) == True:
##                        print('\n')
##                        printBoard(checkP2(board, b))
 #               if legalMove(board, b, 2) == False:
                        

                while legalMove(board, b, 2) == False:
                        b = input("Enter a move for player 2: ")
                        print('\n')
##                        
                if legalMove(board, b, 2) ==True :

                        print('\n')
                        printBoard(checkP2(board, b))
               
  #                      printBoard(checkP2(board, b))
##                if legalMove(board, b, 2) == True:
##                        print('\n')
##                        printBoard(board)
                        if isGameOver(board, 1) == True:
                                return scoreCounter(board)
                                
                        if legalMove(board, a, 1) == 'over':
                                scoreCounter(board)
                        a = input('Enter a move for Player 1: ')
                        if legalMove(board, a, 1) == 'over':
                                scoreCounter(board)
                        while legalMove(board, a, 1) == False:
                                a = input('Enter a move for player 1: ')
 #                       if legalMove(board, a, 1) == 'over':
        else:
                gameOver == True




                if legalMove(board, b, 2) == 'over':
                        print('\n')
                        printBoard(board)
                        print('bye')
                                
                        
                


     

        
        if legalMove(board, a, 1) == "over":
                printBoard(board)
                print('P1')
                print('bye')

        if legalMove(board, b, 2) == "over":
                printBoard(board)
                print('P2')
                print('bye')






def add1(a):
        a = int(a)
        a = a +1
        return a
     


###DONT WORKKKKKKKKKKK        
def gameRunner1(board,p):
        r = []
        if p == 1:
                #if isGameOver(board, p) == True:
#                        return "overrr"
                
                if isGameOver(board, p) !=True:
                
                        a = input("enter move p1 ")
                        a = int(a)
                        if legalMove(board, a, p) == True:
                                r = checkP1(board, a)
                                printBoard(r)
                                p = 2
                                gameRunner(board,2)
        if p == 2:
 #       p = 2
        
                if isGameOver(board, p) !=True:
               
                        b = input("enter move p2 ")
                        b = int(b)
                        if legalMove(board, b, p) == True:
                                r = checkP2(board, b)
                                p = 1
                        
                                printBoard(r)
                                gameRunner(board, 1)
                #if legalMove(board, b, p) == False:
#                        print('buttzzz')
                        
        if isGameOver(board, p) ==True:
                return 'overrr'


def gameRunner(board):
        
        a = input("enter move p1 ")
        a = int(a)
        if legalMove(board, a, 1) == True:
                board = doMoveP1(board, a)
               # if doMoveP1(board, a) == False:
#                        print('GameOver')
                                              
        b = input("enter move p2 ")
        b = int(b)
        print(b)
        board = doMoveP1(board, b)
        
        if legalMove(board, b, 2) == True:
                print('hi')
                board = doMoveP2(board, b)

        if isGameOver(board,2) ==True or isGameOver(board,1) ==True:
                return endGameFunc(board)
        else:
                gameRunner(board)
        #r = checkP1(board, a)
 #       printBoard(r)


                gameRunner(board,2)
                               
        if isGameOver(board, p) ==True:
                return 'overrr'
        
        
def doMoveP2(board, position):
        if isGameOver(board, 2) == True:
                return endGameFunc(board)
        if isGameOver(board, 2) !=True:
                r = checkP2(board, position)
                printBoard(r)
                return r
                

def doMoveP1(board, position):
        if isGameOver(board, 1) == True:
                return False
        if isGameOver(board, 1) !=True:
                r = checkP1(board, position)
                printBoard(r)
                return r



def legalMove(board, position, player):
    position = int(position)
    #print(board[position])
    if board[position] == 0:
 #           print('u suck')
            return False
    
    l = len(board)
    h = l//2
    lastI = l -1
    hMinus1 = h -1
    #print(type(position))
    position = int(position)
    if position >lastI:
 #           position = str(position)
            player = str(player)
            print('Sorry, the move ' + str(position) + " is invalid for player 1" + player)
            print('\n')
            return False
    stoneNum = board[position]
    playerPosition = board[position]
    if player > 2 or player < 1:
            return False


    
    if(player ==1):
            if isGameOver(board, 1) == True:
                          return "over"
        
            if position > hMinus1:
 #                   position = str(position)
 #                   player = str(player)
                    print('Sorry, the move ' + str(position) + " is invalid for player2 " + str(player))
                    print('\n')

                    return False
                
            if stoneNum == 0:
 #                   position = str(position)
 #                   player = str(player)
                    print('Sorry, the move ' + str(position) + " is invalid for player 3" + str(player))
                    print('\n')
                    
                    return False
            if position == 0:
 #                   position = str(position)
 #                   player = str(player)
                    print('Sorry, the move ' + str(position) + " is invalid for player 4" + str(player))
                    print('\n')

                    return False
            ###edit later so not hardwired vals
            #if(position == 0 or position >=h):
#                    print('d')
#                    return False
            #if(board[position] != 
            if(position !=0 and position<h):
                    return True
    if(player == 2):
            if isGameOver(board, 2):
                          return "over"
            if position > lastI:
  #                  position = str(position)
#                    player = str(player)
                    print('Sorry, the move ' + str(position) + " is invalid for player5 " + str(player))
                    print('\n')

                    return False
            if position <= h:
 #                   position = str(position)
#                    player = str(player)
                    print('Sorry, the move ' + str(position) + " is invalid for player 6" + str(player))
                    print('\n')

                    return False
                #########RECENTLY EDITED
            #if stoneNum == 0:

#                    print('Sorry, the move ' + str(position) + " is invalid for player 7" + str(player))
#                    print('\n')

                    return False
                
            return True
            
                
    else:
 #       print("legal")
        return True
        
                            
            




def doMove(board, position, player):
 #       a = legalMove(board, position, player)
       p = board[position]
       count = 0
       lenthB = len(board)
 #      halfB = lengthB // 2
       if player == 1:
               r = checkP1(board, position)
       if player == 2:
               r = checkP2(board, position)
       return r



def checkP1(board, position):
        position = int(position)
        a = board[position]
        #print(a)
        lenthB = len(board)
        lastI = lenthB - 1
        b = 0
        temp2 =0
        i = 1
        temp = 1
        halfB = lenthB // 2
        if position + a > lastI:
                board[position] =0
                b = position + a
#                print('b= ', b)
                b = b-lastI
#                print('b= ', b)
                temp2 = a - b
 #               print('temp2', temp2)
                if temp2 !=0:
                        while temp2 != 0:
                                board[position +i] = board[position +i] +1
                                i = i +1
                                temp2 = temp2 -1
                                
                while b !=0:
                        
                        board[temp] = board[temp] + 1
                        b = b - 1
                        temp = temp + 1

        else:
            board[position] = 0
#            print(board[position])
            while a != 0:
                board[position + i] = board[position + i] + 1
                i = i +1
                a = a - 1
 #       print(board)
        return board


def scoreCounter(board):
        length = len(board)
        h = length //2
        h1 = h + 1
        p2Pit = board[0]
        p1List = board[1:h1]
#        print(p1List)
        p2List = board[h1:]
  #      print(p2List)
        p2List.insert(0, p2Pit)
        score1 = sumList(p1List)
        score2 = sumList(p2List)
        
        if score1 > score2:
                score1 = str(score1)
                score2 = str(score2)
                print("Player 1 wins " + score1 + " to " + score2 + "!")
        if score2 > score1:
                score1 = str(score1)
                score2 = str(score2)
                print("Player 2 wins " + score2 + " to  " + score1 + "!")
                


def sumList(L):
        if L == []:
                return 0
        else:
                return L[0] + sumList(L[1:])



def checkP2(board, position):
    position = int(position)
    a = board[position]
    lenthB = len(board)
    lastI = lenthB - 1
    b = 0
    temp2 =0
    i = 1
    temp = 0
    halfB = lenthB // 2
    
    if position + a > lastI:
                board[position] =0
                b = position + a
 #               print('b= ', b)
                b = b-lastI
 #               print('b= ', b)
                temp2 = a - b
#                print('temp2', temp2)
                if temp2 !=0:
                        while temp2 != 0:

                                board[position +i] = board[position +i] +1
                                i = i +1
                                temp2 = temp2 -1
                                
                while b !=0:
                        if(temp == halfB):
                            temp = temp +1
                        board[temp] = board[temp] + 1
                        b = b - 1
                        temp = temp + 1

    else:
            board[position] = 0
 #           print(board[position])
            while a != 0:
                board[position + i] = board[position + i] + 1
                i = i +1
                a = a - 1
                
    return board
    

                

def isGameOver(board, player):
        a = board
        i = 1
        j = 8
        
        count1 = 0
        count2 = 0
        l = len(board)
        h = l//2
        hAnd1 = h +1
        list1 = board[1:h]
        list2 = board[hAnd1:]
        if player ==1:
                for i in range(len(list1)):
                        count1 = count1 + list1[i]
##                while i >h:
##                        count1 = count1 + a[i]
##                        i = i +1
                if count1 ==0:
                        return True
        if player == 2:
                for i in range(len(list2)):
                        count2 = count2 + list2[i]
 #               while j < l:
 #                       count2 = count2 + a[j]
                if count2 == 0:
                        return True
        
        return False


def reverse(L):
    l = len(L)
    lastI = l-1
    for i in range(l//2):
        temp = L[i]
        L[i] = L[l- i -1]
        L[l-i-1]= temp
    return L                       
         
def createboard(stonesPerPit = 4, playerPits = 6):
    numString1 = '  13 12 11 10  9  8  7'
    numString2 = '0  1  2  3  4  5  6'
    plus1 = playerPits + 1
   
    total = plus1 * 2 
    s1 = [stonesPerPit] * total
    half = len(s1) //2
    s1[0] = 0
    s1[half] = 0

 #   l = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
    halfPlus1 = half +1
    a = s1[1:len(s1)//2]
    b = s1[halfPlus1:]
    return s1

def printBoard(board):
    numString1 = '  13 12 11 10  9  8  7'
    numString2 = '0  1  2  3  4  5  6'
    half = len(board) //2
    length = len(board)
    halfPlus1 = half +1 
    halfMin1 = half -1
    a = board[1:len(board)//2]
    b = board[halfPlus1:]
    
    aString = ""
    bString = ""

    for j in range(len(board)):
        if(j < half):
                aString = aString + "  " + str(j)
        if(j > halfMin1):
                bString = str(j) + " "+ bString 
    space = " " * len(a)
    print("   ",bString)
    print('\n')
#    stringOfA = reverse(stringOfA)
    for i in range(len(b)):
        b[i] = str(b[i])
    for i in range(len(a)):
        a[i] = str(a[i])
    b = reverse(b)
    stringOfA = "  ".join(a)
    stringOfB = "  ".join(b)
    print("    ", stringOfB)
    print(" ", board[0], " ", space, "        ", board[half])
    print("    ", stringOfA)
    print('\n')
    print(aString)
                
####### END OF PROGRAM #########
if __name__ == "__main__":
    main()




##
##
##gameOver = False  # boolean variable!
##while not gameOver
##     get move for player 1
##     do move for player 1
##     if validMove for player 2  # call your isGameOver function here to see
##         get move for player 2
##         do move for player 2
##         gameover = not valudMove for Player1
##     else:
##        gameOver = True
##             
