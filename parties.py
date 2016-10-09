import general_reference
import states

import string

capitalized_acronyms = [
  "LLC",
  "LLC,"
]

allowed_abbrvs = {
  "CENTER": "Ctr.",
  "CENTER,": "Ctr.,",
  "DEPARTMENT": "Dep't"
}

allowed_lowers = {
  'OF': 'of',
}


# def format_party_name(str):
  # party_name = ""
  # org_words = str.split()
  # for word in org_words:
  #   if word == word.upper() and word not in general_reference.initials:
  #     if word in allowed_abbrvs.keys():
  #       word = allowed_abbrvs[word]
  #     elif word in allowed_lowers.keys():
  #       word = allowed_lowers[word]
  #     elif word not in capitalized_acronyms:
  #       word = word.capitalize()
  #     if word in states.us_state_abbrvs.keys():
  #       word = states.us_state_abbrvs[word]
  #     party_name += word + " "
  # # This is breakable, only works for "LLC," right now
  # if party_name[-2] == ',' and party_name[-5:-2] != "LLC":
  #   party_name = party_name[:-2]
  # else:
  #   party_name = party_name[:-1]
  # return party_name

converters = [
  allowed_abbrvs,
  allowed_lowers
]

nonconverters = [
  capitalized_acronyms
]

trailing_punc = [
  'LLC'
]

def part_of_party_name(word):
  return word == word.upper() and word not in general_reference.initials

def converted(word):
  for converter in converters:
    if word in converter.keys():
      return converter[word]
  return False

def nonconverted(word):
  for nonconverter in nonconverters:
    if word in nonconverter:
      return word
  return False

def has_trailing_punc(party_name):
  if party_name[-2] in string.punctuation:
    for punc_word in trailing_punc:
      if party_name[:-2].endswith(punc_word):
        return True
  return False

def set_trailing_punc(party_name):
  if has_trailing_punc(party_name):
    return party_name[:-1]
  else:
   return party_name[:-2]

def format_party_name(party):
  party_list = party.split()
  party_name = ""

  # Look at each word in party name
  for word in party_list:
    # Check if word should be kept (is mostly caps)
    if part_of_party_name(word):
      if converted(word):
        party_name += converted(word)
      elif nonconverted(word):
        party_name += word
      elif states.find_state(word.capitalize()):
        party_name += states.find_state(word.capitalize())
      else:
        party_name += word.capitalize()
      party_name += " "

  # Should the party have a trailing comma? If so, keep it
  party_name = set_trailing_punc(party_name)

  return party_name


def find_parties(citation_list):
  v = citation_list.index('v.')
  p1, p2 = citation_list[v-1], citation_list[v+1]
  p1, p2 = format_party_name(p1), format_party_name(p2)
  return p1, p2