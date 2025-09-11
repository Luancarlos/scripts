#!/usr/bin/env python3
"""Agente que combina módulos: AppActions, MouseActions, TypingActions."""
from __future__ import annotations
import random
import time
from services.app_actions import AppActions
from services.mouse_actions import MouseActions
from services.typing_actions import TypingActions
from data.text_blocks import JAVA_GARANTIA_BLOCKS

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

    def scroll_down(self):
        self.mouse.scroll_human(10)

    def page_down(self):
        self.apps.press_page_down(5)

    def page_up(self):
        self.apps.press_page_up(5)

    def execute(self, texto: str):
        i = 0
        self.human_type(texto, long_pause_chance=0.02, long_pause_range=(1, 5), allow_errors=False)
        self.save_active_file()

        time.sleep(5)
        acoes = ['MOVER', 'CLICK', 'DOUBLE_CLICK', 'RIGHT_CLICK', 'ESPERA', 'TECLADO']
        while i < 10:
            acao = random.choice(acoes)
            if acao == 'MOVER':
                self.move_mouse()
            elif acao == 'CLICK':
                self.click(500, random.randint(400, 600))
            elif acao == 'DOUBLE_CLICK':
                self.mouse.double_click(500, random.randint(400, 600))
            elif acao == 'RIGHT_CLICK':
                self.mouse.right_click(500, random.randint(400, 600))
            elif acao == 'ESPERA':
                time.sleep(random.randint(1, 5))
            elif acao == 'TECLADO':
                for _ in range(3):
                    direcoes = ['LEFT', 'RIGHT', 'UP', 'DOWN']
                    direcao = random.choice(direcoes)
                    getattr(self.apps, f"press_{direcao.lower()}")()
                    time.sleep(0.5)
            i += 1
            
        time.sleep(2)
        self.apps.press_page_down(3)
        time.sleep(2)
        self.move_mouse_human(500, random.randint(400, 600))
        self.click(500, random.randint(400, 600))
        self.move_mouse()
        self.scroll_human(10)
        self.scroll_human(10)

if __name__ == "__main__":
    agent = ProductW()
    agent.countdown(10)
    while True:
        agent.move_mouse()
        time.sleep(5)
        for block in JAVA_GARANTIA_BLOCKS:
            agent.execute(block)






