from cli.prompts.form import Form
from user import User

NEW_USER_ASCII_ART = """
┳┓        ┳┳       •  
┃┃┏┓┓┏┏┓  ┃┃┏┓┏┏┓┏┓┓┏┓
┛┗┗┛┗┛┗┛  ┗┛┛┗┻┗┻┛ ┗┗┛

[bright_black]Preencha os campos a seguir ou precione[/bright_black] [bold]esc[/bold] [bright_black]para voltar[/bright_black]
"""


class NewUser(Form):
    def __init__(self, on_back):
        super().__init__(NEW_USER_ASCII_ART)

        self.on_back = on_back

        self.request_name()
        self.request_contact()

        if not self.skip:
            self.on_save()

        self.on_back()

    def request_name(self, field="name"):
        self.text_question(field, "🤓 Digite o nome do usuário")
        self.is_required(field, self.request_name)

    def request_contact(self, field="contact"):
        self.text_question("contact", "📞 Qual o telefone para contato")
        self.is_required(field, self.request_contact)
        self.is_numeric(field, self.request_contact)

    def on_save(self):
        User.save(self.form_anwsers)
        self.sucess_log("Usúario cadastrado com sucesso!")
