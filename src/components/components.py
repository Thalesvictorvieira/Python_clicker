from PySide6.QtWidgets import QPushButton, QLabel,QMessageBox,QApplication
from PySide6.QtCore import QSize

def create_button(Connect_funcion):
    button = QPushButton("Clique aqui")
    button.clicked.connect(Connect_funcion)
    button.setFixedSize(QSize(100,40))
    return button

def create_label(texto):
    from PySide6.QtWidgets import QLabel
    return QLabel(texto)


#Create a principal button
def create_Upgrade_button(text = '', Price=0):
    botao = QPushButton(f"{text}({Price} Clicks)")
    botao.setFixedSize(QSize(160,40))
    return botao
    

def upgrade(preco, up, snakes, multiplicador, label_clicks, upgrade_button, parent):
    if snakes["count"] >= preco:
        snakes["count"] -= preco
        multiplicador["Valor"] *= up
        label_clicks.setText(f"Snakes: {snakes['count']}")
        upgrade_button.hide()  # esconde o botão após a compra
    else:
        QMessageBox.warning(parent, "Alerta", "Cobras insuficientes para comprar o upgrade!")

