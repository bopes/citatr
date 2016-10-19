from citatr.converter_pkg import courts, parties, reporters, states, years

def convert_citation(input_citation, pages):
  citation_list = input_citation.split('\r\n')
  reporter = reporters.find_reporter(citation_list)
  court = courts.find_court(citation_list)
  party_1, party_2 = parties.find_parties(citation_list)
  year = years.find_year(citation_list)

  output_citation = "%s v. %s, %s, %s (%s%s)." % (party_1, party_2, reporter, pages, court, year)
  # output_citation = "<em>%s v. %s</em>, %s, %s (%s%s)." % (party_1, party_2, reporter, pages, court, year)
  return output_citation