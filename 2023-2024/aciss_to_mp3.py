from googletrans import Translator
from gtts import gTTS


def convert_string_to_mp3(text, source_language, target_language, filename):
    # Translate the text to the target language
    translator = Translator()
    translation = translator.translate(text, src=source_language, dest=target_language)
    text = translation.text

    # Convert the text to speech
    speech = gTTS(text=text, lang=target_language, slow=False)

    # Save the speech to a file
    speech.save(filename)0


# Example usage
text = "Skúška"
source_language = "sk"
target_language = "sk"  # French
filename = "output.mp3"
convert_string_to_mp3(text, source_language, target_language, filename)