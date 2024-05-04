import os
import time
from abc import abstractmethod

import keyboard
from cli.keyboard_extends import KeyboardExtends
from cli.prompts.table import Table
from rich import box
from rich.console import Console, Group
from rich.panel import Panel


class Search(Console):
    def __init__(self, title, selection=False):
        super().__init__(log_time=False, log_path=False)

        self.search_text = ""
        self.rows = []

        self.search_title = title

        self.selected_index = 0 if selection else None

        self.run()

    @abstractmethod
    def on_back(self):
        pass

    @abstractmethod
    def get_columns(self) -> list[str]:
        pass

    @abstractmethod
    def on_search(self, text):
        pass

    @abstractmethod
    def on_select(self, row):
        pass

    def on_key_press(self, event):
        if event.name == "esc":
            self.handler_to_run = self.on_back
            self.running = False
        elif (
            event.name == "enter"
            and self.selected_index != None
            and len(self.rows) != 0
        ):
            self.__select()
        elif (
            (event.name == "down" or event.name == "up")
            and self.selected_index != None
            and len(self.rows) != 0
        ):
            self.__move_selection(1 if event.name == "down" else -1)
        else:
            new_text = KeyboardExtends.simulate_type(self.search_text, event.name)

            if new_text != self.search_text:
                self.search_text = new_text
                self.__render_search()

    def run(self):
        off_press = keyboard.on_press(
            lambda event: self.on_key_press(event), suppress=True
        )

        self.handler_to_run = None
        self.running = True

        self.__render_search()

        while self.running:
            time.sleep(0.05)

        off_press()

        if self.handler_to_run != None:
            self.handler_to_run()

    def __move_selection(self, to):
        if 0 <= self.selected_index + to < len(self.rows):
            self.selected_index += to
            self.__render_search()

    def __select(self):
        self.handler_to_run = lambda: self.on_select(self.rows[self.selected_index])
        self.running = False

    def __render_search(self):
        os.system("cls||clear")
        super().log(self.search_title)

        self.rows = self.on_search(self.search_text)

        layout = Group(
            Panel.fit(self.search_text.ljust(50, " "), box=box.SQUARE),
            Table(
                self.get_columns(),
                self.rows,
                self.selected_index,
            ),
        )

        super().log(layout)
