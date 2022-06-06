# 0 NOTES according to PEP8 the names of functions and variables should say something to make it easier to analyze the code. If something is unclear, comments can be used, but unnecessary comments should be avoided.
# There is a note that there are two lines between functions, we should avoid using will - it improves the readability of the code

# 1 -> ENVIRONMENT required for the model to work - first you need to take care of the environment - in our case you will need the random library

import random

# PREZENTACJA --> https://prezi.com/view/ujPDUivwPe3voacHQk2s/

# 2 -> GLOBAL VARIABLES - required in the proposed solution
difficulties = {"0": ["IMMORTALITY",26, 0],"1": ["EASY", 16, 1], "2": ["MID", 8, 2], "3": ["HARD", 4, 4], "4": ["CHALLANGE", 2, 8]} # tablica menu - poziom gry z ich nazwą oraz przypisane in limity "żyć" oraZ multiplikator do wyboru grafiki
difficulties_choice = {}                                            # wybrany funkcją game_level odpowiedni wariant gry
difficulty =""

country_capital = {}                                                # pusty słownik słów, zostaną zaimportowane z pliku countries-and-capitals.txt za pomocą import_dictionery()
category = (0, 1)
category_massage = ""
choosen_word = set()
choosen_word_status = []
choosen_word_letters = 0
already_tried_letters = []

# 3 -> GRAPHICS
hangman = (

"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |
    |###########                 
    """,
"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |
    |###########
    """,
"""
   _________       
    |/   |              
    |   (
    |                         
    |                       
    |                         
    |                          
    |
    |###########                       
    """,
""" _________       
    |/   |              
    |   (_
    |                         
    |                       
    |                         
    |                          
    |
    |###########                       
    """,
""" _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |
    |###########                       
    """,
"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |                        
    |                           
    |                            
    |
    |###########                    
    """,
"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |
    |###########                    
    """,
"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |  / |                    
    |                        
    |                          
    |
    |###########                                              
    """,
"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |  / |                       
    |                             
    |                            
    |
    |###########                                              
    """,
"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |  / | \                      
    |                             
    |                            
    |
    |###########                                              
    """,
"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |  / | \                         
    |   /                            
    |                                  
    |
    |###########                                                  
    """,
"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |  / | \       
    |   /         
    |  /             
    |
    |###########                               
    """,
"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |  / | \      
    |   / \        
    |  /             
    |
    |###########                               
    """,
"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |  / | \       
    |   / \        
    |  /   \          
    |
    |###########                               
    """,
"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |  / | \       
    |   / \        
    | _/   \          
    |
    |###########                               
    """,
""" 
    ________
    |/   |    
    |   (_)     ~( !! help !!  )   
    |   /|\         
    |  / | \        
    |   / \        
    | _/   \          
    |LAST CHANCE
    |###########                               
    """,
""" 
    ________
    |/   |     
    |   (_)    
    |   /|\           
    |  / | \        
    |   / \        
    | _/   \_          
    |  R.I.P    
    |###########                               
    """,  
    )

geme_titele = (
    """
                                                                                      _________
      ###  ###  ########  ###    ###  ########  ###         ###  ########  ##      ##  |/   |
     ###  ###  ########  ####   ###  ########  ####       ####  ########  ###    ###   |   (_) 
    ###  ###  ###  ###  #####  ###  ###       #####     #####  ###  ###  #####  ###    |   /|\     
   ########  ###  ###  ### ## ###  ### ####  ### ### ### ###  ###  ###  ### ## ###     |  / | \ 
  ###  ###  ########  ###  #####  ###  ###  ###  ###### ###  ########  ###  #####      |   / \  
 ###  ###  ###  ###  ###   ####  ########  ###   ####  ###  ###  ###  ###    ###       | _/   \_
###  ###  ###  ###  ###    ###  ########  ###    ###  ###  ###  ###  ###     ##        |#########

    created by Paulina & Arek
    """
)
# 4 -> FUNCTIONS
def import_dictionery(): 
    """a function that imports a file and converts it into a dictionary and supplements variable values (from a file named countries-and-capitals.txt )"""
    with open("countries-and-capitals.txt", "r", encoding='utf8') as f: 
        # taka składania z "with" skutkuje brakiem konieczności zamykania pliku - PAMIĘTAJ inaczej samo open("nazaw_pliku") wymaga zamknięcia pliku komendą nazwa_pliku.close()
        # parametr "r" - ozancza czytaj, są jeszcze "w" - możesz pisać oraz "a" możesz dodawać - PAMIĘTAJ otwarcie pliku z parametrem "w" i jego natychmiastowe zamknięcie powoduje skasowanie zawartości!!
        # encoding='utf8' - to parametr określający typ danych - uzależniony od tego w jaki sposób plik był wcześniej kodowany utf8 - tak dla bezpieczęństwa i wymuszenia pamięci
        contents = f.readlines()                                            # czytanie zawartości pliku w postaci linii
        for line in contents:                                               # czytanie linia po lini
            line_clean = line.strip("\n").split(" | ")                      # formatowanie - otwarte pliki kończą się zawsze zapisem kończącym linie "/n", którego trzeba się pozbyć, dodatkowo zamieniam wartości ;lini na 2 zmienne pozbywając się widoczengo separatora " | "
            country = line_clean[0]                                         # pobranie wartości pierwszej zmiennej z linii jako kraj 
            capitol = line_clean[1]                                         # pobranie wartości drugiej zmiennej z linii jako stolica
            country_capital[country] = capitol                              # wprowadzenie danych do słownika country_capital - key = country, value = capital

