import joblib
from Helpers import helper as hp
from Helpers import preproc as pp
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print('Started')
movies = pp.preProcess()
helper = hp.Helper(movies)
movies = helper.makeTags()

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['Tags']).toarray()
similarity = cosine_similarity(vectors)

joblib.dump(movies, './Models/movies.joblib')
joblib.dump(similarity, './Models/similarity.joblib')
print('Completed')
