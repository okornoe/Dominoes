# Write your code here
import random

domino_set = []
dummy_domino_set = []
save_stock_pieces = []
stock_pieces = []
computer_pieces = []
player_pieces = []
domino_snake = []
status = "Computer"

sum_com_piece_list = []
sum_player_piece_list = []


def generate_domino_set():
    global dummy_domino_set
    for x in range(28):
        domino_set.append([])
        for i in range(2):
            domino_set[x].append(random.randint(0, 6))
    dummy_domino_set = domino_set[:]
    return dummy_domino_set


def generate_stock_pieces():
    global save_stock_pieces
    for x in range(14):
        idx = random.randint(0, len(dummy_domino_set) - 1)
        stock_pieces.append(dummy_domino_set[idx])
        dummy_domino_set.pop(idx)
    save_stock_pieces = stock_pieces[:]
    return stock_pieces


def generate_computer_pieces():
    for x in range(7):
        idx = random.randint(0, len(dummy_domino_set) - 1)
        computer_pieces.append(dummy_domino_set[idx])
        dummy_domino_set.pop(idx)
    return computer_pieces


def generate_player_pieces():
    global player_pieces
    player_pieces = dummy_domino_set[:]
    return player_pieces


def reshuffle_domino_set():
    global dummy_domino_set
    random.shuffle(domino_set)
    dummy_domino_set = domino_set[:]
    generate_stock_pieces()
    generate_computer_pieces()
    generate_player_pieces()


def find_domino_snake():
    generate_domino_set()
    generate_stock_pieces()
    generate_computer_pieces()
    generate_player_pieces()
    while True:
        global status
        global sum_com_piece_list
        global sum_player_piece_list
        for x in range(7):
            sum_com_piece_list.append(sum(computer_pieces[x]))
            sum_player_piece_list.append(sum(player_pieces[x]))
        max_com_piece = max(sum_com_piece_list)
        max_player_piece = max(sum_player_piece_list)

        if max_com_piece != max_player_piece:
            break
        else:
            # generate_domino_set()
            stock_pieces.clear()
            computer_pieces.clear()
            player_pieces.clear()
            sum_player_piece_list.clear()
            sum_com_piece_list.clear()
            reshuffle_domino_set()

    if max_com_piece > max_player_piece:
        status = "player"
        idx = sum_com_piece_list.index(max_com_piece)
        domino_snake.append(computer_pieces[idx])
        computer_pieces.pop(idx)
    else:
        status = "computer"
        idx = sum_player_piece_list.index(max_player_piece)
        domino_snake.append(player_pieces[idx])
        player_pieces.pop(idx)

    print("Stock pieces: {}".format(save_stock_pieces))
    print("computer pieces: {}".format(computer_pieces))
    print("player pieces: {}".format(player_pieces))
    print("domino snake: {}".format(domino_snake))
    print("status: {}".format(status))


# if __name__ == "__main__":
find_domino_snake()
