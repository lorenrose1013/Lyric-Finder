import requests

r = requests.get('http://www.google.com')
page = r.text

def getLyrics( htmlPage): ## takes html text and gets lyrics out of it
    if("<!-- start of lyrics -->" in htmlPage):
        start =(htmlPage.find("<!-- start of lyrics -->")) ##start of lyrics on page
        start += len("<!-- start of lyrics -->") ## offset to not include that string
        end = (htmlPage.find("<!-- end of lyrics -->")) ## end of lyrics
        lyrics = htmlPage[start:end] # string of just lyrics
        lyrics = lyrics.replace("<br />", "") ## remove breaks
    else:
        lyrics = "nogo"
    return lyrics


print(getLyrics(page))



    

