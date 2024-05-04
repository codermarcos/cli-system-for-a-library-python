import os
import time

from book import Book
from cli.menus.search_user import UserSearch
from cli.prompts.search import Search
from rich.console import Console

LEND_BOOK_ASCII_ART = """
┳┓      ┓        ┓ •      
┃┃┏┓┓┏┏┓┃┓┏┏┓┏┓  ┃ ┓┓┏┏┓┏┓
┻┛┗ ┗┛┗┛┗┗┛┗ ┛   ┗┛┗┗┛┛ ┗┛

[bright_black]Preencha os campos a seguir ou precione[/bright_black] [bold]esc[/bold] [bright_black]para voltar[/bright_black]
"""

from book import Book


class BookSearchForReturn(Search):
    def __init__(self, art, on_back, on_select, user_id):

        self.user_id = user_id
        self.on_back = on_back
        self.on_select = on_select

        art_book = f"{art}\nSelecione o livro que o usuario está devolvendo:\n"

        super().__init__(art_book, selection=True)

    def get_columns(self) -> list[str]:
        return ["ID", "Titulo", "Autor", "Publicado em"]

    def on_search(self, text):
        return Book.search_books_borrowed(self.user_id, text)


class ReturnBook(Console):
    def __init__(self, on_back):
        super().__init__(log_time=False, log_path=False)

        self.user = None
        self.book = None

        art_user = f"{LEND_BOOK_ASCII_ART}\nSelecione um usuário:\n"

        UserSearch(on_back, art=art_user, on_select=self.set_user, selection=True)

        user_id, user_name, _ = self.user

        art_selected_user = f"{LEND_BOOK_ASCII_ART}\nFazendo devolução para usuário: [bold bright_green]{user_name}[/bold bright_green]"

        BookSearchForReturn(
            art=art_selected_user,
            on_back=on_back,
            on_select=self.set_book,
            user_id=user_id,
        )

        _, book_name, _, _ = self.book

        art_selected_book = f"{art_selected_user}\nDo livro: [bold bright_green]{book_name}[/bold bright_green]"

        os.system("cls||clear")

        super().log(art_selected_book)

        self.update()

        on_back()

    def set_user(self, user):
        self.user = user

    def set_book(self, book):
        self.book = book

    def update(self):
        book_code, _, _, _ = self.book

        Book.update({"loaned_to_id": None, "code": book_code})

        super().log(
            "[bold bright_green]Livro devolvido com sucesso![/bold bright_green]"
        )

        time.sleep(2)
