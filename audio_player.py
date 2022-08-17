from enum import Enum
from itertools import count
import random

class PlayerState(Enum):
    STOP = 1
    PLAYING = 2
    PAUSE = 3

class Song:
    def __init__(self, title, artist, year, file_name):
        self._title = title
        self._artist = artist
        self._year = year
        self._file_name = file_name

    def title(self):
        return self._title

    def artist(self):
        return self._artist

    def year(self):
        return self._year

    def file_name(self):
        return self._file_name


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
        if song.file_name().endswith(".mp3"):
            self.play_list.append(song)

    def print_list(self):
        for song in self.play_list:
            print(song.title(), song.artist(), song.year(), song.file_name())
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

    
    #musica.print_list()
    
    song = Song('Obsessed', 'Celine', 2000, 'Obsessed.mp3')
    
    musica.add(song)
    musica.print_list()
    # print(song.title())
    