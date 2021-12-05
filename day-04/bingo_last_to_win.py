from typing import List


class BoardNumber:

    def __init__(self, value: int):
        self._drawn_subscribers = []
        self.value = value
        self.drawn = False

    def __eq__(self, other):
        if isinstance(other, BoardNumber):
            return self.value == other.value and self.drawn == other.drawn
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.value, self.drawn))

    def add_drawn_subscriber(self, subscriber) -> None:
        self._drawn_subscribers.append(subscriber)

    def notify_drawn_subscribers(self) -> None:
        for drawn_subscriber in self._drawn_subscribers:
            drawn_subscriber.drawn_notification(self)

    @property
    def drawn(self) -> bool:
        return self._drawn

    @drawn.setter
    def drawn(self, drawn: bool) -> None:
        self._drawn = drawn

        if drawn:
            self.notify_drawn_subscribers()


class Line:

    def __init__(self, parent_board):
        self.board = parent_board
        self.winner = False
        self.board_numbers = {0: None, 1: None, 2: None, 3: None, 4: None}
        self.drawn_numbers = {}

    def add_board_number(self, board_number, position) -> None:
        self.board_numbers[position] = board_number
        board_number.add_drawn_subscriber(self)

    def drawn_notification(self, board_number) -> None:
        if not self.drawn_numbers.get(board_number):
            self.drawn_numbers[board_number] = True

        if len(self.drawn_numbers) == 5:
            self.notify_winner_subscribers()

    def notify_winner_subscribers(self) -> None:
        self.winner = True
        self.board.winner_notification(self)


class Board:

    def __init__(self, numbers: List[List[int]]):
        self.rows = [Line(self) for _ in range(0, 5)]
        self.columns = [Line(self) for _ in range(0, 5)]
        self.winner = False
        self._winning_line = None
        self._numbers_lookup = {}
        self._undrawn_numbers = {}

        for i in range(0, 5):
            input_row = numbers[i]

            for j in range(0, 5):
                value = input_row[j]
                board_number = BoardNumber(value)

                self.rows[i].add_board_number(board_number, j)
                self.columns[j].add_board_number(board_number, i)
                self._numbers_lookup[value] = board_number
                self._undrawn_numbers[value] = board_number

    def drawn_number(self, value: int) -> None:
        board_number = self._numbers_lookup.get(value)

        if board_number:
            board_number.drawn = True
            del(self._undrawn_numbers[board_number.value])

    def winner_notification(self, line: Line) -> None:
        self.winner = True
        self._winning_line = line

    def undrawn_numbers_sum(self) -> int:
        total = 0

        for value in self._undrawn_numbers.keys():
            total += value

        return total


def populate_boards() -> List[Board]:
    populated_boards = []

    with open("boards_input") as boards_input_file:
        board_input = []

        for boards_input_line in boards_input_file:
            stripped_line = boards_input_line.strip()

            if stripped_line:
                board_line = [int(converted_number) for converted_number in stripped_line.split()]
                board_input.append(board_line)
            else:
                populated_boards.append(Board(board_input))
                board_input = []

    return populated_boards


boards = populate_boards()

with open("numbers_input") as drawn_numbers_input_file:
    drawn_numbers = drawn_numbers_input_file.readline().strip().split(",")
    winning_boards = []
    last_winning_number = 0

    for drawn_number in drawn_numbers:
        converted_drawn_number = int(drawn_number)

        for i in range(0, len(boards)):
            board = boards[i]

            if board.winner:
                continue

            board.drawn_number(converted_drawn_number)

            if board.winner:
                winning_boards.append(board)
                last_winning_number = converted_drawn_number

    last_winning_board = winning_boards[-1]
    undrawn_numbers_sum = last_winning_board.undrawn_numbers_sum()
    final_score = undrawn_numbers_sum * last_winning_number
    print(f" -> Last board to win: Undrawn numbers sum x last drawn number = {final_score}")
