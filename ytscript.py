import yt_dlp
import os
import re
from datetime import datetime

def temizle_baslik(baslik):
    baslik = re.sub(r'#\w+', '', baslik)           
    baslik = baslik.replace(" ", "")               
    baslik = re.sub(r'[^\w\-]', '', baslik)       
    return baslik

def indir_link(link):
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(link, download=False)
            tarih = datetime.strptime(info['upload_date'], "%Y%m%d").strftime("%Y%m%d")
            baslik = temizle_baslik(info['title'])
            dosya_adi = f"{tarih}_{baslik}.mp4"

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': dosya_adi,
            'quiet': False
        }

        print(f"\n📥 İndiriliyor: {info['title']}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"✅ Kaydedildi: {dosya_adi}\n")
    except Exception as e:
        print(f"⚠️ Hata oluştu: {e}")

def indir_playlist(playlist_link):
    indir_link(playlist_link)

def indir_dosya(dosya_adı="linkler.txt"):
    try:
        with open(dosya_adı, "r", encoding="utf-8") as f:
            linkler = [satır.strip() for satır in f if satır.strip()]
        for link in linkler:
            indir_link(link)
    except FileNotFoundError:
        print(f"❌ {dosya_adı} bulunamadı.")

def menu():
    print("🎬 YouTube Video İndirici")
    print("1. Tek Video Linki")
    print("2. Playlist Linki")
    print("3. linkler.txt Dosyasından İndir")
    secim = input("Seçiminizi yapın (1/2/3): ")

    if secim == "1":
        link = input("🎯 Video linkini girin: ")
        indir_link(link)
    elif secim == "2":
        playlist_link = input("🎯 Playlist linkini girin: ")
        indir_playlist(playlist_link)
    elif secim == "3":
        indir_dosya()
    else:
        print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    menu()
                                
