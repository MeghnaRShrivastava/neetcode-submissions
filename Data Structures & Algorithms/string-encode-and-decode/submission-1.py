class Solution:

    #Fixed key for the XOR operation 

    _key = 42

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "setinel_empty" #return empty string/sentinel

        #if not empty list:
        encoded_eachstring = []
        for each_string in strs:
            encoded_character = []
            for each_char in each_string:
                #convert the char in num and then xor it to store it as encoded character.
                #Then store it in converted character i.e encoded_character
                #The append it to the encoded_string to pass it on to the decode function
                en_ch = ord(each_char) ^ self._key #encode a character
                encoded_character.append(chr(en_ch)) #store in the encoded list
            encoded_eachstring.append("".join(encoded_character)) #join each character into a word/each string

        return "//".join(encoded_eachstring)



    def decode(self, s: str) -> List[str]:
        if s == "setinel_empty":
            return []

        #If its not empty
        original_list = []
        #break the string from // to create a list
        #For each coded word in an encoded list, convert it into the original character, then word and then original list
        split_list = s.split("//")
        for word in split_list:
            decode_character = []
            for each_ch in word:
                dec_ch = ord(each_ch) ^ self._key
                decode_character.append(chr(dec_ch))
            original_list.append("".join(decode_character))

        return original_list


