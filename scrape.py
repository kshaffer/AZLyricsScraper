from os import listdir

def read_html(filename):
    f = open(filename, 'r')
    return f.read()

songlist = []
for file in (listdir('songfiles')):
    songlist.append('songfiles/' + file)

for song in songlist:
    html_text = read_html(song)
    one_big_string = html_text.replace('\n', ' ').replace('\r', ' ')

    a = one_big_string.split('<!-- END OF JANGO PLAYER -->  <div class="lyricsh"> <h2><b>')[1]
    artist = a.split('LYRICS</b></h2> </div>  <div class="ringtone"> <span id="cf_text_top"></span>')[0]
    t = one_big_string.split('<div class="ringtone"> <span id="cf_text_top"></span> </div>  <b>"')[1]
    title = t.split('"</b><br> <br>  <div> <!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->')[0]
    l = one_big_string.split('<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. --> ')[1]
    lyrics = l.split(' </div>  <br>')[0]
    lyrics_clean = lyrics.replace('<br> ', '\n')


    """
    print(artist)
    print(title)
    print('\n')
    """
    print(lyrics_clean)
    print('\n')
