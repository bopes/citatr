import general_reference
import states

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


def format_party_name(str):
  formatted_name = ""
  org_words = str.split()
  for word in org_words:
    if word == word.upper() and word not in general_reference.initials:
      if word in allowed_abbrvs.keys():
        word = allowed_abbrvs[word]
      elif word in allowed_lowers.keys():
        word = allowed_lowers[word]
      elif word not in capitalized_acronyms:
        word = word.capitalize()
      if word in states.us_state_abbrvs.keys():
        word = states.us_state_abbrvs[word]
      formatted_name += word + " "
  # This is breakable, only works for "LLC," right now
  if formatted_name[-2] == ',' and formatted_name[-5:-2] != "LLC":
    formatted_name = formatted_name[:-2]
  else:
    formatted_name = formatted_name[:-1]
  return formatted_name


def find_parties(ary):
  v_location = ary.index('v.')
  raw_party_1 = ary[v_location - 1]
  party_1 = format_party_name(raw_party_1)
  raw_party_2 = ary[v_location + 1]
  party_2 = format_party_name(raw_party_2)
  return party_1, party_2