import streamlit as st
from exa_py import Exa

# Initialize Exa with your API key
exa = Exa('API KEY')

# Streamlit app
st.title('Exa Search App')

# Input field for search query
query = st.text_input('Search here:')

# Button to trigger the search
if st.button('Search'):
    if query:
        response = exa.search(
            query,
            num_results=5,
            type='keyword',
            include_domains=['https://www.google.com'],
        )

        # Display the search results
        for result in response.results:
            st.subheader(result.title)
            st.write(result.url)
            st.write('---')
    else:
        st.write("Please enter a search query.")
