import unittest
import datetime
from song import Song


class SongTest(unittest.TestCase):
    def setUp(self):
        self.title = "title"
        self.artist = "artist"
        self.album = "album"
        self.song_length = 4830
        self.song2_length = 1230
        self.song3_length = 30
        self.song = Song(self.title, self.artist, self.album, "1:20:30")
        self.song2 = Song(self.title, self.artist, self.album, "20:30")
        self.song3 = Song(self.title, self.artist, self.album, "30")

    def test_init(self):
        self.assertEqual(self.song.title, 'title')
        self.assertEqual(self.song.artist, 'artist')
        self.assertEqual(self.song.album, 'album')
        self.assertEqual(self.song.song_length, 4830)

    def test_str(self):
        formated_length = str(datetime.timedelta(seconds=4830))
        song_string = "{} - {} from {} - {}".format(self.title, self.artist,
                                                    self.album, formated_length)
        self.assertEqual(str(self.song), song_string)

    def test_eq(self):
        song2 = Song(self.title, self.artist, self.album, "1:20:30")
        self.assertTrue(self.song == song2)

    def test_hash(self):
        self.assertEqual(hash(self.song), hash((self.title, self.artist,
                                               self.album, self.song_length)))

    def test_len(self):
        formated_length = str(datetime.timedelta(seconds=4830))
        self.assertEqual(self.song.length(), formated_length)
        self.assertEqual(self.song.length(seconds=True), self.song_length)
        self.assertEqual(self.song.length(minutes=True), self.song_length // 60)
        self.assertEqual(self.song.length(hours=True), self.song_length // 3600)
        self.assertEqual(self.song2.length(seconds=True), self.song2_length)
        self.assertEqual(self.song2.length(minutes=True), self.song2_length // 60)
        self.assertEqual(self.song2.length(hours=True), self.song2_length // 3600)
        self.assertEqual(self.song3.length(seconds=True), self.song3_length)
        self.assertEqual(self.song3.length(minutes=True), self.song3_length // 60)
        self.assertEqual(self.song3.length(hours=True), self.song3_length // 3600)


if __name__ == '__main__':
    unittest.main()
