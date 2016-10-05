import states
import party_name_exceptions
import general_reference

def find_state(str):
  state_loc = ""
  for state in states.us_states:
    if state in str:
      state_loc = states.us_state_abbrvs[state]
      break
  return state_loc

def format_party_name(str):
  formatted_name = ""
  org_words = str.split()
  for word in org_words:
    if word == word.upper() and word not in general_reference.initials:
      if word in party_name_exceptions.allowed_abbrvs.keys():
        word = party_name_exceptions.allowed_abbrvs[word]
      elif word in party_name_exceptions.allowed_lowers.keys():
        word = party_name_exceptions.allowed_lowers[word]
      elif word not in party_name_exceptions.capitalized_acronyms:
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


def find_court(str1, str2):
  if str1 == "Supreme Court of the United States":
    court = ""
  elif str1 == "United States Court of Appeals,":
    for word in str2.split():
      if word in general_reference.order_numerals.keys():
        court = "%s Cir. " % general_reference.order_numerals[word]
  elif "United States District Court" in str1:
    split_court = str1.split(", ")
    court = states.abbrev_state(split_court[1]) + " "
  elif "Appeals" in str1:
    court = "%s App. " % find_state(str1)
  else:
    court = find_state(str1) + " "
  return court


def convert_citation(raw_citation, pages):
  citation_list = raw_citation.split('\r\n')
  case_id = citation_list[0]
  # state = find_state(citation_list[1])
  court = find_court(citation_list[1], citation_list[2])
  v_location = citation_list.index('v.')
  raw_party_1 = citation_list[v_location - 1]
  party_1 = format_party_name(raw_party_1)
  raw_party_2 = citation_list[v_location + 1]
  party_2 = format_party_name(raw_party_2)
  year = citation_list[-1][-5:-1]
  consolidated_citation = "%s v. %s, %s, %s (%s%s)." % (party_1, party_2, case_id, pages, court, year)
  return consolidated_citation