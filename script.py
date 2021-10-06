"""Generates turtle python programs for drawing images"""
from typing import Iterable
import numpy as np
from imageio import imread


class Coder:
    """Coder class. It codes for you :D"""

    def __init__(self, handle) -> None:
        """Gets the file handle yay"""
        self.file = handle

    def write(self, value: str, end="\n") -> None:
        """I hate writing \n for each line change so.."""
        self.file.write(f"{value}{end}")

    def close(self) -> None:
        """Everyone gets mad if I don't close the file :("""
        self.file.close()

    def start_coding(self, picture_height: int = 500) -> None:
        """The turtle is in up position"""
        self.write("import turtle")
        self.write("turtle.colormode(255)")
        self.write("turtle.speed(0)")
        self.write("turtle.up()")
        self.write("turtle.left(90)")
        self.write(f"turtle.forward({picture_height})")
        self.write("turtle.right(90)")

    def code(
        self,
        color_data: Iterable = (255, 255, 255),
        multiplier=1,
        is_up=False,
        up=False,
    ):
        """Writes some code for me"""
        self.write(f"turtle.color({','.join(str(i) for i in color_data)})")
        if is_up:
            self.write("turtle.down()")
        self.write(f"turtle.forward({multiplier})")
        if up:
            self.write("turtle.up()")

    def next_row(self, picture_breadth: int = 500):
        """Change the row :)"""
        self.write("turtle.right(90)")
        self.write("turtle.forward(1)")
        self.write("turtle.right(90)")
        self.write(f"turtle.forward({picture_breadth})")
        self.write("turtle.right(180)")


def code_optimized(row: np.ndarray) -> list:
    """Replaces redundant data with a single forward"""
    analyzed = [[row[0], 1]]
    for i in row[1:]:
        if list(i) == list(analyzed[-1][0]):
            analyzed[-1][1] += 1
        else:
            analyzed.append([i, 1])
    return analyzed


def generate(data):
    """Generate the code"""
    length_x = len(data[0])
    coding = Coder(open("generated.py", "w"))
    coding.start_coding(len(data))
    for y, row in enumerate(data):
        for x, element in enumerate(code_optimized(row)):
            if x == 0:
                coding.code(element[0], multiplier=element[1], is_up=True)
            elif x == length_x - 1:
                coding.code(element[0], multiplier=element[1], up=True)
            else:
                coding.code(element[0], multiplier=element[1])
        coding.next_row(len(row))
    coding.close()


if __name__ == "__main__":
    """The main segment"""
    im = imread(input("Enter file name with extension: "), pilmode="RGB")
    generate(im)
