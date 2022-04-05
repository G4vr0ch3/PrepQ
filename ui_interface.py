from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

from os.path import exists

import maps
import os
import webbrowser
import PySide2
import resources_rc
import warnings

import submit_function as sf
import geopandas as gpd

warnings.filterwarnings("ignore")


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

font3 = QFont()
font3.setFamily(u"URW Gothic")
font3.setPointSize(16)
font3.setBold(True)
font3.setWeight(75)

def namechanged(text):
    navname = text

def infoschanged(text):
    navinfos = text

def zonechanged(text):
    navzone = text

def testname(nme):

    try:
        df = gpd.read_file("zones/zones.json")
        df.head(2)

        for i in range(len(df)):
            if (df["name"][i] == nme):
                return True

        return False

    except:
        try:
            print("Trying old json file")
            df = gpd.read_file("zones/zones.json.old")
            df.head(2)

            for i in range(len(df)):
                if (df["name"][i] == nme):
                    return True
            rfile = open("zones/zones.json.old", "r")
            file = open("zones/zones.json", "w")
            file.write(rfile.read())

            return False

        except:
            print("Error loading json file.")

def getid(item):

    try:
        df = gpd.read_file("zones/zones.json")
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
            df = gpd.read_file("zones/zones.json.old")
            df.head(2)

            nme = item.text()
            nme = nme.split(" - ")
            nme = nme[0]

            for i in range(len(df)):
                if (df["name"][i] == nme):
                    return df["id"][i]

            rfile = open("zones/zones.json.old", "r")
            file = open("zones/zones.json", "w")
            file.write(rfile.read())

            return "notfound"

        except:
            print("Error loading json file.")


class searchengine(QLineEdit):

    def __init__(self):
        super().__init__()
        self.setObjectName(u"lineEdit")
        self.textChanged.connect(self.search)


    def search(self):
        self.setText("")

#data = [["id", ["mots"]]]

#query = self.text().split(" ")
#for i in query:
#   dt = []
#   for j in range data:
#       if i in j:
#           dt.append(j)
#   data = np.unique(dt)
#
#


class easterbutton(QPushButton):

    click_counter = 0

    def Clicked(self):
        self.click_counter += 1

        if self.click_counter == 3:
            self.hide()
            self.window().ui.infoTitle.hide()
            self.window().ui.infotodo.hide()
            self.window().ui.infothanks.hide()

            self.window().ui.egg = customEngineView()

            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "icons/game/game.html"))
            local_url = QUrl.fromLocalFile(file_path)
            self.window().ui.egg.load(QUrl(local_url))

            self.window().ui.egg.page().settings().setAttribute(PySide2.QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)

            self.window().ui.egg.titleChanged.connect(self.window().ui.egg.ChangedC)

            self.window().ui.verticalLayout_13.addWidget(self.window().ui.egg)


class printbtn(QPushButton):

    title = ""

    def __init__(self, rtitle=""):
        super().__init__()
        self.title = rtitle
        self.setFont(font1)
        self.setText("Imprimer")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon12)
        self.setIconSize(QSize(24, 24))

    def printf(self):
        link = os.path.dirname(os.path.abspath(__file__)) + '\prepa\\' + self.title
        webbrowser.open(link)

