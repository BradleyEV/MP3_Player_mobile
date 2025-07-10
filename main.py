from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from downloader import download_single_video
import os

class DownloaderLayout(BoxLayout):
    def download(self, instance=None):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            print("✅ DownloaderLayout initialized")
        url = self.ids.url_input.text.strip()
        if url:
            self.ids.status_label.text = "Downloading..."
            output = download_single_video(
                url,
                target_folder=os.path.join(os.getcwd(), "downloads")
            )
            if output:
                self.ids.status_label.text = f"Downloaded to:\n{output}"
            else:
                self.ids.status_label.text = "Failed to download."
        else:
            self.ids.status_label.text = "Please enter a URL."


class YouTubeDownloaderApp(App):
    def build(self):
        Builder.load_file("youtube_downloader.kv")  # Force-load KV
        return DownloaderLayout()

if __name__ == '__main__':
    YouTubeDownloaderApp().run()
