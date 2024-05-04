from cli.menus.lend_book import LendBook
from cli.menus.new_book import NewBook
from cli.menus.new_user import NewUser
from cli.menus.return_book import ReturnBook
from cli.menus.search_book import BookSearch
from cli.menus.search_user import UserSearch
from cli.prompts.menu import Menu

BOOK_ASCII_ART = """
       .--.                   .---.
   .---|__|           .-.     |~~~|
.--|===|--|_          |_|     |~~~|--.
|  |===|  |'\     .---!~|  .--|   |--|
|%%|   |  |.'\    |===| |--|%%|   |  |
|%%|   |  |\.'\   |   | |__|  |   |  |
|  |   |  | \  \  |===| |==|  |   |  |
|  |   |__|  \.'\ |   |_|__|  |~~~|__|
|  |===|--|   \.'\|===|~|--|%%|~~~|--|
^--^---'--^    `-'`---^-^--^--^---'--'
"""


class Main(Menu):

    def __init__(self):
        super().__init__(
            f"{BOOK_ASCII_ART}\nSelecione uma ação usando as setas ou números:"
        )

    def get_options(self):
        return [
            ("1", "🤓  Cadastrar Usuário", self.on_access_new_user),
            ("2", "📖  Cadastrar Livro", self.on_access_new_book),
            ("3", "➜   Emprestar Livro", self.on_access_lend_book),
            ("4", "⮌   Devolver Livro", self.on_access_return_book),
            ("5", "👥  Consultar Usuários", self.on_access_user_search),
            ("6", "📚  Consultar Livros", self.on_access_book_search),
            ("esc", "❌  Sair", self.on_quit),
        ]

    def on_access_new_user(self):
        NewUser(self.run)

    def on_access_new_book(self):
        NewBook(self.run)

    def on_access_lend_book(self):
        LendBook(self.run)

    def on_access_return_book(self):
        ReturnBook(self.run)

    def on_access_user_search(self):
        UserSearch(self.run)

    def on_access_book_search(self):
        BookSearch(self.run)

    def on_quit(self):
        exit()
