from streamlit import *
import streamlit as st 
import requests
import joblib
import numpy as np
df=joblib.load('testF')
tfidf_matrix=joblib.load('vectorF1')
from sklearn.metrics.pairwise import cosine_similarity


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=aba4c7dbcc53a9b4d846acf5ece6e82b&language=en%2Cnull&language=en".format(movie_id)

    data = requests.get(url)
    data = data.json()
    try:
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" +str( poster_path)
        return full_path
    except Exception as e:
        return str("Something went/n Wrong")

    

def recommend(movie):
    index = df[df['title'] == movie].index[0]
    sim_scores = list(enumerate(cosine_similarity(tfidf_matrix,tfidf_matrix[index])))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    recommended_movie_names = []
    recommended_movie_posters=[]
    for i in sim_scores[1:6]:
        movie_id = df.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(df.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender')
movie_list = df['title'].unique()
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        if recommended_movie_posters[0]=="Something went/n Wrong":
            st.text("!Oops Something")
            st.text("went wrong")
        else:
            st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        if recommended_movie_posters[1]=="Something went/n Wrong":
            st.text("!Oops Something")
            st.text("went wrong")
        else:
            st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        if recommended_movie_posters[2]=="Something went/n Wrong":
            st.text("!Oops Something")
            st.text("went wrong")
        else:
            st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        if recommended_movie_posters[3]=="Something went/n Wrong":
            st.text("!Oops Something")
            st.text("went wrong")
        else:
            st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        if recommended_movie_posters[4]=="Something went/n Wrong":
            st.text("!Oops Something")
            st.text("went wrong")
        else:
            st.image(recommended_movie_posters[4])




    
