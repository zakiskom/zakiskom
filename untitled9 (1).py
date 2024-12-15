# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14cEZYRn1doPTrJL2814iOPN1KV5QOIN9
"""

from google.colab import files
uploaded = files.upload()  # Pilih file untuk diunggah

import pandas as pd

# 1. Load dataset dengan pemisah titik koma
file_path = '/content/GojekAppReviewV4.0.0-V4.9.3_Cleaned.csv'
data = pd.read_csv(file_path, sep=';', engine='python')

# 2. Tampilkan informasi dataset
print("Jumlah baris dan kolom:", data.shape)
print("Kolom dalam dataset:", data.columns.tolist())

# 3. Tampilkan 5 baris pertama untuk verifikasi
print(data.head())

import pandas as pd

# 1. Load dataset
file_path = '/content/GojekAppReviewV4.0.0-V4.9.3_Cleaned.csv'  # Ganti dengan nama file Anda
data = pd.read_csv(file_path, sep=';', engine='python')

# 2. Hapus kolom yang tidak diinginkan
columns_to_drop = ['Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8']
data = data.drop(columns=[col for col in columns_to_drop if col in data.columns])

# 3. Kurangi jumlah baris menjadi 7.000 (sampling secara acak)
data_sampled = data.sample(n=7000, random_state=42)  # Pilih 7000 baris secara acak

# 4. Tampilkan informasi dataset untuk verifikasi
print("Jumlah baris dan kolom setelah sampling:", data_sampled.shape)
print("Kolom dalam dataset setelah penghapusan:", data_sampled.columns.tolist())

# 5. Simpan dataset hasil ke file baru
data_sampled.to_csv('sampled_data.csv', index=False)
print("Dataset telah disimpan ke 'sampled_data.csv'")

import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# 1. Unduh resource NLTK (dijalankan satu kali)
nltk.download('punkt')
nltk.download('stopwords')

# 2. Load dataset
file_path = 'sampled_data.csv'  # Ganti dengan nama file hasil sampling Anda
data = pd.read_csv(file_path)

# 3. Fungsi untuk membersihkan teks
def clean_text(text):
    # 3.1 Ubah teks menjadi huruf kecil
    text = text.lower()
    # 3.2 Hapus angka, simbol, dan tanda baca
    text = re.sub(r'[^a-z\s]', '', text)
    # 3.3 Tokenisasi (memisahkan teks menjadi kata-kata)
    tokens = word_tokenize(text)
    # 3.4 Hapus stop words (kata umum yang tidak memiliki banyak arti)
    stop_words = set(stopwords.words('indonesian'))  # Ganti 'indonesian' jika teks dalam bahasa lain
    tokens = [word for word in tokens if word not in stop_words]
    # Gabungkan kembali token menjadi teks
    return ' '.join(tokens)

# 4. Terapkan fungsi pembersihan teks
# Ganti 'kolom_teks' dengan nama kolom teks pada dataset Anda
if 'kolom_teks' in data.columns:  # Pastikan kolom teks ada di dataset
    data['cleaned_text'] = data['kolom_teks'].apply(clean_text)

# 5. Simpan dataset yang sudah dibersihkan
data.to_csv('cleaned_data.csv', index=False)
print("Dataset telah dibersihkan dan disimpan ke 'cleaned_data.csv'")

!pip install pandas scikit-learn gensim nltk

print(data.columns)

if 'content' not in data.columns:
    raise ValueError("Kolom 'content' tidak ditemukan. Pastikan teks sudah dibersihkan.")

print(data.columns)

print("Kolom yang tersedia dalam dataset:", data.columns)

text_column = 'content'

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Load data
data = pd.read_csv('cleaned_data.csv')

# Step 1: Extract the 'content' column
texts = data['content'].fillna('').values  # Handle missing values if any

# Step 2: Initialize CountVectorizer for BoW representation
vectorizer = CountVectorizer(stop_words='english', min_df=2)  # Remove stopwords, ignore rare words

# Step 3: Fit and transform the text data to BoW
bow_matrix = vectorizer.fit_transform(texts)

# Step 4: Convert the BoW matrix to a DataFrame
bow_df = pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# Display the BoW DataFrame
print("Bag of Words representation:")
print(bow_df.loc[:, (bow_df != 0).any(axis=0)].head())  # Show columns with non-zero values

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load data
data = pd.read_csv('cleaned_data.csv')

# Step 1: Extract the 'content' column
texts = data['content'].fillna('').values  # Handle missing values if any

# Step 2: Initialize TfidfVectorizer for TF-IDF representation
vectorizer = TfidfVectorizer(stop_words='english', min_df=2)  # Remove stopwords, ignore rare words

# Step 3: Fit and transform the text data to TF-IDF
tfidf_matrix = vectorizer.fit_transform(texts)

# Step 4: Convert the TF-IDF matrix to a DataFrame
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# Display the TF-IDF DataFrame
print("TF-IDF representation:")
print(tfidf_df.loc[:, (tfidf_df != 0).any(axis=0)].head())  # Show columns with non-zero values

import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, precision_score

# Contoh data prediksi (ubah dengan data Anda)
# y_true: Label asli
# y_scores: Probabilitas prediksi dari model
y_true = [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]  # Contoh label asli
y_scores = [0.1, 0.4, 0.35, 0.8, 0.55, 0.2, 0.85, 0.3, 0.7, 0.6]  # Contoh probabilitas prediksi

# Hitung precision dan recall pada berbagai ambang batas
precision, recall, thresholds = precision_recall_curve(y_true, y_scores)

# Plot grafik precision
plt.figure(figsize=(8, 6))
plt.plot(thresholds, precision[:-1], label='Precision', color='b')
plt.xlabel('Threshold')
plt.ylabel('Precision')
plt.title('Precision vs Threshold')
plt.legend()
plt.grid()
plt.show()

import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Dataset
file_path = 'cleaned_data.csv'  # Ganti dengan path dataset Anda
data = pd.read_csv(file_path)

# 2. Periksa kolom dalam dataset
print("Kolom yang tersedia dalam dataset:", data.columns)

# Pastikan kolom yang digunakan untuk teks dan label ada
text_column = 'content'  # Kolom teks
label_column = 'score'   # Kolom skor (diasumsikan untuk sentimen, ganti jika berbeda)

if text_column not in data.columns or label_column not in data.columns:
    raise ValueError(f"Kolom '{text_column}' atau '{label_column}' tidak ditemukan dalam dataset.")

# 3. Preprocessing Teks
def clean_text(text):
    text = text.lower()  # Ubah ke huruf kecil
    text = re.sub(f"[{string.punctuation}]", "", text)  # Hapus tanda baca
    text = re.sub(r'\d+', '', text)  # Hapus angka
    text = re.sub(r'\s+', ' ', text).strip()  # Hapus spasi berlebih
    return text

data[text_column] = data[text_column].astype(str).apply(clean_text)

# 4. Kategorikan label (misalnya: skor 1-2 = negatif, 3 = netral, 4-5 = positif)
# 4. Kategorikan label (misalnya: skor 1-2 = negatif, 3 = netral, 4-5 = positif)

# Konversi kolom score menjadi integer
data[label_column] = pd.to_numeric(data[label_column], errors='coerce')

# Pastikan tidak ada nilai NaN setelah konversi
if data[label_column].isnull().any():
    print("Terdapat nilai NaN setelah konversi. Menghapus baris dengan nilai NaN...")
    data = data.dropna(subset=[label_column])

# Fungsi untuk mengkategorikan sentimen
def categorize_sentiment(score):
    if score <= 2:
        return "negative"
    elif score == 3:
        return "neutral"
    else:
        return "positive"

# Terapkan fungsi ke kolom score
data['sentiment'] = data[label_column].apply(categorize_sentiment)

# 5. Split Data
X = data[text_column]
y = data['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Representasi Teks (Bag of Words)
vectorizer = CountVectorizer()
X_train_bow = vectorizer.fit_transform(X_train)
X_test_bow = vectorizer.transform(X_test)

# 7. Model Logistic Regression
model = LogisticRegression()
model.fit(X_train_bow, y_train)

# 8. Prediksi
y_pred = model.predict(X_test_bow)

# 9. Evaluasi
print("Classification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred, labels=["negative", "neutral", "positive"])
sns.heatmap(conf_matrix, annot=True, fmt='d', xticklabels=["negative", "neutral", "positive"], yticklabels=["negative", "neutral", "positive"])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load data
data = pd.read_csv('cleaned_data.csv')

# Step 1: Extract the 'content' column and 'score' column
texts = data['content'].fillna('').values  # Handle missing values if any
labels = data['score'].astype(str).values  # Convert scores to integers

# Step 2: Initialize TfidfVectorizer for TF-IDF representation
vectorizer = TfidfVectorizer(stop_words='english', min_df=2)  # Remove stopwords, ignore rare words

# Step 3: Fit and transform the text data to TF-IDF
tfidf_matrix = vectorizer.fit_transform(texts)

# Step 4: Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, labels, test_size=0.2, random_state=42)

# Step 5: Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 6: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sns

# Load data
data = pd.read_csv('cleaned_data.csv')

# Step 1: Extract the 'content' column and 'score' column
texts = data['content'].fillna('').values  # Handle missing values if any
labels = data['score'].astype(str).values  # Convert scores to integers

# Step 2: Initialize TfidfVectorizer for TF-IDF representation
vectorizer = TfidfVectorizer(stop_words='english', min_df=2)  # Remove stopwords, ignore rare words

# Step 3: Fit and transform the text data to TF-IDF
tfidf_matrix = vectorizer.fit_transform(texts)

# Step 4: Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, labels, test_size=0.2, random_state=42)

# Step 5: Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 6: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Step 8: Plot Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=sorted(set(labels)), yticklabels=sorted(set(labels)))
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()