from bibliotecas import *

class Validadores():
    def validate_entry2(self, text):
        # Valida apenas a entrada de números na parte 'Código', apenas até três digitos.

        if text == '':
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        # Caso queira aumentar os dígitos, acrescente mais um zero
        return 0 <= value <= 1000

