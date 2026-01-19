class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # number = 10
        # binary_string_no_prefix = bin(number)[2:]
        # print(binary_string_no_prefix)
        lst_date = date.split("-")
        str_date= ""
        binary_list=[]
        for date in lst_date:
            
            int_date = int(date)
            binary_date = bin(int_date)[2:]
            # for date in binary_date:
            
            binary_list.append(binary_date)
        return "-".join(binary_list)
        