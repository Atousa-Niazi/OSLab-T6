#Atousa Niazi-98440127-python-OSLab-translate

# dar python or /else darim  :  dar for break ejra she else ejra nemy she va baraks

WORDS_BANK=[]
#############################
def file_check():
    try:
        with open('words_bank.txt','r') as f:
            print('file exist.')
    except:
        print("\033[38;5;202mFile not found. Check the path variable and filename")
        exit()
#############################
def load_data():
    #f=open('words_bank.txt','r')
    with open('words_bank.txt','r') as f :
        big_text=f.read()
        words=big_text.split('\n')
        
        for i in range(0,len(words),2):
            WORDS_BANK.append({'english':words[i],'persian':words[i+1]})
            
    for w in WORDS_BANK:
        print("\033[38;5;204m",w)
    print('\033[38;5;118mloaded!')
#############################
def add():
    print("\033[38;5;215madd a new word:")
    print("to add a new item: ")
    print('english:')
    en_in=input()
    print('persian:')
    fa_in=input()
    adding=[en_in,fa_in]
    WORDS_BANK.append({'english':adding[0],'persian':adding[1]})
    print('do you want to save the new word? (y or n) ')
    answer=input()
    if answer=='y':
        save()
#############################
def input_text_user():
    user_text=input('\033[38;5;78mplease write your text: ')
    return user_text
#############################
def en2fa(user_text):
    output_sentence=''
    user_sentences=user_text.split('.')
    for user_sentence in user_sentences:
        user_words=user_sentence.split(' ')
        output_text=''
        for user_word in user_words:
            for word in WORDS_BANK:
                if user_word == word['english']:
                    output_text+=word['persian']+' '
                    break
            else:
                output_text+=user_word+' '
        output_sentence+=output_text
    return output_sentence
#############################
def fa2en(user_text):
    output_sentence=''
    user_sentences=user_text.split('.')
    for user_sentence in user_sentences:
        user_words=user_sentence.split(' ')
        output_text=''
        for user_word in user_words:
            for word in WORDS_BANK:
                if user_word == word['persian']:
                    output_text+=word['english']+' '
                    break
            else:
                output_text+=user_word+' '
        output_sentence+=output_text
    return output_sentence
#############################
def show_menu():
    print("\033[1;95m~~~~~~~~~~~~~~~~~~~~~~")
    print('Welcome to Sadjad Translator!')
    print('1- Add new word ')
    print('2- Translation english2persian')
    print('3- Translation persian2english')
    print('4- Exit')
    print("~~~~~~~~~~~~~~~~~~~~~~\n")
#############################
def save():
    f=open('words_bank.txt','w') # i opened the file with w to prevent overwritting
    for row in WORDS_BANK:
        f.write(row['english']+'\n'+row['persian'])
    f.close()
    print('\033[38;5;222msaved')
    print('\033[38;5;220m.......................')
#############################

print("\033[38;5;118mloading...")
file_check()
load_data()
print("\033[38;5;220mdatabase loaded. app is ready to use.\n")
while True:
    show_menu()
    print("\033[38;5;33mEnter your choice:")
    choice=int(input())
    
    if choice==1:
        add()
    elif choice==2:
        user_text=input_text_user()
        output_sentence=en2fa(user_text)
        print("\033[38;5;78myour Translated text is :")
        print("\033[38;5;215m",output_sentence)
    elif choice==3:
        user_text=input_text_user()
        output_sentence=fa2en(user_text)
        print("\033[38;5;93myour Translated text is :")
        print("\033[38;5;198m",output_sentence)
    elif choice==4:
        print('good luck.')
        break
