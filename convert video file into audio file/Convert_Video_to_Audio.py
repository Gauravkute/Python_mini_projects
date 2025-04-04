from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

vid = askopenfilename(filetypes=[("cat_video","*.mp4")])  # Specify filetypes to filter for mp4 files
video = moviepy.editor.VideoFileClip(vid)

aud = video.audio
aud.write_audiofile("demo.mp3")

print("End")
