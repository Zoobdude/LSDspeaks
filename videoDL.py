import re

text = 'text = "You've never, ever wandered at any pointduring that year and a day.", start = 693.72, url = https://www.youtube.com/watch?v=9kmlwZ_BOvU&t=693s, word = never'

#find the url remove the comma at the end
url = re.search(r"(?<=url = ).*?(?=,)", text).group(0)

print(url)

#find the word
word = re.search(r"(?<=word = ).*?(?=$)", text).group(0)
print(word)