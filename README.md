# 🎵 YouTube Playlist MP3 Downloader

Bu Python betiği, bir **YouTube çalma listesindeki tüm videoları MP3 formatında** indirmenizi sağlar. `yt-dlp` ve `ffmpeg` araçlarını kullanarak en kaliteli ses dosyalarını elde eder.

## 🚀 Özellikler

- YouTube çalma listesinden MP3 indirme
- Her video için başlığa göre isimlendirme
- 192 kbps kalitesinde ses dönüştürme
- Hatalı videoları atlayarak indirime devam etme
- Otomatik `indirilen_mp3ler` klasörüne kayıt

## 🔧 Gereksinimler

- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/download.html)

### Kurulum

Terminal veya komut satırında aşağıdaki komutları çalıştırarak bağımlılıkları yükleyin:

```bash
pip install yt-dlp
```

**FFmpeg** sisteminize kurulu olmalıdır:

- **Windows:** [FFmpeg indir](https://www.gyan.dev/ffmpeg/builds/)
- **macOS (Homebrew):**

```bash
brew install ffmpeg
```

- **Linux (Debian/Ubuntu):**

```bash
sudo apt install ffmpeg
```

## 🧪 Kullanım

1. Terminali açın.
2. Betiği çalıştırın:

```bash
python mp3_downloader.py
```

3. Sizden istenecek olan YouTube playlist bağlantısını girin.
4. Tüm videolar `indirilen_mp3ler` klasörüne MP3 olarak kaydedilecektir.

## 📁 Klasör Yapısı

```
proje_klasörü/
├── mp3_downloader.py
└── indirilen_mp3ler/
    ├── video1.mp3
    ├── video2.mp3
    └── ...
```

## ⚠️ Notlar

- Playlist'teki telifli veya bölgenizde engellenmiş videolar indirilemeyebilir.
- Playlist'teki bozuk linkler veya silinmiş videolar atlanır (`ignoreerrors=True`).

## 📝 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.
