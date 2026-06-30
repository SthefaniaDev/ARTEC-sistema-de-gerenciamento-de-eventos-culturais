"""Módulo contendo a classe base e subclasses dos Trabalhos Artísticos."""
from abc import abstractmethod
from interfaces import Avaliavel

class Trabalho(Avaliavel):
    """Classe abstrata que representa um trabalho artístico genérico."""
    
    def __init__(self, titulo: str, participante, nivel_avaliacao: str):
        if not titulo or not titulo.strip():
            raise ValueError("O título do trabalho não pode ser vazio.")
        
        self.titulo = titulo
        self.participante = participante
        self.nivel_avaliacao = nivel_avaliacao
        self.status = "Inscrito"
        self.jurado = None
        self.nota = None
        self.comentario = None

    @abstractmethod
    def avaliar(self, nota: float, comentario: str) -> None:
        pass

    @abstractmethod
    def calcular_nivel_avaliacao(self) -> str:
        """Garante que todas as subclasses implementarão este método para o polimorfismo."""
        pass

    def alterar_status(self, novo_status: str) -> None:
        self.status = novo_status

    def __str__(self) -> str:
        base_info = f"Título: {self.titulo} | Participante: {self.participante.nome} | "
        if self.jurado:
            return base_info + (f"Jurado: {self.jurado.nome} | Status: {self.status} | "
                                f"Nível de Avaliação: {self.nivel_avaliacao} | Nota: {self.nota}")
        return base_info + f"Status: {self.status} | Nível de Avaliação: {self.nivel_avaliacao}"

class TrabalhoPintura(Trabalho):
    def __init__(self, titulo: str, participante):
        super().__init__(titulo, participante, "Alta")

    def avaliar(self, nota: float, comentario: str) -> None:
        self.nota = nota
        self.comentario = comentario
        self.status = "Avaliado"
        print(f"Trabalho de pintura '{self.titulo}' avaliado.")

    def calcular_nivel_avaliacao(self) -> str:
        return self.nivel_avaliacao


class TrabalhoFotografia(Trabalho):
    def __init__(self, titulo: str, participante):
        super().__init__(titulo, participante, "Média")

    def avaliar(self, nota: float, comentario: str) -> None:
        self.nota = nota
        self.comentario = comentario
        self.status = "Avaliado"
        print(f"Trabalho de fotografia '{self.titulo}' avaliado.")

    def calcular_nivel_avaliacao(self) -> str:
        return self.nivel_avaliacao


class TrabalhoMusica(Trabalho):
    def __init__(self, titulo: str, participante):
        super().__init__(titulo, participante, "Variável")

    def avaliar(self, nota: float, comentario: str) -> None:
        self.nota = nota
        self.comentario = comentario
        self.status = "Avaliado"
        print(f"Trabalho de música '{self.titulo}' avaliado.")

    def calcular_nivel_avaliacao(self) -> str:
        return self.nivel_avaliacao