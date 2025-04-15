import subprocess

email = input("Email: ")
password = input("Şifre: ")
dosya_yolu = input("Yüklenecek dosya yolu: ")

# Giriş
subprocess.run(["mega-login", email, password])

# Dosya yükleme
subprocess.run(["mega-put", dosya_yolu, "/"])
