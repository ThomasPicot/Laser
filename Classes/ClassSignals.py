from Classes.ClassRedPitaya import MyRedpitaya
from PyQt5 import QtCore, QtWidgets, QtGui


class PulseSignals:

    def __init__(self, addr=None, output=None):
        self.addr = addr
        self.output = output
        self.red = MyRedpitaya()
        self.MainWindow = QtWidgets.QMainWindow()
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.lineEdit_offset = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_frequency = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_amplitude = QtWidgets.QLineEdit(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.lineEdit_amplitude.setText('10')
        self.lineEdit_frequency.setText('1')
        self.lineEdit_offset.setText('0')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "    background-color : #303030;\n"
                                 "     color : #FDFAEB;\n"
                                 "}")
        self.centralwidget.setStyleSheet("QWidget {\n"
                                         "    background-color : #303030;\n"
                                         "     color : #FDFAEB;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.setObjectName("gridLayout")
        self.label_3.setStyleSheet("QLabel {\n"
                                   "    background-color : #303030;\n"
                                   "     color : #FDFAEB;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
                                 "    background-color : #303030;\n"
                                 "     color : #FDFAEB;\n"
                                 "}")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4.setStyleSheet("QLabel {\n"
                                   "    background-color : #303030;\n"
                                   "     color : #FDFAEB;\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        sizePolicy.setHeightForWidth(self.lineEdit_offset.sizePolicy().hasHeightForWidth())
        self.lineEdit_offset.setSizePolicy(sizePolicy)
        self.lineEdit_offset.setStyleSheet("QLineEdit{\n"
                                           "    background-color:#f6f6f6;\n"
                                           "    border: 2px solid gray;\n"
                                           "    border-radius: 5px;\n"
                                           "    padding: 0 8px;\n"
                                           "    selection-background-color: darkgray;\n"
                                           "    font-size: 16px;\n"
                                           "    color: #303030;"
                                           "}\n"
                                           "\n"
                                           " QLineEdit:focus { \n"
                                           "    background-color#f6f6f6;\n"
                                           "}\n"
                                           "")
        self.lineEdit_offset.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_offset, 3, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_frequency.sizePolicy().hasHeightForWidth())
        self.lineEdit_frequency.setSizePolicy(sizePolicy)
        self.lineEdit_frequency.setStyleSheet("QLineEdit{\n"
                                              "    background-color:#f6f6f6;\n"
                                              "    border: 2px solid gray;\n"
                                              "    border-radius: 5px;\n"
                                              "    padding: 0 8px;\n"
                                              "    selection-background-color: darkgray;\n"
                                              "    font-size: 16px;\n"
                                              "    color: #303030;"
                                              "}\n"
                                              "\n"
                                              " QLineEdit:focus { \n"
                                              "    background-color#f6f6f6;\n"
                                              "}\n"
                                              "")
        self.lineEdit_frequency.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_frequency, 2, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_amplitude.sizePolicy().hasHeightForWidth())
        self.lineEdit_amplitude.setSizePolicy(sizePolicy)
        self.lineEdit_amplitude.setStyleSheet("QLineEdit{\n"
                                              "    background-color:#f6f6f6;\n"
                                              "    border: 2px solid gray;\n"
                                              "    border-radius: 5px;\n"
                                              "    padding: 0 8px;\n"
                                              "    selection-background-color: darkgray;\n"
                                              "    font-size: 16px;\n"
                                              "    color: #303030;"
                                              "}\n"
                                              "\n"
                                              " QLineEdit:focus { \n"
                                              "    background-color#f6f6f6;\n"
                                              "}\n"
                                              "")
        self.lineEdit_amplitude.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_amplitude, 1, 0, 1, 1)
        self.label_2.setStyleSheet("QLabel {\n"
                                   "    background-color : #303030;\n"
                                   "     color : #FDFAEB;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    background-color:#FFF9D4;\n"
                                      "    color:#303030;\n"
                                      "    border-radius: 8px;\n"
                                      "    transition-duration: 0.4s;\n"
                                      "    height:40px;\n"
                                      "    width:115px;\n"
                                      "    color: #303030;"
                                      "}\n"
                                      "                      \n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #D4DAFF; \n"
                                      "    color:#FDFAEB;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.setSignal)
        self.pushButton.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setSignal(self):
        amplitude = float(self.lineEdit_amplitude.text())
        frequency = float(self.lineEdit_frequency.text())
        offset = float(self.lineEdit_offset.text())
        self.red.set_pulse(output=self.output, frequency=frequency, amplitude=amplitude, offset=offset)

    def retranslateUi(self, MainWindow):
        """
        write txt on UI
        :param MainWindow: yes
        :return: void
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Frequency [Hz]"))
        self.label.setText(_translate("MainWindow", "Pulse"))
        self.label_4.setText(_translate("MainWindow", "Offset [V]"))
        self.label_2.setText(_translate("MainWindow", "Amplitude [V]"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))


class RampSignals:
    def __init__(self, addr=None, output=None):
        print('init')
        self.addr = addr
        self.output = output
        self.red = MyRedpitaya()
        self.RampWindow = QtWidgets.QMainWindow()
        self.centralwidget = QtWidgets.QWidget(self.RampWindow)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.lineEdit_offset = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_frequency = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_amplitude = QtWidgets.QLineEdit(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.lineEdit_amplitude.setText('10')
        self.lineEdit_frequency.setText('1')
        self.lineEdit_offset.setText('0')
        print('init finished')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "    background-color : #303030;\n"
                                 "     color : #FDFAEB;\n"
                                 "}")
        self.centralwidget.setStyleSheet("QWidget {\n"
                                         "    background-color : #303030;\n"
                                         "     color : #FDFAEB;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.setObjectName("gridLayout")
        self.label_3.setStyleSheet("QLabel {\n"
                                   "    background-color : #303030;\n"
                                   "     color : #FDFAEB;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
                                 "    background-color : #303030;\n"
                                 "     color : #FDFAEB;\n"
                                 "}")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4.setStyleSheet("QLabel {\n"
                                   "    background-color : #303030;\n"
                                   "     color : #FDFAEB;\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_offset.sizePolicy().hasHeightForWidth())
        self.lineEdit_offset.setSizePolicy(sizePolicy)
        self.lineEdit_offset.setStyleSheet("QLineEdit{\n"
                                           "    background-color:#f6f6f6;\n"
                                           "    border: 2px solid gray;\n"
                                           "    border-radius: 5px;\n"
                                           "    padding: 0 8px;\n"
                                           "    selection-background-color: darkgray;\n"
                                           "    font-size: 16px;\n"
                                           "    color: #303030;"
                                           "}\n"
                                           "\n"
                                           " QLineEdit:focus { \n"
                                           "    background-color#f6f6f6;\n"
                                           "}\n"
                                           "")
        self.lineEdit_offset.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_offset, 3, 0, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_frequency.sizePolicy().hasHeightForWidth())
        self.lineEdit_frequency.setSizePolicy(sizePolicy)
        self.lineEdit_frequency.setStyleSheet("QLineEdit{\n"
                                              "    background-color:#f6f6f6;\n"
                                              "    border: 2px solid gray;\n"
                                              "    border-radius: 5px;\n"
                                              "    padding: 0 8px;\n"
                                              "    selection-background-color: darkgray;\n"
                                              "    font-size: 16px;\n"
                                              "    color: #303030;"
                                              "}\n"
                                              "\n"
                                              " QLineEdit:focus { \n"
                                              "    background-color#f6f6f6;\n"
                                              "}\n"
                                              "")
        self.lineEdit_frequency.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_frequency, 2, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_amplitude.sizePolicy().hasHeightForWidth())
        self.lineEdit_amplitude.setSizePolicy(sizePolicy)
        self.lineEdit_amplitude.setStyleSheet("QLineEdit{\n"
                                              "    background-color:#f6f6f6;\n"
                                              "    border: 2px solid gray;\n"
                                              "    border-radius: 5px;\n"
                                              "    padding: 0 8px;\n"
                                              "    selection-background-color: darkgray;\n"
                                              "    font-size: 16px;\n"
                                              "    color: #303030;"
                                              "}\n"
                                              "\n"
                                              " QLineEdit:focus { \n"
                                              "    background-color#f6f6f6;\n"
                                              "}\n"
                                              "")
        self.lineEdit_amplitude.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_amplitude, 1, 0, 1, 1)
        self.label_2.setStyleSheet("QLabel {\n"
                                   "    background-color : #303030;\n"
                                   "     color : #FDFAEB;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    background-color:#FFF9D4;\n"
                                      "    color:#303030;\n"
                                      "    border-radius: 8px;\n"
                                      "    transition-duration: 0.4s;\n"
                                      "    height:40px;\n"
                                      "    width:115px;\n"
                                      "    color: #303030;"
                                      "}\n"
                                      "                      \n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #D4DAFF; \n"
                                      "    color:#FDFAEB;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.setSignal)
        self.pushButton.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setSignal(self):
        amplitude = float(self.lineEdit_amplitude.text())
        frequency = float(self.lineEdit_frequency.text())
        offset = float(self.lineEdit_offset.text())
        self.red.set_ramp(output=self.output, frequency=frequency, amplitude=amplitude, offset=offset)

    def retranslateUi(self, MainWindow):
        """
        write txt on UI
        :param MainWindow: yes
        :return: void
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Frequency [Hz]"))
        self.label.setText(_translate("MainWindow", "Ramp"))
        self.label_4.setText(_translate("MainWindow", "Offset [V]"))
        self.label_2.setText(_translate("MainWindow", "Amplitude [V]"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))


class SineSignals:
    def __init__(self, addr=None, output=None):
        self.addr = addr
        self.output = output
        self.red = MyRedpitaya()
        self.MainWindow = QtWidgets.QMainWindow()
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.lineEdit_frequency = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_amplitude = QtWidgets.QLineEdit(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.lineEdit_amplitude.setText('10')
        self.lineEdit_frequency.setText('1')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "    background-color : #303030;\n"
                                 "     color : #FDFAEB;\n"
                                 "}")
        self.centralwidget.setStyleSheet("QWidget {\n"
                                         "    background-color : #303030;\n"
                                         "     color : #FDFAEB;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.setObjectName("gridLayout")
        self.label_3.setStyleSheet("QLabel {\n"
                                   "    background-color : #303030;\n"
                                   "     color : #FDFAEB;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
                                 "    background-color : #303030;\n"
                                 "     color : #FDFAEB;\n"
                                 "}")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_frequency.sizePolicy().hasHeightForWidth())
        self.lineEdit_frequency.setSizePolicy(sizePolicy)
        self.lineEdit_frequency.setStyleSheet("QLineEdit{\n"
                                              "    background-color:#f6f6f6;\n"
                                              "    border: 2px solid gray;\n"
                                              "    border-radius: 5px;\n"
                                              "    padding: 0 8px;\n"
                                              "    selection-background-color: darkgray;\n"
                                              "    font-size: 16px;\n"
                                              "    color: #303030;"
                                              "}\n"
                                              "\n"
                                              " QLineEdit:focus { \n"
                                              "    background-color#f6f6f6;\n"
                                              "}\n"
                                              "")
        self.lineEdit_frequency.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_frequency, 2, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_amplitude.sizePolicy().hasHeightForWidth())
        self.lineEdit_amplitude.setSizePolicy(sizePolicy)
        self.lineEdit_amplitude.setStyleSheet("QLineEdit{\n"
                                              "    background-color:#f6f6f6;\n"
                                              "    border: 2px solid gray;\n"
                                              "    border-radius: 5px;\n"
                                              "    padding: 0 8px;\n"
                                              "    selection-background-color: darkgray;\n"
                                              "    font-size: 16px;\n"
                                              "    color: #303030;"
                                              "}\n"
                                              "\n"
                                              " QLineEdit:focus { \n"
                                              "    background-color#f6f6f6;\n"
                                              "}\n"
                                              "")
        self.lineEdit_amplitude.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_amplitude, 1, 0, 1, 1)
        self.label_2.setStyleSheet("QLabel {\n"
                                   "    background-color : #303030;\n"
                                   "     color : #FDFAEB;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    background-color:#FFF9D4;\n"
                                      "    color:#303030;\n"
                                      "    border-radius: 8px;\n"
                                      "    transition-duration: 0.4s;\n"
                                      "    height:40px;\n"
                                      "    width:115px;\n"
                                      "    color: #303030;"
                                      "}\n"
                                      "                      \n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #D4DAFF; \n"
                                      "    color:#FDFAEB;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.setSignal)
        self.pushButton.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setSignal(self):
        amplitude = float(self.lineEdit_amplitude.text())
        frequency = float(self.lineEdit_frequency.text())
        self.red.set_sine(output=self.output, frequency=frequency, amplitude=amplitude)

    def retranslateUi(self, MainWindow):
        """
        write txt on UI
        :param MainWindow: yes
        :return: void
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Frequency [Hz]"))
        self.label.setText(_translate("MainWindow", "Sine"))
        self.label_2.setText(_translate("MainWindow", "Amplitude [V]"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))


class SquareSignals:
    def __init__(self, addr=None, output=None):
        self.addr = addr
        self.output = output
        self.red = MyRedpitaya()
        self.MainWindow = QtWidgets.QMainWindow()
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.lineEdit_offset = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_frequency = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_amplitude = QtWidgets.QLineEdit(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.lineEdit_amplitude.setText('10')
        self.lineEdit_frequency.setText('1')
        self.lineEdit_offset.setText('0')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "    background-color : #303030;\n"
                                 "     color : #FDFAEB;\n"
                                 "}")
        self.centralwidget.setStyleSheet("QWidget {\n"
                                         "    background-color : #303030;\n"
                                         "     color : #FDFAEB;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.setObjectName("gridLayout")
        self.label_3.setStyleSheet("QLabel {\n"
                                   "    background-color : #303030;\n"
                                   "     color : #FDFAEB;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
                                 "    background-color : #303030;\n"
                                 "     color : #FDFAEB;\n"
                                 "}")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4.setStyleSheet("QLabel {\n"
                                   "    background-color : #303030;\n"
                                   "     color : #FDFAEB;\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_offset.sizePolicy().hasHeightForWidth())
        self.lineEdit_offset.setSizePolicy(sizePolicy)
        self.lineEdit_offset.setStyleSheet("QLineEdit{\n"
                                           "    background-color:#f6f6f6;\n"
                                           "    border: 2px solid gray;\n"
                                           "    border-radius: 5px;\n"
                                           "    padding: 0 8px;\n"
                                           "    selection-background-color: darkgray;\n"
                                           "    font-size: 16px;\n"
                                           "    color: #303030;"
                                           "}\n"
                                           "\n"
                                           " QLineEdit:focus { \n"
                                           "    background-color#f6f6f6;\n"
                                           "}\n"
                                           "")
        self.lineEdit_offset.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_offset, 3, 0, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_frequency.sizePolicy().hasHeightForWidth())
        self.lineEdit_frequency.setSizePolicy(sizePolicy)
        self.lineEdit_frequency.setStyleSheet("QLineEdit{\n"
                                              "    background-color:#f6f6f6;\n"
                                              "    border: 2px solid gray;\n"
                                              "    border-radius: 5px;\n"
                                              "    padding: 0 8px;\n"
                                              "    selection-background-color: darkgray;\n"
                                              "    font-size: 16px;\n"
                                              "    color: #303030;"
                                              "}\n"
                                              "\n"
                                              " QLineEdit:focus { \n"
                                              "    background-color#f6f6f6;\n"
                                              "}\n"
                                              "")
        self.lineEdit_frequency.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_frequency, 2, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_amplitude.sizePolicy().hasHeightForWidth())
        self.lineEdit_amplitude.setSizePolicy(sizePolicy)
        self.lineEdit_amplitude.setStyleSheet("QLineEdit{\n"
                                              "    background-color:#f6f6f6;\n"
                                              "    border: 2px solid gray;\n"
                                              "    border-radius: 5px;\n"
                                              "    padding: 0 8px;\n"
                                              "    selection-background-color: darkgray;\n"
                                              "    font-size: 16px;\n"
                                              "    color: #303030;"
                                              "}\n"
                                              "\n"
                                              " QLineEdit:focus { \n"
                                              "    background-color#f6f6f6;\n"
                                              "}\n"
                                              "")
        self.lineEdit_amplitude.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_amplitude, 1, 0, 1, 1)
        self.label_2.setStyleSheet("QLabel {\n"
                                   "    background-color : #303030;\n"
                                   "     color : #FDFAEB;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    background-color:#FFF9D4;\n"
                                      "    color:#303030;\n"
                                      "    border-radius: 8px;\n"
                                      "    transition-duration: 0.4s;\n"
                                      "    height:40px;\n"
                                      "    width:115px;\n"
                                      "    color: #303030;"
                                      "}\n"
                                      "                      \n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #D4DAFF; \n"
                                      "    color:#FDFAEB;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.setSignal)
        self.pushButton.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setSignal(self):
        amplitude = float(self.lineEdit_amplitude.text())
        frequency = float(self.lineEdit_frequency.text())
        offset = float(self.lineEdit_offset.text())
        self.red.set_square(output=self.output, frequency=frequency, amplitude=amplitude, offset=offset)

    def retranslateUi(self, MainWindow):
        """
        write txt on UI
        :param MainWindow: yes
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Frequency [Hz]"))
        self.label.setText(_translate("MainWindow", "Square"))
        self.label_4.setText(_translate("MainWindow", "Offset [V]"))
        self.label_2.setText(_translate("MainWindow", "Amplitude [V]"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))

