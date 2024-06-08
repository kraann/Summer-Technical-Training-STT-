def reverse(s: str) -> str:
    
    words = s.split()
    
    words.reverse()

    reversed_s = ' '.join(words)
    return reversed_s

s = "the sky is blue"
print(reverse(s)) 
