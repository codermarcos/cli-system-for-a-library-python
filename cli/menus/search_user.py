from cli.prompts.search import Search
from user import User

SEARCH_USER_ASCII_ART = """
┳┓         ┓    ┳┳       •  
┣┫┓┏┏┏┏┓┏┓┏┫┏┓  ┃┃┏┓┏┏┓┏┓┓┏┓
┻┛┗┻┛┗┗┻┛┗┗┻┗┛  ┗┛┛┗┻┗┻┛ ┗┗┛

[bright_black]Precione[/bright_black] [bold]esc[/bold] [bright_black]para voltar[/bright_black]
"""


class UserSearch(Search):
    def __init__(
        self, on_back, art=SEARCH_USER_ASCII_ART, on_select=None, selection=False
    ):
        self.on_back = on_back
        self.on_select = on_select

        super().__init__(art, selection)

    def get_columns(self) -> list[str]:
        return ["ID", "Nome", "Contato"]

    def on_search(self, text):
        return User.search(text)
