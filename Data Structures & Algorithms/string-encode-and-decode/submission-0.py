class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for s in strs:
            string += str(len(s)) + '#' + s
        return string
    def decode(self, s: str) -> List[str]:
        res = []
        inx = 0
        while inx < len(s):
            tmp = inx
            while s[tmp] != '#':
                tmp += 1
            length = int(s[inx : tmp])
            res.append(s[tmp +1 :tmp+ 1+ length])
            inx = tmp + 1 + length
        return res