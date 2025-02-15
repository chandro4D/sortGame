import tkinter as tk


class Tube:
    def __init__(self):
        self.colors = []

    def add_color(self, color):
        self.colors.append(color)
    def remove_color(self):
        if self.is_empty():
            return None
        return self.colors.pop()

    def peek_color(self):
        if self.is_empty():
            return None
        return self.colors[-1]