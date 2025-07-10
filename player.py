from ffpyplayer import MediaPlayer

class MP3Player:
    def __init__(self):
        self.player = None
        self.is_playing = False

    def play_mp3(self, file_path: str):
        try:
            if self.is_playing:
                self.stop()

            self.player = MediaPlayer(file_path)
            self.is_playing = True
            print(f"Playing: {file_path}")

        except Exception as e:
            print(f"Error playing file: {file_path}: {e}")

    def stop(self):
        if self.player:
            self.player.toggle_pause()
            self.player = None
            self.is_playing = False
            print("Playback stopped")

    def pause(self):
        if self.player and self.is_playing:
            self.player.toggle_pause()
            print("Playback paused")

    def resume(self):
        if self.player and not self.is_playing:
            self.player.toggle_pause()
            print("Playback Resumed")