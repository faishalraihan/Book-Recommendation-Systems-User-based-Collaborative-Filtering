"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import pickle

list_books_dict = pickle.load(open('book_dict.pkl','rb'))
df = pd.DataFrame(list_books_dict)
indices = pd.Series(df.index,index=df['title'])

list_books = df.sort_values(by='title')
list_books = list_books.title

similarity = pickle.load(open('similarity.pkl','rb'))

def content_based_recommender(title,cosine_sim_cv=similarity,df=df,indices=indices):
	idx = indices[title]
	sim_scores = list(enumerate(cosine_sim_cv[idx]))
	sim_scores = sorted(sim_scores, key = lambda x: x[1],reverse=True)
	sim_scores = sim_scores[1:11]
	book_indices = [i[0] for i in sim_scores]
	return df[['title','author', 'language', 'avg_rating']].iloc[book_indices]


st.sidebar.title('Sistem Rekomendasi Buku')
st.sidebar.markdown('Aplikasi ini membantu anda dalam menemukan buku yang mirip dengan buku yang kamu sukai, silahkan pilih beberapa buku yang tersedia di sistem kami')
selected_book = st.sidebar.selectbox('Masukkan nama buku', list_books)  

if st.sidebar.button('Rekomendasi') : 
  st.markdown('#### Hasil Rekomendasi')
  hasil_rekomendasi_df = content_based_recommender(selected_book)
  
  for i in range(0, len(hasil_rekomendasi_df), 3) : 
    col1, col2, col3 = st.columns(3)

    col1.markdown('#### {}'.format(hasil_rekomendasi_df.iloc[i].title))
    col1.markdown("Author : {}".format(hasil_rekomendasi_df.iloc[i].author))
    col1.markdown("Language : {}".format(hasil_rekomendasi_df.iloc[i].language))
    col1.markdown("Average Rating : {}".format(hasil_rekomendasi_df.iloc[i].avg_rating))
      
    if i + 1 in range(0, len(hasil_rekomendasi_df)) : 
      col2.markdown('#### {}'.format(hasil_rekomendasi_df.iloc[i + 1].title))
      col2.markdown("Author : {}".format(hasil_rekomendasi_df.iloc[i + 1].author))
      col2.markdown("Language : {}".format(hasil_rekomendasi_df.iloc[i + 1].language))
      col2.markdown("Average Rating : {}".format(hasil_rekomendasi_df.iloc[i + 1].avg_rating))
    
    if i + 2 in range(0, len(hasil_rekomendasi_df)) : 
      col3.markdown('#### {}'.format(hasil_rekomendasi_df.iloc[i + 2].title))
      col3.markdown("Author : {}".format(hasil_rekomendasi_df.iloc[i + 2].author))
      col3.markdown("Language : {}".format(hasil_rekomendasi_df.iloc[i + 2].language))
      col3.markdown("Average Rating : {}".format(hasil_rekomendasi_df.iloc[i + 2].avg_rating))
        
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    # st.text(hasil_rekomendasi_df.iloc[i].title)
      
#   col1, col2, col3 = st.columns(3)
#   with col1:
#       st.markdown('#### Mantap Jiwa')
#       st.text('ini description')
#   with col2:
#       st.markdown('#### Mantap Jiwa')
#       st.text('ini description')
#   with col3:
#       st.markdown('#### Mantap Jiwa')
#       st.text('ini description')

# else : 
  # st.markdown('#### Silahkan pilih buku dan klik rekomendasi')
