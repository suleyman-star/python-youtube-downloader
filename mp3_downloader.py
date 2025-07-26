import os
import yt_dlp

playlist_url = input("YouTube Playlist URL'si: ")

output_dir = "indirilen_mp3ler"
os.makedirs(output_dir, exist_ok=True)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': False,
    'noplaylist': False, 
    'ignoreerrors': True
}

print("🎵 İndirme başlatılıyor...\n")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("\n✅ Tüm videolar başarıyla MP3 olarak indirildi!")