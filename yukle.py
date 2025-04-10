import requests

# Flask uygulamanın upload endpoint'i
url = 'https://savci19.pythonanywhere.com/upload'

# Kullanıcıdan dosya yolunu al
file_path = input("Yüklemek istediğiniz dosyanın yolunu girin: ")

try:
    # Dosyayı aç ve POST isteği ile yükle
    with open(file_path, 'rb') as file:
        files = {'file': (file_path, file)}
        response = requests.post(url, files=files)

    # Sunucudan gelen yanıtı kontrol et
    if response.status_code == 200:
        print(f'✅ Dosya başarıyla yüklendi! Yüklenen dosya: {response.text}')
    else:
        print(f'❌ Hata oluştu: {response.text}')

except FileNotFoundError:
    print(f"❌ {file_path} dosyası bulunamadı!")
except Exception as e:
    print(f"❌ Beklenmeyen bir hata oluştu: {e}")
