# Lida com abertura de aplicativos e escolha de editor padrão
from __future__ import annotations
import os
import platform
import subprocess
import time
try:
    import pyautogui  # type: ignore
except Exception:
    pyautogui = None  # type: ignore

class AppActions:
    def open_application(self, name_or_path: str) -> None:
        system = platform.system().lower()
        if system == 'darwin':
            if os.path.splitext(name_or_path)[1] == '.app' or '/' in name_or_path:
                subprocess.Popen(['open', name_or_path])
            else:
                subprocess.Popen(['open', '-a', name_or_path])
        elif system == 'windows':
            try:
                os.startfile(name_or_path)  # type: ignore[attr-defined]
            except OSError:
                subprocess.Popen(['start', '', name_or_path], shell=True)
        else:
            subprocess.Popen([name_or_path])

    def default_text_editor(self) -> str:
        system = platform.system().lower()
        if system == 'darwin':
            return 'TextEdit'
        if system == 'windows':
            return 'notepad'
        return 'gedit'

    # --- Novos métodos ---
    def close_active_application(self) -> None:
        system = platform.system().lower()
        if not pyautogui:
            return
        if system == 'darwin':
            pyautogui.hotkey('command', 'q')
        else:
            pyautogui.hotkey('alt', 'f4')

    def open_vscode(self) -> None:
        system = platform.system().lower()
        if system == 'darwin':
            self.open_application('Visual Studio Code')
        elif system == 'windows':
            # Tenta a CLI 'code' ou o executável instalado
            try:
                subprocess.Popen(['code'])
            except Exception:
                self.open_application('Code')
        else:
            try:
                subprocess.Popen(['code'])
            except Exception:
                self.open_application('code')

    def open_vscode_new_tab(self, wait_open: float = 3.0) -> None:
        """Abre o VS Code e cria uma nova aba/arquivo (Cmd/Ctrl+N) para digitar."""
        self.open_vscode()
        # Aguarda a janela abrir/ganhar foco
        time.sleep(wait_open)
        if not pyautogui:
            return
        # Novo arquivo (não nova janela)
        if platform.system().lower() == 'darwin':
            pyautogui.hotkey('command', 'n')
        else:
            pyautogui.hotkey('ctrl', 'n')
        time.sleep(0.3)

    def open_teams(self) -> None:
        system = platform.system().lower()
        if system == 'darwin':
            self.open_application('Microsoft Teams')
        elif system == 'windows':
            # Protocolo registrado costuma existir
            subprocess.Popen(['start', '', 'msteams:'], shell=True)
        else:
            self.open_application('teams')

    def open_onenote(self) -> None:
        system = platform.system().lower()
        if system == 'darwin':
            self.open_application('Microsoft OneNote')
        elif system == 'windows':
            subprocess.Popen(['start', '', 'onenote:'], shell=True)
        else:
            self.open_application('onenote')

    def open_insomnia(self) -> None:
        system = platform.system().lower()
        if system == 'darwin':
            self.open_application('Insomnia')
        elif system == 'windows':
            try:
                subprocess.Popen(['insomnia'])
            except Exception:
                # Tenta via caminho padrão (pode variar)
                self.open_application('Insomnia')
        else:
            try:
                subprocess.Popen(['insomnia'])
            except Exception:
                self.open_application('insomnia')

    def open_default_text_editor(self) -> None:
        """Abre o editor de texto padrão do sistema."""
        editor = self.default_text_editor()
        self.open_application(editor)

    def press_enter(self) -> None:
        """Pressiona a tecla Enter."""
        if not pyautogui:
            return
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.2)

    # Novas teclas direcionais
    def press_left(self) -> None:
        if not pyautogui:
            return
        pyautogui.press('left')

    def press_right(self) -> None:
        if not pyautogui:
            return
        pyautogui.press('right')

    def press_up(self) -> None:
        if not pyautogui:
            return
        pyautogui.press('up')

    def press_down(self) -> None:
        if not pyautogui:
            return
        pyautogui.press('down')

    def press_page_down(self, times: int = 1) -> None:
        """Pressiona Page Down 'times' vezes."""
        if not pyautogui:
            return
        for _ in range(max(1, times)):
            pyautogui.press('pagedown')
            time.sleep(0.1)

    def press_page_up(self, times: int = 1) -> None:
        """Pressiona Page Up 'times' vezes."""
        if not pyautogui:
            return
        for _ in range(max(1, times)):
            pyautogui.press('pageup')
            time.sleep(0.1)

    def save_active_file(self) -> None:
        """Dispara o atalho de salvar no app ativo (Cmd/Ctrl+S)."""
        if not pyautogui:
            return
        time.sleep(0.1)
        if platform.system().lower() == 'darwin':
            pyautogui.hotkey('command', 's')
        else:
            pyautogui.hotkey('ctrl', 's')
        time.sleep(0.2)

    def save_active_file_as(self, file_path: str) -> None:
        """Abre 'Salvar como', digita o caminho e confirma (Cmd/Ctrl+Shift+S)."""
        if not pyautogui:
            return
        if platform.system().lower() == 'darwin':
            pyautogui.hotkey('command', 'shift', 's')
        else:
            pyautogui.hotkey('ctrl', 'shift', 's')
        time.sleep(0.6)
        pyautogui.typewrite(file_path)
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(0.4)
        pyautogui.press('enter')

    def go_to_end_of_file(self) -> None:
        """Atalho para ir ao final do arquivo no editor ativo."""
        if not pyautogui:
            return
        sys = platform.system().lower()
        if sys == 'darwin':
            pyautogui.hotkey('command', 'down')
        else:
            pyautogui.hotkey('ctrl', 'end')
        time.sleep(0.1)
