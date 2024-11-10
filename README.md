### The docker container is used for generating the subtitles for .mp4 videos
https://genai.acloudfan.com

# openai-whisper
https://pypi.org/project/openai-whisper/

Used for generating subtitkes *.srt* file.


# Docker container

To use the container you MUST have Docker installed on your machine. You can build the local container image with the Dockerfile.

## Dockerfile
This Dockerfile sets up an environment for running a Whisper-based transcription script with all dependencies pre-installed and configured, ready to process files in /home/videos upon container launch.

1. Change directory to project root

2. Create the Docker image

```
docker build -t subtitle-with-whisper .
```

# Usage

1. Run the Docker deamon

2. Setup an environment variable that points at a folder that contains the videos. All subfolders of the specified folder will be searched for *.mp4* files. Subtitles will be generated for all the *.mp4* in all subfolders of the specified *VFOLDER*.

   ```
   export VFOLDER=/mnt/c/Users/raj/Documents/my-videos
   ```
3. Generate the subtitles for your .mp4 videos

```
docker run -v $VFOLDER:/home/videos  -a STDERR -a STDOUT  subtitle-with-whisper
```

---
READ below this ONLY, if you are learning how the subtitles are getting generated !!

# generate.py
Main file for generation of the subtitles.

Here’s a usage documentation for the script, explaining its purpose, functionality, and instructions for running it:



# Subtitle Generation Script Documentation

### generate.py
It is in the docuker file.

## Overview

This script automates the process of finding `.mp4` video files within a specified directory, generating subtitles for each file using OpenAI's Whisper model, and saving the subtitles in `.srt` format in an organized directory structure. 

## Prerequisites

- Python 3.x
- The `whisper` package from OpenAI
  - Install Whisper via pip if not already installed:
    ```bash
    pip install openai-whisper
    ```

## Usage

### Command-line Syntax

```bash
python script_name.py <root_dir>
```

**Arguments:**

- `<root_dir>`: The root directory where the script will begin searching for `.mp4` files. The script will process each `.mp4` file it finds in this directory and all of its subdirectories.

### Example

```bash
python script_name.py /path/to/your/videos
```

This command will:
1. Search `/path/to/your/videos` and its subdirectories for `.mp4` files.
2. Generate `.srt` subtitle files for each `.mp4` file found.
3. Save the subtitles in an `st` folder inside the same directory as each video file, with the filename `subtitles.srt`.

### Output Structure

For each `.mp4` file found, the script:
1. Creates an `st` subdirectory in the directory containing the video file.
2. Saves the generated subtitle file as `subtitles.srt` within the `st` subdirectory.

### Example Output

If an `.mp4` file is located at `/path/to/your/videos/sample_video.mp4`, the subtitle file will be saved as:
```
/path/to/your/videos/st/subtitles.srt
```

## Script Workflow

1. **File Search**: The script first scans `root_dir` and its subdirectories to locate `.mp4` files.
2. **Subtitle Generation**: For each `.mp4` file found, it uses Whisper’s `transcribe` function to generate subtitle text, formatting the output as `.srt` with time stamps.
3. **Output Saving**: The generated subtitles are saved in a structured format in an `st` subdirectory for easy access.

## Functions and Details

### `find_files(root_dir)`

Recursively searches for `.mp4` files in the specified root directory.

- **Input**: `root_dir` (string) - Directory to search in.
- **Output**: List of file paths for all `.mp4` files found.

### `generate_subtitles(video_file, model_name="base")`

Generates subtitle content for a given video file in `.srt` format.

- **Input**: 
  - `video_file` (string) - The path to the `.mp4` file.
  - `model_name` (string, optional) - The Whisper model to use for transcription (default is `"base"`).
- **Output**: Subtitle content in `.srt` format as a string.

### `format_timestamp(seconds)`

Converts a timestamp from seconds to `HH:MM:SS,mmm` format used in `.srt` files.

- **Input**: `seconds` (float) - Timestamp in seconds.
- **Output**: Formatted timestamp string.

### `process_file(path)`

Handles subtitle generation and saving for a single `.mp4` file.

- **Input**: `path` (string) - Path to the `.mp4` file.
- **Output**: Saves the `.srt` file in the appropriate directory.

## Notes

- **Model Selection**: By default, the script uses the Whisper `"base"` model for transcription. You may adjust the `model_name` parameter in `generate_subtitles` for other Whisper models if available and necessary.
- **Error Handling**: Ensure that Whisper is properly installed, as it handles the transcription process.
  
