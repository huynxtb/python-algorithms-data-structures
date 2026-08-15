from typing import List

class LZW:
    """
    Lempel-Ziv-Welch (LZW) compression and decompression algorithm implementation.
    """

    @staticmethod
    def compress(uncompressed: str) -> List[int]:
        """
        Compresses a input string into a list of integer codes.
        """
        if not uncompressed:
            return []

        dict_size = 256
        dictionary = {chr(i): i for i in range(dict_size)}

        w = ""
        result = []
        for c in uncompressed:
            wc = w + c
            if wc in dictionary:
                w = wc
            else:
                result.append(dictionary[w])
                dictionary[wc] = dict_size
                dict_size += 1
                w = c

        if w:
            result.append(dictionary[w])
        return result

    @staticmethod
    def decompress(compressed: List[int]) -> str:
        """
        Decompresses a list of LZW integer codes back into a string.
        """
        if not compressed:
            return ""

        dict_size = 256
        dictionary = {i: chr(i) for i in range(dict_size)}

        w = chr(compressed[0])
        result = [w]
        for k in compressed[1:]:
            if k in dictionary:
                entry = dictionary[k]
            elif k == dict_size:
                entry = w + w[0]
            else:
                raise ValueError(f"Invalid compressed code: {k}")

            result.append(entry)
            dictionary[dict_size] = w + entry[0]
            dict_size += 1
            w = entry

        return "".join(result)
