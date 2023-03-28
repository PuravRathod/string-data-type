"""used DS T02 as reference. In this programe used 3 functions together in one string- replace , upper & reverse in a string"""

sentence= "The!quick!brown!fox!jumps!over!the!lazy!dog!."
print(sentence.replace("!" , " "))
print(sentence.upper().replace("!"," "))
print(sentence[::-1].upper().replace("!"," "))