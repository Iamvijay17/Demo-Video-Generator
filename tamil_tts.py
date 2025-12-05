import requests
import time
import os
from urllib.parse import quote

def google_translate_tts(text, lang='ta', output_file='tamil_output.mp3'):
    """
    Generate Tamil TTS using Google Translate API
    """
    print(f"🔄 Generating Tamil TTS for: {text[:50]}...")

    # Google Translate TTS URL
    base_url = "https://translate.google.com/translate_tts"
    params = {
        'ie': 'UTF-8',
        'q': text,
        'tl': lang,  # ta for Tamil
        'client': 'tw-ob'
    }

    try:
        # Make request
        response = requests.get(base_url, params=params, timeout=30)
        response.raise_for_status()

        # Save audio file
        with open(output_file, 'wb') as f:
            f.write(response.content)

        print(f"✅ Tamil audio saved to: {output_file}")
        print(f"📏 File size: {os.path.getsize(output_file)} bytes")
        return True

    except requests.exceptions.RequestException as e:
        print(f"❌ Error generating Tamil TTS: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    print("🗣️ Tamil TTS using Google Translate API")
    print("=" * 50)

    # Tamil text examples
    # tamil_texts = [
    #     "வணக்கம் விஜய்! இது தமிழ் மொழியில் உரையாக்க சோதனை.",
    #     "என் பெயர் விஜய். நான் ஒரு மென்பொருள் பொறியாளர்.",
    #     "தமிழ் மொழி ஒரு பழமையான மொழியாகும்.",
    #     "நன்றி! இந்த சேவை உதவியாக இருந்தது."
    # ]

    story = """
ஒரு காலத்தில் ஒரு மன்னன் வாழ்ந்தான். 
அவன் மிகவும் நீதி மிக்கவர். 
ஒரு நாள், அவன் அரசாட்சியில் ஒரு அதிசயம் நடந்தது...
அதுவே இந்த கதை ஆரம்பம்.
"""

    print(f"📝 Testing {len(tamil_texts)} Tamil text samples...")

    for i, text in enumerate(tamil_texts, 1):
        print(f"\n🔊 Sample {i}/{len(tamil_texts)}")
        print(f"📝 Text: {text}")

        output_file = f"tamil_sample_{i}.mp3"
        success = google_translate_tts(text, 'ta', output_file)

        if success:
            print("✅ Success!")
        else:
            print("❌ Failed")
        time.sleep(1)  # Small delay between requests

    print("\n🎉 Tamil TTS testing completed!")
    print("📁 Check the generated tamil_sample_*.mp3 files")

if __name__ == "__main__":
    main()
