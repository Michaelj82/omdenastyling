import streamlit as st
from PIL import Image


# set page configuration
st.set_page_config(
    page_title="GRE-Omdena",
    page_icon='https://omdena.com/wp-content/uploads/2022/11/Omdena-Logo.png',
)


# styling
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    



# Function to recommend groceries based on user preferences
def recommend_groceries(preferences):
    # Add your recommendation logic here
    recommended_items = ["Chicken", "BBQ", "chicken 65"]
    return recommended_items











# Streamlit app
def stream():




    # Set title 
    st.title('Grocery Recommendation System for the Berlin Area') 
    image = Image.open('berlin-chapter-omdena.png')
    st.image(image)

    st.write('The OMDENA Berlin Chapter is happy to present their Grocery Recommendation System for the Berlin Area. The goal of this project is to help customers make informed decisions about what groceries to buy and where from. With so many options available, it can be overwhelming to know what product or store may be the best suited for you. Therefore, our recommendation system aims to alleviate this problem.')
    product_name = ["","Mango", "Onions","Potato", "Chicken","Eggs","Milk","Yogurt","Biscuits","Cakes","Olive oil"]
    c = st.selectbox(" *Search For Products*", product_name)    
    result_without_filter = st.button("RECOMMEND", key = "1")
    if result_without_filter:
        st.success("These are the recommentations --")




    



    Category = ["Food & Beverage", "Special Occasions & Gifts","Baby & Infant"]
    Subcategory = ["Coffee & Tea", "Cocoa & Hot Chocolate","lemonade"]

    protein = ["Low","Medium", "High"]

    fiber = ["Low", "Medium","High"]

    carbohydrates = ["Low","Medium" ,"High"]
    sugar = ["Low","Medium" ,"High"]

    st.write("*Recommend The Products Using Filters*")
    with st.expander("*FILTERS*"):
        st.write("Select your personal choice")

        Category_options = st.selectbox("Category", Category)
        Subcategory_options = st.selectbox("Subcategory", Subcategory )
        
    
    with st.expander("Nutrients"):
        st.write("recommend based on nutrients")
        protein_option = st.radio("Protein content", protein)
        Fiber_option = st.radio("Fiber content", fiber)
        carbohydrates_option = st.radio("carbohydrates content", carbohydrates)
        sugar_option = st.radio("Sugar content", sugar)

    
    Allergens , Ingredients =  st.columns(2)

    with Allergens:
        A = st.text_input("Enter Your Allergenic Substances")

    with Ingredients:
        I = st.text_input("What Are The Ingredients You Want")


    Price = st.slider("Enter your Price", 0 , 5000,10, step = 6)


    
    result_with_filters = st.button("RECOMMEND", key = "2")
    if result_with_filters:
        st.success("These are the recommentations")




         


    





    

    #ecommend groceries based on user preferences
    #recommended_items = recommend_groceries()

    # Display recommended items
    #st.subheader('Recommended Groceries')
    


stream()