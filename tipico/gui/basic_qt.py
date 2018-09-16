import sys
import Qt
from Qt.QtWidgets import QApplication, QLabel


def main():
    app = QApplication(sys.argv)
    label = QLabel("Hello World.\nUsing Qt binding %s" % Qt.Qt.__binding__)
    label.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
