
#  Gerekli kütüphaneler
from textblob import TextBlob
import re
import string
import emoji
import contractions
import os
import ftfy
import zipfile
#CSV’yi Okuma
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer




#kaggle.json dosyasını yükle
from google.colab import files
files.upload()


#Kaggle Bağlantısını Aktif Etme
os.makedirs('/root/.kaggle', exist_ok=True)
!cp kaggle.json /root/.kaggle/
!chmod 600 /root/.kaggle/kaggle.json


#Dataset’i İndir
!kaggle datasets download -d durgeshrao9993/twitter-analysis-dataset-2022


os.listdir()


#ZIP Açma
with zipfile.ZipFile('twitter-analysis-dataset-2022.zip', 'r') as zip_ref:
    zip_ref.extractall('data')


#1... Veri Seti İncelemesi ...
#İçeriğe Bak
os.listdir('data')


df = pd.read_csv('data/twitter.csv')
df.head()

df.shape

df.columns

df.info()

df['label'].value_counts()

#gereksiz kolonu atalım, temiz veri seti oluşturma (id kaldırıldı)
df = df[['tweet', 'label']]
df.head()

#tweet örneklerini inceleme
df['tweet'].iloc[6]


# NLTK için gerekli veri setlerini indir
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Stopwords ve stem/lemmatizer objeleri
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


#indirilecekler
!pip install ftfy #bozuk Unicode karakterleri düzeltir
!pip install emoji
!pip install contractions

# 2... Veri Hazırlama (Preprocessing) Yöntemleri ...
# 1. Bozuk karakterleri düzeltme
def fix_text(text):
    return ftfy.fix_text(text).encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')

# 2. Lowercase
def to_lower(text):
    return text.lower()

# 3. HTML tag temizleme
def remove_html(text):
    return re.sub(r'<.*?>', '', text)

# 4. URL temizleme
def remove_urls(text):
    return re.sub(r'http\S+|www\S+', '', text)

# 5. Mention temizleme
def remove_mentions(text):
    return re.sub(r'@\w+', '', text)

# 6. Hashtag temizleme (kelimeyi bırak)
def remove_hashtags(text):
    return re.sub(r'#', '', text)

# 7. Contractions düzeltme
def fix_contractions(text):
    return contractions.fix(text)

# 8. Emoji → text
def emoji_to_text(text):
    return emoji.demojize(text, delimiters=(" ", " "))

# 9. Noktalama temizleme
punc = string.punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', punc))

# 10. Tokenization
def tokenize(text):
    return word_tokenize(text)

# 11. Stopwords kaldırma
def remove_stopwords(tokens):
    return [w for w in tokens if w not in stop_words]

# 12. Lemmatization
def lemmatize_tokens(tokens):
    return [lemmatizer.lemmatize(w) for w in tokens]

# 13. Spelling correction (opsiyonel, zaman alabilir)
def correct_spelling(text):
    return str(TextBlob(text).correct())

# Ana preprocessing fonksiyonu
def preprocess_tweet(text, apply_spelling=False):
    text = fix_text(text)
    text = to_lower(text)
    text = remove_html(text)
    text = remove_urls(text)
    text = remove_mentions(text)
    text = remove_hashtags(text)
    text = fix_contractions(text)
    text = emoji_to_text(text)
    text = remove_punctuation(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize_tokens(tokens)
    text = " ".join(tokens)
    if apply_spelling:
        text = correct_spelling(text)
    return text





# Örnek tweet
sample_index = 3
original_tweet = df['tweet'].iloc[sample_index]

print("Orijinal Tweet:")
print(original_tweet)

# 1. Bozuk karakterleri düzelt (ftfy)
fixed_tweet = fix_text(original_tweet)

# 2. Sadece Hashtag temizleme
tweet_no_hashtags = remove_hashtags(fixed_tweet)

# 3. Emoji → Text
tweet_emoji_text = emoji_to_text(fixed_tweet)

# 4. Ana preprocessing fonksiyonunu çağır
cleaned_tweet = preprocess_tweet(original_tweet)

print("\nBozuk karakterleri düzeltilmiş Tweet:")
print(fixed_tweet)

print("\nHashtag Temizlenmiş Tweet:")
print(tweet_no_hashtags)

print("\nEmoji → Text Tweet:")
print(tweet_emoji_text)

print("\nAna preprocessing fonksiyonunu çağırdıktan sonra tüm temizleme işlemleri:")
print(cleaned_tweet)





# CSV dosyaya uygulama
df = pd.read_csv('data/twitter.csv', encoding='utf-8')  # encoding ekleyelim
df['cleaned_tweet'] = df['tweet'].apply(preprocess_tweet)
# Kontrol
df[['tweet', 'cleaned_tweet']].head(10)