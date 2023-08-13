import moviepy.editor

# Replace the parameter with the location of the video
video = moviepy.editor.VideoFileClip("/mnt/c/Users/MORT/Desktop/sample.mp4")

audio = video.audio

# Replace the parameter with the location along with file name
audio.write_audiofile("/mnt/c/Users/MORT/Desktop/sample.mp3")
