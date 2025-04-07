# Mysteryc
    #### Video Demo:  https://youtu.be/gZihelJX7K8
    #### Description:
    **Mysteryc** is python program designed to be a unique way of allowing users to test their knowledge of their favorite songs, by guessing missing lyrics. It utilizes the Musixmatch API to extract the lyrics.

    ##Introduction

    By using Mysteric, you can challenge your memory when it comes to song lyrics.It generates an incomplete version of any song you choose, and your goal is to complete it.

    ##Features

    - Interactive guessing game for song lyrics.
    - Utilizes the Musixmatch API to extract lyrics(30% of the lyrics of each song).
    - It allows to choose up to 3 difficulty levels: easy, medium, and hard. By increasing the difficulty, you will have more lyrics to guess.
    - Tracks correct and total guesses to keep you informed of your progress.

    ##Files contents

    -project.py

    1.**main()** In this file there is the main program which contains a main function asking for the user's input on the name of the artist and song they want to use, apart from the calling of multiple functions contained in the program. Also there is a couple of printed visual effects to make the experience of reading the lyrics more readable and ejoyable.

    2.**get_lyrics(song, name)** The first function in the project.py is **get_lyrics** which uses the **matcher_lyrics_get(song, name)** function from the Musixmatch API, utilizing the *musixmatch-py* package which returns the lyrics as a song as a json file, including the song lyrics in a *lyrics_body* key/value pair that is extracted and later separated by new lines(or "\n") to make a list, that has the lines of the song as elements. (Also in this function some extra text is removed from what is returned which is not useful for the program). And it raises a ValueError in case the song or the artist name don't exist or are not a match when combining them.

    3.**remove_lyrics(lines)** This function takes as an argument the return value of the **get_lyrics** function, and then removes one word of the song and replaces it with as many **-** as it has letters therein.

    4.**set_level(lines)** Mysteric also has a function that can set the diffulty in the game, using the length of the song to determine proportionally how many words should be removed from the song. By increasing the diffculty you increase the number of times by which the **remove_lyrics** function is called. If the user doesn't input a value that ranges from easy, medium or hard, then the program will ask the user to reprompt for a new difficulty.

    5.**guess_missing_words(complete_song, incomplete_song)** Finally the program ends with the guessing function, which passes as arguments the complete song and the incomplete song, and before this function is called, the user will get the incomplete song printed to make the corresponding guesses. The guesses are made individually, meaning that each word must be guessed one by one, with the program informing the user of which word has to be guessed in each try, and also showing the user the right answer in case that they input a wrong guess. At the end of the game, the user will get a score on how well they did in guessing the lyrics.

    -test_project.py

    Since most of the functions are difficult to test since they have a different or randomized output in every try (since the matcher_lyrics_get function always returns different lyrics for the same song in multiple tries), the only tested funtion is the **get_lyrics** function, to make sure that it raises a *ValueError* in case that a invalid song name or artist name is entered and that the extra characters that come with the original function output are deleted.


    ##Design choices

    -I decided to use *-* instead of *_* to represent the missing lyrics, so the user can know how many letters there are in the missing word.