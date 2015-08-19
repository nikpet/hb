from random import shuffle
from tabulate import tabulate
import json


class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.volt = []
        self.play_list = []
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle

    def add_song(self, song):
        self.volt.append(song)

    def remove_song(self, song):
        self.volt.remove(song)

    def add_songs(self, song_list):
        self.volt += song_list
        # for song in song_list:
        #     self.add_song(song)

    def total_length(self):
        total_length = 0
        for song in self.volt:
            total_length += song.length(seconds=True)
        return self._prety_length(total_length)

    def _prety_length(self, seconds):
        hours = seconds // 3600
        minutes = seconds // 60 % 60
        seconds = seconds % 60 % 60
        if hours:
            return '{}:{:0>2d}:{:0>2d}'.format(hours, minutes, seconds)
        elif minutes:
            return '{}:{:0>2d}'.format(minutes, seconds)
        else:
            return '{}'.format(seconds)

    def artists(self):
        artists_histogram = {}
        for song in self.volt:
            if song.artist not in artists_histogram:
                artists_histogram[song.artist] = 1
            else:
                artists_histogram[song.artist] += 1
        return artists_histogram

    def next_song(self):
        if self.play_list == []:
            self.play_list = self.volt[:]
            if self.shuffle:
                shuffle(self.play_list)
        next_song = self.play_list.pop(0)
        if self.repeat:
            self.play_list.append(next_song)
        return next_song

    def pprint_playlist(self):
        print(tabulate([[x.artist, x.title, x.length()] for x in self.volt],
                       headers=['Artist', 'Song', 'Length'], tablefmt="grid"))

    def save(self):
        f = open(self.name.replace(' ', '-') + '.json', 'w')
        json.dump({'repeat': self.repeat, 'shuffle': self.shuffle,
                   'volt': [repr(x) for x in self.volt]}, f)
        f.close()

    @staticmethod
    def load(path):
        f = open(path)
        playlist_data = json.load(f)
        f.close()
        name = path.replace('-', ' ')
        if name.endswith('.json'):
            name = name[:-5]
        playlist = Playlist(name, playlist_data['repeat'],
                            playlist_data['shuffle'])
        songs = [eval(x) for x in playlist_data['volt']]
        playlist.add_songs(songs)
        return playlist

if __name__ == '__main__':
    pass
    # print(Playlist.load('name.json'))
