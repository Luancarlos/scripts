# Lógica de digitação humana
from __future__ import annotations
import random
import string
import time
from typing import Tuple
try:
    import pyautogui  # type: ignore
except ImportError:  # pragma: no cover
    pyautogui = None  # type: ignore

class TypingActions:
    def __init__(self,
                 min_char_delay: float = 0.035,
                 max_char_delay: float = 0.18,
                 error_rate: float = 0.07):
        self.min_char_delay = min_char_delay
        self.max_char_delay = max_char_delay
        self.error_rate = error_rate
        self._keyboard_neighbors = self._build_keyboard_neighbors()

    def human_type(self, text: str, select_all: bool = False,
                   long_pause_chance: float = 0.012,
                   long_pause_range: Tuple[float, float] = (20.0, 120.0),
                   on_long_pause=None) -> None:
        if not pyautogui:
            return
        if select_all:
            system_hotkey = ['command', 'a'] if pyautogui.platform.system().lower() == 'darwin' else ['ctrl', 'a']  # type: ignore
            pyautogui.hotkey(*system_hotkey)
            time.sleep(0.15)
        for token in text:
            if token in (' ', '\n', '.', '!', '?') and random.random() < long_pause_chance:
                lp = random.uniform(*long_pause_range)
                print(f"Pausa humana longa (~{lp:.1f}s)...")
                if on_long_pause:
                    on_long_pause()
                time.sleep(lp)
            time.sleep(random.uniform(self.min_char_delay, self.max_char_delay))
            if token == '\n':
                pyautogui.press('enter'); continue
            if token == '\t':
                pyautogui.press('tab'); continue
            if token.isalpha() and random.random() < self.error_rate:
                wrong = self._random_error_char(token)
                pyautogui.typewrite(wrong)
                time.sleep(random.uniform(0.05, 0.22))
                if random.random() < 0.25 and token.isalpha():
                    pyautogui.typewrite(self._random_error_char(token))
                    time.sleep(random.uniform(0.04, 0.18))
                for _ in range(random.randint(1, 2)):
                    pyautogui.press('backspace')
                    time.sleep(random.uniform(0.03, 0.09))
            pyautogui.typewrite(token)
            if token in '.!?':
                time.sleep(random.uniform(0.25, 0.55))
            elif token == ' ' and random.random() < 0.3:
                time.sleep(random.uniform(0.08, 0.2))

    def _build_keyboard_neighbors(self):
        rows = ["1234567890", "qwertyuiop", "asdfghjkl", "zxcvbnm"]
        neighbors = {}
        for r, row in enumerate(rows):
            for c, ch in enumerate(row):
                adj = set()
                for dr in (-1, 0, 1):
                    nr = r + dr
                    if 0 <= nr < len(rows):
                        for dc in (-1, 0, 1):
                            if dr == 0 and dc == 0: continue
                            nc = c + dc
                            if 0 <= nc < len(rows[nr]): adj.add(rows[nr][nc])
                neighbors[ch] = list(adj)
        return neighbors

    def _random_error_char(self, correct: str) -> str:
        base = correct.lower()
        if base in self._keyboard_neighbors and self._keyboard_neighbors[base]:
            cand = random.choice(self._keyboard_neighbors[base])
            return cand.upper() if correct.isupper() else cand
        letters = string.ascii_lowercase
        cand = random.choice(letters.replace(base, ''))
        return cand.upper() if correct.isupper() else cand