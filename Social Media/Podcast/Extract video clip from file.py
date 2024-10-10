from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

# Path to the original video file
user=os.getenv('USERPROFILE')
os.chdir(f'{user}\\Downloads')
input_file = "20240602.mkv"

# Load the video file
video = VideoFileClip(input_file)

# Get the duration of the video in seconds
video_duration = video.duration

# Define the start time (in seconds)
start_time = 15 * 60  # 15 minutes = 15 * 60 seconds

# Define the end time
end_time = min(90 * 60, video_duration)  # 1 hour 30 minutes or the end of the video, whichever is smaller

# Path to the output video file
output_file = "path_to_output_video.mp4"

# Extract the subclip
ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)

print("Video has been successfully cut and saved.")
