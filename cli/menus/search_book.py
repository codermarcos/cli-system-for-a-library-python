from book import Book
from cli.prompts.search import Search

SEARCH_BOOK_ASCII_ART = """
┳┓         ┓    ┓ •      
┣┫┓┏┏┏┏┓┏┓┏┫┏┓  ┃ ┓┓┏┏┓┏┓
┻┛┗┻┛┗┗┻┛┗┗┻┗┛  ┗┛┗┗┛┛ ┗┛

[bright_black]Precione[/bright_black] [bold]esc[/bold] [bright_black]para voltar[/bright_black]
"""


class BookSearch(Search):
    def __init__(self, on_back):
        self.on_back = on_back

        super().__init__(SEARCH_BOOK_ASCII_ART)

    def get_columns(self) -> list[str]:
        return ["ID", "Titulo", "Autor", "Publicado em", "Copias", "Emprestados"]

    def on_search(self, text):
        return Book.search(text)
