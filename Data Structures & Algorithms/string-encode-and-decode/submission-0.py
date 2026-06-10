class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        decoded = []
        i = 0

        while i < len(s):
            curr_len = ""
            while s[i] != "#":
                curr_len += s[i]
                i += 1
            curr_len = int(curr_len)

            decoded.append(s[i + 1 : i + curr_len + 1])
            i = i + curr_len + 1
        
        return decoded

