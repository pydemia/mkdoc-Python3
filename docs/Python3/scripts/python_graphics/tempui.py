# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataQueryTool_UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#


import datetime as dt
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_CONFIRM = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CONFIRM.setGeometry(QtCore.QRect(490, 270, 99, 27))
        self.pushButton_CONFIRM.setObjectName("pushButton_CONFIRM")
        self.pushButton_CANCEL = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CANCEL.setGeometry(QtCore.QRect(600, 270, 99, 27))
        self.pushButton_CANCEL.setObjectName("pushButton_CANCEL")
        self.FAC_ID_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.FAC_ID_inputText.setGeometry(QtCore.QRect(140, 56, 211, 27))
        self.FAC_ID_inputText.setObjectName("FAC_ID_inputText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(22, 60, 101, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(22, 90, 101, 17))
        self.label_2.setObjectName("label_2")
        self.AREA_CD_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.AREA_CD_inputText.setGeometry(QtCore.QRect(140, 86, 211, 27))
        self.AREA_CD_inputText.setObjectName("AREA_CD_inputText")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(22, 120, 101, 17))
        self.label_3.setObjectName("label_3")
        self.EQP_MODEL_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.EQP_MODEL_inputText.setGeometry(QtCore.QRect(140, 116, 211, 27))
        self.EQP_MODEL_inputText.setObjectName("EQP_MODEL_inputText")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(22, 150, 101, 17))
        self.label_4.setObjectName("label_4")
        self.EQP_ID_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.EQP_ID_inputText.setGeometry(QtCore.QRect(140, 146, 211, 27))
        self.EQP_ID_inputText.setObjectName("EQP_ID_inputText")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(22, 180, 101, 17))
        self.label_5.setObjectName("label_5")
        self.RECIPE_ID_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.RECIPE_ID_inputText.setGeometry(QtCore.QRect(140, 176, 211, 27))
        self.RECIPE_ID_inputText.setObjectName("RECIPE_ID_inputText")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(22, 210, 101, 17))
        self.label_6.setObjectName("label_6")
        self.END_DT_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.END_DT_inputText.setGeometry(QtCore.QRect(140, 206, 121, 27))
        self.END_DT_inputText.setObjectName("END_DT_inputText")
        self.START_DT = QtWidgets.QLineEdit(self.centralwidget)
        self.START_DT.setGeometry(QtCore.QRect(140, 266, 121, 27))
        self.START_DT.setText("")
        self.START_DT.setReadOnly(True)
        self.START_DT.setObjectName("START_DT")
        self.TM_WINDOW_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.TM_WINDOW_inputText.setGeometry(QtCore.QRect(140, 236, 51, 27))
        self.TM_WINDOW_inputText.setObjectName("TM_WINDOW_inputText")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 90, 101, 17))
        self.label_7.setObjectName("label_7")
        self.YTYPE_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.YTYPE_inputText.setGeometry(QtCore.QRect(490, 86, 211, 27))
        self.YTYPE_inputText.setObjectName("YTYPE_inputText")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(390, 60, 101, 17))
        self.label_8.setObjectName("label_8")
        self.YPRMT_NM_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.YPRMT_NM_inputText.setGeometry(QtCore.QRect(490, 116, 211, 27))
        self.YPRMT_NM_inputText.setObjectName("YPRMT_NM_inputText")
        self.YOPER_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.YOPER_inputText.setGeometry(QtCore.QRect(490, 56, 211, 27))
        self.YOPER_inputText.setObjectName("YOPER_inputText")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(390, 120, 101, 17))
        self.label_10.setObjectName("label_10")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(360, 26, 20, 271))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 16, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(490, 16, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(22, 239, 101, 17))
        self.label_9.setObjectName("label_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 270, 101, 17))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(390, 190, 101, 17))
        self.label_14.setObjectName("label_14")
        self.FILENAME_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.FILENAME_inputText.setGeometry(QtCore.QRect(490, 185, 211, 27))
        self.FILENAME_inputText.setReadOnly(True)
        self.FILENAME_inputText.setObjectName("FILENAME_inputText")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(370, 160, 351, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.DIRECTORY_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.DIRECTORY_inputText.setGeometry(QtCore.QRect(490, 216, 211, 27))
        self.DIRECTORY_inputText.setReadOnly(True)
        self.DIRECTORY_inputText.setObjectName("DIRECTORY_inputText")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(390, 221, 101, 17))
        self.label_15.setObjectName("label_15")
        self.END_TM_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.END_TM_Text.setGeometry(QtCore.QRect(270, 206, 81, 27))
        self.END_TM_Text.setReadOnly(True)
        self.END_TM_Text.setObjectName("END_TM_Text")
        self.START_TM_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.START_TM_Text.setGeometry(QtCore.QRect(270, 266, 81, 27))
        self.START_TM_Text.setReadOnly(True)
        self.START_TM_Text.setObjectName("START_TM_Text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 25))
        self.menubar.setObjectName("menubar")
        self.menuPopup = QtWidgets.QMenu(self.menubar)
        self.menuPopup.setObjectName("menuPopup")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMenu1 = QtWidgets.QAction(MainWindow)
        self.actionMenu1.setObjectName("actionMenu1")
        self.actionSetting1 = QtWidgets.QAction(MainWindow)
        self.actionSetting1.setObjectName("actionSetting1")
        self.menuPopup.addAction(self.actionMenu1)
        self.menuSetting.addAction(self.actionSetting1)
        self.menubar.addAction(self.menuPopup.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_CONFIRM.clicked.connect(self.createDict)
        self.pushButton_CANCEL.clicked.connect(MainWindow.close)
        self.END_DT_inputText.editingFinished.connect(self.start_tm_calculate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_CONFIRM.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_CANCEL.setText(_translate("MainWindow", "Cancel"))
        self.FAC_ID_inputText.setText(_translate("MainWindow", "M14"))
        self.label.setText(_translate("MainWindow", "FAC_ID"))
        self.label_2.setText(_translate("MainWindow", "AREA_CD"))
        self.AREA_CD_inputText.setText(_translate("MainWindow", "T/F"))
        self.label_3.setText(_translate("MainWindow", "EQP_MODEL"))
        self.EQP_MODEL_inputText.setText(_translate("MainWindow", "CHALLENGER_HT"))
        self.label_4.setText(_translate("MainWindow", "EQP_ID"))
        self.EQP_ID_inputText.setText(_translate("MainWindow", "4TPE1601"))
        self.label_5.setText(_translate("MainWindow", "RECIPE_ID"))
        self.RECIPE_ID_inputText.setText(_translate("MainWindow", "DE_ARC_450_ABC"))
        self.label_6.setText(_translate("MainWindow", "END_DT_TM"))
        self.END_DT_inputText.setText(_translate("MainWindow", "20170303"))
        self.TM_WINDOW_inputText.setText(_translate("MainWindow", "2"))
        self.label_7.setText(_translate("MainWindow", "TYPE"))
        self.YTYPE_inputText.setText(_translate("MainWindow", "PT1H"))
        self.label_8.setText(_translate("MainWindow", "OPER"))
        self.YPRMT_NM_inputText.setText(_translate("MainWindow", "PT1H"))
        self.YOPER_inputText.setText(_translate("MainWindow", "Z1020000A"))
        self.label_10.setText(_translate("MainWindow", "PRMT_NM"))
        self.label_11.setText(_translate("MainWindow", "X value"))
        self.label_12.setText(_translate("MainWindow", "Y value"))
        self.label_9.setText(_translate("MainWindow", "TM_WINDOW"))
        self.label_13.setText(_translate("MainWindow", "START_DT_TM"))
        self.label_14.setText(_translate("MainWindow", "FILENAME"))
        self.FILENAME_inputText.setText(_translate("MainWindow", "(Optional)"))
        self.DIRECTORY_inputText.setText(_translate("MainWindow", "D:/workspaces/SKHy_MCC/300. Python/mcc_pjt"))
        self.label_15.setText(_translate("MainWindow", "DIRECTORY"))
        self.END_TM_Text.setText(_translate("MainWindow", "065959"))
        self.START_TM_Text.setText(_translate("MainWindow", "070000"))
        self.menuPopup.setTitle(_translate("MainWindow", "File"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionMenu1.setText(_translate("MainWindow", "menu1"))
        self.actionSetting1.setText(_translate("MainWindow", "setting1"))


    def start_tm_calculate(self):
        #_translate = QtCore.QCoreApplication.translate
        end_dt = dt.datetime.strptime(self.END_DT_inputText.text(), '%Y%m%d')
        window = dt.timedelta(days=int(self.TM_WINDOW_inputText.text()))
        self.START_DT.setText((end_dt - window).strftime('%Y%m%d'))


    def createDict(self):
        resDict = {'FAC_ID': self.FAC_ID_inputText.text(),
                   'AREA_CD': self.AREA_CD_inputText.text(),
                   'EQP_MODEL': self.EQP_MODEL_inputText.text(),
                   'EQP_ID': self.EQP_ID_inputText.text(),
                   'RECIPE_ID': self.RECIPE_ID_inputText.text(),
                   'END_DT_TM': self.END_DT_inputText.text(),
                   'TM_WINDOW': self.TM_WINDOW_inputText.text(),
                   'STT_DT_TM': '1',
                   'YOPER': self.YOPER_inputText.text(),
                   'YTYPE': self.YTYPE_inputText.text(),
                   'YPRMT_NM': self.YPRMT_NM_inputText.text()
                   #'SAVEDIR': self.SAVEDIR_inputText.text()
                   }
        print(resDict)
        MainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

