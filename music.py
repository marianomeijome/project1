import webbrowser

class Music():
    def __init__(self, song_title, song_artist, song_image, music_video):
        self.title = song_title
        self.artist = song_artist
        self.cover_art_url = song_image
        self.music_video_url = music_video

    def show_music_video(self):
        webbrowser.open(self.music_video_url)
