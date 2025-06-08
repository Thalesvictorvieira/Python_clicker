from PySide6.QtWidgets import QApplication,QPushButton,QVBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from my_window import My_window_creator
from components import create_button, create_label
import sys

app = QApplication(sys.argv)
window = My_window_creator()
contador = {"Snakes": 0}

# Label inicial com o valor do contador
label = create_label(f"Snakes: {contador['Snakes']}")

# Função para incrementar o contador e atualizar o texto da label
def Action_cliclk():
    contador["Snakes"] += 1
    label.setText(f"Snakes: {contador['Snakes']}")
    print(f"Contador: {contador['Snakes']}")

# Botão com ação personalizada
#botao = create_button()
#botao.clicked.connect(acao_click)  # agora conectado à função correta


# Prinipal Button
Principal_button = QPushButton()

#input a image in a Principal Button
Icone = QIcon("/media/thales/LINUX_HD/Programacao/Python_clicker/src/icon_python.png")
Principal_button.setIcon(Icone)  # Substitua por seu arquivo de imagem
Principal_button.setIconSize(QSize(64, 64))  # Tamanho da imagem no botão
Principal_button.setStyleSheet("font-size: 14px; padding: 10px;")
Principal_button.clicked.connect(Action_cliclk)




# Adiciona os widgets na janela
window.add_widget(label)
window.add_widget(Principal_button)
# Exibe a janela
window.show()
sys.exit(app.exec())


#Primeira versao o contador funciona mas nao tem upgrade 
#Basicamente sim, mas ele vei ter upgrade, tipo cokie clicker
