#import necessary modules 
from openai import OpenAI
from PIL import Image # Pillow PIL library for image processing 
import streamlit as st 
from streamlit_carousel import carousel
from apikey import apikeys

#Initialise your image generation client
client=OpenAI(api_key=apikeys)

#creating dict of diff features/items of images
single_img= dict(
       title="",
       text="",
       interval=None,
       img="",
)
    

#Define function to generate images, for loop to generate as many images user inputs
def generate_images(image_description, num_images):
        image_gallery=[] #contains all images user has generated 
        for i in range(num_images): 
              
            # Make the API call to generate the images
            img_response = client.images.generate(
               model="dall-e-3",  # Use the correct DALL·E model
               prompt=image_description,
               size="1024x1024",  # Desired size for generated images
               n=1,      # set the number of images based on the input
               quality="standard" # Standard quality setting
            )

            # Extract the URLs for the generated images
            image_urls = img_response.data[0].url
        
            new_image=single_img.copy() #using copy of the image in func
            new_image["title"]=f"Image {i+1}" # 0+1=1, 1+1=2 so it will show Image-1 , Image-2 as loop runs
            new_image["text"]=image_description # user prompt used as text
            new_image["img"]=image_urls 
            image_gallery.append(new_image) #appending all new images in our gallery 

        return image_gallery





#Initialising Streamlit app 

st.set_page_config(page_title="Dalle-Image-Generator", page_icon=":camera",layout="wide")

#create a title 

st.title("DALL-E-3 Image Generator")

#create a subheader

st.subheader("Generate stunning images from text prompts with Dalle-3!")

#create a text-input box 
prompt = st.text_area("Enter a description to generate an image:")

#How many images the user wants to make, maximum value of images could be 5 and 1 is the default value
num_of_images = st.number_input("Select the number of images you want to generate", min_value=1,max_value=5,value=1)

#create a button 
if st.button("Generate Images"):
    generate_img = generate_images(prompt, num_of_images)
   
    carousel(items=generate_img, width=1)