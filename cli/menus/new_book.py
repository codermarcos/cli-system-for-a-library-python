from book import Book
from cli.prompts.error import BIGER_THAN, LESS_THAN, Error
from cli.prompts.form import Form

NEW_BOOK_ASCII_ART = """
┳┓        ┓ •      
┃┃┏┓┓┏┏┓  ┃ ┓┓┏┏┓┏┓
┛┗┗┛┗┛┗┛  ┗┛┗┗┛┛ ┗┛

[bright_black]Preencha os campos a seguir ou precione[/bright_black] [bold]esc[/bold] [bright_black]para voltar[/bright_black]
"""


class NewBook(Form):
    def __init__(self, on_back):
        super().__init__(NEW_BOOK_ASCII_ART)

        self.on_back = on_back

        self.request_title()
        self.request_author()
        self.request_published()
        self.request_copies()

        if not self.skip:
            self.on_save()

        self.on_back()

    def request_title(self, field="title"):
        self.text_question(field, "📕 Digite o titulo do livro")
        self.is_required(field, self.request_title)

    def request_author(self, field="author"):
        self.text_question(field, "📝 Qual o nome do autor", default="Desconhecido")

    def request_published(self, field="published"):
        self.text_question(field, "📆 Quando ano da publicação")
        self.is_required(field, self.request_published)
        self.is_numeric(field, self.request_published)

    def request_copies(self, field="copies"):
        self.text_question(field, "🔢 Quantas copias")
        self.is_required(field, self.request_copies)
        self.is_numeric(field, self.request_copies)

        if self.skip:
            return None

        if int(self.form_anwsers[field]) < 1:
            self.form_anwsers[field] = "1"
            Error(BIGER_THAN)
            self.request_copies()

        if int(self.form_anwsers[field]) > 1000:
            self.form_anwsers[field] = "1000"
            Error(LESS_THAN)
            self.request_copies()

    def on_save(self):
        Book.save(self.form_anwsers)
        self.sucess_log("Livro cadastrado com sucesso!")
