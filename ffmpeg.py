import subprocess
import os

subprocess.call(
	'ffmpeg -framerate 1/5 -i img%03d.jpg -c:v libx264-vf fps=25 -pix_fmt yuv420p out.mp4',shell=True)
