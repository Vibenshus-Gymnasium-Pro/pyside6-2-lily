# [[file:README.org::*Direkte indlæsning af designfil][Direkte indlæsning af designfil:1]]
import sys
import os

import roeversprog

from PySide6.QtWidgets import QApplication, QLabel, QPlainTextEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject

# loader-objekt som bruges til at loade .ui-filen
loader = QUiLoader()

class Roeversprogsoversaetter(QObject):
    def __init__(self):
        super().__init__()
        # Her loades brugerfladen fra Designer.
        basepath = os.path.dirname(__file__)
        uifile = os.path.join(basepath, "roeversprogsoversaetter.ui")
        self.ui = loader.load(uifile, None)
        # self.ui refererer til selve brugerfladen som for nu er af typen
        # QMainWindow, og som indeholder et gridLayout og en pushbutton
        self.ui.setWindowTitle("Direkte indlæsning fra ui")
        # Her sættes signal og slot op for oversaetknap og metoden oversaet
        oversaet_knap = self.ui.findChild(QObject, "oversaet_knap")
        oversaet_knap.clicked.connect(self.oversaet)

        # find skift_knap og connect den til funktionen skift_sprog
        skift_knap = self.ui.findChild(QObject, "skift_knap")
        skift_knap.clicked.connect(self.skift_sprog)

    def oversaet(self):
        # find input og output tekster
        input = self.ui.findChild(QObject, "input_text")
        output = self.ui.findChild(QObject, "output_text")

        inputtext = input.toPlainText()
        label_dansk = self.ui.findChild(QLabel, "dansk_label")

        # bestemmer hvilken funktion der skal bruges ud fra hvilket label der er på venstre side
        if label_dansk.text() == "Dansk":
            translated = roeversprog.oversaet_til_roeversprog(inputtext)
            output.setPlainText(translated)
        else:
            translated = roeversprog.oversaet_fra_roeversprog_til_andet_sprog(inputtext)
            output.setPlainText(translated)

    def skift_sprog(self):
        # find Labels
        label_dansk = self.ui.findChild(QLabel, "dansk_label")
        label_roeversprog = self.ui.findChild(QLabel, "roeversprog_label")

        # få teksten fra labels
        tekst_dansk = label_dansk.text()
        tekst_roeversprog = label_roeversprog.text()
        
        # skift labelerne så "Dansk" bliver til "Røversprog" og omvendt
        label_dansk.setText(tekst_roeversprog)
        label_roeversprog.setText(tekst_dansk)
        
        # input textboks og output textboks gøres tom
        input = self.ui.findChild(QPlainTextEdit, "input_text")
        input.setPlainText("")

        output = self.ui.findChild(QPlainTextEdit, "output_text")
        output.setPlainText("")

program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
roeversprogsoversaetter = Roeversprogsoversaetter()
roeversprogsoversaetter.ui.show()
program.exec()
