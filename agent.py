#!/usr/bin/env python3
"""Agente que combina módulos: AppActions, MouseActions, TypingActions."""
from __future__ import annotations
import time
from app_actions import AppActions
from mouse_actions import MouseActions
from typing_actions import TypingActions

class HumanAgent:
    def __init__(self,
                 min_char_delay: float = 0.035,
                 max_char_delay: float = 0.18,
                 error_rate: float = 0.07):
        self.apps = AppActions()
        self.mouse = MouseActions()
        self.typing = TypingActions(min_char_delay, max_char_delay, error_rate)

    # Facades
    def open_application(self, name_or_path: str):
        self.apps.open_application(name_or_path)

    def default_text_editor(self) -> str:
        return self.apps.default_text_editor()

    def move_mouse_human(self, x: int, y: int, **kw):
        self.mouse.move_mouse_human(x, y, **kw)

    def click(self, x: int, y: int, **kw):
        self.mouse.click(x, y, **kw)

    def scroll_human(self, clicks: int):
        self.mouse.scroll_human(clicks)

    def human_type(self, text: str, **kw):
        """Apenas digita (não movimenta mouse automaticamente)."""
        # Separado: nenhuma chamada de movimento de mouse aqui.
        self.typing.human_type(text, **kw)

    def countdown(self, seconds: int = 3):
        for i in range(seconds, 0, -1):
            print(f"Iniciando em {i}...")
            time.sleep(1)
        print("Executando...")

if __name__ == "__main__":
    agent = HumanAgent()
    agent.countdown(3)
    editor = agent.default_text_editor()
    print(f"Abrindo editor: {editor}")
    agent.open_application(editor)
    time.sleep(3)

    # Exemplo estruturado: você controla explicitamente a ordem
    # 1. Mover mouse para uma área (exemplo coordenadas fictícias)
    agent.move_mouse_human(400, 300)
    # 2. Digitar primeiro bloco
    texto1 = "Primeiro bloco de texto.\n\n"
    agent.human_type(texto1, long_pause_chance=0.0)  # sem pausas longas aqui
    time.sleep(3)
    # 3. Outra movimentação manual de mouse (se quiser)
    agent.move_mouse_human(600, 320)
    time.sleep(3)
    # 4. Digitar segundo bloco com possibilidade de pausas longas
    texto2 = (
        "Segundo bloco com pausas longas possíveis.\n"
        "Você pode ajustar long_pause_chance e long_pause_range quando chamar.\n"
    )
    agent.human_type(texto2, long_pause_chance=0.02, long_pause_range=(20, 40))
    time.sleep(3)
    # 5. Clique opcional (exemplo)
    agent.move_mouse_human(1000, 600)
    agent.move_mouse_human(100, 200)
    time.sleep(3)
    agent.move_mouse_human(0, 1000)
    agent.click(600, 320)
    


    print("Concluído.")
