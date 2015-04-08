class Song:
    def __init__(self, title, artist, album, length):
        self.title = title.replace("'", "")
        self.artist = artist
        self.album = album
        self.song_length = 0
        self.original_length = length
        length_parts = length.split(':')
        time_part = 0
        for part in reversed(length_parts):
            self.song_length += (60 ** time_part) * int(part)
            time_part += 1
        # print(self.length)

    def __str__(self):
        formated_length = self._prety_length()
        return "{} - {} from {} - {}".format(self.title, self.artist,
                                             self.album, formated_length)

    def __repr__(self):
        return "Song('{}', '{}', '{}', '{}')".format(self.title, self.artist,
                                                     self.album, self.original_length)

    def __eq__(self, other):
        return (self.title == other.title and self.artist == other.artist
                and self.album == other.album
                and self.song_length == other.song_length)

    def __hash__(self):
        return hash((self.title, self.artist, self.album, self.song_length))

    def length(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return self.song_length
        if minutes:
            return self.song_length // 60
        if hours:
            return self.song_length // 3600
        return self._prety_length()

    def _prety_length(self):
        hours = self.length(hours=True)
        minutes = self.length(minutes=True) % 60
        seconds = self.length(seconds=True) % 60 % 60
        if hours:
            return '{}:{:0>2d}:{:0>2d}'.format(hours, minutes, seconds)
        elif minutes:
            return '{}:{:0>2d}'.format(minutes, seconds)
        else:
            return '{}'.format(seconds)


if __name__ == '__main__':
    s = Song('asdf', 'ad', 'asdf', '30')
    print(s.length(minutes=True))
