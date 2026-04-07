class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:return ""

        t_dict = collections.Counter(t)
        required_length = len(t_dict) 

        filtered_s = []
        for i, ch in enumerate(s):
            filtered_s.append((i,ch))

        l, r =0,0
        char_match =0
        dict_filtered_s = {}
        ans = float('inf'), None, None
        while r < len(filtered_s):
            character = filtered_s[r][1]
            dict_filtered_s[character] = dict_filtered_s.get(character,0) + 1
            if dict_filtered_s[character] == t_dict[character]:
                char_match +=1

            while l <=r and char_match == required_length:
                character = filtered_s[l][1]
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                dict_filtered_s[character] -=1
                if dict_filtered_s[character] < t_dict[character]:
                    char_match -=1
                l +=1
            r +=1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]           


        