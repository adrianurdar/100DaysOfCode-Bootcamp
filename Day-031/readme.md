# Flashcard App
## Day 31 - Intermediate - \#100DaysOfCode

**To do:**
* Create a flashcard app

**Acceptance criteria:**
* Use the images in the image folder, to create the following user interface. The ❌ and ✅ are buttons. 
You can add images to buttons like this: 
```
my_image = PhotoImage(file="path/to/image_file.png")
button = Button(image=my_image, highlightthickness=0)
```
* Fonts, measurements and positioning:
```
padx = 50
pady = 50
card width = 800
card height = 525
language word font = ("Arial", 40, "italic)
language word coordinates = (x=400, y=150)
word font = ("Arial", 60, "italic)
word coordinates = (x=400, y=263)
the flash card taking up 2 columns
```
* Read the data from the `french_words.csv` file in the data folder.

* Pick a random French word/translation and put the word into the flashcard. Every time you press the ❌ or ✅ buttons,
it should generate a new random word to display.

* After a delay of 3s (3000ms), the card should flip and display the English translation for the current word.

* The card image should change to the `card_back.png` and the text colour should change to white. The title of the card 
should change to "English" from "French".

* When the user presses on the ✅ button, it means that they know the current word on the flashcard and that word 
should be removed from the list of words that might come up.

e.g. If `french_words.csv` had only 3 records:
```
chaque,each
parlé,speak
arrivé,come
```
After the user has seen `parlé,speak` it should be removed from the list of words that can come up again.

* The updated data should be saved to a new file called `words_to_learn.csv`

e.g. `words_to_learn.csv`
```
chaque,each
arrivé,come
```

* The next time the program is run, it should check if there is a `words_to_learn.csv` file. If it exists, the program 
should use those words to put on the flashcards. If the `words_to_learn.csv` does not exist (i.e., the first time the 
program is run), then it should use the words in the `french_words.csv`

* We want our flashcard program to only test us on things we don't know. So if the user presses the ✅ button, that 
means the current card should not come up again.
