import os
import time
from abc import abstractmethod

import keyboard
from cli.prompts.error import NUMERIC_FIELD, REQUIRED_FIELD, Error
from rich.console import Console
from rich.prompt import Prompt


class Form(Console):
    def __init__(self, title):
        super().__init__(log_time=False, log_path=False)

        self.form_title = title
        self.skip = False
        self.form_anwsers = {}
        self.form_questions = []

    @abstractmethod
    def on_back(self):
        pass

    def is_required(self, key, repeat):
        if not self.skip:
            anwser = self.form_anwsers[key]

            if anwser == None:
                Error(REQUIRED_FIELD)
                repeat()

    def is_numeric(self, key, repeat):
        if not self.skip:
            anwser = self.form_anwsers[key]

            if not anwser.isdigit():
                Error(NUMERIC_FIELD)
                repeat()

    def text_question(self, key, title, choices=None, default=None):
        if self.skip:
            return None

        off_press = None

        remove_hotkey = keyboard.add_hotkey(
            "esc", lambda: self.__on_back(), suppress=True
        )

        if key not in self.form_anwsers:
            self.form_questions.append([key, title, choices])
            self.form_anwsers[key] = ""

        self.__render_form()

        self.form_anwsers[key] = Prompt.ask(title, default=default)

        remove_hotkey()

        if off_press != None:
            off_press()

    def sucess_log(self, text):
        self.log(f"[bright_green]{text}[/bright_green]")
        time.sleep(1.5)

    def __on_back(self):
        self.skip = True
        keyboard.press_and_release("enter")

    def __render_form(self):
        os.system("cls||clear")
        super().log(self.form_title)

        for key, title, _ in self.form_questions[:-1]:
            self.log(f"{title}:", self.form_anwsers[key])
