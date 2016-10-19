"""
Manual check for the conversion algorithm. Is not unittest. Requires CLI execution and manual reivew

"""

import os
import sys

root = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(root)

from citatr.converter_pkg import converter

total_count, fail_count, fails = 0, 0, []

def test(num, raw, real, pages):
  global total_count, fail_count, fails
  total_count += 1
  generated = converter.convert_citation(raw,pages)
  correct_citation = generated == real
  if correct_citation:
    print("#%i: PASS" % (num))
  else:
    fail_count += 1
    fails.append(str(num))
    print("#%i: FAIL" % (num))
    print("Real:\n %s" % real)
    print("Generated:\n %s" % generated)
    for i in range(len(real)):
      if real[i] != generated[i]:
        print("* char%i (real, generated): %s, %s" % (i, real[i], generated[i]))
        break
  print("------")

def display_results():
  global fail_count, total_count, fails
  success_count = total_count - fail_count
  percentage = success_count / total_count * 100
  print()
  print("------")
  print("Results:")
  print("Score: %i / %i (%.1f%%)" % (success_count, total_count, percentage))
  if fail_count > 0:
    print("Failures: %i" % fail_count)
    print("Failed Citations: #" + ", #".join(fails))
  else:
    print("Perfect.")
  print()



raw_6 = "903 So. 2d 913\r\nSupreme Court of Florida\r\nCRESCENT MIAMI CENTER, LLC, Petitioner,\r\nv.\r\nFLORIDA DEPARTMENT OF REVENUE, Respondent.\r\nNo. SC03-2063. May 19, 2005."
real_6 = "Crescent Miami Ctr., LLC, v. Fla. Dep't of Revenue, 903 So. 2d 913, 914-15 (Fla. 2005)."

raw_7 = "132 S.W. 3d 501\r\nCourt of Appeals of Texas\r\nHouston (1st Dist.).\r\nMichael Marvin McKITTRICK, Appellant,\r\nv.\r\nThe STATE of Texas, Appellee.\r\nNo. 01-03-00056-CR. Feb. 19, 2004. Petition for Discretionary Review Refused Aug. 31, 2004."
real_7 = "McKittrick v. State, 132 S.W. 3d 501, 502 (Tex. App. 2004)."

raw_8 = "959 F. Supp. 1040\r\nUnited States District Court, E.D. Wisconsin.\r\nCarol RUSHMAN, Plaintiff\r\nv.\r\nCITY OF MILWAUKEE, Defendant.\r\nCivil Action No. 95-C-1096. March 27, 1997."
real_8 = "Rushman v. City of Milwaukee, 959 F. Supp. 1040, 1042 (E.D. Wis. 1997)."

raw_9 = "930 F.2d 204\r\nUnited States Court of Appeals,\r\nSecond Circuit.\r\nMarshall RATTNER, Marshall Rattner Inc., National Limousine Service, Inc., and Profession Indemnity Agency, Plaintiffs-Appellants,\r\nv.\r\nMalcolm NETBURN, John B. Farrington, and The Incorporated Village of Pleasantville, Defendants-Appellees.\r\nNo. 178, Docket 90-7317. Argued Oct. 1, 1990. Decided April 9, 1991."
real_9 = "Rattner v. Netburn, 930 F.2d 204, 210 (2d Cir. 1991)."

# This Supreme Court case refers to 531 U.S. 98 - I don't know where this came from
raw_10 = "121 S. Ct. 525\r\nSupreme Court of the United States\r\nGeorge W. BUSH, et al., Petitioners,\r\nv.\r\nAlbert GORE, Jr., et al.\r\nNo. 00-949. Argued Dec. 11, 2000 Dec. 12, 2000."
real_10 = "Bush v. Gore, 531 U.S. 98, 99–100 (2000)."



test(6, raw_6, real_6, "914-15")
test(7, raw_7, real_7, "502")
test(8, raw_8, real_8, "1042")
test(9, raw_9, real_9, "210")
test(10, raw_10, real_10, "99-199")

display_results()


"""

903 So. 2d 913
Supreme Court of Florida
CRESCENT MIAMI CENTER, LLC, Petitioner,
v.
FLORIDA DEPARTMENT OF REVENUE, Respondent.
No. SC03-2063. May 19, 2005.

914-15

"""