import os
import cv2
import numpy as np

# Parameter
DATASET_PATH = r"C:\Users\Lenovo\Desktop\schule\OneDrive - HTL Anichstrasse\WPG_KISY\4 Klasse\Korber\4 Klasse\4. Neuronal Networks\Schrifterkennungs-KI\BigDataSet"
IMG_SIZE = 28
OUTPUT_IMAGES = "images.npy"
OUTPUT_LABELS = "labels.npy"

# Existiert der Ordner?
if not os.path.exists(DATASET_PATH):
    raise FileNotFoundError(f"Der Pfad '{DATASET_PATH}' existiert nicht!")

# Initialisiere Listen
images = []
labels = []

# Durchlaufe alle Unterordner (A-Z)
for letter_folder in os.listdir(DATASET_PATH):
    folder_path = os.path.join(DATASET_PATH, letter_folder)

    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path) and filename.lower().endswith((".png", ".jpg", ".jpeg")):
                image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

                if image is None:
                    print(f"Warnung: '{filename}' konnte nicht geladen werden.")
                    continue

                if image.shape != (IMG_SIZE, IMG_SIZE):
                    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

                normalized_img = 1-image / 255.0
                images.append(normalized_img)
                labels.append(letter_folder)

# Fehler, falls nichts geladen wurde
if not images:
    raise RuntimeError("Keine validen Bilder gefunden!")

# In NumPy-Arrays umwandeln
images_array = np.array(images, dtype=np.float32)
label_mapping = {chr(65 + i): i for i in range(26)}  # A-Z → 0-25
labels_array = np.array([label_mapping[label] for label in labels], dtype=np.int32).reshape(-1, 1)

# Speichern
np.save(OUTPUT_IMAGES, images_array)
np.save(OUTPUT_LABELS, labels_array)

print(f"Gespeichert: {OUTPUT_IMAGES} ({images_array.shape}), {OUTPUT_LABELS} ({labels_array.shape})")
