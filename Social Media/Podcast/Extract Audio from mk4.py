from moviepy.editor import VideoFileClip
import os
from tkinter import Tk, filedialog

# Create a Tkinter root window, but don't display it
root = Tk()

# Bring the dialog box to the front
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

# Set the initial directory to the Downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
# Set the dedault name to Erediens.mp3
default_filename = "Erdiens.mp3"


# Open the file dialog to select an Excel file in the Downloads folder
file_path = filedialog.askopenfilename(
    initialdir=downloads_folder,
    title="Select an Video FileExcel file",
    filetypes=[('MP4 files', '*.mp4'),('MOV files','*.mov')],
    initialfile=default_filename
)

# Check if a file was selected
if file_path:
    print(f"Selected file: {file_path}")
else:
    print("No file selected.")
    exit()

root.destroy()

# Initialize the root window
root = Tk()
root.lift()

# Define file types
file_types = [('MP3 files', '*.mp3')]

# Define the default file name
default_filename = 'untitled.mp3'

# Open the save file dialog
save_file_path = filedialog.asksaveasfilename(
    title="Save as",
    defaultextension=".mp3",
    filetypes=file_types,
    initialfile=default_filename,
    initialdir="C:/Users/<YourUsername>/AppData/Roaming/Microsoft/Windows/Recent/AutomaticDestinations/"  # Quick Access
)
root.destroy()


def extract_audio(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file) 

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()

if __name__ == "__main__":
    extract_audio(file_path, save_file_path)
    print(f"Audio extracted successfully and saved to: {save_file_path}")

    # shutil.move(output_file_path,r'C:\Users\nprol195\Documents\Nico Docs\Kerk\Audio projects\RAW')

