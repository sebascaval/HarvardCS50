from musixmatch import Musixmatch
import random
import json

musixmatch = Musixmatch("2e19cd693263baf48090a04830c728b9")

#response = musixmatch.artist_get(118)
#o = json.dumps(response)
#print (response["message"]["body"]["artist"]["artist_name"])

#response = musixmatch.matcher_lyrics_get('Blue World', 'Mac Miller')
#o = response["message"]["body"]["lyrics"]["lyrics_body"]
#lines = o.split("\n")
#for line in lines:
#    if line == "":
#        lines.remove("")
#    if line == "******* This Lyrics is NOT for Commercial use *******":
#        lines.remove("******* This Lyrics is NOT for Commercial use *******")
#    if line == "...":
#        lines.remove("...")

lyrics = (musixmatch.matcher_lyrics_get("Blue World", "Mac Miller"))["message"]["body"]["lyrics"]["lyrics_body"]
lines = lyrics.split("\n")
for line in lines:
    if line == "":
        lines.remove("")
    if line == "******* This Lyrics is NOT for Commercial use *******":
        lines.remove("******* This Lyrics is NOT for Commercial use *******")
    if line == "...":
        lines.remove("...")
lines.pop(len(lines)-1)



chosen_line=random.choice(lines).split(" ") #line from which to remove some of the words
word_index=random.randint(0,len(chosen_line)-1)
print (word_index)
print (chosen_line[word_index])
hidden_word=""

for letter in chosen_line[word_index]:
    hidden_word= hidden_word + "-"

chosen_line[word_index] = hidden_word

print(chosen_line)
