from typing import Tuple
import unittest

class Direction:

    def __init__(self, initial_coords: Tuple) -> None:
        self.coords = initial_coords

    def update_coords(self, dir: str):
        if dir == "N": 
            self.coords = (self.coords[0], self.coords[1] + 1)
        if dir == "S": 
            self.coords = (self.coords[0], self.coords[1] - 1)
        if dir == "W": 
            self.coords = (self.coords[0] + 1, self.coords[1])
        if dir == "E":
            self.coords = (self.coords[0] - 1, self.coords[1])

class Rover:
    COLS = 10
    POSITIONS = ["N", "E", "S", "W"]

    def __init__(self, direction: Direction) -> None:
        self.board = direction
        self.dir = "N"

    def get_final_position(self, input: str) -> str:
        board_coords = (0, 0)

        for c in input:
            if c == "M":
                self.board.update_coords(self.dir)
            elif c == "L":
                self.dir = self.POSITIONS[(self.POSITIONS.index(self.dir) - 1) % 4]
            elif c == "R":
                self.dir = self.POSITIONS[(self.POSITIONS.index(self.dir) + 1) % 4]

        return f'{board_coords[0] % self.COLS}:{board_coords[1] % self.COLS}:{dir}'

POSITIONS = ["N", "E", "S", "W"]

def get_final_rover_position(input = "", cols = 10, board_coords = (0, 0)):
    dir = "N"

    for c in input:
        if c == "M":
            board_coords = move_rover(dir, board_coords)
        elif c == "L":
            dir = POSITIONS[(POSITIONS.index(dir) - 1) % 4]
        elif c == "R":
            dir = POSITIONS[(POSITIONS.index(dir) + 1) % 4]

    return parse_output(board_coords, cols, dir)

def parse_output(board_coords, cols, dir):
    return f'{board_coords[0] % cols}:{board_coords[1] % cols}:{dir}'


def move_rover(dir, board_coords):
    X = 0
    Y = 1

    coords = [board_coords[X], board_coords[Y]]

    if dir == "N": coords[Y] += 1
    if dir == "S": coords[Y] -= 1
    if dir == "W": coords[X] -= 1
    if dir == "E": coords[X] += 1

    return tuple(coords)


class RoverTestCase(unittest.TestCase):
    def test_parsea_correctamente(self):
        assert True

    def test_initial_position_rover(self):
        assert get_final_rover_position() == "0:0:N"

    def test_only_one_movement(self):
        assert get_final_rover_position("M") == "0:1:N"

    def test_two_movements(self):
        assert get_final_rover_position("MM") == "0:2:N"

    def test_movement_with_front_left(self):
        assert get_final_rover_position("ML") == "0:1:W"

    def test_movement_with_front_two_times_right(self):
        assert get_final_rover_position("MMR") == "0:2:E"

    def test_max_height_of_board(self):
        assert get_final_rover_position("MMMMMMMMMM") == "0:0:N"

    def test_starts_rotation_position(self):
        assert get_final_rover_position("LM") == "9:0:W"

    def test_starts_rotation_right_position(self):
        assert get_final_rover_position("RM") == "1:0:E"

    def test_two_rotations_right(self):
        assert get_final_rover_position("RR") == "0:0:S"

    def test_two_rotations_left(self):
        assert get_final_rover_position("LL") == "0:0:S"

    def test_kata_case_one(self):
        assert get_final_rover_position("MMRMMLM") == "2:3:N"

    def test_kata_case_three(self):
        assert get_final_rover_position("RMMLMRMMMLLLM") == "5:0:S"

if __name__ == "__main__":
    unittest.main()
