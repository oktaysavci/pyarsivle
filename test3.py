import subprocess
import requests

def is_m3u8_url_valid(url):
    try:
        r = requests.head(url, timeout=10, allow_redirects=True)
        content_type = r.headers.get("Content-Type", "")
        return "application/vnd.apple.mpegurl" in content_type or "application/x-mpegURL" in content_type
    except:
        return False

def download_video_from_m3u8():
    m3u8_url = input("M3U8 video linkini yapıştır: ").strip()

    if not is_m3u8_url_valid(m3u8_url):
        print("❌ Bu geçerli bir .m3u8 linki değil gibi görünüyor.")
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
