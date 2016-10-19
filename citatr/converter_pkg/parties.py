from citatr.converter_pkg import general_reference, states

import string


# Captialization & Punctuation Exceptions Storage

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

trailing_punc = [
  'LLC'
]

lowercase_prefixes = [
  'Mc',
  'Mac'
]


# Higher level list and dict storage

standard_words = [
  allowed_abbrvs,
  allowed_lowers
]

remaining_caps = [
  capitalized_acronyms
]

# Capitalization functions

def is_capitalized(word):
  if word == word.upper() and word not in general_reference.initials:
    return True
  return False

def has_lowercase_prefix(word):
  for prefix in lowercase_prefixes:
    if word.startswith(prefix):
      word = word.replace(prefix,"")
      if word == word.upper():
        return True
  return False

def capitalize_with_prefix(word):
  for prefix in lowercase_prefixes:
    if word.startswith(prefix):
      rest_of_word = word.replace(prefix,"")
      return prefix + rest_of_word.capitalize()

def part_of_party_name(word):
  if is_capitalized(word):
    return True
  elif has_lowercase_prefix(word):
    return True
  return False

def standard_word(word):
  for stan_dict in standard_words:
    if word in stan_dict.keys():
      return stan_dict[word]
  return False

def remain_caps(word):
  for cap_list in remaining_caps:
    if word in cap_list:
      return word
  return False

def correct_capitalization(word):
  output = ""
  # check if word has standard abbreviation or styling
  if standard_word(word):
    return standard_word(word)
  # check if word should remain all caps
  elif remain_caps(word):
    return word
  # check if word is a state (needs to be capitalized)
  elif states.find_state(word.capitalize()):
    return states.find_state(word.capitalize())
  # check if word is all caps except for a prefix
  elif has_lowercase_prefix(word):
    return capitalize_with_prefix(word)
  # capitalize the word normally
  else:
    return word.capitalize()
  output += " "


# Punctuation Functions

def keep_trailing_punc(party_name):
  if party_name[-2] in string.punctuation:
    for punc_word in trailing_punc:
      if party_name[:-2].endswith(punc_word):
        return True
  return False

def remove_trailing_punc(party_name):
  if party_name[-2] in string.punctuation:
    return True
  return False

def correct_trailing_punc(party_name):
  if keep_trailing_punc(party_name):
    return party_name[:-1]
  elif remove_trailing_punc(party_name):
    return party_name[:-2]
  else:
    return party_name[:-1]


# Callable Execution Functions

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