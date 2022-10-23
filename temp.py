import re

text = 'text = "<font color="#FFAAFF">And I have to do head math,which is gonna be bad.</font>", start = 418.433, url = https://www.youtube.com/watch?v=FJSI7QTAt_o&t=418s, word = gonna'

#regex to find url in text

url = re.search(r"(?<=url = ).*?(?=,)", text).group(0)


print(url)