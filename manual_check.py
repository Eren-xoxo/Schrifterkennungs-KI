import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Modell und Daten laden
model = tf.keras.models.load_model("mein_tf_model.h5")
x_test = np.load("images.npy")
y_test = np.load("labels.npy").flatten()

# Zufällig 10% für Testdaten nehmen (wie beim Training)
from sklearn.model_selection import train_test_split
_, x_test, _, y_test = train_test_split(x_test, y_test, test_size=0.1, random_state=42)

# Vorhersagen berechnen
predictions = model.predict(x_test)
predicted_labels = np.argmax(predictions, axis=1)

# Funktion zur Umwandlung von Index in Buchstabe
def label_to_char(index):
    return chr(65 + index)  # 0 -> A, 1 -> B, ..., 25 -> Z

# 10 zufällige Vorhersagen anzeigen
for i in range(10):
    idx = random.randint(0, len(x_test) - 1)
    image = x_test[idx]
    true_label = y_test[idx]
    pred_label = predicted_labels[idx]

    plt.imshow(image, cmap='gray')
    plt.title(f"Vorhersage: {label_to_char(pred_label)} | Richtig: {label_to_char(true_label)}")
    plt.axis('off')
    plt.show()

# Konfusionsmatrix anzeigen
cm = confusion_matrix(y_test, predicted_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[chr(i) for i in range(65, 91)])
disp.plot(cmap='Blues')
plt.title("Konfusionsmatrix")
plt.show()