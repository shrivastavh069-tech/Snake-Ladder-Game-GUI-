import sys
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QMovie
from PyQt6.QtGui import QPixmap
from playertwo import Ui_MainWindow as gamerUI
from player import Ui_MainWindow as pwinUI
from playerdus import Ui_MainWindow as bwinUI
from glogic import dice
import time





class twoplayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user_position=0
        self.bot_position=0
        self.ui=gamerUI()
        self.ui.setupUi(self)
        self.movie=QMovie("music/board.gif")
        self.ui.label.setMovie(self.movie)
        self.movie.start()
        self.positions = {
            1:(456,483),
            2:(492,483),
            3:(532,483),
            4:(570,483),
            5:(615,483),
            6:(658,483),
            7:(694,483),
            8:(738,483),
            9:(780,483),
            10:(819,483),

            11:(819,439),
            12:(780,439),
            13:(738,439),
            14:(694,439),
            15:(658,439),
            16:(615,439),
            17:(570,439),
            18:(532,439),
            19:(492,439),
            20:(456,439),

            21:(456,395),
            22:(492,395),
            23:(532,395),
            24:(570,395),
            25:(615,395),
            26:(658,395),
            27:(694,395),
            28:(738,395),
            29:(780,395),
            30:(819,395),

            31:(819,353),
            32:(782,353),
            33:(730,353),
            34:(694,353),
            35:(658,353),
            36:(615,353),
            37:(570,353),
            38:(532,353),
            39:(492,353),
            40:(456,353),

            41:(456,320),
            42:(492,320),
            43:(532,320),
            44:(570,320),
            45:(615,320),
            46:(658,320),
            47:(694,320),
            48:(738,320),
            49:(780,320),
            50:(819,320),
            
            51:(819,280),
            52:(780,280),
            53:(738,280),
            54:(694,280),
            55:(658,280),
            56:(615,280),
            57:(570,280),
            58:(532,280),
            59:(492,280),
            60:(456,280),

            61:(456,240),
            62:(492,240),
            63:(532,240),
            64:(570,240),
            65:(615,240),
            66:(658,240),
            67:(694,240),
            68:(738,240),
            69:(780,240),
            70:(819,240),

            71:(819,200),
            72:(780,200),
            73:(738,200),
            74:(694,200),
            75:(658,200),
            76:(615,200),
            77:(570,200),
            78:(532,200),
            79:(492,200),
            80:(456,200),

            81:(456,160),
            82:(492,160),
            83:(532,160),
            84:(570,160),
            85:(615,160),
            86:(658,160),
            87:(694,160),
            88:(738,160),
            89:(780,160),
            90:(819,160),

            91:(819,120),
            92:(780,120),
            93:(738,120),
            94:(694,120),
            95:(658,120),
            96:(615,120),
            97:(570,120),
            98:(532,120),
            99:(492,120),
            100:(456,120),
            }
        self.menu_hide("hide")
        self.ui.label_4.mousePressEvent=self.menubar
        self.ui.pushButton.clicked.connect(self.user_turn)
        self.ui.pushButton_2.clicked.connect(self.bot_turn)


    def menu_hide(self,menu):
        if menu =="hide":
            self.ui.label_11.hide()
            self.ui.resume_push.hide()
            self.ui.menu_push.hide()
            self.ui.exit_push.hide()
            self.ui.label_12.hide()
            self.ui.label_13.hide()
            self.ui.label_8.hide()
            
        if menu == "show":
            self.ui.label_11.show()
            self.ui.resume_push.show()
            self.ui.menu_push.show()
            self.ui.exit_push.show()
            self.ui.label_12.show()
            self.ui.label_13.show()
            self.ui.label_8.show()

    


    def menubar(self,menu):
        self.menu_hide("show")
        self.hide_token("hide")
        self.ui.resume_push.clicked.connect(lambda:self.menu_hide("hide"))
        self.ui.menu_push.clicked.connect(self.open_menu)
        self.ui.exit_push.clicked.connect(self.exit)

    def open_menu(self):
        from main import menuWindow
        self.menu = menuWindow()
        self.menu.show()   
        self.hide()



    def hide_token(self,hide):
        if hide == "user":
            self.ui.pushButton.hide()
            self.ui.label_7.hide()

        if hide =="bot":
            self.ui.pushButton_2.hide()
            self.ui.label_9.hide()
    

    def show_token(self,show):
        if show == "user":
            self.ui.pushButton.show()
            self.ui.label_7.show()

        if show =="bot":
            self.ui.pushButton_2.show()
            self.ui.label_9.show()
            
    def user_turn(self):
        self.show_token("user")
        self.hide_token("bot")
        self.dice_player=QMediaPlayer() 
        self.dice_audio=QAudioOutput()
        self.dice_player.setAudioOutput(self.dice_audio)
        self.dice_player.setSource(QUrl.fromLocalFile("music/dice.mpeg"))
        self.dice_audio.setVolume(0.7)
        self.dice_player.play()
        self.user=dice()
        if  self.user == 1:
            self.ui.label_3.setPixmap(QPixmap("dice/one.jpeg"))

        elif  self.user== 2:
            self.ui.label_3.setPixmap(QPixmap("dice/two.jpeg"))

        elif self.user== 3:
            self.ui.label_3.setPixmap(QPixmap("dice/three.jpeg"))


        elif self.user== 4:
            self.ui.label_3.setPixmap(QPixmap("dice/four.jpeg"))

        elif self.user== 5:
            self.ui.label_3.setPixmap(QPixmap("dice/five.jpeg"))

        else:
            self.ui.label_3.setPixmap(QPixmap("dice/six.jpeg"))
        self.hide_token("user")
        print("user dice:",self.user)
        self.userki_goti()
            
   
    def userki_goti(self):
        if self.user_position == 0:
            QTimer.singleShot(500,self.usergoti)           
        else:
            QTimer.singleShot(1000,self.user_move)

            
    #user ki 6 anne prr goti khulegi
    def usergoti(self):
        if self.user_position ==0:
            if self.user == 6:
                self.user_position =1
                self.mplay()
                QTimer.singleShot(800,self.user_check)
            else:
                self.show_token("bot")
                


    def user_move (self):
        for i in range (self.user):
            blend=self.user

            if self.user_position == 100:
                self.user_position+=1
                self.mplay()
                QApplication.processEvents()
                time.sleep(0.20)
                self.marine.stop_bg()
                self.user_win()

            
            if self.user_position+self.user > 100:
                QTimer.singleShot(500,self.user_check)
                return
                

                
            self.user_position+=1
            self.mplay()
            QApplication.processEvents()
            time.sleep(0.20)
        QTimer.singleShot(500,self.user_check)
       


    def user_win(self):
        self.win=user_winner()
        self.win.show()
        self.hide()

        

    def user_check(self):
        self.user_position,self.bot_position=self.playbot(self.user_position,self.bot_position)
        self.show_token("bot")
        
            
