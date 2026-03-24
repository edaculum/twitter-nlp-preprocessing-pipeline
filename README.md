## Proje Açıklaması
Bu projede, Twitter veri seti kullanılarak **Doğal Dil İşleme (NLP)** kapsamında kapsamlı bir **metin ön işleme (text preprocessing) pipeline** oluşturulmuştur. Amaç, ham (kirli) metin verisini temizleyerek makine öğrenmesi modelleri için daha anlamlı ve kullanılabilir hale getirmektir.

---

## 📊 Veri Seti
Projede Kaggle üzerinden indirilen Twitter veri seti kullanılmıştır. Veri seti:

🔗 Dataset Linki:  
https://www.kaggle.com/datasets/durgeshrao9993/twitter-analysis-dataset-2022

- Tweet metinlerinden (`tweet`)
- Duygu etiketlerinden (`label`)

oluşmaktadır. Gereksiz `id` kolonu kaldırılarak veri sadeleştirilmiştir.

---

## Yapılan İşlemler

### 1. Veri Setinin Yüklenmesi
- Kaggle API kullanılarak veri seti indirilmiştir  
- ZIP dosyası açılarak CSV dosyası okunmuştur  
- Veri seti temel olarak incelenmiştir (`shape`, `columns`, `info`, `value_counts`)  



### 2. Metin Ön İşleme (Text Preprocessing)

####  Metin Temizleme
- Bozuk karakterler düzeltildi (`ftfy`)
- Tüm harfler küçültüldü
- HTML etiketleri kaldırıldı
- URL’ler temizlendi
- Kullanıcı mention’ları (@user) kaldırıldı
- Hashtag sembolü kaldırıldı (kelime korunarak)

#### Metin Normalizasyonu
- Kısaltmalar düzeltildi (can't → cannot)
- Emojiler metne dönüştürüldü (😊 → smiling_face)
- Noktalama işaretleri kaldırıldı

#### Metni Anlamlandırma
- Tokenization (kelimelere ayırma) yapıldı
- Stopwords (anlamsız kelimeler) kaldırıldı
- Lemmatization ile kelimeler kök haline indirildi

#### Opsiyonel İşlem
- Yazım hatası düzeltme (TextBlob)

---

## 🧠 Preprocessing Fonksiyonu
Tüm bu adımlar, `preprocess_tweet()` fonksiyonu içinde birleştirilmiştir. Bu fonksiyon:

- Ham tweet verisini alır  
- Tüm temizleme işlemlerini uygular  
- Model için hazır hale getirilmiş metni döndürür  

---

##  Örnek 
Projede tek bir tweet üzerinde aşağıdaki dönüşümler gösterilmiştir:

- Orijinal hali  
- Bozuk karakterleri düzeltilmiş hali  
- Hashtag temizlenmiş hali  
- Emoji dönüştürülmüş hali  
- Tam preprocessing uygulanmış hali  

---

## 📦 Sonuç
Tüm veri setine preprocessing uygulanarak yeni bir sütun oluşturulmuştur:

- `tweet` → Orijinal veri  
- `cleaned_tweet` → Temizlenmiş veri  

Bu sayede veri, NLP görevleri için hazır hale getirilmiştir.

---

##  Amaç
Bu projenin amacı:

- Metin verisini temizleme sürecini öğrenmek  
- NLP preprocessing adımlarını uygulamalı görmek  
- Veriyi hazırlamak  
