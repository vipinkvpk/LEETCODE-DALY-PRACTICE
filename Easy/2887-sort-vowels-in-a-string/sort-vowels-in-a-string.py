class Solution:
    def sortVowels(self, s: str) -> str:
        vowels= sorted([ch for ch in s if ch.lower() in 'aeiou'])
        
        result_list= list(s)

        vowels_index=0
        for i in range(len(result_list)):
            if result_list[i].lower() in 'aeiou':
                result_list[i] = vowels[vowels_index]
                vowels_index +=1 
        return "".join(result_list)


            

        