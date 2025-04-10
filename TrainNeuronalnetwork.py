import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random


# 1. Daten laden
images = np.load("images.npy")           # Form: (194, 28, 28)
labels = np.load("labels.npy")           # Form: (194, 1)

# 2. Normalisieren und Labels vorbereiten
#images = images / 255.0                  # Werte von 0–1
labels = labels.astype('int32').flatten()  # Form: (194,)

# 3. Trainings-/Testdaten aufteilen (90% / 10%)
x_train, x_test, y_train, y_test = train_test_split(
    images, labels, test_size=0.1, random_state=42)

#labels bilder testen
for i in range(5):
    idx = random.randint(0, len(x_train) - 1)
    plt.imshow(x_train[idx], cmap='gray')
    plt.title(f"Label: {y_train[idx]}")  # Label anzeigen
    plt.axis('off')
    plt.show()
#########################

# 4. Feedforward-Netzwerk definieren
model = Sequential([
    Flatten(input_shape=(28, 28)),     # 784 Inputs
    Dense(128, activation='relu'),    # Hidden Layer 1
    Dense(64, activation='relu'),     # Hidden Layer 2
    Dense(26, activation='softmax')   # 26 Klassen (A–Z)
])

# 5. Kompilieren
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 6. Trainieren
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# 7. Testen
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"\n Test Accuracy: {test_acc * 100:.2f}%")

# 8. Modell speichern
model.save("mein_tf_model.h5")
print("Modell gespeichert als 'mein_tf_model.h5'")
