import re

class ValidadorPlaca:
    def __init__(self):
        self.expressao_regular = r"^[A-Z]{3}-?[0-9][A-Z0-9][0-9]{2}"

    def validar(self, entrada: str) -> bool:

        return re.fullmatch(self.expressao_regular, entrada) is not None


class CorretorPlaca:
    def __init__(self):
        self.simbolos_dict = {
            "2":"Z",
            "Z":"2",
            "1":"I",
            "I":"1",
            "O":"0",
            "0":"O",
            "S":"5",
            "5":"S"
            }
        
    def corrigir(self, texto: str):
        texto = texto.replace("-", "").replace(".", "").upper()
        texto = texto.replace(" ", "")

        if len(texto) != 7:
            return texto

        caracteres = list(texto)

        # Na placa Merconsul, as posições 1, 2 e 3 devem ser letras
        self.posicoes_1_2_3(caracteres)

        # A posição 4 deve ser um número
        self.posicao_4(caracteres)

        # A posição 5 deve ser uma letra
        self.posicao_5(caracteres)

        # As posições 6 e 7 devem ser numéros
        self.posicoes_6_7(caracteres, len(caracteres))

        return "".join(caracteres)

    def numero_para_letra(self, caractere: str) -> str:
        if caractere.isdigit():
            return self.simbolos_dict.get(caractere, caractere)
        return caractere

    def letra_para_numero(self, caractere: str) -> str:
        if caractere.isalpha():
            return self.simbolos_dict.get(caractere, caractere)
        return caractere

    def posicoes_1_2_3(self, lista: list) -> None:
        for i in range(3):
            lista[i] = self.numero_para_letra(lista[i])

    def posicao_4(self, lista: list) -> None:
        lista[3] = self.letra_para_numero(lista[3])

    def posicao_5(self, lista: list) -> None:
        lista[4] = self.numero_para_letra(lista[4])

    def posicoes_6_7(self, lista: list, final: int) -> None:
        for i in range(5, final):
            lista[i] = self.letra_para_numero(lista[i])