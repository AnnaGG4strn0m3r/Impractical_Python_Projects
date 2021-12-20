from my_utils import process_choice, find_anagrams


def my_process_choice(name): 
    print('my_process_choice:', name)
    #return 'Yamada Taro' - always return same things no matter what 
    #don't mix up with function you imported 
    return name

def main(name):
    print('main name:', name)
    name=''.join(name.lower().split()) 
    name=name.replace('-','')
    phrase=''
    #limit=17 - will continue in endless loop if not match with input
    limit=len(name)
    running=True
    counter=0 
    print('beginning:', counter)
    print('Entering main')
    word_list = []
    while running:
        counter+=1
        print('while loop running:', running, 'counter:', counter)
        temp_phrase=phrase.replace(' ','')
        print('temp_phrase length:',len(temp_phrase), 'limit:', limit)
        if len(temp_phrase) < limit:
            print('working')
            #phrase='ryouzaburousuzuki'
            find_anagrams(name, word_list)
            phrase=process_choice(name) #importinng from my_utils.py
            print('phrase:', phrase)
            phrase=name
        elif len(temp_phrase) == limit:
            print('finishing up')
            break #escape while 


#print('before main')

if __name__=='__main__':
    ini_name=input('Please Input your Name:')
    print(ini_name) #you can change how you call it 
    main(ini_name)
    #main('akiko kobayashi')
#print('after main')