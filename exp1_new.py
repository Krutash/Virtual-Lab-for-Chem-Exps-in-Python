import PyQt5
import PyQt5.QtCore
from PyQt5.QtCore import *
import PyQt5.QtGui
from PyQt5.QtGui import *
import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
import random
import sys
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

class Exp1_class(QWidget):
    def __init__(self):
        super().__init__()
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        #self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Theory")
        self.tabs.addTab(self.tab2,"Perform")
        self.tabs.addTab(self.tab3, "Video")
        self.tabs.addTab(self.tab4, "Question Bank")
        
        self.label = QLabel("1.Standarizing Hypo Solution\n with known concentration of CuSO4")
        self.label2 = QLabel("Process to prepare standard CuSO4.5H2O solution :")

        self.weight = QLineEdit()
        
        self.init_bur = 50.00
        self.n2 = QLineEdit()
        self.n2.setReadOnly(True)
        self.ans = QLineEdit()
        self.ans.setReadOnly(True)
        
        
        self.label3 = QLabel("Enter weight(grm) of CuSO4.5H2O salt\n(Taken in 100 ml of H2O)")
        self.WeightLine = QLineEdit()
        self.WeightLine.setFixedWidth(100)
        self.WeightLine.returnPressed.connect(self.getWeight)
        
        
        self.VolLabel = QLabel("Enter Volume(ml) of CuSO4.5H2O salt\n(Taken in conical flask)")
        self.VolLine = QLineEdit()
        self.VolLine.setFixedWidth(100)
        self.VolLine.setReadOnly(True)
        #self.vol = QLineEdit()
        self.VolLine.returnPressed.connect(self.getvol)
        self.tempLine = QLineEdit()
        self.tempLine.setReadOnly(True)
        self.tempLine.textChanged.connect(self.randomVol)
        
        self.label4 = QLabel()
        self.lab45 = QLabel()
        self.label5 = QLabel()
        self.label6 = QLabel()
        
        
        
        self.label7 = QLabel("2. Finding the strength of unknown CuSO4 solution")
        self.label8 = QLabel("Enter the Volume(ml) of unknown\n CuSO4.5H2O salt taken")
        self.Unknown = QLineEdit()
        self.Unknown.setFixedWidth(100)
        self.Unknown.setReadOnly(True)
        self.Unknown.returnPressed.connect(self.calculate)
        self.lab9 = QLabel()
        
        self.label9 = QLabel()
        self.label10 = QLabel()
        
        self.label11 = QLabel("Calculate the strength of unknown solution\n Put your answer below :")
        self.ansLine = QLineEdit()
        self.ansLine.setFixedWidth(100)
        self.ansLine.setReadOnly(True)
        self.ansLine.returnPressed.connect(self.checkAns)
        self.correctLabel = QLabel()

        self.HomeLay = QVBoxLayout()
        
        
        for i in[self.label, self.label2, self.label3, self.WeightLine, self.VolLabel, self.VolLine,
                   self.label4, self.lab45, self.label5, self.label6, self.label7, self.label8,
                   self.Unknown,self.lab9, self.label9, self.label10, self.label11, self.ansLine, self.correctLabel]:
            self.HomeLay.addWidget(i)
            
        
        self.Title = QLabel("DETERMINING THE STRENGTH OF UNKNOWN SOLUTION OF CuSO4")
        self.Title.setAlignment(Qt.AlignCenter)
        self.movie2 = QMovie("an2.gif")
        
        #self.movie2.frameChanged.connect(self.repaint)
        ##print("insideClass1")
        self.movie = QLabel()
        
        self.movie.setMovie(self.movie2)
        self.movie2.start()
        ##print("insideClass2")
        
        ##print("insideClassMid")
        self.movieBox = QVBoxLayout()
        self.movieBox.addWidget(self.Title)
        self.movieBox.addWidget(self.movie)
        self.group1 = QGroupBox()
        self.group1.setLayout(self.movieBox)
        self.group2 = QGroupBox()
        self.group2.setLayout(self.HomeLay)

        self.pageBox = QHBoxLayout()
        self.pageBox.addWidget(self.group2)
        self.pageBox.addWidget(self.group1)
        
        self.tab2.setLayout(self.pageBox)
        
        #self.tab1text = QPlainTextEdit()
        
        self.l1 = QLabel()
        self.l1.setPixmap(QPixmap("Copper-1.jpg"))
        #self.l1.setAlignment(Qt.AlignCenter)
        self.l1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l1.setAlignment(Qt.AlignCenter)
        self.l1.setStyleSheet("QLabel {background-color: red;}")
        
        self.l2 = QLabel()
        self.l2.setPixmap(QPixmap("Copper-2.jpg"))
        self.l2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.l2.setAlignment(Qt.AlignCenter)
        self.l2.setStyleSheet("QLabel {background-color: red;}")
        
        self.tab3text = QPlainTextEdit()
        self.tab4text = QPlainTextEdit()

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playButton = QPushButton("Play")
        self.playButton.setEnabled(True) #default is on False, will not play video
        #self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay)) #How the button looks
        self.playButton.clicked.connect(self.play)  #when clicked, should play
 
        self.positionSlider = QSlider(Qt.Horizontal) #the video slider
        self.positionSlider.setRange(0, 0) #setting the range of the slider
        self.positionSlider.sliderMoved.connect(self.setPosition)
 
        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
 
        # Create a widget for window contents
 
        # Create layouts to place inside widget
        self.videoWidget = QVideoWidget()
        self.controlLayout = QHBoxLayout()
        self.controlLayout.setContentsMargins(0, 0, 0, 0)
        self.controlLayout.addWidget(self.playButton)
        self.controlLayout.addWidget(self.positionSlider)
 
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.videoWidget)
        self.layout.addLayout(self.controlLayout)
        self.layout.addWidget(self.errorLabel)
 
        # Set widget to contain window contents
        self.Video_widget = QWidget()
        self.Video_widget.setLayout(self.layout)
 
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        self.loaded1 = 0
        self.tab1Lay = QVBoxLayout()
        self.tab1Lay.addWidget(self.l1)
        self.tab1Lay.addWidget(self.l2)

        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.tab1Lay)

        self.scrollAr = QScrollArea()
        self.scrollAr.setWidget(self.scrollWidget)
        
        self.tab3Lay = QVBoxLayout()
        self.tab3Lay.addWidget(self.Video_widget)
        
        self.tab4Lay = QVBoxLayout()
        self.tab4Lay.addWidget(self.tab4text)
        
        self.tab1Lay2 = QVBoxLayout()
        self.tab1Lay2.addWidget(self.scrollAr)
        
        self.tab1.setLayout(self.tab1Lay2)
        self.tab3.setLayout(self.tab3Lay)
        self.tab4.setLayout(self.tab4Lay)
        
        self.HomePage_lay = QHBoxLayout()
        self.HomePage_lay.addWidget(self.tabs)
        
        
        self.Exp1_widget = QWidget()
        self.setLayout(self.HomePage_lay)
        self.setGeometry(100,100,200,200)
        #self.Exp1_widget.setWindowTitle("Experiment 1")
        #print("insideClassend")

 
    def play(self):
        
        fileName = "exp1.mp4"
        if self.loaded1 == 0:
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.playButton.setText("Pause")
            self.loaded1 = 1
            
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setText("Play")
            self.mediaPlayer.pause()
        else:
            self.playButton.setText("Pause")
            self.mediaPlayer.play()
 
    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
 
    def positionChanged(self, position):
        self.positionSlider.setValue(position)
 
    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)
 
    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
 
    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

        
    def getWeight(self):
        try:
            flo = float(self.WeightLine.text())
            ##print("ok")
            self.label4.setText("Processing.....")
            ##print("ok2")
            self.weight.setText(str(flo))
            ##print("ok3")
            self.VolLine.setReadOnly(False)
        except:
            self.WeightLine.setText("")
            self.errorMessage()
        
    def getvol(self):
        try:
            f = float(self.VolLine.text())
            #self.vol = f
            init_bur = 50.00
            
            self.lab45.setText("Following are the burrette readings")
            #print("ok1")
            self.label5.setText("Initial Reading : "+str(init_bur)+ " ml")
            #print("ok2")
            self.tempLine.setText(str(f))
            #print("ok3")
            self.Unknown.setReadOnly(False)
            
        except:
            self.VolLine.setText("")
            self.errorMessage()
            
    def randomVol(self):
        f = float(self.tempLine.text())
        k = float(random.randint(10000, 40000))
        final_bur = k/1000
        we = float(self.weight.text())
        self.label6.setText("Final Reading : "+str(final_bur)+ " ml")
        n1 = we/249.68
        v2 = 50.00-f
        n2 = (n1*f)/v2
        self.n2.setText(str(n2))
            
    def calculate(self):
        try:
            n2 = float(self.n2.text())
            v3 = float(self.Unknown.text())
            k = float(random.randint(9000, 45000))
            v4 = k/1000
            self.lab9.setText("Following are the burrette readings")
            self.label9.setText("Initial Reading : "+str(self.init_bur)+ " ml")
            self.label10.setText("Final Reading : "+str(v4)+" ml")
            vlo4 = 50.00-v4
            n3 = (n2*vlo4)/v3
            self.ans.setText(str(n3))
            self.ansLine.setReadOnly(False)
        except:
            self.Unknown.setTeext("")
            self.errorMessage()
    def checkAns(self):
        try:
            an = float(self.ans.text())
            an = round(an, 3)
            user = float(self.ansLine.text())
            
            if(user >= an*0.95 and user <= an*1.05):
                self.correctLabel.setText("Correct Answer !")
            else:
                self.correctLabel.setText("Incorrect ! Ans = "+str(an))
        except :
            self.correctLabel.setText("Invalid !")

    def errorMessage(self):
        self.w = QMessageBox()
        self.w.resize(150, 150)
        self.w.setIcon(QMessageBox.Warning)
        self.w.setInformativeText("Invalid entry !")
        self.w.setWindowTitle("Warning")
        self.w.exec()


def main_exp1():
    obj = Exp1_class()
    return obj
