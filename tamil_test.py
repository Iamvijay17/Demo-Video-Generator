from TTS.api import TTS
import time

# Load the multilingual TTS model
print("🔄 Loading XTTS v2 multilingual model...")
start_time = time.time()
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
print(f"✅ Model loaded in {time.time() - start_time:.2f} seconds")

# Check supported languages
print(f"🌍 Supported languages: {tts.languages}")
try:
    speaker_count = len(tts.synthesizer.tts_model.speaker_manager.speakers)
    print(f"🎤 Available speakers: {speaker_count} speakers")
except:
    print("🎤 Speaker information: Available through speaker manager")

# Test texts in different languages
test_texts = [
    {
        "language": "en",
        "text": "Hello Vijay! This is a test of English language support.",
        "speaker": "Alma María"
    },
    {
        "language": "hi",
        "text": "नमस्ते विजय! यह हिंदी भाषा समर्थन का परीक्षण है।",
        "speaker": "Alma María"
    },
    {
        "language": "ta",
        "text": "வணக்கம் விஜய்! இது தமிழ் மொழி ஆதரவின் சோதனை.",
        "speaker": "Alma María"
    },
    {
        "language": "es",
        "text": "¡Hola Vijay! Esta es una prueba del soporte del idioma español.",
        "speaker": "Alma María"
    },
    {
        "language": "fr",
        "text": "Bonjour Vijay! Ceci est un test du support de la langue française.",
        "speaker": "Alma María"
    }
]

print("\n🧪 Starting language tests...")

for i, test in enumerate(test_texts):
    lang_code = test["language"]
    text = test["text"]
    speaker = test["speaker"]

    print(f"\n🔊 Test {i+1}/{len(test_texts)}: {lang_code.upper()} language")
    print(f"📝 Text: {text}")
    print(f"🎤 Speaker: {speaker}")

    try:
        file_name = f"test_{lang_code}.mp3"
        start_time = time.time()

        tts.tts_to_file(
            text=text,
            language=lang_code,
            speaker=speaker,
            file_path=file_name
        )

        generation_time = time.time() - start_time
        print(f"✅ SUCCESS: Generated {file_name} in {generation_time:.2f} seconds")

    except Exception as e:
        print(f"❌ FAILED: {str(e)}")

print("\n🎉 Language testing completed!")
print("📁 Check the generated audio files in your folder.")
