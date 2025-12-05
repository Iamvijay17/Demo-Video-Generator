from TTS.api import TTS
import time

# Load the multilingual TTS model
print("🔄 Loading TTS model...")
start_time = time.time()
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
print(f"✅ Model loaded in {time.time() - start_time:.2f} seconds")

# Text examples
female_text = "Hello Vijay! This is a female voice speaking."
male_text = "Hi Vijay! This is a male voice speaking."

story_text = """
Once upon a time, in a small village, there lived a curious little boy named Ravi. 
Every day, he would explore the forests and fields around his home, discovering new plants, animals, and hidden streams. 
One sunny afternoon, he found a sparkling stone by the river. 
It shone with colors he had never seen before. 
Ravi picked it up and heard a soft voice whisper, 'Thank you for freeing me.' 
The stone was a magical spirit trapped for many years. 
From that day on, Ravi's adventures became even more extraordinary, full of magic, friendship, and wonder.
"""


# # Generate female voice (default voice)
# tts.tts_to_file(
#     text=female_text,
#     speaker="Alma María",    # use a female speaker from the available list
#     language="en",           # important for multilingual model
#     file_path="female.mp3"
# )

# Generate male voice (we just change the text, using same default voice)
tts.tts_to_file(
    text=story_text,
    speaker="Aaron Dreschner",  # use a male speaker from the available list
    language="en",
    file_path="male.mp3"
)

print("✅ Done! Check female.mp3 and male.mp3 in your folder.")
