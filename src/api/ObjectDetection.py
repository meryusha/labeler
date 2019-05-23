# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget


class FasterRCNN(QWidget):
    ObjectFound = pyqtSignal(list, str)  # (list, str) as [x,y,w,h]] and label
    ObjectsFound = pyqtSignal(list)  # list of (list, str) with BB and label

    def __init__(self):
        super(FasterRCNN, self).__init__()
        self.pippo = 1

    def detectObjects(self, image):
        print("FasterRCNN detectObjects")
        # self.ObjectFound.emit([100, 100, 30, 200], "myLabelClass")
        shapes = [[[i, i, 50 + i, 50 + i], "obj" + str(i)] for i in range(200)]
        self.ObjectsFound.emit(shapes)
        # self.ObjectsFound.emit([[[100, 100, 30, 200], "myLabelClass"],
        #                         [[200, 200, 60, 400], "myLabelClass2"]])
        return
