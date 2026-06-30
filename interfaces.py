"""Módulo responsável pelas interfaces e contratos do sistema ARTEC."""
from abc import ABC, abstractmethod

class Avaliavel(ABC):
    """Contrato de comportamento para objetos que podem ser avaliados."""
    
    @abstractmethod
    def avaliar(self, nota: float, comentario: str) -> None:
        pass