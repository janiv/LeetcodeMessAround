

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        h = len(s) // 2
        first = s[0:h]
        second = s[h:]
        print(first)
        print(second)
        vowels = "aeiou"
        f_count, s_count = 0, 0
        for letter in first:
            if letter in vowels:
                f_count += 1
        for letter in second:
            if letter in vowels:
                s_count += 1
        return f_count == s_count


s = Solution()
test_cases = ["book", "textbook", "test", "oo", "OO", "shalam", "SHaLAm"]
for word in test_cases:
    print(s.halvesAreAlike(word))
