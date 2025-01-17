import cmd
import textwrap
import sys
import os
import time
import random
import typing

screen_width = 100

#Status Gracza
class player:
    def __init__(self):
        self.won = False
        self.military = 50
        self.religion = 50
        self.money = 50
        self.food = 50
        self.people = 50
myPlayer = player()
myPlayer.won = False


#Pytania

listapytan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

#Ekran Poczatkowy
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("graj"):
        setup_game()
    elif option.lower() == ("pomoc"):
        help_menu()
    elif option.lower() == ("wyjdz"):
        sys.exit()
    while option.lower() not in ['graj', 'pomoc', 'wyjdz']:
        print("Wprowadz poprawna komende.")
        option = input("> ")
        if option.lower() == ("graj"):
            setup_game() #napisac to
        elif option.lower() == ("pomoc"):
            help_menu()
        elif option.lower() == ("wyjdz"):
            sys.exit()

def title_screen():
    def clear():
        if sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
    print('########################')
    print('# Witaj w grze Wladca! #')
    print('########################')
    print('        - Graj  -       ')
    print('        - Pomoc -       ')
    print('        - Wyjdz -       ')
    print('########################')
    title_screen_selections()

def help_menu():
    print('########################')
    print('# Witaj w grze Wladca! #')
    print('########################\n')
    print('- Na wszystkie pytania odpowiadaj tak/nie.')
    print('- Twoje odpowiedzi wplywaja na stan wojska, wiary, pieniedzy, zywnosci i zadowolenia mieszkancow w kraju.')
    print('- Stan tych parametrow mierzony jest w skali 0-100, gdzie przy osiagnieciu 0 w ktorymkolwiek z parametrow powoduje przegrana, a zdobycie 100 punktow powoduje wygrana.')
    print('- Gre zaczynasz z 50 punktami w kazdej kategorii.')
    print('- Wybieraj rozwaznie!')
    print('- Powodzenia!\n')
    print('########################')
    print('\nWybierz jedna z opcji, aby kontynuowac.')
    print('########################')
    print('        - Graj  -       ')
    print('        - Pomoc -       ')
    print('        - Wyjdz -       ')
    print('########################')
    title_screen_selections()


#GRA

def setup_game():
    def clear():
        if sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")

    pytanie1 = "Witaj przybyszu, jak sie nazywasz?\n"
    for character in pytanie1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

#Wstep

    wstep1 = "\nNareszcie sie obudziles " + player_name + "! Zaczynalem sie martwic."
    for character in wstep1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    wstep2 = "\nPewnie zastanawiasz sie, skad sie tu wziales, ale mam zbyt malo czasu na wyjasnienia."
    for character in wstep2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    wstep3 = "\nJuz za chwile przejmiesz wladze nad krajem, w ktorym ludzie u wladzy sa dosc kompetetni, ale niezdecydowani."
    for character in wstep3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    wstep4 = "\nDlatego potrzebuja zdecydowanego lidera, ktory poniesie za nich odpowiedzialnosc!"
    for character in wstep4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    wstep5 = "\nWystarczy, ze bedziesz odpowiadac na ich pytania 'tak' lub 'nie'. Calkiem proste, co nie?"
    for character in wstep5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)

    os.system('cls')
    print('############################################')
    print('# Reszte zrozumiesz w trakcie. Powodzenia! #')
    print('############################################')
    print('\nBudzisz sie w wygodnym fotelu w przestronnym biurze.')
    print("Rozlega sie pukanie do drzwi.")
    main_game_loop()



#glowna czesc gry
quitgame = "wyjdz"

def main_game_loop():
    while myPlayer.won is False:
        prompt()


