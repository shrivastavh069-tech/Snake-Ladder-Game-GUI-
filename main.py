import sys
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QMovie
from frnt import Ui_MainWindow as IntroUI
from welcome import Ui_MainWindow as welUI
from playerbott import Ui_MainWindow as gameUI
from playertwo import Ui_MainWindow as gamerUI
from twologic import twoplayWindow
from glogic import dice
from pwin import Ui_MainWindow as pwinUI
from menu_system import menuWindow
from bwin import Ui_MainWindow as bwinUI
import time



class music_manager:
    def __init__(self):
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.player.mediaStatusChanged.connect(self.loop)

    def play_bg(self,volume=0.1):
        self.player.setSource(QUrl.fromLocalFile("music/sound.mpeg"))
        self.audio.setVolume(volume)
        self.player.play()

    def bg_pause(self):
        self.player.pause()

    def stop_bg(self):
        self.player.stop()
        
    def loop (self,status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.player.play()



class IntroWindow(QMainWindow):
    def __init__(self):
        super().__init__()                                                                                                                                    
        self.ui = IntroUI()
        self.ui.setupUi(self)
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.video = QVideoWidget(self.ui.videowidget)
        self.video.setGeometry(self.ui.videowidget.rect())
        self.player.setVideoOutput(self.video)
        self.player.setSource(QUrl.fromLocalFile("music/intro.mp4"))
        self.audio.setVolume(0.5)
        self.player.play()
        self.player.mediaStatusChanged.connect(self.video_end)                                                                                                                                                
    def video_end(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.open_welco()
            
    def open_welco(self):
        self.welcome =welcoWindow()
        self.welcome.show()
        self.hide()            


class welcoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.music=music_manager()
        self.music.play_bg()
        self.ui=welUI()
        self.ui.setupUi(self)
        self.movie=QMovie("music/pla.gif")
        self.ui.label.setMovie(self.movie)
        self.movie.start()
        self.ui.pushButton.clicked.connect(self.open_menu)
       
    
        
    def open_menu(self):
        from menu_system import menuWindow 
        self.menu = menuWindow()
        self.menu.show()   
        self.hide()

        
from PyQt6.QtGui import QPixmap
class gameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.marine=music_manager()
        self.user_position=0
        self.bot_position=0
        self.ui=gameUI()
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

            11:(819,445),
            12:(780,445),
            13:(738,445),
            14:(694,445),
            15:(658,445),
            16:(615,445),
            17:(570,445),
            18:(532,445),
            19:(492,445),
            20:(456,445),

            21:(456,410),
            22:(492,410),
            23:(532,410),
            24:(570,410),
            25:(615,410),
            26:(658,410),
            27:(694,410),
            28:(738,410),
            29:(780,410),
            30:(819,410),

            31:(819,365),
            32:(782,365),
            33:(730,365),
            34:(694,365),
            35:(658,365),
            36:(615,365),
            37:(570,365),
            38:(532,365),
            39:(492,365),
            40:(456,365),

            41:(456,330),
            42:(492,330),
            43:(532,330),
            44:(570,330),
            45:(615,330),
            46:(658,330),
            47:(694,330),
            48:(738,330),
            49:(780,330),
            50:(819,330),
            
            51:(819,290),
            52:(780,290),
            53:(738,290),
            54:(694,290),
            55:(658,290),
            56:(615,290),
            57:(568,290),
            58:(532,290),
            59:(492,290),
            60:(456,290),

            61:(456,250),
            62:(492,250),
            63:(532,250),
            64:(570,250),
            65:(615,250),
            66:(658,250),
            67:(694,250),
            68:(738,250),
            69:(780,250),
            70:(819,250),

            71:(819,210),
            72:(780,210),
            73:(738,210),
            74:(694,210),
            75:(658,210),
            76:(615,210),
            77:(570,210),
            78:(532,210),
            79:(492,210),
            80:(456,210),

            81:(456,170),
            82:(492,170),
            83:(532,170),
            84:(570,170),
            85:(615,170),
            86:(658,170),
            87:(694,170),
            88:(738,170),
            89:(780,170),
            90:(819,170),
            
            91:(819,130),
            92:(780,130),
            93:(738,130),
            94:(694,130),
            95:(658,130),
            96:(615,130),
            97:(570,130),
            98:(532,130),
            99:(492,130),
            100:(456,130),
            }

    
        self.menu_hide("hide")
        self.ui.label_4.mousePressEvent=(self.menubar)
        self.ui.pushButton.clicked.connect(self.user_turn)

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
                QTimer.singleShot(1000,self.bot_turn)


    def user_move (self):
        
        if self.user_position+self.user > 100:
            QTimer.singleShot(500,self.user_check)
            return
        for i in range (self.user):
            blend=self.user
            self.user_position+=1
            self.mplay()
            QApplication.processEvents()
            time.sleep(0.20)            
        if self.user_position == 100:
            self.user_win()
            return
            
        QTimer.singleShot(500,self.user_check)
       


    def user_win(self):
        self.win=user_winner()
        self.win.show()
        self.hide()

        

    def user_check(self):
        self.user_position,self.bot_position=self.playbot(self.user_position,self.bot_position)
        self.show_token("bot")
        QTimer.singleShot(1000,self.bot_turn)
            
#yah se user ka mamla khatam
        
#yah se bot ka mamla shuru
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
        if self.bot_position+self.bot >100:
            QTimer.singleShot(500,self.checking)
            return

        for i in range (self.bot):
            border=self.bot
            self.bot_position+=1
            self.bplay()
            QApplication.processEvents()
            time.sleep(0.20)
                        
            if self.bot_position == 100:
                self.bot_win()
                return

        QTimer.singleShot(500,self.checking)


    def bot_win(self):
        self.bati=bot_winner()
        self.bati.show()
        self.hide()

    
    def checking(self):
        self.user_position,self.bot_position=self.playbot(self.user_position,self.bot_position)
        self.show_token("user")
        
    def playbot(self,user_position,bot_position):
        self.user_position,self.bot_position= self.ladder(self.user_position,self.bot_position)
        self.user_position,self.bot_position= self.snake(self.user_position,self.bot_position)
        return self.user_position,self.bot_position

    def ladder(self,user_position,bot_position):
        
        ladder={
            14:87,
            40:80,
            23:43,
            50:70
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
            92:69,
            53:49,
            75:64,
            25:17,
            99:2,
            11:9
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
        self.ui.label_6.move(x-16, y-47)
        

    def bplay(self):
        x, y = self.positions[self.bot_position]
        print("bot:",self.bot_position)
        self.ui.label_10.move(x-11, y-47)


    def exit (self):
        QApplication.quit()
    

    


class user_winner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=pwinUI()
        self.ui.setupUi(self)
        self.movie=QMovie("music/winner.gif")
        self.ui.label.setMovie(self.movie)
        self.movie.start()
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.player.setSource(QUrl.fromLocalFile("music/winning.mpeg"))
        self.audio.setVolume(0.7)
        self.player.play()
        self.ui.rematch.clicked.connect(self.open_game)
        self.ui.pushButton.clicked.connect(self.open_menu)


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
        self.movie=QMovie("music/botwinner.gif")
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
   




if __name__=="__main__":
    app =QApplication(sys.argv)
    window=IntroWindow()
    window.show()
    sys.exit(app.exec())





    


