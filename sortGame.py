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


class WaterSortGame:
    def __init__(self, root, num_tubes):
        self.tubes = [Tube() for _ in range(num_tubes)]
        self.root = root
        self.selected_tube = None

        self.setup_ui()

    def setup_ui(self):
        self.root.configure(bg="#303036")
        self.root.geometry("1650x1000")

        title = tk.Label(
            self.root,
            text="WATER SORT PUZZLE",
            font=("Arial", 40, "bold"),
            bg="#303036",
            fg="#FFD700",
        )
        title.pack(pady=120)
        
        self.tube_frames = []
        tube_container = tk.Frame(self.root, bg="#303036")
        tube_container.pack(pady=10)
        
        for i in range(len(self.tubes)):
            frame = tk.Frame(
                tube_container, relief=tk.RAISED, borderwidth=2, bg="#444", padx=15, pady=15
            )
            frame.grid(row=0, column=i, padx=20)
            self.tube_frames.append(frame)

        self.update_ui()