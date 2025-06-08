from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
import sys

# Primeiro: crie a aplicação
app = QApplication(sys.argv)

# Agora você pode usar QIcon, QPixmap etc.
window = QWidget()
layout = QVBoxLayout()

botao = QPushButton()
botao.setFixedSize(80, 80)
botao.setIcon(QIcon("/media/thales/LINUX_HD/Programacao/Python_clicker/src/icon_python.png"))  # Caminho completo
botao.setIconSize(QSize(64, 64))
botao.setText("")  # Sem texto
botao.setStyleSheet("""
    QPushButton {
        border: none;
        border-radius: 40px;
        background-color: #f0f0f0;
    }
""")

layout.addWidget(botao)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
