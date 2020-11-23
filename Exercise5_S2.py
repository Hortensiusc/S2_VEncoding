# Carlos Hortensius  U1500010

# Exercise 5: Integrate all the exercises done before in a python script
# /home/carloshortensius/Desktop/VideoEncoding/P2/S2/PruebaScript

import os
import subprocess


print('Welcome to Seminar 2: Introduce the path where your video is located:\n')
path = input()
os.chdir(path)

print('Introduce the name of your video:\n')
video = input()

subprocess.call(['ffmpeg', '-ss', '120', '-i', video, '-t', '10', '-c', 'copy', 'BBBcutted.mp4'])

print('We have cutted your video to a length of 10s, and named it as BBBcutted.mp4')
print('What do you want to do with your video?:')
print('1- Extract the YUV histogram')
print('2- Resize the video')
print('3- Convert audio to mono and change the audio codec')


while True:
    option = int(input("-> "))

    if option == 1:
        subprocess.call(['ffmpeg', '-i', 'BBBcutted.mp4', '-vf',
                         'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay', 'BBBcutted_histogram.mp4'])
        print('Now you have your video with the display of the YUV histogram, saved as BBBcutted_histogram.mp4')
        break

    elif option == 2:
        print('Which resize do yo want to apply?')
        print('1- 720p')
        print('2- 480p')
        print('3- 360x240')
        print('4- 160x120')
        resize_option = int(input("-> "))

        if resize_option == 1:
            subprocess.call(['ffmpeg', '-i', 'BBBcutted.mp4', '-vf', 'scale=-1:720', 'BBBcutted720p.mp4'])
        if resize_option == 2:
            subprocess.call(['ffmpeg', '-i', 'BBBcutted.mp4', '-s', 'hd480',
                             'c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-strict', '-2', 'BBBcutted480p.mp4'])
        if resize_option == 3:
            subprocess.call(['ffmpeg', '-i', 'BBBcutted.mp4', '-vf', 'scale=360:240', 'BBBcutted360x240.mp4'])
        if resize_option == 4:
            subprocess.call(['ffmpeg', '-i', 'BBBcutted.mp4', '-vf', 'scale=160:120', 'BBBcutted160x120.mp4'])
        break

    elif option == 3:
        subprocess.call(['ffmpeg', '-i', 'BBBcutted.mp4', '-ac', '1', '-acodec', 'mp3', 'BBBmono.mp4'])
        break

    else:
        print("Invalid option")
