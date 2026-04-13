def translate(text):
    vowels = 'aeiou'
    specials = ('xr', 'yt')
    result = []

    for word in text.split():
        # Regla 1: starts with vowel or "xr"/"yt"
        if word[:2] in specials or word[0] in vowels:
            result.append(word + 'ay')
            continue

        # If there is no traditional vowel, add 'y' to the group
        vowset = vowels
        if not any(ch in vowels for ch in word):
            vowset += 'y'

        # Look for the first vowel (respecting 'qu')
        i = 0
        while i < len(word):
            if word[i] == 'q' and i + 1 < len(word) and word[i+1] == 'u':
                i += 2
            elif word[i] not in vowset:
                i += 1
            else:
                break

        # Add the word to the result
        result.append(word[i:] + word[:i] + 'ay')

    return ' '.join(result)
            
