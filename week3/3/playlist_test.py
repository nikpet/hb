import unittest
from playlist import Playlist
from song import Song


class PlaylistTest(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist('name')
        self.repeat_playlist = Playlist('name', repeat=True)
        self.shuffle_playlist = Playlist('name', shuffle=True)
        self.song_a1_1 = Song('title1', 'artist1', 'album1', '1:00')
        self.song_a1_2 = Song('title2', 'artist1', 'album1', '1:00')
        self.song_a1_3 = Song('title3', 'artist1', 'album1', '1:00')
        self.song_a2_2 = Song('title2', 'artist2', 'album2', '2:00')
        self.song_a3_3 = Song('title3', 'artist3', 'album3', '3:00')

    def test_init(self):
        self.assertEqual(self.playlist.volt, [])
        self.assertEqual(self.playlist.name, 'name')
        self.assertFalse(self.playlist.repeat)
        self.assertFalse(self.playlist.shuffle)
        self.assertTrue(self.repeat_playlist.repeat)
        self.assertFalse(self.repeat_playlist.shuffle)
        self.assertFalse(self.shuffle_playlist.repeat)
        self.assertTrue(self.shuffle_playlist.shuffle)

    def test_add_song(self):
        self.playlist.add_song(self.song_a1_1)
        self.assertIn(self.song_a1_1, self.playlist.volt)

    def test_remove_song(self):
        self.playlist.add_song(self.song_a1_1)
        self.playlist.remove_song(self.song_a1_1)
        self.assertNotIn(self.song_a1_1, self.playlist.volt)

    def test_total_length(self):
        self.playlist.add_song(self.song_a1_1)
        self.playlist.add_song(self.song_a1_2)
        self.playlist.add_song(self.song_a1_3)
        self.assertEqual(self.playlist.total_length(), '3:00')


if __name__ == '__main__':
    unittest.main()
