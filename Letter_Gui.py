import tkinter as tk
from tkinter import Canvas, Label, Button, Frame
import numpy as np
import tensorflow as tf
import cv2
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pygame  # Für Musik

# Modell laden
model = tf.keras.models.load_model("buchstaben_klassifizierer.keras")

# Musik initialisieren
pygame.mixer.init()
MUSIK_DATEI = "musik.mp3"  # unverdächtiger Name

CANVAS_SIZE = 280
IMG_SIZE = 28

class LetterApp:
    def __init__(self, root):
        self.root = root
        root.title("🧠 Buchstaben-KI")
        root.configure(bg='#f0f0f0')

        self.title_label = Label(root, text="🅰️ Buchstaben-Erkennung", font=("Helvetica", 18, "bold"), bg='#f0f0f0')
        self.title_label.pack(pady=5)

        self.author_label = Label(root, text="Eren Akman – 4AHEL", font=("Helvetica", 11, "bold"), bg='#f0f0f0')
        self.author_label.pack(pady=0)

        self.main_frame = Frame(root, bg='#f0f0f0')
        self.main_frame.pack(pady=5)

        self.canvas = Canvas(self.main_frame, width=CANVAS_SIZE, height=CANVAS_SIZE, bg='white', highlightthickness=2, highlightbackground='black')
        self.canvas.grid(row=0, column=0, rowspan=7, padx=10)

        self.preview_label = Label(self.main_frame, text="Vorschau", font=("Helvetica", 12), bg='#f0f0f0')
        self.preview_label.grid(row=0, column=1, pady=5)

        self.preview_canvas = Canvas(self.main_frame, width=IMG_SIZE*4, height=IMG_SIZE*4, bg='white', highlightthickness=1)
        self.preview_canvas.grid(row=1, column=1)

        self.read_button = Button(self.main_frame, text="🔍 Vorhersagen", command=self.predict_letter, bg='#4caf50', fg='white', font=("Helvetica", 12))
        self.read_button.grid(row=2, column=1, pady=5)

        self.clear_button = Button(self.main_frame, text="🗑️ Löschen", command=self.clear_canvas, bg='#f44336', fg='white', font=("Helvetica", 12))
        self.clear_button.grid(row=3, column=1, pady=5)

        self.music_button = Button(self.main_frame, text="🎵 Musik abspielen", command=self.spiele_musik, bg='#2196f3', fg='white', font=("Helvetica", 12))
        self.music_button.grid(row=4, column=1, pady=5)

        self.prediction_label = Label(self.main_frame, text="", font=("Helvetica", 16, "bold"), bg='#f0f0f0')
        self.prediction_label.grid(row=5, column=1, pady=5)

        self.detail_label = Label(self.main_frame, text="", font=("Helvetica", 10), bg='#f0f0f0')
        self.detail_label.grid(row=6, column=1, pady=5)

        self.graph_frame = Frame(root, bg='#f0f0f0')
        self.graph_frame.pack(pady=10)

        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<Button-1>", self.start_draw)

        self.image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), color=255)

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(self.last_x, self.last_y, x, y, fill="black", width=20, capstyle=tk.ROUND, smooth=tk.TRUE)
        draw_img = self.image.load()
        for i in range(-10, 11):
            for j in range(-10, 11):
                if 0 <= x + i < CANVAS_SIZE and 0 <= y + j < CANVAS_SIZE:
                    draw_img[x + i, y + j] = 0
        self.last_x, self.last_y = x, y

    def clear_canvas(self):
        self.canvas.delete("all")
        self.preview_canvas.delete("all")
        self.prediction_label.config(text="")
        self.detail_label.config(text="")
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        self.image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), color=255)

    def predict_letter(self):
        img_array = np.array(self.image)
        img_resized = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        img_normalized = 1 - (img_resized / 255.0)
        img_input = img_normalized.reshape(1, IMG_SIZE, IMG_SIZE)

        prediction = model.predict(img_input)
        predicted_index = np.argmax(prediction)
        confidence = np.max(prediction) * 100
        predicted_letter = chr(65 + predicted_index)

        self.prediction_label.config(
            text=f"➡️ Vorhersage: {predicted_letter} ({confidence:.1f}%)"
        )

        bar_text = "\n".join([
            f"{chr(65+i)}: {round(p*100, 1)}%" for i, p in enumerate(prediction[0]) if p > 0.01
        ])
        self.detail_label.config(text=bar_text)

        self.preview_canvas.delete("all")
        img_scaled = Image.fromarray((img_normalized * 255).astype(np.uint8))
        img_scaled = img_scaled.resize((IMG_SIZE*4, IMG_SIZE*4), Image.NEAREST)
        self.tk_preview = ImageTk.PhotoImage(img_scaled)
        self.preview_canvas.create_image(0, 0, anchor="nw", image=self.tk_preview)

        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(7, 2))
        letters = [chr(i + 65) for i in range(26)]
        ax.bar(letters, prediction[0], color="#4caf50")
        ax.set_ylim(0, 1)
        ax.set_ylabel("Wahrscheinlichkeit")
        ax.set_title("Vorhersage-Wahrscheinlichkeiten")
        fig.tight_layout()

        chart = FigureCanvasTkAgg(fig, self.graph_frame)
        chart.get_tk_widget().pack()
        chart.draw()

    def spiele_musik(self):
        try:
            pygame.mixer.music.load(MUSIK_DATEI)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Fehler beim Abspielen: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    app = LetterApp(root)
    root.mainloop()
