import os
import time
from abc import abstractmethod

import keyboard
from rich.console import Console


class Menu(Console):
    def __init__(self, title):
        super().__init__(log_time=False, log_path=False)

        self.menu_options = self.get_options()
        self.menu_title = title

        self.shortcuts = [key for (key, _, _) in self.menu_options]

        self.selected_index = 0

        self.run()

    @abstractmethod
    def get_options(self):
        pass

    def on_key_press(self, event):
        if event.name == "enter":
            self.__select(self.selected_index)
        if event.name == "down" or event.name == "up":
            self.__move_selection(1 if event.name == "down" else -1)
        elif event.name in self.shortcuts:
            self.__select(self.shortcuts.index(event.name))

    def run(self):
        off_press = keyboard.on_press(
            lambda event: self.on_key_press(event), suppress=True
        )

        self.handler_to_run = None
        self.running = True

        self.__menu_render()

        while self.running:
            time.sleep(0.05)

        off_press()

        if self.handler_to_run != None:
            self.handler_to_run()

    def __menu_render(self):
        os.system("cls||clear")
        print(self.menu_title)

        for i, (key, option, _) in enumerate(self.menu_options):
            super().log(
                (
                    f"[bold bright_green]>[/bold bright_green] [white]{key.rjust(3, ' ')}[/white] . {option}"
                    if i == self.selected_index
                    else f"  [bright_black]{key.rjust(3, ' ')}[/bright_black] . [grey70]{option}[/grey70]"
                ),
            )

    def __move_selection(self, to):
        if 0 <= self.selected_index + to < len(self.menu_options):
            self.selected_index += to
            self.__menu_render()

    def __select(self, index):
        *_, handler = self.menu_options[index]
        self.handler_to_run = handler
        self.running = False
