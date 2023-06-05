# Write a program that prompts the user to enter a sentence, 
# and then prints out the number of times each letter appears in the sentence. 
# The output should be sorted alphabetically.

sentence =input("Please write me a sentence ")

print(sentence)

# To count each later in the sentence 

count_dic = {}

for char in sentence:
    if char.isalpha():
        # I check if a key is in a dictionary
        if char in count_dic:
            value = count_dic[char]
            #  updating the value stored in the dictionary
            count_dic[char] = value + 1
        
        else:

            # adding a new key value pair to the dictionary
            count_dic[char] = 1

print(count_dic)