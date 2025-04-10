import requests

# Kullanıcıdan gerekli bilgileri al
session_cookie = input("🟡 MediaFire session_id (user_session_token) değerini girin: ")
file_path = input("📄 Yüklemek istediğiniz dosyanın yolunu girin: ")

headers = {
    'Cookie': f'user_session_token={session_cookie}',
    'User-Agent': 'Mozilla/5.0'
}

upload_url = 'https://www.mediafire.com/basicapi/uploader.php?simple=1'

try:
    with open(file_path, 'rb') as f:
        files = {'file': (file_path.split("/")[-1], f)}
        print("⏳ Dosya yükleniyor...")
        response = requests.post(upload_url, headers=headers, files=files)
        
        if response.ok:
            print("✅ Yükleme tamamlandı!")
            print("🔗 MediaFire yanıtı:")
            print(response.text)
        else:
            print("❌ Yükleme başarısız:", response.status_code)
            print(response.text)

except FileNotFoundError:
    print("❌ Dosya bulunamadı.")
except Exception as e:
    print("❌ Hata oluştu:", e)
  
