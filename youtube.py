import yt_dlp

def video_indir(link, dosya_adi):
    ydl_opts = {
        'format': 'bv*+ba/best',
        'merge_output_format': 'mp4',
        'outtmpl': f'{dosya_adi}.mp4',  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

if __name__ == "__main__":
    link = input("YouTube video linkini girin: ").strip()
    dosya_adi = input("Kaydetmek istediğin dosya adını gir (uzantı yazma): ").strip()
    video_indir(link, dosya_adi)
