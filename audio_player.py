class AudioPlayer:
    def __init__(self, music):
        self.music = music
        
    def play(self):
        print("play")

    def stop(self):
        print("stop")


if __name__ == "__main__":
    musica = AudioPlayer("This_is_me.mp3")
    musica.play()