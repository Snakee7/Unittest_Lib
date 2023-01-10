from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QPixmap
		
class View(QtWidgets.QMainWindow):
    _presenter = None

    def __init__(self, presenter):
        super(View, self).__init__()
        uic.loadUi('Desain.ui', self)

        self._presenter = presenter
        self.pushButton.clicked.connect(self.OnButtonClick)
        self.initComboBox()
	
        self.actionclose.triggered.connect(self.closeApp)

        self.show()

    def OnButtonClick(self):
        album_title = self.comboBox.currentText()
        track_list = self._presenter.getTrackList(album_title)
        self.tableWidget.setRowCount(len(track_list)-1)
        self.tableWidget.setColumnCount(len(track_list[0]))
        self.tableWidget.setHorizontalHeaderLabels(track_list[0])
        self.tableWidget.setColumnWidth(0, 75)
        self.tableWidget.setColumnWidth(1, 195)
        self.tableWidget.verticalHeader().hide()

        for y in range(1, len(track_list)):
            for x in range(len(track_list[0])):
                self.tableWidget.setItem(y-1, x, QTableWidgetItem(str(track_list[y][x])))

    def initComboBox(self):   
        self.comboBox.activated.connect(self.GetCover)

        albums = self._presenter.getAlbums()
        self.comboBox.clear() 
        self.comboBox.addItems(albums)

        self.GetCover(0)

    def GetCover(self, index):
        album_title = self.comboBox.currentText()
        self.pixmap = QPixmap(self._presenter.GetCoverImage(album_title))
        self.pixmap = self.pixmap.scaled(250, 250)
        self.imageCover.setPixmap(self.pixmap) 

    def closeApp(self):
        self.close()
