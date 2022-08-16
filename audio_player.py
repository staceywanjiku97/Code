from enum import Enum
from itertools import count
import random

class PlayerState(Enum):
    STOP = 1
    PLAYING = 2
    PAUSE = 3

class AudioPlayer:
    def __init__(self):
        # self.music = music
        self.play_list = []
        self.state = PlayerState.STOP
                   
    def play(self):
        if self.count() == 0:
            print("Empty playlist!")
            return

        for items in self.play_list:
             print("Playing...", items)

        self.state = PlayerState.PLAYING


    def stop(self):
        if self.state == PlayerState.PLAYING:
            print("Stop playing the music!")
        else:
            print("The music is not in play state!")

        self.state = PlayerState.STOP

    def pause(self):
        if self.state == PlayerState.PLAYING:
            print("The music has been paused!")
        else:
            print("The music is in pause state!")

        self.state = PlayerState.PAUSE

    def print_state(self):
        if self.state == PlayerState.STOP:
            print("Stop playing music!")
        elif self.state == PlayerState.PLAYING:
            print("Music is playing!")
        elif self.state == PlayerState.PAUSE:
            print("The music has been paused!")
        else:
            print("Invalid state!")

    def add(self, song):
        if song.endswith(".mp3"):
            self.play_list.append(song)

    def print_list(self):
        for songs in self.play_list:
            print(songs)
        # songs = self.play_list
        # print(songs)

    def count(self):
        return len(self.play_list)
            
 
if __name__ == "__main__":
    musica = AudioPlayer()
    musica.play()
    #musica.stop()
    #musica.pause()
    #musica.print_state()

    musica.add('Deceiver_of_fools.mp3')
    musica.add('Obsessed.mp3')
    musica.add('In_my_own_words.avi')

    #musica.print_list()
    
    