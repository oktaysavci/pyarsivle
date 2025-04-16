import yt_dlp

def video_indir(link):
    ydl_opts = {
        'format': 'bv*+ba/best',  
        'merge_output_format': 'mp4',  
        'outtmpl': '%(title)s.%(ext)s',  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

if __name__ == "__main__":
    link = input("YouTube video linkini girin: ").strip()
    video_indir(link)
