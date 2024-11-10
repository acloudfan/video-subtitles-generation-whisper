# This Python script searches a specified directory for .mp4 files, 
# generates subtitles for each video file using OpenAI’s Whisper model, 
# and saves the subtitles in .srt format in a subdirectory.

import os
import argparse
import whisper

extension = ".mp4"

def find_files(root_dir):
    file_paths = []

    for root, dirs, files in os.walk(root_dir):
        # print(root)
        for file in files:
            if file.endswith(extension):
                file_paths.append(os.path.join(root, file))

    return file_paths


##############
def generate_subtitles(video_file, model_name="base"):
    """Generates subtitles for a video using OpenAI's Whisper."""

    model = whisper.load_model(model_name)
    result = model.transcribe(video_file)

    srt_content = ""
    
    # Previous end time
    prev_end = -1
    for i, segment in enumerate(result["segments"]):
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]

        # Added this to take care of the mismatch between end/start
        # The segment's start time MUST match the previous segment's end time
        if prev_end < 0:
            start_time = start
        else:
            start_time = prev_end

        # Used in next iteration
        prev_end = end

        srt_content += f"{i+1}\n"
        # srt_content += f"{format_timestamp(start)} --> {format_timestamp(end)}\n"
        srt_content += f"{format_timestamp(start_time)} --> {format_timestamp(end)}\n"
        srt_content += f"{text}\n\n"

    return srt_content

def format_timestamp(seconds):
    """Formats a timestamp in seconds to HH:MM:SS,mmm format."""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{milliseconds:03}"

# Process folder
def   process_file(path):
    
    # Directory that contains the .mp4
    directory = os.path.dirname(path)
    
    # Get the folder name from the directory path
    folder_name = os.path.basename(directory)


    # Create a subtitles folder under the folder that has the .mp4 file
    os.makedirs(directory+"/st", exist_ok=True)

    # Generate the content
    srt_content = generate_subtitles(path)

    # 
    with open(directory+"/st/"+"subtitles.srt", "w") as f:
        f.write(srt_content)


# Main entry point
if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Find files with a specific extension in a directory.")
    parser.add_argument("root_dir", type=str, help="The root directory to search in.")
    
    args = parser.parse_args()
    
    # Call the function with the provided root directory
    found_files = find_files(args.root_dir)
    
    # Print the results
    # process_file(found_files[0])

    for file in found_files:
        print(file)
        process_file(file)
        print("Done................")
