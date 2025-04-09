import zipfile
import os

def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, arcname)

folder_path = input("Arşivlemek istediğiniz klasörün yolunu girin: ").strip()
output_path = input("Oluşturulacak .zip dosyasının adını (örnek: arsivim.zip) girin: ").strip()

if os.path.isdir(folder_path):
    zip_folder(folder_path, output_path)
    print(f"✅ '{folder_path}' klasörü başarıyla '{output_path}' olarak arşivlendi.")
else:
    print(f"❌ Hata: '{folder_path}' geçerli bir klasör değil.")