#yah se player 1 ka mamla khatam
        
#yah se player 2 ka mamla shuru
 
    def bot_turn(self):
        self.dice_player=QMediaPlayer() 
        self.dice_audio=QAudioOutput()
        self.dice_player.setAudioOutput(self.dice_audio)
        self.dice_player.setSource(QUrl.fromLocalFile("music/dice.mpeg"))
        self.dice_audio.setVolume(0.7)
        self.dice_player.play()
        self.bot=dice()
        if self.bot ==1:
            self.ui.label_3.setPixmap(QPixmap("dice/one.jpeg"))

        elif  self.bot== 2:
            self.ui.label_3.setPixmap(QPixmap("dice/two.jpeg"))

        elif self.bot== 3:
            self.ui.label_3.setPixmap(QPixmap("dice/three.jpeg"))

        elif self.bot== 4:
            self.ui.label_3.setPixmap(QPixmap("dice/four.jpeg"))

        elif self.bot== 5:
            self.ui.label_3.setPixmap(QPixmap("dice/five.jpeg"))

        else:
            self.ui.label_3.setPixmap(QPixmap("dice/six.jpeg"))

            
        self.hide_token("bot")
        print("bot dice:",self.bot)
        self.botki_goti()

     #bot ki goti khul
    def botki_goti(self):
        if self.bot_position == 0:
            QTimer.singleShot(800,self.gotikhul)
        else:
            QTimer.singleShot(1000,self.bot_move)
            
            
    def gotikhul(self):
        if self.bot_position ==0:
            if self.bot == 6:
                self.bot_position=1
                self.bplay()
                QTimer.singleShot(800,self.checking)
                
            else:
                self.ui.pushButton.show()
                self.ui.label_7.show()         
           

    def bot_move (self):
        for i in range (self.bot):
            border=self.bot
            if self.bot_position+self.bot == 100:
                self.bot_position+=1
                self.bplay()
                QApplication.processEvents()
                time.sleep(0.20)
                self.marine.stop_bg()
                self.bot_win()
                return
            
            if self.bot_position+self.bot >100:
                QTimer.singleShot(500,self.checking)
                return
                
            self.bot_position+=1
            self.bplay()
            QApplication.processEvents()
            time.sleep(0.20)
        QTimer.singleShot(500,self.checking)


    def bot_win(self):
        self.bati=bot_winner()
        self.bati.show()
        self.hide()

    
    def checking(self):
        self.user_position,self.bot_position=self.playbot(self.user_position,self.bot_position)
        self.show_token("user")


    def exit (self):
        QApplication.quit()

        
    def playbot(self,user_position,bot_position):
        self.user_position,self.bot_position= self.ladder(self.user_position,self.bot_position)
        self.user_position,self.bot_position= self.snake(self.user_position,self.bot_position)
        return self.user_position,self.bot_position

    def ladder(self,user_position,bot_position):
        
        ladder={
            76:96,
            71:92,
            41:80,
            2:23,
            26:54,
            11:51
            }
        if user_position in ladder:
            self.ladder_player=QMediaPlayer()
            self.ladder_audio=QAudioOutput()
            self.ladder_player.setAudioOutput(self.ladder_audio)
            self.ladder_player.setSource(QUrl.fromLocalFile("music/ladder.mpeg"))
            self.ladder_audio.setVolume(0.7)
            self.ladder_player.play()
            self.user_position = ladder[user_position]
            self.mplay()
        
            
        if bot_position in ladder:
            self.ladder_player=QMediaPlayer()
            self.ladder_audio=QAudioOutput()
            self.ladder_player.setAudioOutput(self.ladder_audio)
            self.ladder_player.setSource(QUrl.fromLocalFile("music/ladder.mpeg"))
            self.ladder_audio.setVolume(0.5)
            self.ladder_player.play()
            self.bot_position=ladder[bot_position]
            self.bplay()
    
            

        return self.user_position,self.bot_position

    def snake(self,user_position,bot_position):
        snakes = {
            99:22,
            95:88,
            66:43,
            32:8
            }
        

        if user_position in snakes:
            self.snake_player=QMediaPlayer()
            self.snake_audio=QAudioOutput()
            self.snake_player.setAudioOutput(self.snake_audio)
            self.snake_player.setSource(QUrl.fromLocalFile("music/snake.mpeg"))
            self.snake_audio.setVolume(0.7)
            self.snake_player.play()
            self.user_position = snakes[user_position]
            self.mplay()
        
            
        if bot_position in snakes:
            self.snake_player=QMediaPlayer()
            self.snake_audio=QAudioOutput()
            self.snake_player.setAudioOutput(self.snake_audio)
            self.snake_player.setSource(QUrl.fromLocalFile("music/snake.mpeg"))
            self.snake_audio.setVolume(0.7)
            self.snake_player.play()
            self.bot_position=snakes[bot_position]
            self.bplay()
            
        return self.user_position,self.bot_position

    
    def mplay(self):
        x, y = self.positions[self.user_position]
        print("user:",self.user_position)
        self.ui.label_6.move(x-16, y-45)
        

    def bplay(self):
        x, y = self.positions[self.bot_position]
        print("bot:",self.bot_position)
        self.ui.label_10.move(x-9, y-47)




