import sys
import random
import io
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication

tmp = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>800</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>340</x>
     <y>740</y>
     <width>93</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Нарисовать</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Example(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(tmp)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_krug(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_krug(self, qp):
        n = random.randrange(1, 100)
        for i in range(n):
            r = random.randrange(0, 256)
            g = random.randrange(0, 256)
            b = random.randrange(0, 256)
            qp.setBrush(QColor(r, g, b))
            rad = random.randrange(1, 401)
            qp.drawEllipse(random.randrange(1, 800), random.randrange(1, 800), rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())