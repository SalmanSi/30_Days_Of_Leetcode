class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        

        def check_v_error(q,word):
            q=q.lower()
            word=word.lower()
            vowels="aeiou"
            if len(q)!=len(word):
                return False
            for i in range(len(q)):
                if q[i] != word [i]:
                    if q[i] in vowels and word[i] in vowels:
                        pass
                    else:
                        return False
            return True
        answer=[]
        # 1- exact match, then return same
        # 2- capitilzation mismatcj
        # 3- vowel error
        # 4- no match
        vowels="aeiou"
        def replace(word):
            word=list(word)
            for i in range(len(word)):
                if word[i] in vowels:
                    word[i]="*"
            return "".join(word)

        lower_map=defaultdict(list)
        error_map=defaultdict(list)
        for word in wordlist:
            lower_map[word.lower()].append(word)
            key=replace(word.lower())
            error_map[key].append(word)
        actual_set=set(wordlist)

        print(error_map)
        for q in queries:
            if q in actual_set:
                answer.append(q)
            elif q.lower() in lower_map:
                answer.append(lower_map[q.lower()][0])
            else:
                key=replace(q.lower())
                answer.append(error_map.get(key,[""])[0])
        return answer