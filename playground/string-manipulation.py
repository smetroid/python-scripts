#!/bin/env/python
#from scipy import stats as st
string = "If whateverthismeanstoyou you're visiting this page, you're likely here because you're searching for a random sentence. Sometimes a random word just isn't enough, and that is where the random sentence generator comes into play. By inputting the desired number, you can make a list of as many random sentences as you want or need. Producing random sentences can be helpful in a number of different ways."


def get_array(sentence):
  array = sentence.split(" ")
  print(array)
  characters = []
  for i in array:
    characters.append(len(i))

  appears_the_most = 0
  print(characters)
  characters.sort()
  for c in characters:
    count = characters.count(c)
    if count >= appears_the_most:
      print("%s character words appears: %s times" % (c, count))
      appears_the_most = count

def main():
  get_array(string)

if __name__ == "__main__":
  main()