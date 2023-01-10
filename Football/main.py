import sys
from PyQt5.QtWidgets import QApplication
import Presenter
	
if __name__ == "__main__":
    app = QApplication(sys.argv)
    presenter = Presenter.Presenter()
    app.exec_()



