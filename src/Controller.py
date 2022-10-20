#This is where we will put all our imports:
#Regular
import pygame
import sys
import time
import random
import json

class Controller:
    def __init__(self, width=1920, height=1080):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        self.width = width
        self.height = height
        self.hasWon = False
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.hit=0
        self.blow=0
        #self.codes = ["test","temp","no","yes"]
        self.codes = ["corevo"]
        self.locks = 0
        pygame.font.init()
        #INITIAL STATE
        self.state = "MENU"

    def mainLoop(self):
        """Controls the state of the game"""
        #print("Entering the main loop...")
        while True:
            if(self.state == "MENU"):
                self.menuLoop()
            if(self.state == "INPUT"):
                self.inputLoop()

    def menuLoop(self):
        """This is the Menu Loop of the Game"""
        #print("Entering the menu loop...")
        while self.state == "MENU":
            self.locksRight = pygame.transform.smoothscale(pygame.image.load('assets/locks/AllLocked.png').convert_alpha(), (384,1080))
            #BACKGROUND
            if "corevo" not in self.codes:
                                self.menuBG = pygame.transform.smoothscale(pygame.image.load('assets/EscapeRoomTitleScreenBlank.jpg').convert_alpha(), (self.width,self.height))
            else:
                self.menuBG = pygame.transform.smoothscale(pygame.image.load('assets/EscapeRoomTitleScreenBlankUnlocked.jpg').convert_alpha(), (self.width,self.height))

            self.screen.blit(self.menuBG, (0, 0))
            #MOUSE
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    coords=pygame.mouse.get_pos()
                    #print(coords)
                    #CLICKING UNLOCK BUTTON
                    if((coords[0]>=660 and coords[0]<=1250) and (coords[1]>=545 and coords[1]<=705)):
                        if self.locks==1:
                            print("All 4 locks unlocked. Starting game!")
                            pygame.mixer.music.load('assets/sounds/click.ogg')
                            pygame.mixer.music.play(0)
                            self.state = "INPUT"
                            self.mainLoop()
                        else:
                            #print("Not all locks unlocked. Going to input screen.")
                            pygame.mixer.music.load('assets/sounds/click.ogg')
                            pygame.mixer.music.play(0)
                            self.state = "INPUT"
                            self.mainLoop()
            pygame.display.flip()

    def inputLoop(self):
        """This is the INPUT Loop of the Game"""
        #print("Entering the input loop...")
        rightOrWrong = 2
        myfont = pygame.font.Font('assets/HACKED.ttf', 200)
        answer = ""
        while self.state == "INPUT":
            #BACKGROUND
            if rightOrWrong == 2:
                self.helpScreen = pygame.transform.smoothscale(pygame.image.load('assets/InputScreen.png').convert_alpha(), (self.width,self.height))
            elif rightOrWrong==1:
                self.helpScreen = pygame.transform.smoothscale(pygame.image.load('assets/InputScreenUnlocked.png').convert_alpha(), (self.width,self.height))
            elif rightOrWrong==0:
                self.helpScreen = pygame.transform.smoothscale(pygame.image.load('assets/InputScreenLocked.png').convert_alpha(), (self.width,self.height))

            self.screen.blit(self.helpScreen, (0, 0))
            #MOUSE
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #KEYBOARD INPUT
                if event.type == pygame.KEYDOWN:
                    if rightOrWrong==2:
                        if event.unicode.isalpha():
                            answer += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            answer = answer[:-1]
                        # elif event.key == K_RETURN:
                        #     name = ""
                        #print(answer)
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    coords=pygame.mouse.get_pos()
                    #print(coords)
                    #CLICKING BACK BUTTON
                    if((coords[0]>=495 and coords[0]<=675) and (coords[1]>=890 and coords[1]<=970)):
                        #print("Back Button Pressed")
                        pygame.mixer.music.load('assets/sounds/click.ogg')
                        pygame.mixer.music.play(0)
                        self.state = "MENU"
                        self.mainLoop()
                    #CLICKING ENTER BUTTON
                    if((coords[0]>=1246 and coords[0]<=1447) and (coords[1]>=890 and coords[1]<=970)):
                        if rightOrWrong == 2:
                            #print("Enter Button Pressed")
                            for i in range(0,len(self.codes)):
                                if answer.lower()==self.codes[i]:
                                    pygame.mixer.music.load('assets/sounds/unlock.ogg')
                                    pygame.mixer.music.play(0)
                                    self.codes[i]="2"
                                    self.locks+=1
                                    rightOrWrong=1
                            if rightOrWrong==2:
                                pygame.mixer.music.load('assets/sounds/wrong.ogg')
                                pygame.mixer.music.play(0)
                                rightOrWrong=0

            text = myfont.render(answer, True, (255, 255, 255))
            self.screen.blit(text, ((self.width//3)+115, (self.height//3)+75))
            pygame.display.flip()

    def insertCode(self, num, code):
        if len(code) < 4 and num not in code:
            code.append(num)


    def winLoop(self):
        """This is the Menu Loop of the Game"""
        print("Entering the menu loop...")
        pygame.mixer.music.load('assets/sounds/morseCode.ogg')
        pygame.mixer.music.play(0)
        while self.state == "WIN":
            #BACKGROUND
            self.menuBG = pygame.transform.smoothscale(pygame.image.load('assets/Escaped.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.menuBG, (0, 0))

            pygame.display.flip()
