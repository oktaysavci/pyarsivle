import hashlib
import requests
import json
import os

# deneme 
email = input("📧 MediaFire e-posta adresinizi girin: ")
password = input("🔑 Şifrenizi girin: ")
file_path = input("📄 Yüklemek istediğiniz dosyanın yolunu girin: ")

app_id = "42511"  

# SHA1 hesaplama fonksiyonu
def sha1(data):
    return hashlib.sha1(data.encode()).hexdigest()

# 1. Oturum token al
def get_session_token(email, password):
    url = "https://www.mediafire.com/api/1.5/user/get_session_token.php"
    signature = sha1(email + password + app_id)
    payload = {
        "email": email,
        "password": password,
        "application_id": app_id,
        "signature": signature,
        "response_format": "json"
    }

    r = requests.post(url, data=payload)
    result = r.json()
    if result["response"]["result"] == "Success":
        return result["response"]["session_token"]
    else:
        print(f"❌ Hata: {result['response']['error_message']}")
        raise Exception("❌ Oturum alınamadı.")

# 2. Upload URL al
def get_upload_url(session_token):
    url = f"https://www.mediafire.com/api/1.5/upload/get_upload_url.php?session_token={session_token}&response_format=json"
    r = requests.get(url)
    result = r.json()

    print("📄 Upload URL Yanıtı:")
    print(json.dumps(result, indent=4))  # Yanıtı daha iyi görebilmek için formatlı yazdırıyoruz

    if result["response"]["result"] == "Success":
        return result["response"]["upload"]["upload_url"]
    else:
        print(f"❌ Hata: {result['response']['error_message']}")
        raise Exception("❌ Upload URL alınamadı.")

# 3. Dosya yükle
def upload_file(upload_url, file_path):
    file_name = os.path.basename(file_path)
    with open(file_path, "rb") as f:
        files = {"file": (file_name, f)}
        r = requests.post(upload_url, files=files)
        if r.status_code == 200:
            return r.text
        else:
            print(f"❌ Hata: {r.status_code} - {r.text}")
            raise Exception(f"❌ Yükleme başarısız: {r.status_code}")

# 4. Ana kontrol
try:
    print("🔐 Oturum açılıyor...")
    token = get_session_token(email, password)
    print("✅ Oturum alındı!")

    print("🔗 Upload linki alınıyor...")
    upload_url = get_upload_url(token)
    print(f"🟢 Upload URL: {upload_url}")

    print("📤 Dosya yükleniyor...")
    upload_response = upload_file(upload_url, file_path)
    print("✅ Dosya yüklendi!")
    print("🔎 MediaFire yanıtı:")
    print(upload_response)

    # quickkey bul ve link oluştur
    if "quickkey" in upload_response:
        start = upload_response.find("<quickkey>") + 10
        end = upload_response.find("</quickkey>")
        quickkey = upload_response[start:end]
        link = f"https://www.mediafire.com/file/{quickkey}"
        print(f"🔗 İndirilebilir link: {link}")
    else:
        print("⚠️ quickkey bulunamadı. Yanıtı kontrol edin.")

except Exception as e:
    print("❌ Hata:", e)
            