class customEngineView(QWebEngineView):
    def ChangedA(self):

        title = self.title()


        if (title != 'output.html'):

            self.window().ui.footer = QHBoxLayout()

            self.window().ui.returnButton = returnBtn("Retour à la carte")
            self.window().ui.returnButton.clicked.connect(self.window().ui.returnButton.returnB)
            self.window().ui.footer.addWidget(self.window().ui.returnButton)

            self.window().ui.print_btn = printbtn(title)
            self.window().ui.print_btn.setObjectName(u"print_btn")
            self.window().ui.footer.addWidget(self.window().ui.print_btn)
            self.window().ui.print_btn.clicked.connect(self.window().ui.print_btn.printf)

            self.window().ui.verticalLayout_14.addLayout(self.window().ui.footer)
            self.window().ui.page.setLayout(self.window().ui.verticalLayout_14)

    def ChangedB(self):

        title = self.title()

        self.window().ui.footer = QHBoxLayout()

        self.window().ui.rtbtn = returnBtn("Retour à la liste")
        self.window().ui.rtbtn.clicked.connect(self.window().ui.rtbtn.returnA)
        self.window().ui.footer.addWidget(self.window().ui.rtbtn)

        self.window().ui.prntbtn = printbtn(title)
        self.window().ui.prntbtn.setObjectName(u"print_btn")
        self.window().ui.footer.addWidget(self.window().ui.prntbtn)
        self.window().ui.prntbtn.clicked.connect(self.window().ui.prntbtn.printf)

        self.window().ui.verticalLayout_9.addLayout(self.window().ui.footer)
        self.window().ui.page_2.setLayout(self.window().ui.verticalLayout_9)


    def ChangedC(self):

        title = self.title()

        if title == "over":
            self.window().ui.egg.hide()

            self.window().ui.label_11 = QLabel()
            self.window().ui.label_11.setFont(font2)
            self.window().ui.label_11.setText("Game Over")
            self.window().ui.label_11.setAlignment(Qt.AlignCenter)

            self.window().ui.label_12 = QLabel()
            self.window().ui.label_12.setFont(font)
            self.window().ui.label_12.setText("Hope you liked my app ;)")
            self.window().ui.label_12.setAlignment(Qt.AlignCenter)

            self.window().ui.playagainbtn = playbtn()
            self.window().ui.playagainbtn.clicked.connect(self.window().ui.playagainbtn.Clicked)

            self.window().ui.quitbutton = quitbtn()
            self.window().ui.quitbutton.clicked.connect(self.window().ui.quitbutton.Clicked)

            self.window().ui.horizontalLayout_10 = QHBoxLayout()

            self.window().ui.horizontalLayout_10.addWidget(self.window().ui.quitbutton, alignment=Qt.AlignCenter)
            self.window().ui.horizontalLayout_10.addWidget(self.window().ui.playagainbtn, alignment=Qt.AlignCenter)

            self.window().ui.verticalLayout_13.addWidget(self.window().ui.label_11)
            self.window().ui.verticalLayout_13.addLayout(self.window().ui.horizontalLayout_10, alignment=Qt.AlignVCenter)
            self.window().ui.verticalLayout_13.addWidget(self.window().ui.label_12)


class quitbtn(QPushButton):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"quitbtn")
        self.setFont(font1)
        self.setText("Quitter")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon1)
        self.setIconSize(QSize(35, 35))

    def Clicked(self):
        self.hide()
        self.window().ui.playagainbtn.hide()
        self.window().ui.label_11.hide()
        self.window().ui.label_12.hide()
        self.window().ui.label_8.click_counter = 0
        self.window().ui.label_8.show()
        self.window().ui.infoTitle.show()
        self.window().ui.infotodo.show()
        self.window().ui.infothanks.show()

class playbtn(QPushButton):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"playagainbtn")
        self.setFont(font1)
        self.setText("Recommencer")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon1)
        self.setIconSize(QSize(35, 35))

    def Clicked(self):
        self.hide()
        self.window().ui.quitbutton.hide()
        self.window().ui.label_11.hide()
        self.window().ui.label_12.hide()

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "icons/game/game.html"))
        local_url = QUrl.fromLocalFile(file_path)
        self.window().ui.egg.load(QUrl(local_url))

        self.window().ui.egg.show()

class dialog(QMainWindow):

    def __init__(self, error="PrepQ à rencontré une erreur."):
        super().__init__()
        self.setStyleSheet(u"*{\n"
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
        self.resize(300, 150)
        self.setWindowTitle("PrepQ - Error")
        self.setWindowIcon(PySide2.QtGui.QIcon("icons/icon.jpg"))
        self.centralwidget_2 = QWidget(self)
        self.centralwidget_2.setObjectName(u"centralwidget_2")
        self.verticalLayout_15 = QVBoxLayout(self.centralwidget_2)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.errorlabel = QLabel(self)
        self.errorlabel.setText(error)
        self.errorlabel.setFont(font3)
        self.errorlabel.adjustSize()
        self.errorlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.errorlabel)
        self.setCentralWidget(self.centralwidget_2)
        self.centralwidget_2.setLayout(self.verticalLayout_15)


