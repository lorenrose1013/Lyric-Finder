import urllib2, eyed3
response = urllib2.urlopen('http://azlyrics.com/lyrics/matchbox20/3am.html')
page = response.read()

def getLyricsFromURL(htmlPage): ## takes html text and gets lyrics out of it
    if("<!-- start of lyrics -->" in htmlPage):
        start =(htmlPage.find(". -->")) ##start of lyrics on page
        start += len(". -->") ## offset to not include that string
        end = (htmlPage[start::].find("</div>")) + start ## end of lyrics
        lyrics = htmlPage[start:end] # string of just lyrics
        lyrics = lyrics.replace("<br>", "") ## remove breaks
    else:
        lyrics = "nogo"
    return lyrics

def getLyricsFromData (artist, title):
	artist = artist.toLower().relace(" ", "").replace("the", "")
	title = title.toLower().replace(" ", "")
	url = 'http://azlyrics.com/lyrics/' + artist + "/" + title + '.html'
	return getLyricsFromURL(url)

def getLyricsFromFile(filename):
	audiofile = eyed3.load(filename)
	artist = audiofile.tag.artist 
	title = audiofile.tag.title
	eyed3.id3.tag.Tag.lyrics

	audiofile.tag.save()




print(getLyricsFromURL(page))



    

