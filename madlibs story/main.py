import os
import re

if os.path.exists("story.txt"):
    print("file hai bhai")
with open("story.txt", "r+") as file:
    story=file.read()

placeholders=["<place>", "<adjective>", "<animal>","<verb>", "<noun>", "<character>", "<emotion>", "<object>", "<wish>"]
user_input={}
def take_input():
  for placeholder in placeholders: 
    word = input(f"enter a {placeholder.strip("<>")}: ") 
    user_input[placeholder]=word
  return user_input

def replace_word(story, user_input):
    for placeholder, word in user_input.items():
         story=re.sub(re.escape(placeholder), word, story) #re.sub("word to be replaced", "replacing word", "string in which the changes has to be made")
    return story
    
take_input()
newStory=replace_word(story, user_input)

with open("story.txt", "r+") as file:
    file.write(newStory)
