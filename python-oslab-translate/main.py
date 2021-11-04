#Atousa Niazi-98440127-python-OSLab-translate

# dar python or /else darim  :  dar for break ejra she else ejra nemy she va baraks

WORDS_BANK=[]

def load_data():
    #f=open('words_bank.txt','r')
    with open('words_bank.txt','r') as f :
        big_text=f.read()
        words=big_text.split('\n')
        
        for i in range(0,len(words),2):
            WORDS_BANK.append({'english':words[i],'persian':words[i+1]})
            
    for w in WORDS_BANK:
        print(w)
    print('loaded!')


def add():
    print("\033[38;5;76madd a new word:")
    print("to add a new item: ")
    print('english:')
    en_in=input()
    print('persian:')
    fa_in=input()
    adding=[en_in,fa_in]
    WORDS_BANK.append({'english':adding[0],'persian':adding[1]})



def input_text_user():
    user_text=input('\033[38;5;78mplease write your text: ')
    return user_text
    
def en2fa(input_text):
    user_words=user_text.split(' ')
    output_text=''
    for user_word in user_words:
        for word in WORDS_BANK:
            if user_word == word['english']:
                output_text+=word['persian']+' '
                break
        else:
            output_text+=user_word+' '
    return output_text
    
def fa2en(user_text):
    user_words=user_text.split(' ')
    output_text=''
    for user_word in user_words:
        for word in WORDS_BANK:
            if user_word == word['persian']:
                output_text+=word['english']+' '
                break
        else:
            output_text+=user_word+' '
    return output_text


def show_menu():
    print("\033[1;95m~~~~~~~~~~~~~~~~~~~~~~")
    print('Welcome to Sadjad Translator!')
    print('1- Add new word ')
    print('2- Translation english2persian')
    print('3- Translation persian2english')
    print('4- Exit')
    print("\033[1;95m~~~~~~~~~~~~~~~~~~~~~~\n")

def save():
    print('saved')
    f=open('words_bank.txt','w') # i opened the file with w to prevent overwritting
    result = str(WORDS_BANK)
    for row in result:
        f.write(row+'\n')
    f.close()
    print()
    print()

print("\033[38;5;78mloading... \n")
load_data()
print("\033[38;5;78m\ndatabase loaded. app is ready to use.\n")
while True:
    show_menu()
    print("\033[38;5;78mEnter your choice:")
    choice=int(input())
    
    if choice==1:
        add()
        save()
    elif choice==2:
        user_text=input_text_user()
        output_text=en2fa(user_text)
        print("\033[38;5;78myour Translated text is :")
        print("\033[38;5;215m",output_text)
    elif choice==3:
        user_text=input_text_user()
        output_text=fa2en(user_text)
        print("\033[38;5;78myour Translated text is :")
        print("\033[38;5;215m",output_text)
    elif choice==4:
        break
