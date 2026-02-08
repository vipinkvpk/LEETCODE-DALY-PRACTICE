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

        

        # def sort_vowels_in_string(s: str) -> str:
        #     """
        #     Sorts the vowels in a string in non-decreasing order of their ASCII values, 
        #     while keeping the consonants in their original positions.
        #     """
        #     # 1. Extract and sort all vowels by ASCII value
        #     vowels = sorted([char for char in s if char.lower() in 'aeiou'])
            
        #     # 2. Convert the original string to a list for mutability
        #     result_list = list(s)
            
        #     # 3. Iterate through the list and replace vowels with sorted vowels
        #     vowel_index = 0
        #     for i in range(len(result_list)):
        #         if result_list[i].lower() in 'aeiou':
        #             result_list[i] = vowels[vowel_index]
        #             vowel_index += 1
                    
        #     # 4. Join the list back into a string
        #     return "".join(result_list)

        # # Example usage
        # input_string = "lEetcOde"
        # output_string = sort_vowels_in_string(input_string)
        # print(f"Original string: {input_string}")
        # print(f"String with sorted vowels: {output_string}")

        # input_string_2 = "programming"
        # output_string_2 = sort_vowels_in_string(input_string_2)
        # print(f"Original string: {input_string_2}")
        # print(f"String with sorted vowels: {output_string_2}")



            

        