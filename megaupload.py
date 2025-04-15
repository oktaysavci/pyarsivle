from mega import Mega
import getpass
import os

def main():
    print("=== Mega.nz Dosya Yükleyici ===\n")

    email = input("Email adresinizi girin: ")
    password = getpass.getpass("Şifrenizi girin (gizli): ")

    print("\nGiriş yapılıyor...")
    mega = Mega()
    try:
        m = mega.login(email, password)
        print("✅ Giriş başarılı!\n")
    except Exception as e:
        print(f"❌ Giriş başarısız: {e}")
        return

    dosya_yolu = input("Yüklenecek dosyanın tam yolunu girin: ")

    if not os.path.isfile(dosya_yolu):
        print("❌ Dosya bulunamadı! Lütfen geçerli bir dosya yolu girin.")
        return

    print("⏫ Dosya yükleniyor...")
    try:
        yuklenen = m.upload(dosya_yolu)
        link = m.get_upload_link(yuklenen)
        print(f"\n✅ Yükleme tamamlandı!\n🔗 Dosya bağlantısı: {link}")
    except Exception as e:
        print(f"❌ Yükleme sırasında hata oluştu: {e}")

if __name__ == "__main__":
    main()
    