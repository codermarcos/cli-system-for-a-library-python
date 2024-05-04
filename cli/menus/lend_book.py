import os
import time

from book import Book
from cli.menus.search_user import UserSearch
from cli.prompts.search import Search
from rich.console import Console

LEND_BOOK_ASCII_ART = """
┏┓                 ┓•      
┣ ┏┳┓┏┓┏┓┏┓┏╋┏┓┏┓  ┃┓┓┏┏┓┏┓
┗┛┛┗┗┣┛┛ ┗ ┛┗┗┻┛   ┗┗┗┛┛ ┗┛
     ┛

[bright_black]Preencha os campos a seguir ou precione[/bright_black] [bold]esc[/bold] [bright_black]para voltar[/bright_black]
"""

from book import Book


class BookSearchForLend(Search):
    def __init__(self, on_back, on_select):

        self.on_back = on_back
        self.on_select = on_select

        art_book = f"{LEND_BOOK_ASCII_ART}\nSelecione um livro:\n"

        super().__init__(art_book, selection=True)

    def get_columns(self) -> list[str]:
        return ["ID", "Titulo", "Autor", "Publicado em", "Disponiveis"]

    def on_search(self, text):
        return Book.search_only_availables(text)


class LendBook(Console):
    def __init__(self, on_back):
        super().__init__(log_time=False, log_path=False)

        self.user = None
        self.book = None

        BookSearchForLend(on_back, on_select=self.set_book)

        _, book_name, _, _, _ = self.book

        art_selected_book = f"{LEND_BOOK_ASCII_ART}\nEmprestando o livro: [bold bright_green]{book_name}[/bold bright_green]"

        art_user = f"{art_selected_book}\nSelecione um usuário:\n"

        UserSearch(on_back, art=art_user, on_select=self.set_user, selection=True)

        (_, user_name, _) = self.user

        art_selected_user = f"{art_selected_book}\nPara o usuário: [bold bright_green]{user_name}[/bold bright_green]"

        os.system("cls||clear")

        super().log(art_selected_user)

        self.update()

        on_back()

    def set_user(self, user):
        self.user = user

    def set_book(self, book):
        self.book = book

    def update(self):
        book_code, _, _, _, _ = self.book
        user_id, _, _ = self.user

        Book.update({"loaned_to_id": user_id, "code": book_code})

        super().log(
            "[bold bright_green]Livro emprestado com sucesso![/bold bright_green]"
        )

        time.sleep(2)
