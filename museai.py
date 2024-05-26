import streamlit as st
import openai

from openai import AsyncOpenAI
from openai import OpenAI

client = AsyncOpenAI (
    api_key=st.secrets["API_key"]
)

async def generate_response(question, context):
    model = "gpt-3.5-turbo"

    completion = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": question},
                  {"role": "system", "content": context}]
    )
    return completion.choices[0].message.content

async def museai_response(input_text):
    model = "gpt-3.5-turbo"
    response = await client.ChatCompletions.acreate(
        model=model,
        messages=[{"role": "user", "content": "Please give supportive encouragement based on {input_text} and say to them to proceed"},
                  {"role": "system", "content": "You are a supportive system"}],
        max_tokens = 50
    )
    return response.choices[0].message['content']

async def app():
    st.text("Created By: \n"
            "EJ Prince D. Sevilleno \n"
            "BSCS 3A-AI \n"
            "CCS 229 - Intelligent Systems \n"
            "West Visayas State University\n")
    
    st.title("MuseAI: Adding Music to your life")
    st.image("MuseAI.png")
    
    st.write(
    """
    Welcome to MuseAI! A music generator for every happening to your life.
    This is an AI-powered generator powered by GPT 3.5 Turbo model for the final requirement in CCS229-Intelligent Systems.
    """
    )

    #User inputs to process
    feeling_type = st.text_input("What do you feel right now? (e.g., feeling determined)")   
    
    if feeling_type:
        
        museai = asyncio.run(museai_response(feeling_type))
        st.write(museai)
                     
        genre_type = st.selectbox("What genre of music would you like to find?", ['Pop', 'Rock', 'Country', 'Classical', 'Jazz', 'Hip hop', 'Other'])
        if genre_type == 'Other':
            other_genre = st.text_input("Please specify what genre you would like.")
            if other_genre:
                genre_type = other_genre
        
        language_type = st.selectbox("What language do you prefer?", ['English', 'Filipino', 'Korean', 'Other'])
        if language_type == 'Other':
            other_language = st.text_input("Please specify what language you would like.")
            if other_language:
                language_type = other_language
        
        tempo_type = st.selectbox("How fast would you like the song/s?", ['slow', 'moderate', 'fast', 'any'])
        activity_type = st.text_input("What are you doing right now? (e.g., studying or working-out )")   
        music_amount = st.text_input("How many songs would you like to generate? (e.g., 3 or three)") 
        
        context = (f"Generate a music list with artists suggestion based on what I feel: {feeling_type}, genre: {genre_type}, language: {language_type}, speed: {tempo_type}, activity done: {activity_type} and generate {music_amount} song/s. ")
        question = "What music should I play?"
        
        if st.button("Generate Song List"):
            if question and context:
                response = await generate_response(question, context)
                st.write("Songs Generated:")
                st.write(response)
            else:
                st.error("Ensure all fields are filled out.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(app())
            
