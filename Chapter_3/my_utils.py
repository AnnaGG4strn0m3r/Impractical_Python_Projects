from collections import Counter 
from load_dictionary import load

Counter('tomsakarie')

def process_choice(name):
    print("The return value is anagrams.", name)
    return name

def find_anagrams(name, word_list):
    for word in word_list:
        #print(word)
        name_map = Counter(name)
        word_map = Counter(word.lower()) #lower case 
        result = include_anagram(name_map, word_map)
        if result:
            print('hit!', word)
    #if name_map == word_map:
        #print('The first word in the list was anagrams')
    #else:
        #print('The first word in the list was NOT anagrams ')
       # print('The first word in the list was anagrams')

    #print('it will show the choice of elements in actual code:', name)

def include_anagram(name_map, word_map): #(longer name to check, actual name)
    for letter in word_map:
        #print(letter, word_map[letter], name_map[letter], 1<=name_map[letter], word_map[letter] <=name_map[letter])
        #printing like o['t']: how many ts in a word
        if word_map[letter] > name_map[letter]: 
            return False
    return True #everything is True 



if __name__=='__main__': #other file cannot read when you import
    #below this line is only for my_utils.py file 
    name='tomosakarie' #good for testing this script 
    word_list=['morita', 'sakamotoeri', 'night', 'anna', 'hana', 'tamori', 'satomi', 'tomosakarie', 'osake', 'yamada', ]
    word_list = load('2of4brif.txt')
    find_anagrams(name, word_list)

    #phrase=process_choice(name)
    #print(phrase)

    #word_map = Counter('tamori') #object to call function 
    #name_map = Counter('sakamotorie')
    #result = include_anagram(name_map, word_map) #testing new function 
    #print(result)

#print('ADDING to ndiweyfbquygvqjdfvwekfjbfdgvqeufbjsdfvxkcvbl') #other file can read 
#print('is it true################') #make it long to easily find from other functions

