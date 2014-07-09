from string import lowercase
from itertools import groupby

lines = [line.strip() for line in open('diamond.txt')]

count = 0
sum_of_words = 0
letters = []

def number_of_lines(lines):
    return len(lines)

def number_of_letters(letters):
    count = 0
    for l in letters:
        for ll in l:
            count = count+len(ll)
        return count

for s in lines:
    count = count + 1
    counts = [(len(list(cpart))) for c,cpart in groupby(s) if c == '']
    sum_of_words = sum_of_words + len(counts) + 1
    letters.append(s.split())

print 'number of lines in doc',number_of_lines(lines),"\n"
print 'number of words in doc',sum_of_words,"\n"
print 'number of letters in doc',number_of_letters(letters)