class user_winner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=pwinUI()
        self.ui.setupUi(self)
        self.movie=QMovie("music/player.gif")
        self.ui.label.setMovie(self.movie)
        self.movie.start()
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setSource(QUrl.fromLocalFile("music/winning.mpeg"))
        self.audio.setVolume(0.7)
        self.player.play()
        self.ui.rematch_2.clicked.connect(self.open_game)
        self.ui.menu.clicked.connect(self.open_menu)


    def open_game(self):
        self.player.stop()
        self.game=gameWindow()
        self.game.show()
        self.hide()
        

    def open_menu(self):
        self.player.stop()
        self.menu = menuWindow()
        self.menu.show()   
        self.hide()
    
        

class bot_winner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=bwinUI()
        self.ui.setupUi(self)
        self.movie=QMovie("music/playerdus.gif")
        self.ui.label.setMovie(self.movie)
        self.movie.start()
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.player.setSource(QUrl.fromLocalFile("music/winning.mpeg"))
        self.audio.setVolume(0.7)
        self.player.play()
        self.ui.rematch_2.clicked.connect(self.open_game)    
        self.ui.menu.clicked.connect(self.open_menu)
              
    

    def open_game(self):
        self.player.stop()
        self.game=gameWindow()
        self.game.show()
        self.hide()
        
        
    
    def open_menu(self):
        self.player.stop()
        self.menu = menuWindow()
        self.menu.show()   
        self.hide()
   


