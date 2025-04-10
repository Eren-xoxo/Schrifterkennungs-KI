# 📘 Schrifterkennungs-KI

Dieses Projekt nutzt künstliche Intelligenz, um handgeschriebene **Blockbuchstaben** (A–Z) zu erkennen. Die Benutzer*innen können Buchstaben zeichnen, die dann durch ein trainiertes neuronales Netz erkannt werden. Es basiert auf `TensorFlow`, `OpenCV` und `tkinter`.

---

## 📁 Projektstruktur

```
📦 Schrifterkennungs-KI
├── dataset/                  # Trainingsdaten (Buchstabenbilder A–Z)
├── model/                    # Das trainierte Modell (.h5, .keras)
├── screenshots/              # GUI-Screenshots
├── gui/                      # Benutzeroberfläche (tkinter)
│   └── Letter_Gui.py
├── tools/                    # Hilfsprogramme
│   ├── Buchstabenunbenner.py
│   ├── prepare_data.py
│   ├── TrainNeuronalnetwork.py
│   └── manual_check.py
├── musik.mp3                 # Überraschung 😉
├── requirements.txt          # Benötigte Pakete
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

![GUI Screenshot](screenshots/gui_screenshot.png)

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


