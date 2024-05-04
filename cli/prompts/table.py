from rich.table import Table as RichTable


class Table(RichTable):
    def __init__(self, columns, rows, selected=None):
        super().__init__(min_width=50)

        if selected != None:
            self.add_column("Selecionado", style="bold bright_green")

        for column in columns:
            self.add_column(column)

        for i, row in enumerate(rows):
            row_to_print = row

            if selected != None:
                indicator = "------------->" if i == selected else ""
                row_to_print = (indicator, *row)

            self.add_row(*[str(c) for c in row_to_print])
