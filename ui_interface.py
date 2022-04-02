from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

from PyQt5 import QtCore
from PyQt5 import QtGui

import os
import webbrowser
import PySide2
import resources_rc
import geopandas as gpd



font = QFont()
font.setPointSize(12)
font.setBold(True)
font.setWeight(75)

font1 = QFont()
font1.setPointSize(11)
font1.setBold(True)
font1.setItalic(True)
font1.setWeight(75)

font2 = QFont()
font2.setFamily(u"URW Gothic")
font2.setPointSize(20)
font2.setBold(True)
font2.setWeight(75)


def getid(item):

    try:
        df = gpd.read_file("zones.json")
        df.head(2)

        nme = item.text()
        nme = nme.split(" - ")
        nme = nme[0]

        for i in range(len(df)):
            if (df["name"][i] == nme):
                return df["id"][i]

        return "notfound"

    except:
        try:
            print("Trying old json file")
            df = gpd.read_file("zones.json.old")
            df.head(2)

            nme = item.text()
            nme = nme.split(" - ")
            nme = nme[0]

            for i in range(len(df)):
                if (df["name"][i] == nme):
                    return df["id"][i]

            rfile = open("zones.json.old", "r")
            file = open("zones.json", "w")
            file.write(rfile.read())

            return "notfound"

        except:
            print("Error loading json file.")



class donatebtn(QPushButton):
    def donate(self):
        webbrowser.open("https://www.paypal.com/paypalme/AReppelin")

class returnBtn(QPushButton):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"returnButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/skip-back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon1)
        self.setIconSize(QSize(24, 24))
        self.setFont(font1)


    def returnB(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "output.html"))
        local_url = QUrl.fromLocalFile(file_path)
        self.window().ui.webEngineView.load(QUrl(local_url))

    def returnA(self):
        self.window().ui.render.hide()
        self.window().ui.rtbtn.hide()

class CustList(QListWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName(u"navlist")
        self.setFont(font2)

        try:
            df = gpd.read_file("zones.json")
            df.head(2)

            for i in range(len(df)):
                item = df["name"][i] + " - " + df["infos"][i]
                self.addItem(item)

        except:
            try:
                print("Trying old json file")
                df = gpd.read_file("zones.json.old")
                df.head(2)

                for i in range(len(df)):
                    item = df["name"][i] + " - " + df["infos"][i]
                    self.addItem(item)

                rfile = open("zones.json.old", "r")
                file = open("zones.json", "w")
                file.write(rfile.read())

            except:
                print("Error loading json file.")

        self.itemClicked.connect(self.Clicked)


    def Clicked(self, item):
        self.window().ui.verticalLayout_9.removeWidget(self.window().ui.navlist)
        self.window().ui.render = self.window().uirender = QWebEngineView()
        self.window().ui.render.setObjectName(u"render")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.window().ui.render.sizePolicy().hasHeightForWidth())
        self.window().ui.render.setSizePolicy(sizePolicy2)
        self.window().ui.render.setMinimumSize(QSize(0, 0))
        id = getid(item)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "{}.html".format(id)))
        url = QUrl.fromLocalFile(file_path)
        self.window().ui.render.setUrl(QUrl(url))
        self.window().ui.render.load(QUrl(url))
        self.window().ui.verticalLayout_9.addWidget(self.window().ui.render)

        self.window().ui.rtbtn = returnBtn()
        self.window().ui.rtbtn.setText("Retour à la liste")
        self.window().ui.rtbtn.clicked.connect(self.window().ui.rtbtn.returnA)
        self.window().ui.verticalLayout_9.addWidget(self.window().ui.rtbtn)
        self.window().ui.page_2.setLayout(self.window().ui.verticalLayout_9)




