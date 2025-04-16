from pytube import YouTube
import traceback

def video_indir(link):
    try:
        yt = YouTube(link)
        print(f"Video başlığı: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        print("İndiriliyor...")
        stream.download()
        print("İndirme tamamlandı.")
    except Exception as e:
        print("Bir hata oluştu:")
        traceback.print_exc()

if __name__ == "__main__":
    link = input("YouTube video linkini girin: ").strip()
    video_indir(link)
