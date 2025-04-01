
# boss.py
from opponent import Opponent

class Boss(Opponent):
    """
    Clase que representa al jefe final del juego.
    Hereda de Opponent pero se mueve el doble de rápido.
    """

    def __init__(self, x: int, y: int):
        """
        Inicializa al jefe con imagen 'B'.
        Args:
            x (int): Posición horizontal inicial.
            y (int): Posición vertical inicial.
        """
        super().__init__(x, y)
        self._image = 'B'  # Sobrescribe la imagen

    def move(self, board_width: int):
        """
        Movimiento del jefe (más rápido que el oponente normal).
        Este método será gestionado desde Game con velocidad mayor.
        Args:
            board_width (int): Límite del tablero.
        """
        pass  # Lógica gestionada desde Game para mantener consistencia
