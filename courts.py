import general_reference
import states


# Court methods

def supreme_crt(str1, str2):
  return ""

def us_crt_appeals(str1, str2):
  for word in str2.split():
    if word in general_reference.order_numerals.keys():
      return "%s Cir. " % general_reference.order_numerals[word]

def us_dist_crt(str1, str2):
  split_court = str1.split(", ")
  return states.abbrev_state(split_court[1]) + " "

def appeals(str1, str2):
  return "%s App. " % states.find_state(str1)


# Court Storage

courts = {
  "Supreme Court of the United States": supreme_crt,
  "United States Court of Appeals": us_crt_appeals,
  "United States District Court": us_dist_crt,
  "Appeals": appeals
}

sorted_courts = [
  "Supreme Court of the United States",
  "United States Court of Appeals",
  "United States District Court",
  "Appeals"
]

def find_court(str1, str2):
  for court in sorted_courts:
    if court in str1:
      return courts[court](str1,str2)
  return states.find_state(str1) + " "
  # court = str
  # if str1 == "Supreme Court of the United States":
  #   court = ""
  # elif str1 == "United States Court of Appeals,":
  #   for word in str2.split():
  #     if word in general_reference.order_numerals.keys():
  #       court = "%s Cir. " % general_reference.order_numerals[word]
  # elif "United States District Court" in str1:
  #   split_court = str1.split(", ")
  #   court = states.abbrev_state(split_court[1]) + " "
  # elif "Appeals" in str1:
  #   court = "%s App. " % states.find_state(str1)
  # else:
  #   court = states.find_state(str1) + " "
  # return court