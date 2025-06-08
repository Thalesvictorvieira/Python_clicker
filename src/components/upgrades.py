# upgrades.py
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize

def create_upgrade_button(label, value, cost, snakes, upgrade_state, label_clicks, layout):
    botao = QPushButton(f"{label} ({cost} Clicks)")
    botao.setFixedSize(QSize(160, 40))

    def upgrade_action():
        if snakes["Clicks"] >= cost:
            snakes["Clicks"] -= cost
            upgrade_state["multiplier"] = value
            botao.hide()
            label_clicks.setText(f"Snakes: {snakes['Clicks']}")
        else:
            botao.setText("Snakes insuficientes")

    botao.clicked.connect(upgrade_action)
    layout.add_widget(botao)

# upgrades list
# components/upgrades.py

upgrades_list = [
    {"multiplicador": 2, "preco": 200},
    {"multiplicador": 4, "preco": 400},
    {"multiplicador": 8, "preco": 800},
    {"multiplicador": 10, "preco": 1000},
    {"multiplicador": 12, "preco": 1500},
    {"multiplicador": 14, "preco": 2000},
    {"multiplicador": 16, "preco": 3000},
    {"multiplicador": 18, "preco": 4000},
    {"multiplicador": 20, "preco": 5000},
    {"multiplicador": 22, "preco": 6000},
    {"multiplicador": 24, "preco": 7000},
    {"multiplicador": 26, "preco": 8000},
    {"multiplicador": 28, "preco": 9000},
    {"multiplicador": 30, "preco": 10000},
    {"multiplicador": 32, "preco": 12000},
    {"multiplicador": 34, "preco": 14000},
    {"multiplicador": 36, "preco": 16000},
    {"multiplicador": 38, "preco": 18000},
    {"multiplicador": 40, "preco": 20000},
    {"multiplicador": 50, "preco": 25000},
]
