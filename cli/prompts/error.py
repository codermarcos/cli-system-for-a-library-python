import time

from rich.console import Console

BIGER_THAN = "O campo deve ser maior que "
LESS_THAN = "O campo deve ser menor que "
REQUIRED_FIELD = "Campo obrigatório"
NUMERIC_FIELD = "Campo deve ser numérico"


class Error(Console):
    def __init__(self, message):
        super().__init__(log_time=False, log_path=False)
        super().log(f"[red]{message}[/red]")
        time.sleep(1)
