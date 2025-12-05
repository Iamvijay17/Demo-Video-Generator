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

### Option 1: Local Installation

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

### Option 2: Docker Installation

#### Prerequisites
- Docker installed on your system
- Docker Compose installed (usually comes with Docker Desktop)

#### Quick Start with Docker Compose

1. Clone the repository:
```bash
git clone <your-repo-url>
cd story-video-generator
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

This will:
- Build the Docker image with all dependencies
- Generate a story video for the default topic "king story"
- Save the output video to the `output/` directory on your host machine

#### Running with Custom Topics

To generate a story with a different topic, modify the `command` in `docker-compose.yml`:

```yaml
command: ["python", "story_video.py", "your custom topic"]
```

For example, to generate a story about "space exploration":
```yaml
command: ["python", "story_video.py", "space exploration"]
```

Then run:
```bash
docker-compose up --build
```

#### Alternative: Direct Docker Commands

If you prefer using Docker directly:

1. Build the image:
```bash
docker build -t story-video-generator .
```

2. Run the container with a custom topic:
```bash
# Linux/macOS
docker run -v $(pwd)/output:/app/output story-video-generator python story_video.py "your topic"

# Windows (PowerShell)
docker run -v ${PWD}/output:/app/output story-video-generator python story_video.py "your topic"

# Windows (Command Prompt)
docker run -v %cd%/output:/app/output story-video-generator python story_video.py "your topic"
```

#### Docker Development Workflow

For development with live code changes:

1. Mount the source code as a volume:
```bash
docker run -v $(pwd):/app -v $(pwd)/output:/app/output -it story-video-generator bash
```

2. Inside the container, you can run commands directly:
```bash
python story_video.py "your topic"
```

#### Troubleshooting

- **Permission issues with output directory**: Ensure the output directory exists and has proper permissions:
  ```bash
  mkdir -p output
  chmod 755 output
  ```

- **Large model downloads**: First run may take time due to TTS model downloads. Be patient and ensure stable internet connection.

- **Memory issues**: If you encounter memory errors, try increasing Docker's memory limit in Docker Desktop settings.

- **Port conflicts**: The application doesn't expose ports, so no port conflicts should occur.

- **Windows file sharing**: If using Docker Desktop on Windows, ensure the project directory is shared in Docker settings.

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
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose setup
├── .dockerignore           # Docker ignore rules
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
