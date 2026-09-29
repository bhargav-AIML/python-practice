def vowelsconsonants(lines):
    vowels=0
    consonants=0
    for ch in lines:
        if ch in "aeiouAEIOU":
            vowels+=1
        elif ch.isalpha:
            consonants+=1
    return vowels,consonants
def digitspaces(lines):
    digits=0
    space=0
    for ch in lines:
        if ch == " ":
            space+=1
        elif ch.isdigit:
            digits+=1
    return digits,space
def reversepalindrome(lines):
    Reversed=lines[::-1]
    palindromecheck=""
    if lines == Reversed:
        palindromecheck="palindrome"
    else:
        palindromecheck="not palindrome"
    return Reversed,palindromecheck
def frequency(lines):
    Frequency={}
    for ch in lines:
        if ch in Frequency:
            Frequency[ch]+=1
        else:
            Frequency[ch]=1
    most_repeat = 0
    most_character = ""
    for ch in Frequency:
        if Frequency[ch]>most_repeat:
            most_repeat=Frequency[ch]
            most_character = ch
    return Frequency,most_repeat
def duplicates(lines):
    removed_duplicates=[]
    for ch in lines:
        if ch not in removed_duplicates:
            removed_duplicates.append(ch)
    removed=''.join(removed_duplicates)
    return removed
line=input("enter line")
vowels,consonants=vowelsconsonants(line)
digits,spaces=digitspaces(line)
reverse,palindromecheck=reversepalindrome(line)
frquency=frequency(line)
duplicate=duplicates(line)
print("number of vowels: ",vowels)
print("number of consonents: ",consonants)
print("number of digits: ",digits)
print("number of spaces: ",spaces)
print("reversed line: ",reverse)
print("palindrome check: ",palindromecheck)
print("frquency of each character: ",frquency)
print("removed duplicate list",duplicate)

    
