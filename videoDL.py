import re
import os

def timeCalculator(time):
    print("Time:", time)
    mins, sec = divmod(time, 60)
    print(mins, sec)
    if mins < 10:
        mins = "0" + str(mins)
    return("00:" + str(mins) + ":" + str(sec))

if input("Would you like to create a new clips folder? (y/n): ") == "y":
    os.system("rm -r clips")
    os.system("mkdir clips")

with open('output.txt', 'r') as o:
    for line in o:
        url = re.search(r"(?<=url = ).*?(?=,)", line).group(0)
        word = re.search(r"(?<=word = ).*?(?=$)", line).group(0)
        time = int(re.search(r"(?<=\=)[0-9]+", url).group(0))
        startTime = (timeCalculator(int(time) - 2))
        endTime = (timeCalculator(int(time) + 4))
        print("Downloader starting for word: ", word)
        os.system(f"youtube-dl --external-downloader ffmpeg --external-downloader-args '-ss {startTime} -to {endTime}' -o './clips/{word}.%(ext)s' -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' '{url}'")
