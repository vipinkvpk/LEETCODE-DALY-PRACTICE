class Solution:
    def capitalizeTitle(self, title: str) -> str:
        output = list()
        word_arr = title.split()
        for word in word_arr:
            output.append(word.title()) if len(word) > 2 else output.append(word.lower())
        return " ".join(output)
        