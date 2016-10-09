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

lowercase_prefixes = [
  'Mc',
  'Mac'
]

def has_lowercase_prefix(word):
  for prefix in lowercase_prefixes:
    if word.startswith(prefix):
      word = word.replace(prefix,"")
      if word == word.upper():
        return True
  return False

def part_of_party_name(word):
  if word == word.upper() and word not in general_reference.initials:
    return True
  elif has_lowercase_prefix(word):
    return True
  return False

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

def correct_capitalization(word):
  output = ""
  if converted(word):
    return converted(word)
  elif nonconverted(word):
    return word
  elif states.find_state(word.capitalize()):
    return states.find_state(word.capitalize())
  elif has_lowercase_prefix(word):
    for prefix in lowercase_prefixes:
      if word.startswith(prefix):
        rest_of_word = word.replace(prefix,"")
        return prefix + rest_of_word.capitalize()
  else:
    return word.capitalize()
  output += " "

def has_trailing_punc(party_name):
  if party_name[-2] in string.punctuation:
    for punc_word in trailing_punc:
      if party_name[:-2].endswith(punc_word):
        return True
  return False

def correct_trailing_punc(party_name):
  if has_trailing_punc(party_name):
    return party_name[:-1]
  elif party_name[-2] in string.punctuation:
    return party_name[:-2]
  else:
    return party_name[:-1]

def get_party_name(party):
  party_list, party_name = party.split(), ""
  for word in party_list:
    if part_of_party_name(word):
      party_name += correct_capitalization(word) + " "
  party_name = correct_trailing_punc(party_name)
  return party_name

def find_parties(citation_list):
  v = citation_list.index('v.')
  p1, p2 = citation_list[v-1], citation_list[v+1]
  p1, p2 = get_party_name(p1), get_party_name(p2)
  return p1, p2