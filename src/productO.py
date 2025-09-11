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


if __name__ == "__main__":
    garantias = ["garantias_penhor.js", "garantias_veiculos.js", "garantias_maquinas.js", "garantias_agricola.js", "garantias_mercantil.js"]
    agent = ProductW()
    agent.countdown(10)

    while True:
        agent.open_default_text_editor()
        time.sleep(5)
        agent.move_mouse()
        agent.move_mouse()
        time.sleep(5)
        texto = (
            "Veículos, máquinas e equipamentos possuem prazos distintos de garantia, geralmente definidos pelo fabricante\n",
            "Garantia legal: no Brasil, mínimo de 90 dias para bens duráveis (ex.: carros, tratores, empilhadeiras)\n",
            "Garantia contratual: pode ser estendida, dependendo do contrato ou plano de manutenção oferecido\n",
            "É importante guardar nota fiscal e termo de garantia, pois servem como comprovação em caso de defeito\n",
            "A cobertura geralmente inclui defeitos de fabricação e falhas em peças originais, mas não cobre mau uso, desgaste natural ou manutenção inadequada\n",
            "Em máquinas e equipamentos industriais, pode haver cláusula exigindo que a manutenção seja feita em oficinas autorizadas, sob pena de perda da garantia\n",
            "Algumas empresas oferecem garantia estendida ou planos de manutenção preventiva como diferencial competitivo\n",
            "Recomenda-se sempre verificar os prazos de cobertura, o que está incluído/excluído e se há exigências de registro das revisões\n",
            "Em veículos, a garantia pode variar de 1 a 5 anos, dependendo da marca\n",
            "Em tratores, colheitadeiras e outros equipamentos agrícolas, muitas vezes a garantia cobre apenas o trem de força ou componentes críticos\n",
        )
        agent.human_type(texto, long_pause_chance=0.02, long_pause_range=(20, 40))
        # Exemplo de salvar
        agent.save_active_file()
        agent.human_type(garantias[random.randint(0, len(garantias) - 1)], long_pause_chance=0.0)
        agent.move_mouse()
        agent.press_enter()
        time.sleep(5)
        agent.close_active_application()

        agent.open_vscode()
        time.sleep(5)
        agent.vscode_new_tab()
        texto = (
            "// Cadastro de Garantias \n"
            "function Garantia(id, cliente, produto, prazoMeses) \n"
            "\t{ \n"
            "\t\tthis.id = id; \n"
            "\t\tthis.cliente = cliente; \n"
            "\t\tthis.produto = produto; \n"
            "\t\tthis.prazoMeses = prazoMeses; \n"
            "\t\tthis.dataCadastro = new Date(); \n"
            "\t\tthis.status = 'Ativa'; \n"
            "\t} \n"
            "\n"
            "var garantias = []; \n"
            "\n"
            "function cadastrarGarantia(id, cliente, produto, prazoMeses) \n"
            "\t{ \n"
            "\t\tvar novaGarantia = new Garantia(id, cliente, produto, prazoMeses); \n"
            "\t\tgarantias.push(novaGarantia); \n"
            "\t\tconsole.log('Garantia cadastrada:', novaGarantia); \n"
            "\t} \n"
            "\n"
            "function listarGarantias() \n"
            "\t{ \n"
            "\t\tconsole.log('Lista de Garantias:'); \n"
            "\t\tfor(var i = 0; i < garantias.length; i++) \n"
            "\t\t\t{ \n"
            "\t\t\t\tconsole.log(garantias[i]); \n"
            "\t\t\t} \n"
            "\t} \n"
            "\n"
            "function buscarGarantiaPorCliente(cliente) \n"
            "\t{ \n"
            "\t\tvar resultados = []; \n"
            "\t\tfor(var i = 0; i < garantias.length; i++) \n"
            "\t\t\t{ \n"
            "\t\t\t\tif(garantias[i].cliente === cliente) \n"
            "\t\t\t\t\tresultados.push(garantias[i]); \n"
            "\t\t\t} \n"
            "\t\treturn resultados; \n"
            "\t} \n"
            "\n"
            "function atualizarStatusGarantia(id, status) \n"
            "\t{ \n"
            "\t\tfor(var i = 0; i < garantias.length; i++) \n"
            "\t\t\t{ \n"
            "\t\t\t\tif(garantias[i].id === id) \n"
            "\t\t\t\t\t{ \n"
            "\t\t\t\t\t\tgarantias[i].status = status; \n"
            "\t\t\t\t\t\tconsole.log('Status atualizado:', garantias[i]); \n"
            "\t\t\t\t\t} \n"
            "\t\t\t} \n"
            "\t} \n"
            "\n"
            "// Funções repetitivas para gerar mais linhas (simulando operações diversas) \n"
            "function simularOperacoes() \n"
            "\t{ \n"
            "\t\tfor(var i = 0; i < 50; i++) \n"
            "\t\t\t{ \n"
            "\t\t\t\tcadastrarGarantia(i+100, 'Cliente ' + i, 'Produto ' + i, (i%36)+1); \n"
            "\t\t\t\tif(i % 2 === 0) \n"
            "\t\t\t\t\tatualizarStatusGarantia(i+100, 'Expirada'); \n"
            "\t\t\t} \n"
            "\t} \n"
            "\n"
            "simularOperacoes(); \n"
            "listarGarantias(); \n"
        )
        agent.human_type(texto, long_pause_chance=0.02, long_pause_range=(20, 40))
        time.sleep(5)
        agent.save_active_file()
        agent.human_type(garantias[random.randint(0, len(garantias) - 1)], long_pause_chance=0.0)
        agent.move_mouse()
        agent.press_enter()

        
        


