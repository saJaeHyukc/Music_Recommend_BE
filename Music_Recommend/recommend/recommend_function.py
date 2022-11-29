import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

import sys
import os
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Music_Recommend.settings')
django.setup()

from songs.models import Song

data = pd.DataFrame(list(Song.objects.values()))

# tf-idf(Term Frequency - Inverse Document Frequency) _ 연산 기준 : lyrics 
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(data['lyrics'])

# Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(data.index, index=data['title']).drop_duplicates()


# 유사한 노래 추천 기능 함수
def get_recommendations(idx, cosine_sim=cosine_sim):    
    sim_scores = list(enumerate(cosine_sim[int(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_list = sim_scores[1:21]
    new_list = []
    for i in sim_list:
        new_dict = dict()
        new_dict['pk'] = i[0]
        new_dict["title"] = data['title'].iloc[i[0]]
        new_dict["singer"] = data['singer'].iloc[i[0]]
        new_dict["image"] = data['image'].iloc[i[0]]
        new_list.append(new_dict)
    return new_list
