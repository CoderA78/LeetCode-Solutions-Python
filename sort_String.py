class Solution:
    def sortSentence(self, s: str) -> str:

        #spliting the s string into words array like ["is2", "a3", "this1", "test4"]
        words = s.split(" ")

        serial_numbers = [] #serial number of words in above array

        #here we are storing the serial numbers into the array extracting from the words array
        for i in range(len(words)): 
            last_element = int(words[i][-1]) # -1 to get the last element, i.e. serial number in original sentance
            serial_numbers.append(last_element)
            

        #here we are storing words according to the serial numbers
        arranged_words = [0]*len(words) # the final order of words
        for i in range(len(serial_numbers)):
            word = words[i][ :-1] # this will return the string till last element, excludes last element
            arranged_words[serial_numbers[i] -1] = word #-1  for 1 based indexing
            

        #then we took an new string to add the array elements into the string with adding spaces    
        final_string = ""

        for i in range(len(arranged_words)):
            final_string += arranged_words[i] 
            if(i != len(arranged_words) - 1): #adding space between words
                final_string += " "
                

        return final_string

sol= Solution()
print(sol.sortSentence("is2 a3 this1 test4"))

        # string "happen"
        # string[:] = "happen"
        # string[1:] = "appen"
        # string[1:-1] = "appe"