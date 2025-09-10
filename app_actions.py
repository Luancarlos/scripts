# Lida com abertura de aplicativos e escolha de editor padrão
from __future__ import annotations
import os
import platform
import subprocess

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
