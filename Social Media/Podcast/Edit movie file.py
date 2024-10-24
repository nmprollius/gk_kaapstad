from moviepy.video.io.VideoFileClip import VideoFileClip

def cut_first_15_minutes(input_file, output_file):
    # Load the video clip
    video_clip = VideoFileClip(input_file)

    # Define the time range to keep (in seconds)
    start_time = 3 * 60  # 15 minutes
    start_time = 8
    end_time = video_clip.duration

    # Cut the video clip
    cut_clip = video_clip.subclip(start_time, end_time)

    # Write the edited video to a new file
    cut_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

    # Close the video clip
    video_clip.close()

if __name__ == "__main__":

  import os
  os.chdir(r'C:\Users\nprol195\Downloads')
    # Replace 'input.mp4' and 'output.mp4' with your file names
  input_file = "Yahweh (Live) - Elevation Worship truncated.mp4.mp4"
  output_file = "Yahweh (Live) - Elevation Worship truncated2.mp4"

  cut_first_15_minutes(input_file, output_file)
