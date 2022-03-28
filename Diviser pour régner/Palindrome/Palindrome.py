# Kevin Kuzu

from urllib import response


def palindrome(Tab):
    L = ''
    for i in range (len(Tab),0,-1):
        L= L + Tab[i-1]
    return L == Tab

def palindrome_rec(Tab : str, n : int, L =''):
    if n == 0:
        return L == Tab
    else:
        return palindrome_rec(Tab,n-1, L+Tab[n-1])

#Diviser

def palindrome1(mot):
    n = len(mot)
    i = 0
    while n > 0:
        if mot[i] == mot[n-1]:
            n = n-1
            i = 1+i
        else:
            return False
    return True
    
def palindrome_correction(mot):
    n= len(mot)
    i= 0
    reponse = False
    while i<=n//2-1 and mot[i] == mot[n-i-1]:
        i+=1
    if i == n//2:
        reponse = True
    return reponse

def palindrome_correction_rec(mot, i=0):
    if i<=len(mot)//2-1 and mot[i] == mot[len(mot)-i-1]:
        return palindrome_correction_rec(mot, i+1)
    else:
        return i == len(mot)//2

def palindrome_correction_rec2(mot):
    n = len(mot)
    if n<=1:
        return True
    else:
        return mot[0] == mot[n-1] and palindrome_correction_rec2(mot[1:n-1])

if __name__ == '__main__':
    print('*************Palindrome*************\n')

    print(palindrome('kayak'))
    print(palindrome_rec('kayak',5), '\n')

    print(palindrome1('kayak'))
    print(palindrome_correction('kayak'), '\n')

    print(palindrome_correction_rec('elle'))
    print(palindrome_correction_rec(''))
    print(palindrome_correction_rec('k'))
    print(palindrome_correction_rec('kayak'), '\n')