def prompt():
    print("\nMasz goscia.\n")
    pytanie = random.choice(listapytan)
    if pytanie == 1:
        print('Minister Zdrowia Zdrowix:\nSzpitale tona w dlugach! Czy powinnismy zwiekszyc ich finansowanie?')
        player_answer_1 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_1.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_1 = input("> ")
        if player_answer_1.lower() == quitgame:
            sys.exit()
        if player_answer_1 == "tak":
            myPlayer.money -= 10
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_1 == 'nie':
            myPlayer.people -= 10
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 2:
        print('Minister Zdrowia Zdrowix:\nCzy powinnismy zlikwidowac program obowiazkowych szczepien? Mozemy przy tym troche przyoszczedzic.')
        player_answer_2 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_2.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_2 = input("> ")
        if player_answer_2.lower() == quitgame:
            sys.exit()
        if player_answer_2 == "tak":
            myPlayer.money += 5
            myPlayer.people -= 15
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_2 == 'nie':
            myPlayer.money -= 5
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 3:
        print('Minister Zdrowia Zdrowix:\nLekarze sa przepracowani, wiec terminy sie wydluzaja. Czy powinnismy zwiekszyc liczbe personelu?')
        player_answer_3 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_3.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_3 = input("> ")
        if player_answer_3.lower() == quitgame:
            sys.exit()
        if player_answer_3 == "tak":
            myPlayer.money -= 15
            myPlayer.people += 10
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_3 == 'nie':
            myPlayer.money += 5
            myPlayer.people -= 15
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 4:
        print('Minister Zdrowia Zdrowix:\nNiepokoi mnie wzrastajaca ilosc pacjentow z uzaleznieniami. Czy powinnismy wprowadzic program walk z uzaleznieniami?')
        player_answer_4 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_4.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_4 = input("> ")
        if player_answer_4.lower() == quitgame:
            sys.exit()
        if player_answer_4 == "tak":
            myPlayer.money -= 5
            myPlayer.people += 10
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_4 == 'nie':
            myPlayer.money += 5
            myPlayer.people -= 15
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 5:
        print('Minister Zdrowia Zdrowix:\nSpoleczenstwo domaga sie lepszej opieki zdrowotnej w nieczestych chorobach. Czy powinnismy prowadzic badania nad nowymi metodami leczenia chorob rzadkich?')
        player_answer_5 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_5.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_5 = input("> ")
        if player_answer_5.lower() == quitgame:
            sys.exit()
        if player_answer_5 == "tak":
            myPlayer.money -= 10
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_5 == 'nie':
            myPlayer.money += 5
            myPlayer.people -= 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 6:
        print('General Generalix:\nW razie wojny mamy zbyt malo wojska do obrony kraju w calosci. Czy powinnismy wprowadzic obowiazkowa sluzbe wojskowa?')
        player_answer_6 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_6.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_6 = input("> ")
        if player_answer_6.lower() == quitgame:
            sys.exit()
        if player_answer_6 == "tak":
            myPlayer.military += 10
            myPlayer.religion -= 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_6 == 'nie':
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 7:
        print('General Generalix:\nSasiednie panstwa rosna w sile i chetnie przejelyby nasze zasoby na wschodzie! Czy powinnismy zwiekszyc budzet na obrone narodowa?')
        player_answer_7 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_7.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_7 = input("> ")
        if player_answer_7.lower() == quitgame:
            sys.exit()
        if player_answer_7 == "tak":
            myPlayer.military += 15
            myPlayer.money -= 15
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_7 == 'nie':
            myPlayer.military -= 5
            myPlayer.money += 10
            myPlayer.people -= 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 8:
        print('General Generalix:\nOstatni zamach w stolicy spowodowal niepokoje spoleczne. Czy powinnismy przeprowadzic szkolenie jednostek do walki z terroryzmem?')
        player_answer_8 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_8.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_8 = input("> ")
        if player_answer_8.lower() == quitgame:
            sys.exit()
        if player_answer_8 == "tak":
            myPlayer.military += 5
            myPlayer.religion += 5
            myPlayer.money -= 5
            myPlayer.people += 10
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_8 == 'nie':
            myPlayer.money += 5
            myPlayer.people -= 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 9:
        print('General Generalix:\nPrzyjazne nam panstwa zaproponowaly utworzenie sojuszu wojskowego. Czy zamierzamy do niego dolaczyc? Wiaze sie to z placeniem skladek.')
        player_answer_9 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_9.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_9 = input("> ")
        if player_answer_9.lower() == quitgame:
            sys.exit()
        if player_answer_9 == "tak":
            myPlayer.military += 15
            myPlayer.money -= 10
            myPlayer.people += 10
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_9 == 'nie':
            myPlayer.military -= 10
            myPlayer.religion += 5
            myPlayer.money -= 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 10:
        print('General Generalix:\nCzy powinnismy zrezygnowac z kosztownego systemu rozpoznawania satelitarnego?')
        player_answer_10 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_10.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_10 = input("> ")
        if player_answer_10.lower() == quitgame:
            sys.exit()
        if player_answer_10 == "tak":
            myPlayer.military -= 10
            myPlayer.money += 15
            myPlayer.people -= 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_10 == 'nie':
            myPlayer.military -= 10
            myPlayer.religion -= 10
            myPlayer.money -= 10
            myPlayer.food -= 10
            myPlayer.people -= 10
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 11:
        print('General Generalix:\nW najblizszych latach mozliwa jest wojna. Czy powinnismy prowadzic badania nad bronia masowego razenia?')
        player_answer_11 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_11.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_11 = input("> ")
        if player_answer_11.lower() == quitgame:
            sys.exit()
        if player_answer_11 == "tak":
            myPlayer.military += 5
            myPlayer.religion -= 20
            myPlayer.money -= 10
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_11 == 'nie':
            myPlayer.religion += 5
            myPlayer.money += 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 12:
        print('General Generalix:\nPanstwo na zachod od nas jest slabe i nierozwiniete, ale ma zasoby, ktore moga nam sie przydac. Czy powinnismy je zaatakowac celem przejecia zasobow?')
        player_answer_12 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_12.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_12 = input("> ")
        if player_answer_12.lower() == quitgame:
            sys.exit()
        if player_answer_12 == "tak":
            myPlayer.military -= 15
            myPlayer.religion -= 20
            myPlayer.money += 20
            myPlayer.food += 35
            myPlayer.people -= 20
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_12 == 'nie':
            myPlayer.military += 5
            myPlayer.religion += 5
            myPlayer.money += 5
            myPlayer.food += 5
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 13:
        print('Arcybiskup Arcybiskupix:\nSasiedni kraj prosi nas o udzielenie pomocy humanitarnej! Powinnismy natychmiast im ja wyslac!')
        player_answer_13 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_13.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_13 = input("> ")
        if player_answer_13.lower() == quitgame:
            sys.exit()
        if player_answer_13 == "tak":
            myPlayer.religion += 10
            myPlayer.money -= 10
            myPlayer.food -= 15
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_13 == 'nie':
            myPlayer.religion -= 15
            myPlayer.money += 5
            myPlayer.food += 5
            myPlayer.people -= 10
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 14:
        print('Arcybiskup Arcybiskupix:\nOstatnimi czasy coraz mniej wiernych odwiedza swiatynie. Czy pozwolisz na finansowanie budowy nowych miejsc kultu w kraju?')
        player_answer_14 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_14.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_14 = input("> ")
        if player_answer_14.lower() == quitgame:
            sys.exit()
        if player_answer_14 == "tak":
            myPlayer.religion += 10
            myPlayer.money -= 5
            myPlayer.people -= 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_14 == 'nie':
            myPlayer.money += 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 15:
        print('Arcybiskup Arcybiskupix:\nNa ulicach roi sie od bezdomnych. Powinnismy ich wesprzec!')
        player_answer_15 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_15.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_15 = input("> ")
        if player_answer_15.lower() == quitgame:
            sys.exit()
        if player_answer_15 == "tak":
            myPlayer.religion += 5
            myPlayer.money -= 5
            myPlayer.food -= 5
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_15 == 'nie':
            myPlayer.religion -= 5
            myPlayer.money += 5
            myPlayer.food += 5
            myPlayer.people -= 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 16:
        print('Arcybiskup Arcybiskupix:\nLudzie daja coraz mniej na ofiare. Jesli zgodzisz sie, zebym wprowadzil obowiazkowe datki na kosciol, oddam czesc zyskow do skarbu panstwa. To co? Zgoda?')
        player_answer_16 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_16.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_16 = input("> ")
        if player_answer_16.lower() == quitgame:
            sys.exit()
        if player_answer_16 == "tak":
            myPlayer.religion -= 15
            myPlayer.money += 10
            myPlayer.people -= 10
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_16 == 'nie':
            myPlayer.military -= 0
            myPlayer.religion -= 0
            myPlayer.money -= 0
            myPlayer.food -= 0
            myPlayer.people -= 0
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 17:
        print('Arcybiskup Arcybiskupix:\nLudzie boja sie mozliwosci wojny w najblizszej przyszlosci. Publiczne modly moga uspokoic ich ducha, moge je zorganizowac?')
        player_answer_17 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_17.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_17 = input("> ")
        if player_answer_17.lower() == quitgame:
            sys.exit()
        if player_answer_17 == "tak":
            myPlayer.religion += 10
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_17 == 'nie':
            myPlayer.military -= 0
            myPlayer.religion -= 0
            myPlayer.money -= 0
            myPlayer.food -= 0
            myPlayer.people -= 0
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 18:
        print('Arcybiskup Arcybiskupix:\nUwazam, ze przeznaczamy zbyt wiele budzetu na wojsko. Nasz Stworca nie pozwolilby nam cierpiec w wojnie, ale musimy mu pokazac, ze wszyscy jestesmy jego wyznawcami!')
        player_answer_18 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_18.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_18 = input("> ")
        if player_answer_18.lower() == quitgame:
            sys.exit()
        if player_answer_18 == "tak":
            myPlayer.military -= 20
            myPlayer.religion += 10
            myPlayer.money += 10
            myPlayer.people -= 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_18 == 'nie':
            myPlayer.military += 5
            myPlayer.religion -= 15
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 19:
        print('Minister Rolnictwa Rolasix:\nLiczba producentow zywnosci maleje. Czy powinnismy wprowadzic dofinansowania?')
        player_answer_19 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_19.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_19 = input("> ")
        if player_answer_19.lower() == quitgame:
            sys.exit()
        if player_answer_19 == "tak":
            myPlayer.money -= 5
            myPlayer.food += 10
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_19 == 'nie':
            myPlayer.money += 5
            myPlayer.food -= 10
            myPlayer.people -= 10
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 20:
        print('Minister Rolnictwa Rolasix:\nSasiedni kraj jest zainteresowany kupnem znacznej czesci naszych zapasow. Zgodzimy sie?')
        player_answer_20 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_20.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_20 = input("> ")
        if player_answer_20.lower() == quitgame:
            sys.exit()
        if player_answer_20 == "tak":
            myPlayer.money += 20
            myPlayer.food -= 25
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_20 == 'nie':
            myPlayer.food += 5
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 21:
        print('Minister Rolnictwa Rolasix:\nInne kraje juz dawno zezwolily na badania oraz uprawe roslin GMO, czy tez chcemy na to zezwolic?')
        player_answer_21 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_21.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_21 = input("> ")
        if player_answer_21.lower() == quitgame:
            sys.exit()
        if player_answer_21 == "tak":
            myPlayer.money -= 10
            myPlayer.food += 15
            myPlayer.people -= 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_21 == 'nie':
            myPlayer.money += 5
            myPlayer.food += 15
            myPlayer.people += 10
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 22:
        print('Minister Rolnictwa Rolasix:\nJesli wytniemy czesc lasow, nie tylko zyskamy nowe tereny rolne, ale tez materialy na budowe nowych domostw. Jednak wierzacym obywatelom moze sie to nie spodobac ze wzgledu na ich specjalne kaplice ukryte w lasach. Uwazam jednak, ze nowe tereny rolne sa wazniejsze.')
        player_answer_22 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_22.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_22 = input("> ")
        if player_answer_22.lower() == quitgame:
            sys.exit()
        if player_answer_22 == "tak":
            myPlayer.religion -= 10
            myPlayer.money += 15
            myPlayer.food += 10
            myPlayer.people += 20
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_22 == 'nie':
            myPlayer.religion += 5
            myPlayer.people += 10
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 23:
        print('Minister Rolnictwa Rolasix:\nArcybiskup nie jest zadowolony z tego ile lasow zostalo przerobionych na tereny rolne. Czy powinnismy ograniczyc produkcje rolna na rzecz importu produktow?')
        player_answer_23 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_23.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_23 = input("> ")
        if player_answer_23.lower() == quitgame:
            sys.exit()
        if player_answer_23 == "tak":
            myPlayer.religion += 5
            myPlayer.money -= 10
            myPlayer.food -= 5
            myPlayer.people -= 10
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_23 == 'nie':
            myPlayer.religion -= 5
            myPlayer.food += 10
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 24:
        print('Minister Rolnictwa Rolasix:\nOstatnie pozary mocno nadwyrezyly nasz budzet. Czy powinnismy zrezygnowac z rekompensat z powodu klesk zywiolowych?')
        player_answer_24 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_24.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_24 = input("> ")
        if player_answer_24.lower() == quitgame:
            sys.exit()
        if player_answer_24 == "tak":
            myPlayer.religion -= 5
            myPlayer.money += 15
            myPlayer.food -= 10
            myPlayer.people -= 10
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_24 == 'nie':
            myPlayer.money += 5
            myPlayer.food += 10
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)

    elif pytanie == 25:
        print('Minister Rolnictwa Rolasix:\nNa bardzo zyznych terenach niedawno odkryto ogromne zloza dobr naturalnych. Czy powinnismy poswiecic te tereny na rzecz wydobycia dobr?')
        player_answer_25 = input("Jaka jest Twoja decyzja " + myPlayer.name + "?\n> ")
        acceptable_answers = ['tak', 'nie', 'wyjdz']
        while player_answer_25.lower() not in acceptable_answers:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            player_answer_25 = input("> ")
        if player_answer_25.lower() == quitgame:
            sys.exit()
        if player_answer_25 == "tak":
            myPlayer.money += 25
            myPlayer.food -= 15
            myPlayer.people -= 5
            os.system('cls')
            pytanie = random.choice(listapytan)
        elif player_answer_25 == 'nie':
            myPlayer.money += 5
            myPlayer.food += 10
            myPlayer.people += 5
            os.system('cls')
            pytanie = random.choice(listapytan)



    print("\nTwoje statystyki: ")
    print("Wojsko: " + str(myPlayer.military))
    print("wiara: " + str(myPlayer.religion))
    print("Pieniadze: " + str(myPlayer.money))
    print("Zywnosc: " + str(myPlayer.food))
    print("Zadowolenie ludnosci: " + str(myPlayer.people))
    game_won()
    game_lost()