def choose_the_word():
    global choosen_word_letters                                             # ustalenie ilości liter w szukanym słowie bez spacji
    global choosen_word                                                     # dostęp do globalnej zmiennej o nazwie choosen_word - wybrane słowo
    global category_massage                                                 # o taka wiadomość by się wyświatlała w co się gra                                                    
    global choosen_word_status                                              # dostęp do globalnej zmiennej o nazwie choosen_word_status - litery zamienione na "-""
    category_choice = random.choice(category)
    if category_choice == 0:
        choosen_word = random.choice(list(country_capital.keys()))          # wybór kategorii kraj nie jest to zgodnie z instrukcją ale coś od siebie dodamy -  losowo kraj, aby to zrobić na słowniku nalezy doprowadzić key do listy i dopiero z niej wybrać za pomoca random.choice losowy kraj.
        category_massage = "Your game category -'Country'"
    else:
        choosen_word = random.choice(list(country_capital.values()))        # wybór kategorii stolica nie jest to zgodnie z instrukcją ale coś od siebie dodamy -  losowo stolice, aby to zrobić na słowniku nalezy doprowadzić value do listy i dopiero z niej wybrać za pomoca random.choice losowy stolica..
        category_massage = "Your game category -'Capital City'"
    for i in choosen_word:                                                  # ot taka pętelka aby spacje między słowami wyświetlały się jako spacje zamiast -
        if i !=" ":
            choosen_word_status += "_"
            choosen_word_letters += 1
        else:
            choosen_word_status += " "


def game_level(): 
    """initialization function - selecting the level of the game and saving it in the game variables difficulties_choice"""
    global difficulties_choice                                             # dostęp do globalnej zmiennej o nazwie difficulties_choice - wybrany poziom gry
    global difficulty                                                      # dostęp do globalnej zmiennej o nazwie difficulties_choice_key - wybrany poziom gry w postaci klucza
    print(f'\n{geme_titele}')
    while True:                                                            # pętkla sprawdzająca
        print("-" * 114)                                                   # ozdobnik w postaci kresek
        choice_g = input("! Welcome to our game\n! Choose game level - enter 0 for IMMORTALITY, 1 for EASY, 2 for MID, 3 for HARD, 4 for CHALLANGE or write 'quit' to exit game-> ")
        if choice_g.lower() != "quit":                                     # warunek gry wpisanie quit przerywa zabawę
            if choice_g not in difficulties.keys():
                print("\n! Your choice is wrong !")
            else:
                difficulties_choice[choice_g] = difficulties[choice_g]     # przypisanie wybranego poziomu gry do zmiennej obs lugującej daną rozgrywkę
                difficulty = choice_g
                return False
        else:
            print("\n! See you next time !\n")                              # grzecznie jest zaprosić do kolejnej rozgrywki
            exit()


