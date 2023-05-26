class FirstSolution:
    def reverseWords(self, s: str) -> str:
        s = ' '.join(s.split()) # removing any leading, trailing, and extra spaces
        words = s.split(' ')
        words.reverse()

        return ' '.join(words)


class SecondSolution:
    def reverseWords(self, s: str) -> str:
        words = ' '.join(s.split()).split(' ')
        words.reverse()

        return ' '.join(words)

class ThirdSolution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()

        return ' '.join(words)