def game_won():
    if     myPlayer.military >= 100:
        print("\nWygrales wojskowo! Twoje panstwo stalo sie elita militarna na swiecie, ktorej nikt nie bedzie chcial ryzykowac i zwrocic przeciwko sobie!")
        myPlayer.won = True
        print("\nGratulacje!")
        ponowna_gra = input("Czy chcesz zagrac ponownie?\n> ")
        mozliwe_opowiedzi = ['tak', 'nie']
        while ponowna_gra.lower() not in mozliwe_opowiedzi:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            ponowna_gra = input("> ")
        if ponowna_gra.lower() == "tak":
            myPlayer.won = False
            myPlayer.military = 50
            myPlayer.religion = 50
            myPlayer.money = 50
            myPlayer.food = 50
            myPlayer.people = 50
            prompt()
        elif ponowna_gra.lower() == 'nie':
            sys.exit()

    elif myPlayer.religion >= 100:
        print("\nWygrales religijnie! Twoje panstwo jest calkowicie oddane Stworcy, ktory roztacza teraz opieke nad kazdym obywatelem.")
        myPlayer.won = True
        print("\nGratulacje!")
        ponowna_gra = input("Czy chcesz zagrac ponownie?\n> ")
        mozliwe_opowiedzi = ['tak', 'nie']
        while ponowna_gra.lower() not in mozliwe_opowiedzi:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            ponowna_gra = input("> ")
        if ponowna_gra.lower() == "tak":
            myPlayer.won = False
            myPlayer.military = 50
            myPlayer.religion = 50
            myPlayer.money = 50
            myPlayer.food = 50
            myPlayer.people = 50
            prompt()
        elif ponowna_gra.lower() == 'nie':
            sys.exit()

    elif myPlayer.money >= 100:
        print("\nWygrales finansowo! Jako prezydent jednego z najbogatszych panstw mozesz pozwolic sobie na bezpieczne zycie w dostatku.")
        myPlayer.won = True
        print("\nGratulacje!")
        ponowna_gra = input("Czy chcesz zagrac ponownie?\n> ")
        mozliwe_opowiedzi = ['tak', 'nie']
        while ponowna_gra.lower() not in mozliwe_opowiedzi:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            ponowna_gra = input("> ")
        if ponowna_gra.lower() == "tak":
            myPlayer.won = False
            myPlayer.military = 50
            myPlayer.religion = 50
            myPlayer.money = 50
            myPlayer.food = 50
            myPlayer.people = 50
            prompt()
        elif ponowna_gra.lower() == 'nie':
            sys.exit()

    elif myPlayer.food >= 100:
        print("\nWygrales zywnosciowo! Twoje panstwo produkuje tak wiele zywnosci, ze nikt nie chodzi glodny a eksport przynosi znaczace zyski!")
        myPlayer.won = True
        print("\nGratulacje!")
        ponowna_gra = input("Czy chcesz zagrac ponownie?\n> ")
        mozliwe_opowiedzi = ['tak', 'nie']
        while ponowna_gra.lower() not in mozliwe_opowiedzi:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            ponowna_gra = input("> ")
        if ponowna_gra.lower() == "tak":
            myPlayer.won = False
            myPlayer.military = 50
            myPlayer.religion = 50
            myPlayer.money = 50
            myPlayer.food = 50
            myPlayer.people = 50
            prompt()
        elif ponowna_gra.lower() == 'nie':
            sys.exit()

    elif myPlayer.people >= 100:
        print("\nWygrales zadowoleniem spoleczenstwa! Ludzie kochaja Ciebie i swoj kraj. Sa gotowi zrobic wszystko, zeby utrzymac dobrobyt w kraju.")
        myPlayer.won = True
        print("\nGratulacje!")
        ponowna_gra = input("Czy chcesz zagrac ponownie?\n> ")
        mozliwe_opowiedzi = ['tak', 'nie']
        while ponowna_gra.lower() not in mozliwe_opowiedzi:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            ponowna_gra = input("> ")
        if ponowna_gra.lower() == "tak":
            myPlayer.won = False
            myPlayer.military = 50
            myPlayer.religion = 50
            myPlayer.money = 50
            myPlayer.food = 50
            myPlayer.people = 50
            prompt()
        elif ponowna_gra.lower() == 'nie':
            sys.exit()

