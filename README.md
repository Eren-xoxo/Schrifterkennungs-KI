# 📘 Schrifterkennungs-KI

Dieses Projekt nutzt künstliche Intelligenz, um handgeschriebene **Blockbuchstaben** (A–Z) zu erkennen. Die Benutzer*innen können Buchstaben zeichnen, die dann durch ein trainiertes neuronales Netz erkannt werden. Es basiert auf `TensorFlow`, `OpenCV` und `tkinter`.

---

## 📁 Projektstruktur

```
📦 Schrifterkennungs-KI
├── a4_raster_Eren_Akman.zip        # Meine Raster-Bilder
├── Blockbuchstaben.jpeg            # Ausgeschnittener Eingescannter Buchstabenraster
├── Buchstaben_extrahieren.py       # Extrahiert einzelne Buchstaben aus dem Rasterbild
├── Buchstabenunbenner.py           # Benennt extrahierte Buchstaben automatisch um
├── prepare_data.py                 # Wandelt Bilder in NumPy-Daten um
├── TrainNeuronalnetwork.py         # Trainingsskript mit TensorFlow
├── manual_check.py                 # Überprüfung + Konfusionsmatrix
├── save_model.py                   # Speichert Modell als .keras und .h5
├── Letter_Gui.py                   # GUI mit Zeichnen + Musikfunktion
├── requirements.txt                # Abhängigkeiten
├── musik.mp3                       # "harmlose" Audiodatei 😉
├── images.npy / labels.npy         # Trainingsdaten als NumPy-Dateien
├── *.h5 / *.keras                  # Trainierte Modelle
├── letters/ oder BigDataSet/       # Enthält die gelabelten Buchstabenbilder
├── screenshots/                    # Screenshot der GUI (optional)
└── README.md
```

---

## 🧠 Schritt-für-Schritt-Anleitung

### 1️⃣ Datensatz generieren
- Blockbuchstaben auf dem A4 Rasterblatt eintragen (`A4_raster.png`)
- Einscannen und zuschneiden
- Automatisiertes Ausschneiden per `Buchstaben_extrahieren.py`

### 2️⃣ Labeln
- `Buchstabenunbenner.py` nutzen, um Dateien sinnvoll zu benennen (z. B. "AkmanA1.png")
- Alle Bilder in Buchstaben-Ordner sortieren (`dataset/A`, `dataset/B`, …)

### 3️⃣ Daten vorbereiten

```bash
python prepare_data.py
```

- Bilder werden auf 28×28 Pixel skaliert, normalisiert (invertiert), als `images.npy` und `labels.npy` gespeichert

### 4️⃣ Modell trainieren

```bash
python TrainNeuronalnetwork.py
```

- Erstellt ein Feedforward-Netzwerk
- Trainings-/Testsplit 90/10
- Modell wird gespeichert als `mein_tf_model.h5`

### 5️⃣ Modell überprüfen

```bash
python manual_check.py
```

- Zufällige Bilder mit Vorhersage anzeigen
- Konfusionsmatrix wird geplottet

### 6️⃣ Modell exportieren

```bash
python save_model.py
```

- Speichert das Modell als `.keras` und `.h5`

### 7️⃣ GUI starten

```bash
python Letter_Gui.py
```

- Eigene Buchstaben zeichnen
- Vorhersage + Wahrscheinlichkeit als Balkendiagramm
- Bonus: "🎵 Musik abspielen" mit netter Überraschung 😄

---

## 🖼️ Screenshot der GUI

![GUI Screenshot](https://github.com/eren-xoxo/Schrifterkennungs-KI/blob/main/screenshots/Bild1.png)

---

## 🧰 Benötigte Bibliotheken

```bash
pip install tensorflow opencv-python numpy matplotlib pillow pygame
```

Oder alternativ:

```bash
pip install -r requirements.txt
```

---

## 💡 Hinweis

Dieses Projekt wurde im Rahmen des Unterrichts erstellt und kann als Basis für weiterführende Handschriftenerkennung, OCR oder AI-GUIs verwendet werden.

---

## 👤 Autor

Projekt von [Eren Akman] im Rahmen des KI-WPGs an der HTL Anichstraße ✨

---


