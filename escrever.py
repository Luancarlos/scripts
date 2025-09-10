#!/usr/bin/env python3
"""Script de exemplo usando o agente modular."""
from __future__ import annotations
import time
from agent import HumanAgent

if __name__ == "__main__":
    agent = HumanAgent(min_char_delay=0.04, max_char_delay=0.17, error_rate=0.08)
    agent.countdown(3)
    editor = agent.default_text_editor()
    print(f"Abrindo editor: {editor}")
    agent.open_application(editor)
    time.sleep(3.5)
    texto = (
        "Olá, isto é um teste? de digitação humana simulada. "
        "O script insere erros aleatórios, usa backspace e continua.\n\n"
        "Linha nova para demonstrar quebras. Fim.\n"
        "input[type=\"text\"]:focus{box-shadow:0 0 0 4px rgba(37,99,235,0.06); border-color:var(--accent);}\n"
        "..row{display:flex; gap:10px;}..small{flex:1;}\n..btn{ width:100%; padding:12px; border-radius:10px; border:0; background:var(--accent); color:white; font-weight:600; cursor:pointer; }\n"
    )
    agent.human_type(texto, long_pause_chance=0.02, long_pause_range=(20, 120))
    print("Concluído.")
