from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from ui.my_window import My_window_creator
from components.components import create_button,create_label,create_Upgrade_button
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
app = QApplication(sys.argv)


window = My_window_creator()

# Ícone do botão
Icone = QIcon("/media/thales/LINUX_HD/Programacao/Python_clicker/src/icon_python.png")

# Lógica
snakes = {"count": 0}
multiplicador = {"Valor": 1}


# Função principal de clique
def Click():
    snakes["count"] += multiplicador["Valor"]
    label_clicks.setText(f"Snakes: {snakes['count']}")
   

# Botão principal
Principal_button = QPushButton('')
Principal_button.clicked.connect(Click)
Principal_button.setIcon(Icone)
Principal_button.setFixedSize(150, 150)
Principal_button.setIconSize(QSize(100, 100))
Principal_button.setStyleSheet('''
    QPushButton {
        background-color: "darkgray";
        border-radius: 70px;
        border: 50px;
    }
    QPushButton:pressed {
        background-color: gray;
    }
''')

# Label de cliques
label_clicks = create_label(f"Snakes: {snakes['count']}")
label_clicks.setStyleSheet("font-size:35px")

# Botão de upgrade
label2x_upgrade = create_Upgrade_button("2x", 15)
label2x_upgrade.clicked.connect(lambda:(15, 2, snakes, multiplicador, label_clicks, label2x_upgrade, window))



# Adicionar widgets
window.add_widget(Principal_button, 0, 3)
window.add_widget(label_clicks, 3, 3)
window.add_widget(label2x_upgrade, 1, 0)

# Executar app
window.setWindowIcon(Icone)
window.show()
app.exec()
