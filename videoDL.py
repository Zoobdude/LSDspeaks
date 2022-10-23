import re
import os

def timeCalculator(time):
    print(time)
    mins = time % 60
    sec = time - (mins * 60)
    if mins < 10:
        mins = "0" + str(mins)
    return("00:" + str(mins) + ":" + str(sec))

with open('output.txt', 'r') as o:
    for line in o:
        url = re.search(r"(?<=url = ).*?(?=,)", line).group(0)
        word = re.search(r"(?<=word = ).*?(?=$)", line).group(0)
        time = re.search(r"(?<=\=)[0-9]+", url).group(0)
        print(url, word, time)
        startTime = timeCalculator(int(time) - 3)
        endTime = startTime + 8)
        print(startTime, endTime)
        #os.system(f"youtube-dl --external-downloader ffmpeg --external-downloader-args '-ss {startTime} -to {endTime}' -o './clips/{word}.%(ext)s' -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' 'https://www.youtube.com/watch?v=0iSuyY3a9L0&t=175s'")



#https://www.youtube.com/watch?v=egbJ8p2UVKk&t=537s
#regex to find the numbers after the = in https://www.youtube.com/watch?v=egbJ8p2UVKk&t=537s
