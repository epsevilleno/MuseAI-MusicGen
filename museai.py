import streamlit as st
import openai

from openai import AsyncOpenAI
from openai import OpenAI

#API Key was typed into streamlit during the integration process
client = AsyncOpenAI (
    api_key=st.secrets["API_key"]
)

#function for GPT to generate response
async def generate_response(question, context):
    model = "gpt-3.5-turbo"

    completion = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": question},
                  {"role": "system", "content": context}]
    )
    return completion.choices[0].message.content

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
    
    #The following would only appear if feeling_type was filled in
    if feeling_type:
        
        #creating a response based on the user's feeling (based on the input in feeling_type)
        museai_context = f'Provide a one-sentence supportive message based on {feeling_type} and say to proceed to next section.'
        museai_question = "How should I respond to this?"
        museai_response = await generate_response(museai_question, museai_context)
        
        #will write the response
        st.write(museai_response)
        
        #Will accept the type of genre the user selects             
        genre_type = st.selectbox("What genre of music would you like to find?", ['Pop', 'Rock', 'Country', 'Classical', 'Jazz', 'Hip hop', 'Other'])
        
        #a field that would appear if the user selects 'Other'
        if genre_type == 'Other':
            other_genre = st.text_input("Please specify what genre you would like.")
            if other_genre:
                genre_type = other_genre
        
        # Will accept User's the preferred language
        language_type = st.text_input("What language do you prefer?")
        
        #an if-statement that would make the components below appear if language_type is filled in
        if language_type:
            
            st.write("Make your choices more tailored by proceeding to the next section.")
            
            #will accept user's preferences        
            tempo_type = st.selectbox("How fast would you like the song/s?", ['slow', 'moderate', 'fast', 'any'])
            activity_type = st.text_input("What are you doing right now? (e.g., studying or working-out )")   
            music_amount = st.text_input("How many songs would you like to generate? (e.g., 3 or three)") 
            
            #a button that would trigger the generate response function would appear if the music_amount is filled in
            if music_amount:
                
                st.write("Great! Now click the button below.")
                
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
            
