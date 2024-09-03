import numpy as np
import librosa
import tensorflow as tf
from tensorflow.keras.models import load_model

GENRES = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

def preprocess_audio(file_path):
    y, sr = librosa.load(file_path, sr=44100)

    # Convert audio to chunks and spectrogram
    def extract_chunks(y, sr):
        chunk_duration = 4
        overlap_duration = 2
        chunk_samples = chunk_duration * sr
        overlap_samples = overlap_duration * sr
        num_chunks = int(np.ceil((len(y) - chunk_samples) / (chunk_samples - overlap_samples))) + 1
        chunks = []
        for i in range(num_chunks):
            start = i * (chunk_samples - overlap_samples)
            end = start + chunk_samples
            chunk = y[start:end]
            if len(chunk) < chunk_samples:  # In case the chunk is smaller than expected
                chunk = np.pad(chunk, (0, chunk_samples - len(chunk)), mode='constant')
            mel_spectrogram = librosa.feature.melspectrogram(y=chunk, sr=sr)
            mel_spectrogram = tf.image.resize(np.expand_dims(mel_spectrogram, axis=-1), (150, 150))
            chunks.append(mel_spectrogram)
        return np.array(chunks)

    chunks = extract_chunks(y, sr)
    return chunks
def predict_genre(file_path):
    try:
        model = load_model('Music_Genre_Classification_Final_Model.keras')
    except Exception as e:
        return e
    data = preprocess_audio(file_path)

    predictions = model.predict(data)

    mean_prediction = np.mean(predictions, axis=0)
    predicted_class = np.argmax(mean_prediction)

    # Return the genre name instead of the class index
    return GENRES[predicted_class]