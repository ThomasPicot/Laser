from PyQt5 import QtWidgets
from Views.openview import OpenView

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = OpenView(Form)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
