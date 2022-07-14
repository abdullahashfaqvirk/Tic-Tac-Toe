def printBoard(x, o):
    '''
    if x[0] == 1: one = "X"
    elif o[0] == 1: one = "O"
    else: one = 1
    '''
    one = "X" if x[0] else("O" if o[0] else 1)
    two = "X" if x[1] else("O" if o[1] else 2)
    three = "X" if x[2] else("O" if o[2] else 3)
    four = "X" if x[3] else("O" if o[3] else 4)
    five = "X" if x[4] else("O" if o[4] else 5)
    six = "X" if x[5] else("O" if o[5] else 6)
    seven = "X" if x[6] else("O" if o[6] else 7)
    eight = "X" if x[7] else("O" if o[7] else 8)
    nine = "X" if x[8] else("O" if o[8] else 9)

    print(f" {one} | {two} | {three} ")
    print(f"---|---|---")
    print(f" {four} | {five} | {six} ")
    print(f"---|---|---")
    print(f" {seven} | {eight} | {nine} ")


def resultGame(x, o):
    sum = lambda a, b, c: a+b+c
    line = "-"*50
    probability = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in probability:
        if(sum(x[win[0]], x[win[1]], x[win[2]]) == 3):
            print(f"{line}\nPlayer 'X' Won the Match!")
            return True
        if(sum(o[win[0]], o[win[1]], o[win[2]]) == 3):
            print(f"{line}\nPlayer 'O' Won the Match!")
            return True
    return False


if __name__ == "__main__":
    line = "-"*50
    print(f"{line}\nWelcome to Game: Tic Tac Toe\n{line}")

    x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    o = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    printBoard(x, o)
    turn = 1
    while True:
        print(line)
        if turn % 2 != 0:
            player1 = int(input("Player 'X' Turn: "))
            # -1 is added as in func printBoard counting starts with 1 and end to 9
            x[player1-1] = 1
        else:
            player2 = int(input("Player 'O' Turn: "))
            o[player2-1] = 1

        print(line)
        printBoard(x, o)

        win = resultGame(x, o)
        if win == True:
            print(f"{line}\nGame Over!\n{line}")
            break
        if turn == 9:
            print(f"{line}\nGame is Tie!\nGame Over!\n{line}")
            break

        turn += 1