def game_lost():
    if     myPlayer.military <= 0:
        print("\nPrzegrales wojskowo! Sasiedni kraj najechal Twoje panstwo i je przejal. Zostales publicznie stracony.")
        myPlayer.won = False
        print("\nPowodzenia nastepnym razem!")
        ponowna_gra = input("Czy chcesz zagrac ponownie?\n> ")
        mozliwe_opowiedzi = ['tak', 'nie']
        while ponowna_gra.lower() not in mozliwe_opowiedzi:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            ponowna_gra = input("> ")
        if ponowna_gra.lower() == "tak":
            myPlayer.won = False
            myPlayer.military = 50
            myPlayer.religion = 50
            myPlayer.money = 50
            myPlayer.food = 50
            myPlayer.people = 50
            prompt()
        elif ponowna_gra.lower() == 'nie':
            sys.exit()

    elif myPlayer.religion <= 0:
        print("\nPrzegrales religijnie! Zatracajaca sie wiernosc obywateli spowodowala, ze Stworca przestal otaczac was swoja opieka i Twoi obywatele razem z Toba zgineli od klesk zywiolowych.")
        myPlayer.won = False
        print("\nPowodzenia nastepnym razem!")
        ponowna_gra = input("Czy chcesz zagrac ponownie?\n> ")
        mozliwe_opowiedzi = ['tak', 'nie']
        while ponowna_gra.lower() not in mozliwe_opowiedzi:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            ponowna_gra = input("> ")
        if ponowna_gra.lower() == "tak":
            myPlayer.won = False
            myPlayer.military = 50
            myPlayer.religion = 50
            myPlayer.money = 50
            myPlayer.food = 50
            myPlayer.people = 50
            prompt()
        elif ponowna_gra.lower() == 'nie':
            sys.exit()

    elif myPlayer.money <= 0:
        print("\nPrzegrales finansowo! Twoje decyzje doprowadzily do bankructwa. Wsciekly tlum ludzi zdecydowal sie ma samosad, ktory zakonczyl sie Twoja smiercia.")
        myPlayer.won = False
        print("\nPowodzenia nastepnym razem!")
        ponowna_gra = input("Czy chcesz zagrac ponownie?\n> ")
        mozliwe_opowiedzi = ['tak', 'nie']
        while ponowna_gra.lower() not in mozliwe_opowiedzi:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            ponowna_gra = input("> ")
        if ponowna_gra.lower() == "tak":
            myPlayer.won = False
            myPlayer.military = 50
            myPlayer.religion = 50
            myPlayer.money = 50
            myPlayer.food = 50
            myPlayer.people = 50
            prompt()
        elif ponowna_gra.lower() == 'nie':
            sys.exit()

    elif myPlayer.food <= 0:
        print("\nPrzegrales zywnosciowo! Twoi ludzie gloduja. Czesc z ministrow zostala przekupiona przez wrogi kraj. W zamian za pomoc Twoi zaufani ludzie wydali Cie w rece wroga.")
        myPlayer.won = False
        print("\nPowodzenia nastepnym razem!")
        ponowna_gra = input("Czy chcesz zagrac ponownie?\n> ")
        mozliwe_opowiedzi = ['tak', 'nie']
        while ponowna_gra.lower() not in mozliwe_opowiedzi:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            ponowna_gra = input("> ")
        if ponowna_gra.lower() == "tak":
            myPlayer.won = False
            myPlayer.military = 50
            myPlayer.religion = 50
            myPlayer.money = 50
            myPlayer.food = 50
            myPlayer.people = 50
            prompt()
        elif ponowna_gra.lower() == 'nie':
            sys.exit()

    elif myPlayer.people <= 0:
        print("\nPrzegrales zadowoleniem spoleczenstwa! Twoje rzady sa do bani i nikomu nie podoba sie co wyczyniasz z panstwem. Przeprowadzono na Tobie defenestracje.")
        myPlayer.won = False
        print("\nPowodzenia nastepnym razem!")
        ponowna_gra = input("Czy chcesz zagrac ponownie?\n> ")
        mozliwe_opowiedzi = ['tak', 'nie']
        while ponowna_gra.lower() not in mozliwe_opowiedzi:
            print("Mozesz uzywac jedynie slow 'tak' i 'nie'. Sprobuj ponownie.")
            ponowna_gra = input("> ")
        if ponowna_gra.lower() == "tak":
            myPlayer.won = False
            myPlayer.military = 50
            myPlayer.religion = 50
            myPlayer.money = 50
            myPlayer.food = 50
            myPlayer.people = 50
            prompt()
        elif ponowna_gra.lower() == 'nie':
            sys.exit()




title_screen()