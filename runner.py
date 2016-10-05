import string_parser
try:
    input = raw_input
except NameError:
    pass

# pages = input("What pages are referred? ")

# troubleshooting comparison:
# for i in range(len(real_6)):
#   print(real_6[i], real_6[i] == generated_6[i] )
# troubleshooting comparison:

def test(num, raw, real, pages):
  generated = string_parser.convert_citation(raw,pages)
  correct_citation = generated == real
  if correct_citation:
    print("#%i: PASS" % (num))
  else:
    print("#%i: FAIL" % (num))
    print("Real:\n %s" % real)
    print("Generated:\n %s" % generated)
    for i in range(len(real)):
      if real[i] != generated[i]:
        print("* char%i (real, generated): %s, %s" % (i, real[i], generated[i]))
        break
  print("------")


raw_6 = "903 So. 2d 913\nSupreme Court of Florida\nCRESCENT MIAMI CENTER, LLC, Petitioner,\nv.\nFLORIDA DEPARTMENT OF REVENUE, Respondent.\nNo. SC03-2063. May 19, 2005."
real_6 = "Crescent Miami Ctr., LLC, v. Fla. Dep't of Revenue, 903 So. 2d 913, 914-15 (Fla. 2005)."

raw_7 = "132 S.W. 3d 501\nCourt of Appeals of Texas\nHouston (1st Dist.).\nMichael Marvin MCKITTRICK, Appellant,\nv.\nThe STATE of Texas, Appellee.\nNo. 01-03-00056-CR. Feb. 19, 2004. Petition for Discretionary Review Refused Aug. 31, 2004."
real_7 = "McKittrick v. State, 132 S.W. 3d 501, 502 (Tex. App. 2004)."

raw_8 = "959 F. Supp. 1040\nUnited States District Court, E.D. Wisconsin.\nCarol RUSHMAN, Plaintiff\nv.\nCITY OF MILWAUKEE, Defendant.\nCivil Action No. 95-C-1096. March 27, 1997."
real_8 = "Rushman v. City of Milwaukee, 959 F. Supp. 1040, 1042 (E.D. Wis. 1997)."

raw_9 = "930 F.2d 204\nUnited States Court of Appeals,\nSecond Circuit.\nMarshall RATTNER, Marshall Rattner Inc., National Limousine Service, Inc., and Profession Indemnity Agency, Plaintiffs-Appellants,\nv.\nMalcolm NETBURN, John B. Farrington, and The Incorporated Village of Pleasantville, Defendants-Appellees.\nNo. 178, Docket 90-7317. Argued Oct. 1, 1990. Decided April 9, 1991."
real_9 = "Rattner v. Netburn, 930 F.2d 204, 210 (2d Cir. 1991)."

# This Supreme Court case refers to 531 U.S. 98 - I don't know where this came from
raw_10 = "121 S. Ct. 525\nSupreme Court of the United States\nGeorge W. BUSH, et al., Petitioners,\nv.\nAlbert GORE, Jr., et al.\nNo. 00-949. Argued Dec. 11, 2000 Dec. 12, 2000."
real_10 = "Bush v. Gore, 531 U.S. 98, 99–100 (2000)."



test(6, raw_6, real_6, "914-15")
test(7, raw_7, real_7, "502")
test(8, raw_8, real_8, "1042")
test(9, raw_9, real_9, "210")
test(10, raw_10, real_10, "99-199")


"""

903 So. 2d 913
Supreme Court of Florida
CRESCENT MIAMI CENTER, LLC, Petitioner,
v.
FLORIDA DEPARTMENT OF REVENUE, Respondent.
No. SC03-2063. May 19, 2005.

914-15

"""