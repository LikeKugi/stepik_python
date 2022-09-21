dna = 'attcggagct'.upper()
print(dna)          # ATTCGGAGCT
print(dna[1])       # T
print(dna[1:4])     # TTC
print(dna[:4])      # ATTC
print(dna[4:])      # GGAGCT
print(dna[-4:])     # AGCT
print(dna[1:-1])    # TTCGGAGC
print(dna[1:-1:2])  # TCGG
print(dna[::-1])    # TCGAGGCTTA


genome1 = 'caggtggac'.upper()
genome2 = 'gattaca'.upper()

s = genome2
i=0
j=len(s)-1
is_palindrome = True
while i<j:
    if s[i] != s[j]:
        is_palindrome = False
        break
    i+=1
    j-=1
print(s)
print('yes' if is_palindrome else 'no')

genreverse = genome1[::-1]
print(genome1,genreverse)
print('yes' if genome1 == genreverse else 'no')

s = 'abcdefghijk'
print(s[3:6],end=' ')
print(s[:6],end=' ')
print(s[3:], end=' ')
print(s[::-1], end=' ')
print(s[-3:], end=' ')
print(s[:-6], end=' ')
print(s[-1:-10:-2])