class imported(QMainWindow):

    def __init__(self, error="PrepQ à rencontré une erreur."):
        super().__init__()
        self.setStyleSheet(u"*{\n"
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
        self.resize(300, 150)
        self.setWindowTitle("PrepQ - Importation réussie")
        self.setWindowIcon(PySide2.QtGui.QIcon("icons/icon.jpg"))
        self.centralwidget_3 = QWidget(self)
        self.centralwidget_3.setObjectName(u"centralwidget_3")
        self.verticalLayout_16 = QVBoxLayout(self.centralwidget_3)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_15")
        self.verticalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.successlabel = QLabel(self)
        self.successlabel.setText(error)
        self.successlabel.setFont(font3)
        self.successlabel.adjustSize()
        self.successlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.successlabel)
        self.setCentralWidget(self.centralwidget_3)
        self.centralwidget_3.setLayout(self.verticalLayout_16)


class browsebtn(QPushButton):

    filename = ""

    def __init__(self):
        super().__init__()
        self.setObjectName(u"returnButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/paperclip.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon1)
        self.setIconSize(QSize(24, 24))
        self.setFont(font1)

    def Clicked(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', ':', 'Préparation (*.pdf *.html)')
        self.setText(fname[0])
        self.filename = fname[0]


class submitbtn(QPushButton):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"submitbtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon1)
        self.setIconSize(QSize(24, 24))
        self.setFont(font1)
        self.setText("Ajouter")
        self.clicked.connect(self.Clicked)

    def Clicked(self):
        if (self.window().ui.browse.filename == ""):
            self.window().ui.dial = dialog("Vous avez oublié d'ajouter une préparation.")
            self.window().ui.dial.show()

        elif ((self.window().ui.lineEdit_2.text() == '') or (self.window().ui.infos.toPlainText() == '')):
            self.window().ui.dial = dialog("Vous n'avez pas renseigner toutes les informations nécessaires")
            self.window().ui.dial.show()
        elif (testname(self.window().ui.lineEdit_2.text())):
            self.window().ui.dial = dialog("Ce nom de navigation est déjà pris.")
            self.window().ui.dial.show()
        else:
            if (self.window().ui.check.isChecked()):
                self.window().ui.dial = dialog("Cette fonction n'est pas disponnible pour le moment.\nNos équipes font de leur mieux pour vous apporter cette fonctionnalité au plus vite !")
                self.window().ui.dial.show()

            try:
                sf.wrt(self.window().ui.lineEdit_2.text(), self.window().ui.infos.toPlainText(), self.window().ui.browse.filename, self.window().ui.geom.toPlainText())
                self.window().ui.dial = imported("Votre préparation de quart à été ajoutée à votre liste de préparations !")
                self.window().ui.dial.show()
                self.window().ui.navlist.rsetlist()
                self.window().ui.lineEdit_2.setText("")
                self.window().ui.infos.setPlainText("")
                self.window().ui.geom.setPlainText("")
                self.window().ui.browse.setText("Joindre la préparation")
                self.window().ui.browse.filename = ""
                maps.rsetmap()
                file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "output.html"))
                local_url = QUrl.fromLocalFile(file_path)
                self.window().ui.webEngineView.load(QUrl(local_url))

            except:
                self.window().ui.dial = dialog("Echec de l'importation.\nVérifiez les informations renseignées et réessayez.")
                self.window().ui.dial.show()


class donatebtn(QPushButton):
    def donate(self):
        webbrowser.open("https://www.paypal.com/paypalme/AReppelin")

class returnBtn(QPushButton):
    def __init__(self, label = "Retour"):
        super().__init__()
        self.setObjectName(u"returnButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/skip-back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon1)
        self.setIconSize(QSize(24, 24))
        self.setFont(font1)
        self.setText(label)


    def returnB(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "output.html"))
        local_url = QUrl.fromLocalFile(file_path)
        self.window().ui.webEngineView.load(QUrl(local_url))
        self.window()
        self.window().ui.returnButton.hide()
        self.window().ui.print_btn.hide()

    def returnA(self):
        self.window().ui.render.hide()
        self.window().ui.rtbtn.hide()
        self.window().ui.prntbtn.hide()

