import courts
import general_reference
import parties
import states

# def format_party_name(str):
#   formatted_name = ""
#   org_words = str.split()
#   for word in org_words:
#     if word == word.upper() and word not in general_reference.initials:
#       if word in party_name_exceptions.allowed_abbrvs.keys():
#         word = party_name_exceptions.allowed_abbrvs[word]
#       elif word in party_name_exceptions.allowed_lowers.keys():
#         word = party_name_exceptions.allowed_lowers[word]
#       elif word not in party_name_exceptions.capitalized_acronyms:
#         word = word.capitalize()
#       if word in states.us_state_abbrvs.keys():
#         word = states.us_state_abbrvs[word]
#       formatted_name += word + " "
#   # This is breakable, only works for "LLC," right now
#   if formatted_name[-2] == ',' and formatted_name[-5:-2] != "LLC":
#     formatted_name = formatted_name[:-2]
#   else:
#     formatted_name = formatted_name[:-1]
#   return formatted_name




def convert_citation(raw_citation, pages):
  citation_list = raw_citation.split('\r\n')
  case_id = citation_list[0]
  court = courts.find_court(citation_list[1], citation_list[2])
  v_location = citation_list.index('v.')
  raw_party_1 = citation_list[v_location - 1]
  party_1 = parties.format_party_name(raw_party_1)
  raw_party_2 = citation_list[v_location + 1]
  party_2 = parties.format_party_name(raw_party_2)
  year = citation_list[-1][-5:-1]
  consolidated_citation = "%s v. %s, %s, %s (%s%s)." % (party_1, party_2, case_id, pages, court, year)
  return consolidated_citation