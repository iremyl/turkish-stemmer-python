import pandas as pd

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag

# from snowballstemmer import TurkishStemmer
# from TurkishStemmer import TurkishStemmer

etkisiz = list(stopwords.words('turkish'))
# stemmer = TurkishStemmer()

# a = WordNet()

# ariza1 = "iplik kopması ile iplik arızası. kumaş sıkışması. makine fazla gürültülü ve çok sesli çalışıyor."

# kelimeler = word_tokenize(ariza1)
# cumleler = sent_tokenize(ariza1)

# filtreli = []

# print(kelimeler)
# print(cumleler)

# # pos = pos_tag(kelimeler)
# # print(pos)

# for k in kelimeler:
#     if k not in etkisiz:
#         filtreli.append(k)

# print(filtreli)

# for i in range(len(filtreli)):
#     print(stemmer.stem(filtreli[i]))

# pos = pos_tag(filtreli)
# print(pos)

#---------------------------------------------------------------------------------------------------

arizalar = pd.read_excel("deneme_ariza.xlsx")
arizalar.head()

# arizalar_t = pd.DataFrame()
# pos = pd.DataFrame()

# filtreli = []

# for i in range(arizalar.shape[0]):
    
#     kelimeler = [word_tokenize(arizalar.iloc[i][1])]
#     pos = pd.concat([pos, pd.DataFrame([pos_tag(kelimeler[0])])], ignore_index=True)
#     # print(pos)
    
#     # for k in range(len(kelimeler[0])):
#     #     if kelimeler[0][k] not in etkisiz:
#     #         filtreli.append([kelimeler[0][k]])
    
#     # print(filtreli)
        
#     arizalar_t = pd.concat([arizalar_t, pd.DataFrame(kelimeler)], ignore_index=True)

#---------------------------------------------------------------------------------------------------
    
from trnlp import TrnlpWord, writeable

obj = TrnlpWord()

for i in range(arizalar.shape[0]):
    
    kelimeler = [word_tokenize(arizalar.iloc[i][1])]
    
    for k in range(len(kelimeler[0])):
        obj.setword(kelimeler[0][k])
        # print(obj)
        print(obj.get_base,"---->", obj.get_base_type, "---->" , writeable(obj.get_morphology))
    
#---------------------------------------------------------------------------------------------------

#vnlp kütüphanesini dene

















