from TTS.api import TTS
import time

# Load the TTS model
print("🔄 Loading TTS model...")
start_time = time.time()
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
print(f"✅ Model loaded in {time.time() - start_time:.2f} seconds")

# Story sentences with emotions and corresponding speaker styles
story_sentences = [
    {"text": "Once upon a time, in a small village, there lived a curious little boy named Ravi.", "emotion": "happy", "speaker": "Alma María"},
    {"text": "Every day, he would explore the forests and fields around his home, discovering new plants, animals, and hidden streams.", "emotion": "excited", "speaker": "Ana Florence"},
    {"text": "One sunny afternoon, he found a sparkling stone by the river.", "emotion": "surprised", "speaker": "Claribel Dervla"},
    {"text": "It shone with colors he had never seen before.", "emotion": "amazed", "speaker": "Daisy Studious"},
    {"text": "Ravi picked it up and heard a soft voice whisper, 'Thank you for freeing me.'", "emotion": "calm", "speaker": "Gracie Wise"},
    {"text": "The stone was a magical spirit trapped for many years.", "emotion": "mysterious", "speaker": "Tammie Ema"},
    {"text": "From that day on, Ravi's adventures became even more extraordinary, full of magic, friendship, and wonder.", "emotion": "joyful", "speaker": "Alma María"}
]

# Generate audio for each sentence with different speakers for emotional variation
total_sentences = len(story_sentences)
print(f"📚 Starting story generation ({total_sentences} parts)...")

for i, sentence in enumerate(story_sentences):
    file_name = f"story_part_{i+1}.mp3"
    print(f"🔊 Generating part {i+1}/{total_sentences} ({sentence['emotion']} tone)...")
    start_time = time.time()

    tts.tts_to_file(
        text=sentence["text"],
        language="en",
        speaker=sentence["speaker"],
        file_path=file_name
    )

    generation_time = time.time() - start_time
    print(f"✅ Generated: {file_name} (Emotion: {sentence['emotion']}, Speaker: {sentence['speaker']}, Time: {generation_time:.2f}s)")
    print(f"📊 Progress: {((i+1)/total_sentences)*100:.1f}% complete")

print("🎉 All story parts generated! Combine them in any audio editor if you like.")
