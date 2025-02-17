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
        def is_full(self):
        return len(self.colors) == 4

    def is_empty(self):
        return len(self.colors) == 0
    def can_pour_into(self, other):
        if self.is_empty() or other.is_full():
            return False
        if other.is_empty():
            return True
        return self.peek_color() == other.peek_color()
