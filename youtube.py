from pytube import YouTube

def video_indir(link):
    try:
        yt = YouTube(link)
        print(f"Video başlığı: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        print("İndiriliyor...")
        stream.download()
        print("İndirme tamamlandı.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    link = input("İndirmek istediğiniz YouTube video linkini girin: ")
    video_indir(link)
  
