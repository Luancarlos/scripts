#!/usr/bin/env python3
"""Agente que combina módulos: AppActions, MouseActions, TypingActions."""
from __future__ import annotations
import random
import time
from services.app_actions import AppActions
from services.mouse_actions import MouseActions
from services.typing_actions import TypingActions

class ProductW:
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

    def open_default_text_editor(self) -> None:
        self.apps.open_default_text_editor()

    def move_mouse_human(self, x: int, y: int, **kw):
        self.mouse.move_mouse_human(x, y, **kw)

    def click(self, x: int, y: int, **kw):
        self.mouse.click(x, y, **kw)

    def scroll_human(self, clicks: int):
        self.mouse.scroll_human(clicks)

    def human_type(self, text: str, **kw):
        """Apenas digita (não movimenta mouse automaticamente)."""
        self.typing.human_type(text, **kw)

    def get_mouse_position(self) -> tuple[int, int]:
        return self.mouse.get_mouse_position()

    # Facades de salvar (delegam para AppActions)
    def save_active_file(self) -> None:
        self.apps.save_active_file()

    def save_active_file_as(self, file_path: str) -> None:
        self.apps.save_active_file_as(file_path)

    # Novos atalhos de app
    def close_active_application(self):
        self.apps.close_active_application()

    def open_vscode(self):
        self.apps.open_vscode()

    def open_teams(self):
        self.apps.open_teams()

    def open_onenote(self):
        self.apps.open_onenote()

    def open_insomnia(self):
        self.apps.open_insomnia()

    def countdown(self, seconds: int = 3):
        for i in range(seconds, 0, -1):
            print(f"Iniciando em {i}...")
            time.sleep(1)
        print("Executando...")
    
    def move_mouse(self):
        currente_position = self.get_mouse_position()
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        self.move_mouse_human(x, y)
        self.move_mouse_human(currente_position[0], currente_position[1])
        self.move_mouse_human(x, y)
        self.move_mouse_human(random.randint(0, 1000), random.randint(0, 1000))
    
    def press_enter(self):
        self.apps.press_enter()

    def vscode_new_tab(self):
        self.apps.open_vscode_new_tab()

    def keyboardMove(self, direction: str):
        direction = direction.upper()
        if direction == 'LEFT':
            self.apps.press_left()
        elif direction == 'RIGHT':
            self.apps.press_right()
        elif direction == 'UP':
            self.apps.press_up()
        elif direction == 'DOWN':
            self.apps.press_down()


if __name__ == "__main__":
    agent = ProductW()
    agent.countdown(10)
    acoes = ['MOVER', 'CLICK', 'DOUBLE_CLICK', 'RIGHT_CLICK', 'ENTER', 'ESPERA', 'TECLADO']

    while True:
        acao = random.choice(acoes)
        if acao == 'MOVER':
            agent.move_mouse()
        elif acao == 'CLICK':
            agent.click(500, random.randint(400, 600))
        elif acao == 'DOUBLE_CLICK':
            agent.mouse.double_click(500, random.randint(400, 600))
        elif acao == 'RIGHT_CLICK':
            agent.mouse.right_click(500, random.randint(400, 600))
        elif acao == 'ENTER':
            agent.press_enter()
        elif acao == 'ESPERA':
            time.sleep(random.randint(1, 5))
        elif acao == 'TECLADO':
            cont = 0
            while cont < 3 :
                direcoes = ['LEFT', 'RIGHT', 'UP', 'DOWN']
                direcao = random.choice(direcoes)
                agent.keyboardMove(direcao)
                time.sleep(0.5)
                cont += 1

        
        

        
        


