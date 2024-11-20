import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QColorDialog, QSlider, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Простое GUI приложение')
        self.setGeometry(0, 0, 1820, 900)

        self.addRGB()
        self.addHLS()
        self.addCMYK()

        self.btnColor = QPushButton('', self)
        self.btnColor.setGeometry(1250, 250, 120, 30)
        self.btnColor.setMinimumSize(500, 500)
        self.btnColor.clicked.connect(self.openColorDialog)

        self.inputRGB = False
        self.inputHLS = False
        self.inputCMYK = False
        
        self.addSliders()


    def addSliders(self):
        self.sliderR = QSlider(Qt.Horizontal)
        self.sliderG = QSlider(Qt.Horizontal)
        self.sliderB = QSlider(Qt.Horizontal)
        self.sliderH = QSlider(Qt.Horizontal)
        self.sliderL = QSlider(Qt.Horizontal)
        self.sliderS = QSlider(Qt.Horizontal)
        self.sliderC = QSlider(Qt.Horizontal)
        self.sliderM = QSlider(Qt.Horizontal)
        self.sliderY = QSlider(Qt.Horizontal)
        self.sliderK = QSlider(Qt.Horizontal)

        self.sliderR.setRange(0, 800)
        self.sliderG.setRange(0, 800)
        self.sliderB.setRange(0, 800)
        self.sliderH.setRange(0, 800)
        self.sliderL.setRange(0, 800)
        self.sliderS.setRange(0, 800)
        self.sliderC.setRange(0, 800)
        self.sliderM.setRange(0, 800)
        self.sliderY.setRange(0, 800)
        self.sliderK.setRange(0, 800)

        self.sliderR.setValue(800)
        self.sliderG.setValue(800)
        self.sliderB.setValue(800)
        self.sliderL.setValue(800)

        emLabel1 = QLabel('', self)
        emLabel1.setMaximumSize(100, 0)
        emLabel2 = QLabel('', self)
        emLabel2.setMaximumSize(100, 0)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.sliderR)
        self.layout.addWidget(self.sliderG)
        self.layout.addWidget(self.sliderB)
        self.layout.addWidget(emLabel1)
        self.layout.addWidget(self.sliderH)
        self.layout.addWidget(self.sliderL)
        self.layout.addWidget(self.sliderS)
        self.layout.addWidget(emLabel2)
        self.layout.addWidget(self.sliderC)
        self.layout.addWidget(self.sliderM)
        self.layout.addWidget(self.sliderY)
        self.layout.addWidget(self.sliderK)
        self.layout.setContentsMargins(550, 70, 750, 150)
        self.setLayout(self.layout)

        self.sliderR.valueChanged.connect(self.slidersChanchedR)
        self.sliderG.valueChanged.connect(self.slidersChanchedG)
        self.sliderB.valueChanged.connect(self.slidersChanchedB)
        self.sliderH.valueChanged.connect(self.slidersChanchedH)
        self.sliderL.valueChanged.connect(self.slidersChanchedL)
        self.sliderS.valueChanged.connect(self.slidersChanchedS)
        self.sliderC.valueChanged.connect(self.slidersChanchedC)
        self.sliderM.valueChanged.connect(self.slidersChanchedM)
        self.sliderY.valueChanged.connect(self.slidersChanchedY)
        self.sliderK.valueChanged.connect(self.slidersChanchedK)

    def slidersChanchedR(self):
        self.inputR.setText(str(int(float(self.sliderR.value()) / 800 * 255)))

    def slidersChanchedG(self):
        self.inputG.setText(str(int(float(self.sliderG.value()) / 800 * 255)))

    def slidersChanchedB(self):
        self.inputB.setText(str(int(float(self.sliderB.value()) / 800 * 255)))

    def slidersChanchedH(self):
        self.inputH.setText(str(float(self.sliderH.value() / 800)))

    def slidersChanchedL(self):
        self.inputL.setText(str(float(self.sliderL.value() / 800)))

    def slidersChanchedS(self):
        self.inputS.setText(str(float(self.sliderS.value() / 800)))

    def slidersChanchedC(self):
        self.inputC.setText(str(float(self.sliderC.value() / 800)))

    def slidersChanchedM(self):
        self.inputM.setText(str(float(self.sliderM.value() / 800)))

    def slidersChanchedY(self):
        self.inputY.setText(str(float(self.sliderY.value() / 800)))

    def slidersChanchedK(self):
        self.inputK.setText(str(float(self.sliderK.value() / 800)))

    def addRGB(self):
        self.labelRGB = QLabel('RGB', self)
        self.labelRGB.setGeometry(100, 170, 80, 70)
        font = QFont("Arial", 24)
        self.labelRGB.setFont(font)

        self.labelR = QLabel('R:', self)
        self.labelR.setGeometry(250, 100, 60, 40)
        self.inputR = QLineEdit(self)
        self.inputR.setGeometry(280, 100, 60, 30)
        self.inputR.setText('255')

        self.labelG = QLabel('G:', self)
        self.labelG.setGeometry(250, 165, 60, 40)
        self.inputG = QLineEdit(self)
        self.inputG.setGeometry(280, 165, 60, 30)
        self.inputG.setText('255')

        self.labelB = QLabel('B:', self)
        self.labelB.setGeometry(250, 230, 60, 40)
        self.inputB = QLineEdit(self)
        self.inputB.setGeometry(280, 230, 60, 30)
        self.inputB.setText('255')

        font2 = QFont('Arial', 16)
        self.inputR.setFont(font2)
        self.inputG.setFont(font2)
        self.inputB.setFont(font2)
        self.labelR.setFont(font2)
        self.labelG.setFont(font2)
        self.labelB.setFont(font2)

        self.inputR.setMinimumSize(220, 40)
        self.inputG.setMinimumSize(220, 40)
        self.inputB.setMinimumSize(220, 40)

        self.inputR.textChanged.connect(self.updateButtonColorRGB)
        self.inputG.textChanged.connect(self.updateButtonColorRGB)
        self.inputB.textChanged.connect(self.updateButtonColorRGB)

    def updateButtonColorRGB(self):
        self.block_signal(True)

        r_text = self.inputR.text()
        g_text = self.inputG.text()
        b_text = self.inputB.text()

        if r_text == '':
            r_text = '0'
        if g_text == '':
            g_text = '0'
        if b_text == '':
            b_text = '0'

        if len(r_text) > 0 and r_text[-1].isalpha():
            r_text = r_text[:-1]
        if len(g_text) > 0 and g_text[-1].isalpha():
            g_text = g_text[:-1]
        if len(b_text) > 0 and b_text[-1].isalpha():
            b_text = b_text[:-1]
        if int(r_text) > 255:
            r_text = r_text[:-1]
        if int(g_text) > 255:
            g_text = g_text[:-1]
        if int(b_text) > 255:
            b_text = b_text[:-1]
        if len(r_text) > 1 and r_text[0] == '0':
            r_text = r_text[1:]
        if len(g_text) > 1 and g_text[0] == '0':
            g_text = g_text[1:]
        if len(b_text) > 1 and b_text[0] == '0':
            b_text = b_text[1:]

        self.inputR.setText(r_text)
        self.inputG.setText(g_text)
        self.inputB.setText(b_text)

        color = QColor(int(r_text), int(g_text), int(b_text))
        self.inputRGB = True
        self.changeColor(color)
        self.inputRGB = False
        self.block_signal(False)

    def addHLS(self):
        self.labelHLS = QLabel('HLS', self)
        self.labelHLS.setGeometry(100, 420, 170, 30)
        font = QFont("Arial", 24)
        self.labelHLS.setFont(font)

        self.labelH = QLabel('H:', self)
        self.labelH.setGeometry(250, 350, 60, 40)
        self.inputH = QLineEdit(self)
        self.inputH.setGeometry(280, 350, 60, 30)
        self.inputH.setText('-1')

        self.labelL = QLabel('L:', self)
        self.labelL.setGeometry(250, 415, 60, 40)
        self.inputL = QLineEdit(self)
        self.inputL.setGeometry(280, 415, 60, 30)
        self.inputL.setText('1')

        self.labelS = QLabel('S:', self)
        self.labelS.setGeometry(250, 480, 60, 40)
        self.inputS = QLineEdit(self)
        self.inputS.setGeometry(280, 480, 60, 30)
        self.inputS.setText('0')

        font2 = QFont('Arial', 16)
        self.inputH.setFont(font2)
        self.inputL.setFont(font2)
        self.inputS.setFont(font2)
        self.labelH.setFont(font2)
        self.labelL.setFont(font2)
        self.labelS.setFont(font2)
        self.inputH.setMinimumSize(220, 40)
        self.inputL.setMinimumSize(220, 40)
        self.inputS.setMinimumSize(220, 40)

        self.inputH.textChanged.connect(self.updateButtonColorHLS)
        self.inputS.textChanged.connect(self.updateButtonColorHLS)
        self.inputL.textChanged.connect(self.updateButtonColorHLS)

    def updateButtonColorHLS(self):
        self.block_signal(True)

        h_text = self.inputH.text()
        l_text = self.inputL.text()
        s_text = self.inputS.text()

        if h_text == '':
            h_text = '0'
        if l_text == '':
            l_text = '0'
        if s_text == '':
            s_text = '0'

        if len(h_text) > 0 and h_text[-1].isalpha():
            h_text = h_text[:-1]
        if len(l_text) > 0 and l_text[-1].isalpha():
            l_text = l_text[:-1]
        if len(s_text) > 0 and s_text[-1].isalpha():
            s_text = s_text[:-1]
        if (len(h_text) > 1 and h_text[0] == '0' and h_text[1] != '.') or (len(h_text) >= 2 and h_text[1] != '.'):
            h_text = '1'
        if (len(l_text) > 1 and l_text[0] == '0' and l_text[1] != '.') or (len(l_text) >= 2 and l_text[1] != '.'):
            l_text = '1'
        if (len(s_text) > 1 and s_text[0] == '0' and s_text[1] != '.') or (len(s_text) >= 2 and s_text[1] != '.'):
            s_text = '1'
        if len(h_text) == 2 and h_text[1] == '.':
            h_text = '0.'
        if len(l_text) == 2 and l_text[1] == '.':
            l_text = '0.'
        if len(s_text) == 2 and s_text[1] == '.':
            s_text = '0.'

        self.inputH.setText(h_text)
        self.inputL.setText(l_text)
        self.inputS.setText(s_text)
        color = QColor.fromHslF(float(h_text), float(s_text), float(l_text))

        self.inputHLS = True
        self.changeColor(color)
        self.inputHLS = False
        self.block_signal(False)

    def addCMYK(self):
        self.labelCMYK = QLabel('CMYK', self)
        self.labelCMYK.setGeometry(100, 670, 170, 30)
        font = QFont("Arial", 24)
        self.labelCMYK.setFont(font)

        self.labelC = QLabel('C:', self)
        self.labelC.setGeometry(250, 590, 60, 40)
        self.inputC = QLineEdit(self)
        self.inputC.setGeometry(280, 590, 60, 30)
        self.inputC.setText('0')

        self.labelM = QLabel('M:', self)
        self.labelM.setGeometry(250, 655, 60, 40)
        self.inputM = QLineEdit(self)
        self.inputM.setGeometry(280, 655, 60, 30)
        self.inputM.setText('0')

        self.labelY = QLabel('Y:', self)
        self.labelY.setGeometry(250, 720, 60, 40)
        self.inputY = QLineEdit(self)
        self.inputY.setGeometry(280, 720, 60, 30)
        self.inputY.setText('0')

        self.labelK = QLabel('K:', self)
        self.labelK.setGeometry(250, 785, 60, 40)
        self.inputK = QLineEdit(self)
        self.inputK.setGeometry(280, 785, 60, 30)
        self.inputK.setText('0')

        font2 = QFont('Arial', 16)
        self.inputC.setFont(font2)
        self.inputM.setFont(font2)
        self.inputY.setFont(font2)
        self.inputK.setFont(font2)
        self.labelC.setFont(font2)
        self.labelM.setFont(font2)
        self.labelY.setFont(font2)
        self.labelK.setFont(font2)
        self.inputC.setMinimumSize(220, 40)
        self.inputM.setMinimumSize(220, 40)
        self.inputY.setMinimumSize(220, 40)
        self.inputK.setMinimumSize(220, 40)

        self.inputC.textChanged.connect(self.updateButtonColorCMYK)
        self.inputM.textChanged.connect(self.updateButtonColorCMYK)
        self.inputY.textChanged.connect(self.updateButtonColorCMYK)
        self.inputK.textChanged.connect(self.updateButtonColorCMYK)

    def updateButtonColorCMYK(self):
        self.block_signal(True)

        c_text = self.inputC.text()
        m_text = self.inputM.text()
        y_text = self.inputY.text()
        k_text = self.inputK.text()

        if c_text == '':
            c_text = '0'
        if m_text == '':
            m_text = '0'
        if y_text == '':
            y_text = '0'
        if k_text == '':
            k_text = '0'

        if len(c_text) > 0 and c_text[-1].isalpha():
            c_text = c_text[:-1]
        if len(m_text) > 0 and m_text[-1].isalpha():
            m_text = m_text[:-1]
        if len(y_text) > 0 and y_text[-1].isalpha():
            y_text = y_text[:-1]
        if len(k_text) > 0 and k_text[-1].isalpha():
            k_text = k_text[:-1]
        if (len(c_text) > 1 and c_text[0] == '0' and c_text[1] != '.') or (len(c_text) >= 2 and c_text[1] != '.'):
            c_text = '1'
        if (len(m_text) > 1 and m_text[0] == '0' and m_text[1] != '.') or (len(m_text) >= 2 and m_text[1] != '.'):
            m_text = '1'
        if (len(y_text) > 1 and y_text[0] == '0' and y_text[1] != '.') or (len(y_text) >= 2 and y_text[1] != '.'):
            y_text = '1'
        if (len(k_text) > 1 and k_text[0] == '0' and k_text[1] != '.') or (len(k_text) >= 2 and k_text[1] != '.'):
            k_text = '1'
        if len(c_text) == 2 and c_text[1] == '.':
            c_text = '0.'
        if len(m_text) == 2 and m_text[1] == '.':
            m_text = '0.'
        if len(y_text) == 2 and y_text[1] == '.':
            y_text = '0.'
        if len(k_text) == 2 and k_text[1] == '.':
            k_text = '0.'
        self.inputC.setText(c_text)
        self.inputM.setText(m_text)
        self.inputY.setText(y_text)
        self.inputK.setText(k_text)
        color = QColor.fromCmykF(float(c_text), float(m_text), float(y_text), float(k_text))

        self.inputCMYK = True
        self.changeColor(color)
        self.inputCMYK = False
        self.block_signal(False)

    def openColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.changeColor(color)

    def changeColor(self, color):
        if not self.inputRGB:
            r, g, b, _ = color.getRgb()
            self.inputR.setText(str(r))
            self.inputG.setText(str(g))
            self.inputB.setText(str(b))

        if not self.inputHLS:
            h, s, l, _ = color.getHslF()
            if h == 0.0:
                self.inputH.setText('0.')
            else:
                self.inputH.setText(str(h))

            if l == 0.0:
                self.inputL.setText('0.')
            else:
                self.inputL.setText(str(l))

            if s == 0.0:
                self.inputS.setText('0.')
            else:
                self.inputS.setText(str(s))

        if not self.inputCMYK:
            c, m, y, k, _ = color.getCmykF()

            self.inputC.setText(str(c))
            self.inputM.setText(str(m))
            self.inputY.setText(str(y))
            self.inputK.setText(str(k))

        self.sliderR.setValue(int(int(self.inputR.text()) * 800 / 255))
        self.sliderG.setValue(int(int(self.inputG.text()) * 800 / 255))
        self.sliderB.setValue(int(int(self.inputB.text()) * 800 / 255))
        self.sliderH.setValue(int(float(self.inputH.text()) * 800))
        self.sliderL.setValue(int(float(self.inputL.text()) * 800))
        self.sliderS.setValue(int(float(self.inputS.text()) * 800))
        self.sliderC.setValue(int(float(self.inputC.text()) * 800))
        self.sliderM.setValue(int(float(self.inputM.text()) * 800))
        self.sliderY.setValue(int(float(self.inputY.text()) * 800))
        self.sliderK.setValue(int(float(self.inputK.text()) * 800))
        button_color = f'{color.name()}'
        self.btnColor.setStyleSheet(f"background-color: {button_color}; border: 1px solid black;")

    def block_signal(self, block):
        self.inputR.blockSignals(block)
        self.inputG.blockSignals(block)
        self.inputB.blockSignals(block)
        self.inputH.blockSignals(block)
        self.inputL.blockSignals(block)
        self.inputS.blockSignals(block)
        self.inputC.blockSignals(block)
        self.inputM.blockSignals(block)
        self.inputY.blockSignals(block)
        self.inputK.blockSignals(block)
        self.sliderR.blockSignals(block)
        self.sliderG.blockSignals(block)
        self.sliderB.blockSignals(block)
        self.sliderH.blockSignals(block)
        self.sliderL.blockSignals(block)
        self.sliderS.blockSignals(block)
        self.sliderC.blockSignals(block)
        self.sliderM.blockSignals(block)
        self.sliderY.blockSignals(block)
        self.sliderK.blockSignals(block)


app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
