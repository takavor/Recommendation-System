import pickle
import streamlit as st
import numpy as np

print('================================================================================================')
st.set_page_config(
    page_title='Book Recommender'
)

st.header('Book Recommender using collaborative filtering and clustering')

# load artifacts
model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb')) 
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb')) 
df_final = pickle.load(open('artifacts/df_final.pkl', 'rb'))
    
# function to return recommended books and their image urls
def recommend_books(title):
    
    # get book id
    id = np.where(book_pivot.index == title)[0][0]
    
    # get similar books
    distance, suggested_books = model.kneighbors(book_pivot.iloc[id,:].values.reshape(1, -1), n_neighbors=6)
    
    books = []
    for i in range(len(suggested_books)):
        books_for_current = book_pivot.index[suggested_books[i]]
        for book in books_for_current:
            books.append(book)
            
    return books

# create book selector
selected_book = st.selectbox(
    "Type the name of the book you want recommendations for, or select from the list.",
    book_names
)

# button to get recommendations
if st.button('Recommend Similar Books'):
    recommended_books = recommend_books(selected_book)
    
    for book in recommended_books:
        if book != selected_book:
            st.text(book)
    # columns to list movies
    # col1, col2, col3, col4 = st.columns(4)
    
    # with col1:
    #     st.text(recommended_books[1])
    
    # with col2:
    #     st.text(recommended_books[2])
        
    # with col3:
    #     st.text(recommended_books[3])
        
    # with col4:
    #     st.text(recommended_books[4])    