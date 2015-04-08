import os
from mutagen.mp3 import MP3
from playlist import Playlist
from song import Song


class MusicCrawler:
    def __init__(self, path):
        self.path = path
        self.ext = '.mp3'

    def generate_playlist(self):
        playlist = Playlist('name')
        for root, dirname, files in os.walk(self.path):
            for name in files:
                if name.lower().endswith(self.ext):
                    meta = MP3(os.path.join(root, name))
                    artist = meta['TPE1']
                    title = str(meta['TIT2'])
                    album = meta['TALB']
                    length = meta.info.length
                    song = Song(title, artist, album,
                                self._prety_length(int(length)))
                    playlist.add_song(song)
        return playlist

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

if __name__ == '__main__':
    m = MusicCrawler('/home/nikpet/mp_test/')
    playlist = m.generate_playlist()
    playlist.save()
    print(playlist.load('name.json').name)
