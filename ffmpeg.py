import subprocess
import os
#use the subprocess to exetuate the ffmpeg and convert images into video

subprocess.call(
	'ffmpeg -framerate 1/5 -f image2 -s 1920*1080 -i /home/ece-student/EC\ 601/image/img%03d.jpg -crf 25 -pix_fmt yuv420p out.mp4',shell=True)
# use ffmpeg to detect the images in /home/ece-student/EC\ 601/image/ and images with name 'img00'started, convert images into 
#1920*1080 and give me a mp4 video