def game_letter_check():
    """function checking the correctness of the entered character"""
    global already_tried_letters
    global choosen_word
    while True:
        letter = input("\n! Please enter your guess letter. Hope you remember the alphabet else an error will appear -> ").lower()
        if letter.lower() == "quit":
            game_print()
            print("\n! See you next time !\n")                              # grzecznie jest zaprosić do kolejnej rozgrywki
            exit()
        elif len(letter) > 1:
            print(f"! More then 1 is fare too much. Your input {letter}. Try again or write 'quit' !")
            game_print()
        elif not letter:
            print("! Do not be lazy at least enter something. Try again or write 'quit' !")
            game_print()   
        elif letter.isalpha() == False:                                     # sprawdzenie czy wprowadzony znak to litera
            print(f"! Heve you ever seen such letter? Your input > {letter} <. Try again or write 'quit' !")
            game_print()
        elif letter.lower() in already_tried_letters:                       # sprawdzenie czy wprowadzona litera była już używana
            wrong_letters = wrong_letter_used(choosen_word,already_tried_letters)
            print(f"\n! You have already used this letter !\n! Wrong letter used already {sorted(wrong_letters)}")
            game_print()
        elif letter.lower() not in choosen_word.lower():                    # sprawdzenie czy wprowadzona litera jest w szukanym słowie
            already_tried_letters.append(letter.lower())
            if difficulties_choice[difficulty][1] > 1:
                difficulties_choice[difficulty][1] -= 1                     # odebranie życia, zmniejszenie wartości zmiennej o 1 błąd
                wrong_letters = wrong_letter_used(choosen_word,already_tried_letters)
                print(f'\n! Wrong letter used already {sorted(wrong_letters)}')
                game_print()
                if difficulties_choice[difficulty][1] > 1:
                    print(f"! Such letter does not appear in the word, you lose 1 life.\n! You still have {difficulties_choice[difficulty][1]} lives.\n! Try again or write 'quit' !")
                else:
                    print(f"! Such letter does not appear in the word, you lose 1 life.\n! You have last available life, don't waste it.\n! Try again or write 'quit' !")
            else:
                print("-" * 114)                                            # ozdobnik w postaci kresek
                print(f"! Oh My God !\n! You have no more lives sorry !")
                difficulties_choice[difficulty][1] -= 1
                game_print()
                break
        else:
            already_tried_letters.append(letter.lower())
            for i in range(len(choosen_word)):
                if letter.lower() == choosen_word[i].lower():
                    choosen_word_status[i] = choosen_word[i]
            game_print()
            print("-" * 114)
            return False
            

def wrong_letter_used(choosen_word,already_tried_letters):
    """function that provide information about wrong letter used"""
    list_of_word_letters = set(list(choosen_word.lower()))              # zamiana na set (bo to jest zmienna typu lista bez powtórzeń)
    list_of_used_letters = set(list(already_tried_letters))             # zamiana na set (bo to jest zmienna typu lista ale  bez powtórzeń)
    wrong_letters = []                                          # różnica między listą użytych liter a występujących w szukanym słowie
    for element in list_of_used_letters:
        if element not in list_of_word_letters:
            wrong_letters.append(element)
    return wrong_letters


def game_print():
    """function that draws the current state"""
    global choosen_word
    global choosen_word_status
    global category_massage
    global difficulty
    if difficulty =="0":                                                        # o taka wiadomość by się wyświatlała w co się gra
        print(f'\n{category_massage}')                                          # wiadomość o kategorii w którą się gra
        print(f'{hangman[0]}\n    {"".join(choosen_word_status)}\n')            # to fajna konstrukcja "".join(choosen_word_status - łączy elementy listy w jeden ciąg warto to zapamiętać!!
    else:
        current_print = 16 - difficulties_choice[difficulty][1] * difficulties_choice[difficulty][2]
        print(f'\n{category_massage}')                                          # wiadomość o kategorii w którą się gra
        print(f'{hangman[current_print]}\n    {"".join(choosen_word_status)}\n') # to fajna konstrukcja "".join(choosen_word_status - łączy elementy listy w jeden ciąg warto to zapamiętać!!
        
        


def game_start():
    """its managing function initiates the entire application"""
    game_level()
    print("! You have choosen %s level so you have %s available lives " % (difficulties_choice[difficulty][0], difficulties_choice[difficulty][1]))
    print("-" * 114)
    import_dictionery()
    choose_the_word()
    game_print()

    while difficulties_choice[difficulty][1] > 0 and "".join(choosen_word_status) != choosen_word:
        game_letter_check()
    else:
        if difficulties_choice[difficulty][1] > 0:
            number_of_errors_made = len(wrong_letter_used(choosen_word,already_tried_letters))
            print('! CONGRATULATION !\n! You guessed the word, You survived !')
            
            if number_of_errors_made > 1:
                print(f'\n! You lost {number_of_errors_made} lives !\n! Thank you and see you next time !')
            elif number_of_errors_made == 1:
                print(f'\n! You lost only 1 life !\n! Thank you and see you next time !')
            else:
                print(f'\n! You are GENIUS, you have not lost any life !\n! Thank you and see you next time !')
            print("-" * 114)
            print(f'\n{geme_titele}')
            print("-" * 114)
        else:
            print(f"! The word was '{choosen_word}' but You have not found it so you are DEAD !\n! Thank you and see you next time !")
            print("-" * 114)
            print(f'\n{geme_titele}')
            print("-" * 114)
            quit()

if __name__ == '__main__':
    game_start()
