import datetime


class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.volt = []
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle

    def add_song(self, song):
        self.volt.append(song)

    def remove_song(self, song):
        self.volt.remove(song)
