class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        current = 0
        decoded = []
        while current < len(s):
            sep = s.find(":", current)
            length = int(s[current:sep])
            current = sep + 1
            decoded.append(s[current:current+length])
            current += length

        return decoded
