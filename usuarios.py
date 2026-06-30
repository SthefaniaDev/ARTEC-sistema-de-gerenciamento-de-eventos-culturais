"""Módulo contendo os atores e perfis de usuário do sistema ARTEC."""
from trabalhos import Trabalho, TrabalhoPintura, TrabalhoFotografia, TrabalhoMusica

class PessoaARTEC:
    """Classe base para entidades de pessoas no sistema."""
    
    def __init__(self, matricula: str, nome: str):
        if not matricula or not str(matricula).strip():
            raise ValueError("A matrícula/identificação não pode ser vazia.")
        if not nome or not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        
        self.matricula = matricula
        self.nome = nome


class Participante(PessoaARTEC):
    """Classe que representa um candidato competidor."""
    
    LIMITE_INSCRICOES_POR_CATEGORIA = 2

    def __init__(self, matricula: str, nome: str):
        super().__init__(matricula, nome)
        self.trabalhos_inscritos = []

    def inscrever_trabalho(self, tipo: str, titulo: str) -> Trabalho:
        """Padrão Factory para criação e validação de trabalhos."""
        try:
            tipo_normalizado = tipo.strip().lower()
        except AttributeError:
            raise TypeError("O tipo de trabalho deve ser informado como texto.")

        # Dicionário substitui múltiplos if/elifs de forma mais elegante e profissional
        categorias = {
            "pintura": TrabalhoPintura,
            "fotografia": TrabalhoFotografia,
            "musica": TrabalhoMusica
        }

        if tipo_normalizado not in categorias:
            raise ValueError(f"Categoria de trabalho inválida: '{tipo}'.")

        classe_trabalho = categorias[tipo_normalizado]

        total_na_categoria = sum(
            1 for trabalho in self.trabalhos_inscritos if isinstance(trabalho, classe_trabalho)
        )
        
        if total_na_categoria >= self.LIMITE_INSCRICOES_POR_CATEGORIA:
            raise PermissionError(
                f"Limite de {self.LIMITE_INSCRICOES_POR_CATEGORIA} inscrições "
                f"por categoria atingido para '{tipo}'."
            )

        novo_trabalho = classe_trabalho(titulo, self)
        self.trabalhos_inscritos.append(novo_trabalho)
        return novo_trabalho


class Jurado(PessoaARTEC):
    """Classe que representa o avaliador das obras."""
    
    def __init__(self, matricula: str, nome: str):
        super().__init__(matricula, nome)
        self.trabalhos_avaliados = []

    def avaliar_trabalho(self, trabalho: Trabalho, nota: float, comentario: str = "") -> None:
        """Associa o jurado à obra e realiza a validação de regras de negócio."""
        if not isinstance(trabalho, Trabalho):
            raise TypeError("Só é possível avaliar instâncias de Trabalho.")

        if trabalho in self.trabalhos_avaliados:
            raise PermissionError(
                f"O jurado {self.nome} já avaliou o trabalho '{trabalho.titulo}'."
            )

        try:
            nota = float(nota)
        except (TypeError, ValueError):
            raise ValueError("A nota informada é inválida.")

        if not (0 <= nota <= 10):
            raise ValueError("A nota deve estar entre 0 e 10.")

        trabalho.jurado = self
        trabalho.avaliar(nota, comentario)
        self.trabalhos_avaliados.append(trabalho)