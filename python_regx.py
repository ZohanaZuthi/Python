# RegEx means regular expression. It can be used to see if a string contains the specified search pattern.
import re
txt="the rain in spain"
x=re.search("^the.*spain$",txt)
print(x)
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string