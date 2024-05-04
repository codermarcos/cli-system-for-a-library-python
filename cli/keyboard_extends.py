class KeyboardExtends:
    @staticmethod
    def simulate_type(text, key):
        if len(key) == 1 and f"{key}".isalnum():
            text += key
        elif key == "space":
            text += " "
        elif key == "backspace":
            text = text[:-1]

        return text
