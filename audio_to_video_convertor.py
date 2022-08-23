import moviepy.editor as mp 

clip = mp.VideoFileClip("c.mp4")

clip.audio.write_audiofile("c.mp3")