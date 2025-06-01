import subprocess

def download_video_from_m3u8():
    m3u8_url = input("M3U8 video linkini yapıştır: ").strip()
    
    if not m3u8_url.endswith(".m3u8"):
        print("Bu link geçerli bir .m3u8 bağlantısı değil. Siktir et, düzgün link ver.")
        return

    output_file = "output.mp4"

    ffmpeg_command = [
        "ffmpeg",
        "-i", m3u8_url,
        "-c", "copy",
        "-bsf:a", "aac_adtstoasc",
        output_file
    ]

    print(f"\n🚀 İndirme başlıyor...\nLink: {m3u8_url}\nÇıktı: {output_file}\n")

    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"\n✅ İşlem tamam. '{output_file}' oluşturuldu.\n")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ ffmpeg başarısız oldu. Komut çöktü:\n{e}\n")
    except FileNotFoundError:
        print("\n❌ ffmpeg bulunamadı. Terminalde şunu çalıştır:\nsudo apt install ffmpeg\n")

if __name__ == "__main__":
    download_video_from_m3u8()