class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(801, 432)
        MainWindow.setStyleSheet(u"*{\n"
"background-color: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"border: none;\n"
"color: #fff;\n"
"}\n"
"#centralwidget{\n"
"background-color: rgb(39, 43, 54);\n"
"}\n"
"#toggle_button_cont{\n"
"background-color: rgb(28, 37, 49);\n"
"}\n"
"#left_menu_main_container > QWidget{\n"
"border-bottom: 2px solid rgb(28, 37, 49);\n"
"}\n"
"#left_menu_main_container QPushButton{\n"
"padding: 10px 5px;\n"
"text-align: left;\n"
"}\n"
"QStackedWidget > QWidget{\n"
"background-color: rgb(20, 28, 39);\n"
"}\n"
"")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")


        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toggle_button_cont = QWidget(self.header)
        self.toggle_button_cont.setObjectName(u"toggle_button_cont")
        self.horizontalLayout_2 = QHBoxLayout(self.toggle_button_cont)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggle_button = QPushButton(self.toggle_button_cont)
        self.toggle_button.setObjectName(u"toggle_button")
        self.toggle_button.setMinimumSize(QSize(200, 0))

        self.toggle_button.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toggle_button.setIcon(icon)
        self.toggle_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.toggle_button, 1, Qt.AlignLeft)


        self.horizontalLayout_3.addWidget(self.toggle_button_cont, 1, Qt.AlignLeft)

        self.widget_6 = QWidget(self.header)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame = QFrame(self.widget_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.pushButton_8)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_7.addWidget(self.lineEdit)


        self.horizontalLayout_6.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.widget_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.minimizeWindow = QPushButton(self.frame_3)
        self.minimizeWindow.setObjectName(u"minimizeWindow")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/minus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeWindow.setIcon(icon4)
        self.minimizeWindow.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.minimizeWindow)

        self.restoreWindow = QPushButton(self.frame_3)
        self.restoreWindow.setObjectName(u"restoreWindow")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreWindow.setIcon(icon3)
        self.restoreWindow.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.restoreWindow)

        self.closeWindow = QPushButton(self.frame_3)
        self.closeWindow.setObjectName(u"closeWindow")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeWindow.setIcon(icon5)
        self.closeWindow.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.closeWindow)


        self.horizontalLayout_6.addWidget(self.frame_3, 0, Qt.AlignRight)


        self.horizontalLayout_3.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.header)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_main_container = QCustomSlideMenu(self.widget_2)
        self.left_menu_main_container.setObjectName(u"left_menu_main_container")
        self.left_menu_main_container.setMinimumSize(QSize(200, 350))
        self.verticalLayout_2 = QVBoxLayout(self.left_menu_main_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_menu_container = QWidget(self.left_menu_main_container)
        self.top_menu_container.setObjectName(u"top_menu_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.top_menu_container.sizePolicy().hasHeightForWidth())
        self.top_menu_container.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.top_menu_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.top_menu_container)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.dashboard_btn = QPushButton(self.widget_3)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        self.dashboard_btn.setStyleSheet(u"background-color: rgb(20, 28, 39);\n"
"border-left: 3px solid rgb(7 ,98 ,160);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/globe.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon6)
        self.dashboard_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.dashboard_btn)

        self.projects_btn = QPushButton(self.widget_3)
        self.projects_btn.setObjectName(u"projects_btn")
        self.projects_btn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/align-center.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.projects_btn.setIcon(icon7)
        self.projects_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.projects_btn)

        self.reports_btn = QPushButton(self.widget_3)
        self.reports_btn.setObjectName(u"reports_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reports_btn.setIcon(icon8)
        self.reports_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.reports_btn)


        self.verticalLayout_3.addWidget(self.widget_3, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.top_menu_container)

        self.bottom_menu_container = QWidget(self.left_menu_main_container)
        self.bottom_menu_container.setObjectName(u"bottom_menu_container")
        self.verticalLayout_5 = QVBoxLayout(self.bottom_menu_container)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.bottom_menu_container)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")

        self.label.setFont(font1)

        self.verticalLayout_6.addWidget(self.label)

        self.settings_btns = QPushButton(self.widget_5)
        self.settings_btns.setObjectName(u"settings_btns")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btns.setIcon(icon11)
        self.settings_btns.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.settings_btns)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.label_3.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_3)

        self.donatebtn = donatebtn()
        self.donatebtn.setObjectName(u"donatebtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/coffee.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.donatebtn.setIcon(icon11)
        self.donatebtn.setIconSize(QSize(24, 24))
        self.donatebtn.clicked.connect(self.donatebtn.donate)

        self.verticalLayout_6.addWidget(self.donatebtn)

        self.verticalLayout_5.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.bottom_menu_container)


        self.horizontalLayout.addWidget(self.left_menu_main_container, 0, Qt.AlignLeft)

        self.main_body = QWidget(self.widget_2)
        self.main_body.setObjectName(u"main_body")
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.main_body)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QCustomStackedWidget(self.main_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 589, 236))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.webEngineView = QWebEngineView(self.scrollAreaWidgetContents)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy2)
        self.webEngineView.setMinimumSize(QSize(0, 0))
        self.webEngineView.setUrl(QUrl(u"about:blank"))



        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "output.html"))
        local_url = QUrl.fromLocalFile(file_path)

        self.returnButton = returnBtn()
        self.returnButton.setText("Retour à la carte")
        self.returnButton.clicked.connect(self.returnButton.returnB)

        self.verticalLayout_14.addWidget(self.webEngineView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.verticalLayout_14.addWidget(self.returnButton)

        self.stackedWidget.addWidget(self.page)


        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.navlist = CustList()

        self.verticalLayout_9.addWidget(self.navlist)

        self.page_2.setLayout(self.verticalLayout_9)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_10 = QVBoxLayout(self.page_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_11 = QVBoxLayout(self.page_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_12 = QVBoxLayout(self.page_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_13 = QVBoxLayout(self.page_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.page_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.stackedWidget.addWidget(self.page_6)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_7)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.size_grip = QFrame(self.widget_7)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(20, 20))
        self.size_grip.setMaximumSize(QSize(20, 20))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.size_grip)


        self.verticalLayout.addWidget(self.widget_7)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle_button.setText(QCoreApplication.translate("MainWindow", u"  Menu", None))
        self.pushButton_8.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.restoreWindow.setText("")
        self.minimizeWindow.setText("")
        self.closeWindow.setText("")
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"Carte", None))
        self.projects_btn.setText(QCoreApplication.translate("MainWindow", u"Liste", None))
        self.reports_btn.setText(QCoreApplication.translate("MainWindow", u"Ajouter une préparation", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.settings_btns.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.donatebtn.setText(QCoreApplication.translate("MainWindow", u"Paye moi un café !", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PrepQ by VA SIM ^^", None))
