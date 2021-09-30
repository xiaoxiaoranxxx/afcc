from moviepy.editor import *

clip = (VideoFileClip("1.mp4").resize((488, 225)))
clip.write_gif("movie.gif", fps=15)  # 设置为每秒15帧
