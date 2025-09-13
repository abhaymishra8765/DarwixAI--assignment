from gtts import gTTS
from textblob import TextBlob
import os

def generate_audio(text, emotion):
    """
    Generates an audio file using gTTS, modulating the voice accent
    based on the detected emotion.
    """
    print("Generating audio with Google's TTS engine...")
    
    try:
        # 1. Emotion-to-Voice Mapping 
        # We will alter the 'tld' (top-level domain) to get different accents,
        # which changes the vocal characteristics of the synthesized speech. [cite: 13]
        if emotion == "Positive":
            # Sounds enthusiastic
            lang_accent = 'com' # Standard American accent
        elif emotion == "Negative":
            # Sounds more somber or serious
            lang_accent = 'co.uk' # British accent
        else: # Neutral
            lang_accent = 'com'

        # 2. Create the gTTS object with the text and chosen accent
        tts = gTTS(text=text, lang='en', tld=lang_accent, slow=False)
        
        # 3. Save the audio file 
        output_filename = 'output.mp3'
        tts.save(output_filename)
        
        print(f"\nSuccess! ✨ Audio file '{output_filename}' has been generated.")
        # Optional: uncomment the line below to automatically play the file on macOS
        # os.system(f"afplay {output_filename}")

    except Exception as e:
        print(f"\nAn error occurred during audio generation: {e}")
        print("Please check your internet connection, as gTTS requires it.")


def main():
    """
    Main function to get input and detect emotion.
    """
    # 1. Text Input 
    user_text = input("Please enter the text you want to convert to speech: ")

    # 2. Emotion Detection 
    blob = TextBlob(user_text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.1:
        emotion = "Positive"
    elif polarity < -0.1:
        emotion = "Negative"
    else:
        emotion = "Neutral"

    print(f"Detected Emotion: {emotion}")
    
    # 3. Call the function to generate audio
    generate_audio(user_text, emotion)


if __name__ == "__main__":
    main()
