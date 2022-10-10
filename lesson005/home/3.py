print('Крестики-нолики')

board=list(range(1,10))

def b2(board):
    for i in range(3):
        print(board[0+i*3], board[1+i*3],board[2+i*3])

def move(player):
   qwe = False
   while not qwe:
      step = input("каков ваш ход " + player + '? ')
      try:
         step = int(step)
      except:
         print("ты дурак?")
         continue
      if step >= 1 and step <= 9:
         if(str(board[step-1]) not in "XO"):
            board[step-1] = player
            qwe = True
         else:
            print("ЗАНЯТО!")
      else:
        print(" Введите от 1 до 9.")

def win(board):
   combo = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for i in combo:
       if board[i[0]] == board[i[1]] == board[i[2]]:
          return board[i[0]]
   return False

def end(board):
    c = 0
    win2 = False
    while not win2:
        b2(board)
        if c % 2 == 0:
           move("X")
        else:
           move("O")
        c += 1
        if c > 4:
           top = win(board)
           if top:
              print(top, "одержал победу!")
              win2 = True
              break
        if c == 9:
            print("НИЧЬЯ!")
            break
    b2(board)
end(board)