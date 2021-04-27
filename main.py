
from LaserGUIs.Views.openview import OpenView

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = OpenView()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
