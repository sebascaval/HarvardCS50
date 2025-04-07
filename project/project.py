from musixmatch import Musixmatch
import random

musixmatch = Musixmatch("2e19cd693263baf48090a04830c728b9")  # this is my API key to use the Musixmatch API


def main():
    artist = input("What's the artist's which you would like to test yourself with? ")
    song_title = input("Which song would you like to test yourself with?")
    lyrics = get_lyrics(song_title, artist)
    incomplete_song = set_level(lyrics.copy())
    print("\n\n" + song_title + ", " + artist + "\n\n")  ##
    print("-" * 66)
    print(incomplete_song, end="")
    print("-" * 66)
    print("\n")
    guess_missing_words(lyrics, incomplete_song)


def get_lyrics(song, name):
    try:
        lyrics = (musixmatch.matcher_lyrics_get(song, name))["message"]["body"]["lyrics"]["lyrics_body"]
        lines = lyrics.split("\n")
        for line in lines:
            if line == "":
                lines.remove("")
            if line == "******* This Lyrics is NOT for Commercial use *******":
                lines.remove("******* This Lyrics is NOT for Commercial use *******")
            if line == "...":
                lines.remove("...")
        lines.pop(
            len(lines) - 1
        )  # because last space in the lyrics is not deleted by the first if statement cause of the musixmatch function

        return lines

    except TypeError:
        raise ValueError("Invalid artist name and song name combination")


def remove_lyrics(lines):
    chosen_line = random.choice(lines)  # line from which to remove some of the words
    index_of_line = lines.index(chosen_line)
    separated_line = chosen_line.split(" ")
    word_index = random.randint(0, len(separated_line) - 1)
    hidden_word = "" #to get the number of letters in set word and replace them with "-"
    for _ in separated_line[word_index]:
        hidden_word = hidden_word + "-"

    separated_line[word_index] = hidden_word
    lines[index_of_line] = " ".join(separated_line) #to return the song as a string instead of a list of lines

    return lines


def set_level(lines):
    while True:
        level = input("How hard do you want it to be? (easy, medium or hard?)").lower()
        length = len(lines)

        if level == "easy":
            for _ in range(round(length / 3)):
                remove_lyrics(lines)

        elif level == "medium":
            for _ in range(round(length / 2)):
                remove_lyrics(lines)

        elif level == "hard":
            for _ in range(round(length)):
                remove_lyrics(lines)

        else:
            print(
                "Invalid difficulty, input a difficulty between easy, medium or hard!"
            )
            continue

        return "\n".join(lines)


def guess_missing_words(complete_song, incomplete_song):
    hidden_song = incomplete_song.split("\n")
    n_missing = 0
    n_correct = 0  #counter to later inform the user how many answers they got right
    for line in hidden_song:
        for word in line.split(" "):
            if "-" in word:
                n_missing = n_missing + 1
                guess = input("What is the word number " + str(n_missing) + " ?")
                line_index = hidden_song.index(line) #the index of the line in the song to user later
                word_index = line.split(" ").index(word) #the index of the word to later display the correct word in case of mistakes
                correct_line = (
                    complete_song[line_index].lower().replace(",", "").strip()
                )
                correct_word = correct_line.split(" ")[word_index].lstrip(" ")

                if guess.lower().lstrip(" ") == correct_word.lower().lstrip(" "):
                    print("Correct!")
                    n_correct = n_correct + 1
                else:
                    print("Incorrect! The right answer was: " + correct_word) #if the guess is incorrect, the user is informed of the correct answer

    print(f"You got {n_correct}/{n_missing}")


if __name__ == "__main__":
    main()
