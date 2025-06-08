import sys
import os
import json
from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox, QCheckBox, QLabel, QGridLayout, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QUrl, Qt
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect


# Caminhos
CAMINHO_ARQUIVO = "savegame.json"
CLICK_SOUND_PATH = "/media/thales/LINUX_HD/Programacao/Python_clicker/src/assets/sounds/Click.wav"
MUSIC_PATH = "/media/thales/LINUX_HD/Programacao/Python_clicker/src/assets/sounds/Music.mp3"
BACKGROUND_IMAGE_PATH = "/media/thales/LINUX_HD/Programacao/Python_clicker/src/assets/icons/background.png"  # ajuste o caminho

# Variáveis do jogo
snakes = {"Clicks": 0}
upgrade_number = 1

# Inicializa app e janela
app = QApplication(sys.argv)

# Janela principal customizada
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle("Python Clicker")
        self.resize(900, 700)

        # Layouts
        self.main_layout = QVBoxLayout(self)   # vertical: upgrades + botão + outras coisas
        self.upgrades_layout = QGridLayout()   # grade para upgrades

        # Label clicks
        self.Label_num_snakes = QLabel(f"Snakes: {snakes['Clicks']}")
        self.Label_num_snakes.setStyleSheet("font-size: 28px; color: white;")
        self.Label_num_snakes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.Label_num_snakes)

        # Botão principal
        self.Python_button = QPushButton()
        self.Python_button.setIcon(QIcon("/media/thales/LINUX_HD/Programacao/Python_clicker/src/assets/icons/icon_python.png"))
        self.Python_button.setFixedSize(150, 150)
        self.Python_button.setIconSize(QSize(100, 100))
        self.Python_button.setStyleSheet('''
            QPushButton {
                background-color: darkgray;
                border-radius: 70px;
                border: 50px;
            }
            QPushButton:pressed {
                background-color: gray;
            }
        ''')
        self.main_layout.addWidget(self.Python_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Botões salvar, carregar e mutar
        self.botao_salvar = QPushButton("Salvar Progresso")
        self.botao_carregar = QPushButton("Carregar Progresso")
        self.caixa_musica = QCheckBox("Mutar música")

        self.main_layout.addWidget(self.botao_salvar)
        self.main_layout.addWidget(self.botao_carregar)
        self.main_layout.addWidget(self.caixa_musica)

        # Adiciona layout upgrades no topo
        self.main_layout.insertLayout(0, self.upgrades_layout)

        # Conecta ações
        self.Python_button.clicked.connect(self.click)
        self.botao_salvar.clicked.connect(self.salvar_progresso)
        self.botao_carregar.clicked.connect(self.carregar_progresso)
        self.caixa_musica.stateChanged.connect(self.toggle_musica)

        # Som e música
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(MUSIC_PATH))
        self.audio_output.setVolume(0.3)
        self.player.setLoops(QMediaPlayer.Infinite)
        self.player.play()

        self.click_sound = QSoundEffect()
        self.click_sound.setSource(QUrl.fromLocalFile(CLICK_SOUND_PATH))
        self.click_sound.setVolume(0.8)

        # Cria upgrades
        self.upgrades = []
        self.upgrade_number = 1
        self.create_upgrades()

    def create_upgrades(self):
        # Exemplo upgrades: 20 upgrades com multiplicadores e preços
        # preços: 200, 400, 800, 1000, 1500... conforme pedido
        preco_base = 200
        multiplicadores = [2,4,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42]
        precos = [200,400,800,1000,1500,1800,2100,2400,2700,3000,3300,3600,3900,4200,4500,4800,5100,5400,5700,6000]

        for i in range(20):
            mult = multiplicadores[i]
            preco = precos[i]
            btn = QPushButton(f"{mult}x Upgrade ({preco} clicks)")
            btn.setFixedSize(160,40)
            btn.setStyleSheet("background-color: darkgray; border-radius: 10px;")
            btn.clicked.connect(lambda checked, p=preco, m=mult, b=btn: self.tentar_upgrade(p,m,b))
            self.upgrades.append(btn)
            # Organiza em grade: 6 colunas por linha
            linha = i // 6
            coluna = i % 6
            self.upgrades_layout.addWidget(btn, linha, coluna)

    def tentar_upgrade(self, preco, multiplicador, botao):
        if snakes["Clicks"] >= preco:
            snakes["Clicks"] -= preco
            self.upgrade_number = multiplicador
            self.Label_num_snakes.setText(f"Snakes: {snakes['Clicks']}")
            botao.hide()
        else:
            QMessageBox.information(self, "Dinheiro insuficiente", "Você não tem clicks suficientes para esse upgrade.")

    def click(self):
        snakes["Clicks"] += self.upgrade_number
        self.Label_num_snakes.setText(f"Snakes: {snakes['Clicks']}")
        self.click_sound.play()

    def salvar_progresso(self):
        with open(CAMINHO_ARQUIVO, "w") as f:
            json.dump(snakes, f)
        print("Progresso salvo:", snakes)

    def carregar_progresso(self):
        if os.path.exists(CAMINHO_ARQUIVO):
            with open(CAMINHO_ARQUIVO, "r") as f:
                dados = json.load(f)
                snakes["Clicks"] = dados.get("Clicks", 0)
            self.Label_num_snakes.setText(f"Snakes: {snakes['Clicks']}")
        else:
            QMessageBox.information(self, "Aviso", "Arquivo de progresso não encontrado.")

    def toggle_musica(self, state):
        self.audio_output.setMuted(state == 2)  # 2 == QCheckBox.Checked


if __name__ == "__main__":
    window = MainWindow()

    # Aplica fundo na janela, sem afetar botões
    if BACKGROUND_IMAGE_PATH and os.path.exists(BACKGROUND_IMAGE_PATH):
        window.setStyleSheet(f"""
            QWidget#MainWindow {{
                background-image: url("{BACKGROUND_IMAGE_PATH}");
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }}
            QPushButton {{
                background-color: darkgray;
                border-radius: 10px;
                border: 2px solid black;
            }}
            QPushButton:pressed {{
                background-color: gray;
            }}
            QLabel {{
                color: white;
            }}
        """)

    window.show()
    sys.exit(app.exec())
