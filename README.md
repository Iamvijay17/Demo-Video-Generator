# Story Video Generator

A Python application that generates narrated story videos from text prompts. It creates audio narration using Coqui TTS and combines it with text overlays to produce engaging video stories.

## Features

- **Story Generation**: Input any story topic to generate a complete narrative
- **Text-to-Speech**: High-quality audio narration using Coqui TTS (XTTS v2)
- **Video Creation**: Automatic video compilation with text overlays and smooth transitions
- **Customizable**: Easy to modify for different story themes and styles

## Requirements

- Python 3.10+
- FFmpeg (for video processing)
- ImageMagick (for text rendering)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd story-video-generator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install system dependencies:
```bash
# macOS
brew install ffmpeg imagemagick

# Ubuntu/Debian
sudo apt-get install ffmpeg imagemagick

# Windows - download from official websites
```

## Usage

Run the story video generator:

```bash
python story_video.py "your story topic"
```

Example:
```bash
python story_video.py "king story"
```

This will:
1. Generate a story based on the topic
2. Split it into scenes
3. Create audio narration for each scene
4. Generate text overlays
5. Combine everything into `final_story_video.mp4`

## Project Structure

```
story-video-generator/
├── story_video.py          # Main application script
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── .python-version        # Python version specification
└── README.md              # This file
```

## Dependencies

- **TTS**: Coqui TTS for text-to-speech synthesis
- **diffusers**: Hugging Face diffusers for potential image generation
- **torch**: PyTorch deep learning framework
- **moviepy**: Video editing and creation
- **Pillow**: Image processing
- **transformers**: NLP models
- **huggingface_hub**: Model downloading

## Notes

- The current implementation uses text overlays instead of generated images for simplicity
- Audio is generated in WAV format for best compatibility
- Videos are created at 24 FPS with fade transitions
- Large model downloads may be required on first run

## License

MIT License - feel free to use and modify as needed.
