import joblib
import requests
import streamlit as st


def getPoster(movie_id):
    url1 = f'https://api.themoviedb.org/3/movie/{movie_id}?api_'
    url2 = 'key=e6c859d8748eba6f31e32d4cf71ebbcc&language=en-US'
    data = requests.get(url1+url2)
    json_data = data.json()
    return 'https://image.tmdb.org/t/p/w500/' + json_data['poster_path']


def recommend(m):
    index = movies[movies['title'] == m].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda i: i[1])[1:7]
    lst = []
    posters = []
    for j in movies_list:
        movie_id = movies.iloc[j[0]].id
        lst.append(movies.iloc[j[0]].title)
        posters.append(getPoster(movie_id))
    return lst, posters


movies = joblib.load('./Models/movies.joblib')
similarity = joblib.load('./Models/similarity.joblib')

st.title('Movie Recommender')
movie = st.selectbox('Select a Movie', movies['title'].values)
if st.button('Recommend'):
    x, y = recommend(movie)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.image(y[0])
        st.write(x[0])
    with col2:
        st.image(y[1])
        st.write(x[1])
    with col3:
        st.image(y[2])
        st.write(x[2])
    with col4:
        st.image(y[3])
        st.write(x[3])
    with col5:
        st.image(y[4])
        st.write(x[4])
    with col6:
        st.image(y[5])
        st.write(x[5])
