import sys
import os
from TTS.api import TTS
from moviepy.editor import *
import time

# Function to generate story based on topic
def generate_story(topic):
    # Simple story generation - in real app, use LLM
    if "king" in topic.lower():
        story = """
In the ancient kingdom of Eldoria, there lived a wise and just king named Arthur. He ruled over a prosperous land where the fields were always green and the people lived in peace. King Arthur was known for his fairness and his love for his subjects. Every morning, he would ride through the villages, listening to the concerns of his people and ensuring justice was served.

One fateful day, dark clouds gathered over the kingdom. A fierce dragon, awakened from its slumber in the mountains, began terrorizing the villages. It breathed fire and destruction, burning crops and frightening the inhabitants. The king, upon hearing the news, gathered his bravest knights in the grand hall of the castle. "We must protect our people," he declared, his voice echoing through the stone walls.

The knights, clad in shining armor, set out on a perilous journey to confront the dragon. They traveled through dense forests and crossed raging rivers, their hearts filled with determination. Along the way, they encountered challenges that tested their courage and unity. But through teamwork and bravery, they persevered.

Finally, they reached the dragon's lair, a cavern high in the misty peaks. The battle was fierce and intense. Swords clashed against scales, and the air was filled with the roar of the beast. King Arthur, leading from the front, used not just his strength but his wisdom. He noticed the dragon's weakness and devised a clever plan.

With a mighty strike and the help of his loyal knights, the king defeated the dragon. The creature fell, and peace returned to Eldoria. The people cheered as their king returned victorious. From that day forward, King Arthur's legend grew, inspiring generations to come. He taught that true strength lies not in power alone, but in wisdom, courage, and compassion.

The kingdom flourished once more, and the story of the brave king and his knights became a tale told around campfires for centuries. And so, in the heart of Eldoria, peace reigned eternal, a testament to the enduring spirit of a great ruler.
"""
    else:
        story = "Default story about " + topic
    return story.strip()

# Function to split story into scenes (paragraphs)
def split_into_scenes(story):
    scenes = [para.strip() for para in story.split('\n\n') if para.strip()]
    return scenes

# Function to generate audio for each scene
def generate_audios(scenes, tts):
    audio_files = []
    for i, scene in enumerate(scenes):
        file_name = f"output/scene_audio_{i+1}.wav"
        print(f"Generating audio for scene {i+1}...")
        tts.tts_to_file(text=scene, speaker="Aaron Dreschner", language="en", file_path=file_name)
        audio_files.append(file_name)
    return audio_files

# Function to generate image prompt from scene text
def generate_image_prompt(scene_text):
    # Simple prompt generation - extract key elements
    prompt = f"A beautiful illustration of: {scene_text[:100]}... in a fantasy style, detailed, high quality"
    return prompt

# Function to create text clips for each scene
def create_text_clips(scenes):
    text_clips = []
    for i, scene in enumerate(scenes):
        print(f"Creating text clip for scene {i+1}...")
        # Create a text clip with the scene text
        txt_clip = TextClip(scene, fontsize=50, color='white', bg_color='black', size=(1280, 720))
        text_clips.append(txt_clip)
    return text_clips

# Function to create video
def create_video(audio_files, text_clips, output_file="output/final_story_video.mp4"):
    clips = []
    for audio_file, txt_clip in zip(audio_files, text_clips):
        audio = AudioFileClip(audio_file)
        txt_clip = txt_clip.set_duration(audio.duration).set_audio(audio)
        clips.append(txt_clip)

    # Add crossfade transitions
    if len(clips) > 1:
        final_clip = concatenate_videoclips(clips, method="compose", padding=-1)  # -1 for crossfade
    else:
        final_clip = clips[0]

    final_clip.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")

# Main function
def main():
    if len(sys.argv) < 2:
        print("Usage: python story_video.py 'story topic'")
        sys.exit(1)

    topic = sys.argv[1]
    print(f"Generating story video for topic: {topic}")

    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    # Generate story
    story = generate_story(topic)
    print(f"Story generated: {len(story)} characters")

    # Split into scenes
    scenes = split_into_scenes(story)
    print(f"Split into {len(scenes)} scenes")

    # Load TTS
    print("Loading TTS model...")
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

    # Generate audios
    audio_files = generate_audios(scenes, tts)

    # Create text clips
    text_clips = create_text_clips(scenes)

    # Create video
    print("Creating video...")
    create_video(audio_files, text_clips)

    print("Video created: output/final_story_video.mp4")

if __name__ == "__main__":
    main()
