# Lida com abertura de aplicativos e escolha de editor padrão
from __future__ import annotations
import os
import platform
import subprocess
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