class CustList(QListWidget):

    def setlist(self):
        try:
            df = gpd.read_file("zones/zones.json")
            df.head(2)

            itemlist = []

            for i in range(len(df)):
                itemlist.append(df["name"][i] + " - " + df["infos"][i])

            itemlist.sort()
            for item in itemlist:
                self.addItem(item)

        except:
            try:
                print("Trying old json file")
                df = gpd.read_file("zones/zones.json.old")
                df.head(2)

                itemlist = []

                for i in range(len(df)):
                    itemlist.append(df["name"][i] + " - " + df["infos"][i])

                itemlist.sort()
                for item in itemlist:
                    self.addItem(item)

                rfile = open("zones/zones.json.old", "r")
                file = open("zones/zones.json", "w")
                file.write(rfile.read())

            except:
                print("Error loading json file.")

    def rsetlist(self):
        self.clear()
        self.setlist()

    def __init__(self):
        super().__init__()
        self.setObjectName(u"navlist")
        self.setFont(font2)

        self.setlist()

        self.itemClicked.connect(self.Clicked)


    def Clicked(self, item):
        self.window().ui.verticalLayout_9.removeWidget(self.window().ui.navlist)
        self.window().ui.render = customEngineView()
        self.window().ui.render.setObjectName(u"render")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.window().ui.render.sizePolicy().hasHeightForWidth())
        self.window().ui.render.setSizePolicy(sizePolicy2)
        self.window().ui.render.setMinimumSize(QSize(0, 0))
        self.window().ui.render.page().settings().setAttribute(PySide2.QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        id = getid(item)

        if (exists("prepa/"+id+".html")):
            fle = "prepa/"+id+".html"
        elif (exists("prepa/"+id+".pdf")):
            fle = "prepa/"+id+".pdf"
        else:
            fle = ""

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), fle))
        url = QUrl.fromLocalFile(file_path)
        self.window().ui.render.setUrl(QUrl(url))
        self.window().ui.render.load(QUrl(url))
        self.window().ui.render.titleChanged.connect(self.window().ui.render.ChangedB)
        self.window().ui.verticalLayout_9.addWidget(self.window().ui.render)




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
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
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

        self.searchline = searchengine()

        self.horizontalLayout_7.addWidget(self.searchline)


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
        icon6.addFile(u":/icons/icons/compass.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon6)
        self.dashboard_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.dashboard_btn)

        self.projects_btn = QPushButton(self.widget_3)
        self.projects_btn.setObjectName(u"projects_btn")
        self.projects_btn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon11.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        self.webEngineView = customEngineView(self.scrollAreaWidgetContents)
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

        self.verticalLayout_14.addWidget(self.webEngineView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)

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

        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignLeft)

        self.lineEdit_2 = QLineEdit(self.page_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: 1px solid white;")
        self.lineEdit_2.setAlignment(Qt.AlignTop)
        self.lineEdit_2.textChanged.connect(namechanged)

        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignLeft)

        self.infos = QPlainTextEdit(self.page_3)
        self.infos.setObjectName(u"infos")
        self.infos.setFont(font)
        self.infos.setStyleSheet("border: 1px solid white;")

        self.browse = browsebtn()
        self.browse.setText("Joindre la préparation")
        self.browse.clicked.connect(self.browse.Clicked)

        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignLeft)

        self.geom = QPlainTextEdit(self.page_3)
        self.geom.setObjectName(u"geom")
        self.geom.setStyleSheet("border: 1px solid white;")
        self.geom.setFont(font)

        self.check = QCheckBox("Partager", self.page_3)
        self.check.setFont(font)

        self.submit = submitbtn()

        self.verticalLayout_10.addWidget(self.label_5)
        self.verticalLayout_10.addWidget(self.lineEdit_2)
        self.verticalLayout_10.addWidget(self.label_9)
        self.verticalLayout_10.addWidget(self.infos)
        self.verticalLayout_10.addWidget(self.browse)
        self.verticalLayout_10.addWidget(self.label_10)
        self.verticalLayout_10.addWidget(self.geom)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.addStretch(1)
        self.horizontalLayout_9.addWidget(self.check)
        self.horizontalLayout_9.addWidget(self.submit)

        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

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

        self.infoTitle = QPlainTextEdit(self.page_6)
        self.infoTitle.setObjectName(u"infoTitle")
        self.infoTitle.setFont(font)
        self.infoTitle.setPlainText("Développé avec python 3.8 \n\nConçu par et pour les élèves de l'école Navale, ce logiciel vise à centraliser les préparations de quart des navigations qu'ils auront l'occasion de réaliser. \nLa grande expérience de la promotion EN20 se limitant à la rade de Brest et ses alentours, nous espérons voire bientôt les élèves et anciens-élèves d'autre promotions ajouter leur travail et partager leurs connaissances.")
        self.infoTitle.setReadOnly(True)
        self.verticalLayout_13.addWidget(self.infoTitle, alignment=Qt.AlignVCenter)

        self.infotodo = QPlainTextEdit(self.page_6)
        self.infotodo.setObjectName(u"infotodo")
        self.infotodo.setFont(font)
        self.infotodo.setPlainText("\n\nSont en cours de développement les fonctionnalités suivantes :\n - Le partage de préparations de quart (validées par un controleur)\n - La possibilité d'éditer et d'annoter les préprarations existantes\n - La mise à jour en ligne du contenu de l'application\n - Ce que vous nous proposerez !")
        self.infotodo.setReadOnly(True)
        self.verticalLayout_13.addWidget(self.infotodo, alignment=Qt.AlignVCenter)

        self.infothanks = QPlainTextEdit(self.page_6)
        self.infothanks.setObjectName(u"infothanks")
        self.infothanks.setFont(font)
        self.infothanks.setPlainText("Développement : A. REPPELIN")
        self.infothanks.setReadOnly(True)
        self.verticalLayout_13.addWidget(self.infothanks, alignment=Qt.AlignVCenter)

        self.label_8 = easterbutton(self.page_6)
        self.label_8.setObjectName(u"easter")
        self.label_8.setFont(font2)
        self.label_8.clicked.connect(self.label_8.Clicked)

        self.verticalLayout_13.addWidget(self.label_8, alignment=Qt.AlignLeft | Qt.AlignBottom)

        self.stackedWidget.addWidget(self.page_6)

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

        self.page_7 = QWidget(self.widget_3)
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_17 = QVBoxLayout(self.page_7)
        self.verticalLayout_17.setObjectName(u"verticallayout_17")

        self.printlist = CustList()

        self.verticalLayout_17.addWidget(self.printlist)

        self.page_7.setLayout(self.verticalLayout_17)

        self.stackedWidget.addWidget(self.page_7)


        self.verticalLayout_7.addWidget(self.stackedWidget)

        self.webEngineView.titleChanged.connect(self.webEngineView.ChangedA)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle_button.setText(QCoreApplication.translate("MainWindow", u"  Menu", None))
        self.pushButton_8.setText("")
        self.searchline.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.restoreWindow.setText("")
        self.minimizeWindow.setText("")
        self.closeWindow.setText("")
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"Carte", None))
        self.projects_btn.setText(QCoreApplication.translate("MainWindow", u"Liste", None))
        self.reports_btn.setText(QCoreApplication.translate("MainWindow", u"Ajouter une préparation", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.settings_btns.setText(QCoreApplication.translate("MainWindow", u"Informations", None))
        self.donatebtn.setText(QCoreApplication.translate("MainWindow", u"Paye moi un café !", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Version: a1.0.0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PrepQ by VA SIM ^^", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Navigation :", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Informations :", None))
        self.infos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Donnez quelques informations sur la navigation concernée et sur le contenu de votre préparation", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Zone (optionnel) :", None))
        self.geom.setPlaceholderText(QCoreApplication.translate("MainWindow", u'Ecrivez sous la forme "[longitude latitude], [longitude latitude], [longitude latitude], ..."', None))
