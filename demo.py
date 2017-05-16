# -*-coding:utf-8-*-
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *


import sys
class ButtonCollection():#对每一个按键事件进行一个定义
  def __init__(self):
    self.every_point = [0 for i in range(8)]
    for i in range(1,24):
      self._add_button(i)
  def _add_button(self,i):
    def button_function():
      print((i-1)/3)
      self.every_point[(i-1)/3]=i%3
      if(i%3==0):self.every_point[(i-1)/3]=3
      print(self.every_point)
    button_function.__name__ = "radioButton%d"%i
    setattr(self,button_function.__name__,button_function)

class Interface(QtGui.QMainWindow):#初始化UI
  def __init__(self):
    super(Interface, self).__init__()
    uic.loadUi("pyqt.ui", self)
    self.b=ButtonCollection()
    self.setup()
    self.polist = [0 for i in range(10) ]


  def setup(self):#初始化按键绑定
      self.radioButton1.clicked.connect(self.b.radioButton1)
      for i in range(1,24):
        eval("self.radioButton%d.clicked.connect(self.b.radioButton%d)"%(i,i))
      self.pushButton.clicked.connect(self.push_Button)

  def push_Button(self):
     sum=0
     for i in range(8):
       if self.b.every_point[i]==0:#保证用户已经选择所有项目
         QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
         QMessageBox.information(self, "Information",self.tr("你第"+str(i+1)+"题没有做出选择,请做出选择"))
         return
       else:
         sum+=self.b.every_point[i]
     if(sum>24):#>24弹出第一个窗口
       QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
       QMessageBox.information(self, "Information", self.tr("说明你情绪自控能力较好"))
     elif(sum>16):#>16弹出第二个窗口
       QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
       QMessageBox.information(self, "Information", self.tr("说明你情绪自控能力一般"))
     else:#否则弹出第三个窗口
       QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
       QMessageBox.information(self, "Information", self.tr("说明你情绪自控能力很差，还须要努力"))


def run():
    app = QtGui.QApplication(sys.argv)#绘制ui界面
    GUI = Interface()#启动后台
    GUI.show()
    sys.exit(app.exec_())#退出


run()
