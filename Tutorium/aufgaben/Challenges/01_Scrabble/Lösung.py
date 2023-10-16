#%
# import sys, os
# sys.path.insert(0, os.path.realpath(__file__) )

#%
from data import DICTIONARY, LETTER_SCORES

def load_words() -> list:
      """Load dictionary into a list and return list"""
      with open(DICTIONARY) as file:
            words = file.read()
      return words.split("\n")
# load_words()[-5:]


def calc_word_value(word) -> int:
      """Calculate the value of the word entered into function
      using imported constant mapping LETTER_SCORES"""
      mp = map(lambda char: LETTER_SCORES.get(char.upper(), 0), word)
      return sum(mp)


def max_word_value( word_list = load_words() ):
      """Calculate the word(s) with the max value, 
      can receive a list of words as arg, if none provided uses default DICTIONARY"""
      word_list.sort(key = calc_word_value, reverse = True )
      results = []
      max_value = calc_word_value(word_list[0])
      for word in word_list:
            if calc_word_value(word)==max_value:
                  results.append(word)
            else:
                  break
      return results


if __name__ == "__main__":
      print(max_word_value())
