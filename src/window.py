#!/usr/bin/env python3
# coding: utf8
import pyxel
class App:
    def __init__(self):
        pyxel.init(96, 54, caption="Sound API. Multi sounds.")
        self.__set_music0()
        self.__play()
        pyxel.run(self.update, self.draw)
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.is_play: self.__stop()
            else: self.__play()
    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, 'Please SPACE key: ' + ('PLAY' if self.is_play else 'STOP'), 7)
    def __play(self):
        pyxel.playm(self.music0, loop=True)
        self.is_play = True
    def __stop(self):
        pyxel.stop()
        self.is_play = False
    def __set_music0(self):
        self.__set_sounds()
#        ch1 = [pyxel.sound(0)]
#        ch2 = [pyxel.sound(1)]
        ch1 = [self.sounds[0]]
        ch2 = [self.sounds[1]]
        ch3 = []
        ch4 = []
        self.music0 = 0
        pyxel.music(self.music0).set(ch1, ch2, ch3, ch4)
    def __set_sounds(self):
        self.sounds = [0, 1]
        self.__set_sound00()
        self.__set_sound01()
    def __set_sound00(self): # 主旋律（メロディ）
        self.__set_sound(0, "c2c2rd2e2e2e2c2 e2e2c2c2e2e2e2r d2d2re2f2f2e2d2 f2f2f2f2rrrr")
    def __set_sound01(self): # 伴奏 and ベース
        self.__set_sound(1, "c1g1c1g1c1g1c1g1 c1g1c1g1c1g1c1g1 d1a1d1a1d1a1d1a1 d1a1d1a1d1a1d1a1", tones='p', volumes='2', effects='f')
    def __set_sound(self, snd, notes, tones='t', volumes='6', effects='n', speed=26):
        pyxel.sound(snd).set(
            notes,
            tones,
            volumes ,
            effects ,
            speed,
        )
        
App()
