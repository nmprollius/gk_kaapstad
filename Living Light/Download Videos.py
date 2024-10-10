from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import yt_dlp
import os

# Function to download a video from YouTube
# def download_video(url, download_path='.'):
#     try:
#         # Create a YouTube object
#         yt = YouTube(url)
        
#         # Get the highest resolution stream
#         stream = yt.streams.get_highest_resolution()
        
#         # Download the video
#         print(f"Downloading: {yt.title}")
#         stream.download(output_path=download_path)
#         print("Download complete!")
#     except Exception as e:
        # print(f"Error: {e}")


# Function to download a video from YouTube
def download_video(url, download_path='.'):
    ydl_opts = {
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',  # Best video + best audio
        'merge_output_format': 'mp4',  # Merge into mp4
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")


def save_file():
    """
    Open a file dialog to prompt the user to save a file, pre-filled with .mp4 extension and
    MP4 file type. Returns the selected file path, or None if the user cancels.
    """
    root = tk.Tk()
    root.attributes('-topmost', False)
    file_path = filedialog.askdirectory(title="Save Video", initialdir=fr"{os.path.expanduser('~')}\Downloads")
    root.destroy()  
    
    return file_path

# YouTube video URL
video_url = input("Enter the YouTube video URL: ")
save_path= save_file()
# save_path = fr'{os.path.expanduser("~")}\Downloads'
# video_url = "https://youtu.be/EVCIvo3ZGRU?si=bo38IXJeka3Bi-QU"

# Download the video
download_video(video_url, save_path if save_path else '.')
