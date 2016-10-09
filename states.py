us_states = [
  "Alabama",
  "Alaska",
  "Arizona",
  "Arkansas",
  "California",
  "Colorado",
  "Connecticut",
  "Delaware",
  "Florida",
  "Georgia",
  "Hawaii",
  "Idaho",
  "Illinois",
  "Indiana",
  "Iowa",
  "Kansas",
  "Kentucky",
  "Louisiana",
  "Maine",
  "Maryland",
  "Massachusetts",
  "Michigan",
  "Minnesota",
  "Mississippi",
  "Missouri",
  "Montana",
  "Nebraska",
  "Nevada",
  "New Hampshire",
  "New Jersey",
  "New Mexico",
  "New York",
  "North Carolina",
  "North Dakota",
  "Ohio",
  "Oklahoma",
  "Oregon",
  "Pennsylvania",
  "Rhode Island",
  "South Carolina",
  "South Dakota",
  "Tennessee",
  "Texas",
  "Utah",
  "Vermont",
  "Virginia",
  "Washington",
  "West Virginia",
  "Wisconsin",
  "Wyoming"
]

us_state_abbrvs = {
  'Florida': "Fla.",
  "Texas": "Tex.",
  "Wisconsin": "Wis."
}

def abbrev_state(str):
  abbrev_str = str
  # Find replace state name with abbreviation
  for state, abbrev in us_state_abbrvs.items():
    if state in abbrev_str:
      abbrev_str = abbrev_str.replace(state, abbrev)
  # Remove any trailing punctuation
  if abbrev_str[-2] == '.':
    return abbrev_str[:-1]
  # Return abbreviated state
  return abbrev_str



def find_state(string):
  for state in us_states:
    if state in string:
      return us_state_abbrvs[state]
  return False