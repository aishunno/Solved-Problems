from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs: res += str(len(string)) + "#" + string

        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            
            i = j + 1 + length

        return res
    

s = Codec()
print(s.decode(s.encode(["############"])))
        