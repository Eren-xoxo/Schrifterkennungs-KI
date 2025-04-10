import os

def rename_files(folder_path, prefix="Akman"):
    # Alle Dateien im Ordner auflisten und numerisch sortieren
    files = sorted([f for f in os.listdir(folder_path) if f.startswith("letter") and f.endswith(".png")],
                   key=lambda x: int(x.replace("letter", "").replace(".png", "")))
    
    # Definiere die Buchstaben in Gruppen von 8 Dateien
    letters = "ABCDEFGHIJKLM"  # Es gibt 128 Dateien, also 16 Buchstaben à 8 Dateien
    
    # Umbenennen der Dateien
    for index, old_name in enumerate(files):
        letter = letters[index // 8]  # Alle 8 Dateien bekommen den gleichen Buchstaben
        new_name = f"{prefix}{letter}{(index % 8) + 1}.png"
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")

if __name__ == "__main__":
    folder_path = r"C:\Users\Lenovo\Desktop\schule\OneDrive - HTL Anichstrasse\WPG_KISY\4 Klasse\Korber\4 Klasse\4. Neuronal Networks\Schrifterkennungs-KI\letters"
    if os.path.exists(folder_path):
        rename_files(folder_path)
    else:
        print("Der angegebene Ordner existiert nicht.")