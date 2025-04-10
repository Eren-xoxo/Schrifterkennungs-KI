import tensorflow as tf

# Name des neuen Modells als Variable
ausgabe_dateiname = "buchstaben_klassifizierer"

# Modell laden (zuvor trainiert und gespeichert)
model = tf.keras.models.load_model("mein_tf_model.h5")

# Modell als Keras-Datei speichern
model.save(f"{ausgabe_dateiname}.keras")
print(f"Modell wurde als '{ausgabe_dateiname}.keras' gespeichert.")

