import os
import yt_dlp
from typing import Optional, Callable

def sanitize_url(url: str) -> str:
    if "&" in url:
        url = url.split("&")[0]
    return url

def progress_book_factory(callback):
    def hook(data):
        if data['status'] == 'downloading':
            total_bytes = data.get('total bytes') or data.get('total_bytes_estimate')
            downloaded = data.get('download_bytes', 0)

            if total_bytes:
                percent = downloaded / total_bytes * 100
                callback(round(percent, 2))
            elif data['status'] == 'finished':
                callback(100.0)
        return hook

def download_single_video(
    url: str,
    target_folder: str,
    progress_callback: Optional[Callable[[float], None]] = None
) -> str:
    """
    Downloads a single YouTube video as an MP3 in `target_folder`,
    using the YouTube title automatically. Calls progress_callback(percent)
    if provided. Returns the downloaded filepath or an empty string.
    """
    url = sanitize_url(url)

    ydl_opts = {
        'outtmpl': os.path.join(target_folder, '%(title)s.%(ext)s'),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [progress_hook_factory(progress_callback)] if progress_callback else [],
        'noplaylist': True
    }

    if os.name == 'nt':  # Windows only
        ydl_opts['ffmpeg_location'] = r'C:\Path\To\ffmpeg\bin'

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            requested = info.get('requested_downloads', [])
            if requested and len(requested) > 0:
                return requested[0].get('filepath', "")
            else:
                return ""
    except Exception as e:
        print(f"[ERROR] Downloader failed: {e}")
        return ""