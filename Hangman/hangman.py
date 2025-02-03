import time
import random

# list of animal names
animals = [
    'AARDVARK', 'ALBATROSS', 'ALLIGATOR', 'ALPACA', 'ANT', 'ANTEATER', 'ANTELOPE', 'ARMADILLO',
    'AXOLOTL', 'BABOON', 'BADGER', 'BARRACUDA', 'BAT', 'BEAR', 'BEAVER', 'BEE', 'BISON', 'BOAR',
    'BUFFALO', 'BUTTERFLY', 'CAMEL', 'CAPYBARA', 'CARIBOU', 'CASSOWARY', 'CAT', 'CATERPILLAR',
    'CATTLE', 'CHAMELEON', 'CHEETAH', 'CHIMPANZEE', 'CHINCHILLA', 'COBRA', 'COCKROACH', 'COUGAR', 
    'COYOTE', 'CRAB', 'CRANE', 'CROCODILE', 'CROW', 'DEER', 'DINGO', 'DOLPHIN', 'DONKEY', 
    'DORMOUSE', 'DRAGONFLY', 'DUCK', 'DUGONG', 'EAGLE', 'ECHIDNA', 'EEL', 'ELEPHANT', 'ELK', 'EMU', 
    'FALCON', 'FERRET', 'FLAMINGO', 'FOX', 'FROG', 'GAZELLE', 'GECKO', 'GIBBON', 'GIRAFFE', 'GOAT', 
    'GOLDFISH', 'GOOSE', 'GORILLA', 'GRASSHOPPER', 'GUINEA PIG', 'HAMSTER', 'HARE', 'HAWK', 
    'HEDGEHOG', 'HERON', 'HIPPOPOTAMUS', 'HORNET', 'HORSE', 'HUMMINGBIRD', 'HYENA', 'IBEX', 'IBIS', 
    'IGUANA', 'JACKAL', 'JAGUAR', 'JELLYFISH', 'KANGAROO', 'KINGFISHER', 'KOALA', 'KOMODO DRAGON', 
    'KRILL', 'LEMMING', 'LEMUR', 'LEOPARD', 'LION', 'LIZARD', 'LLAMA', 'LOBSTER', 'LYNX', 
    'MEERKAT', 'MOLE', 'MONGOOSE', 'MONKEY', 'MOOSE', 'NARWHAL', 'NEWT', 'OCTOPUS', 'OKAPI', 
    'OPOSSUM', 'ORANGUTAN', 'OSTRICH', 'OTTER', 'OWL', 'OYSTER', 'PANDA', 'PANTHER', 'PARROT', 
    'PEACOCK', 'PELICAN', 'PENGUIN', 'PHEASANT', 'PIG', 'PIGEON', 'PLATYPUS', 'POLAR BEAR', 
    'PORCUPINE', 'POSSUM', 'PUMA', 'QUAIL', 'QUOKKA', 'QUOLL', 'RABBIT', 'RACCOON', 'RAT', 
    'RATTLESNAKE', 'RAVEN', 'RED PANDA', 'REINDEER', 'RHINOCEROS', 'SALAMANDER', 'SALMON', 
    'SCORPION', 'SEAHORSE', 'SEAL', 'SHARK', 'SHEEP', 'SHRIMP', 'SKUNK', 'SLOTH', 'SNAIL', 'SNAKE', 
    'SNOW LEOPARD', 'SPARROW', 'SPIDER', 'SQUID', 'SQUIRREL', 'STARFISH', 'STINGRAY', 'STORK', 
    'SWAN', 'TAPIR', 'TARSIER', 'TERMITE', 'TIGER', 'TOAD', 'TORTOISE', 'TOUCAN', 'TURKEY', 
    'TURTLE', 'VULTURE', 'WALLABY', 'WALRUS', 'WARTHOG', 'WASP', 'WEASEL', 'WHALE', 'WILDEBEEST', 
    'WOLF', 'WOLVERINE', 'WOMBAT', 'WOODPECKER', 'YAK', 'ZEBRA'
]  

# list of birds
birds = [
    "ALBATROSS", "AVOCET", "BITTERN", "BLACKBIRD", "BLUEBIRD", "BLUEJAY", "BOOBY", "BULBUL",
    "BUNTING", "BUZZARD", "CANARY", "CARDINAL", "CARACARA", "CHICKADEE", "COCKATOO", "CONDOR",
    "CORMORANT", "COWBIRD", "CRANE", "CREEPER", "CROW", "CUCKOO", "CURLEW", "DOVE", "DUNLIN",
    "EAGLE", "EGRET", "EMU", "FALCON", "FINCH", "FLYCATCHER", "FRIGATEBIRD", "GANNET",
    "GOLDFINCH", "GOOSEM", "GRACKLE", "GROSBEAK", "GROUSE", "GUAN", "GUILLEMOT", "GUINEAFOWL",
    "GULL", "HAWK", "HERON", "HONEYGUIDE", "HOOPOE", "HORNED LARK", "HUMMINGBIRD", "IBIS",
    "JACANA", "JAY", "JUNCO", "KESTREL", "KINGBIRD", "KINGFISHER", "KITTIWAKE", "KIWI",
    "KITE", "LARK", "LOON", "LYREBIRD", "MAGPIE", "MARTIN", "MEADOWLARK", "MERGANSER",
    "MOCKINGBIRD", "MOORHEN", "MURRE", "NIGHTINGALE", "NIGHTJAR", "NUTHATCH", "ORIOLE",
    "OSPREY", "OSTRICH", "OWL", "OYSTERCATCHER", "PARAKEET", "PARROT", "PARTRIDGE",
    "PEACOCK", "PELICAN", "PENGUIN", "PETREL", "PHOEBE", "PIGEON", "PINTAIL", "PLOVER",
    "PUFFIN", "QUAIL", "QUELEA", "QUETZAL", "RAIL", "RAVEN", "REDSTART", "ROADRUNNER",
    "ROBIN", "RUFF", "SANDPIPER", "SCREECH OWL", "SEAGULL", "SECRETARYBIRD", "SHRIKE",
    "SKIMMER", "SKUA", "SPARROW", "STARLING", "STILT", "STORK", "SWALLOW", "SWAN",
    "TANAGER", "TERN", "THRUSH", "TITMOUSE", "TOUCAN", "TROGON", "TURKEY", "VULTURE",
    "WARBLER", "WEAVER", "WHIMBREL", "WOODPECKER", "WREN"
]

def clear():
    """clears the screen by printing empty lines."""
    print('\n' * 5)

def hangman_interface(index):
    """displays the hangman figure based on the number of incorrect guesses."""
    stages = [
        """
               
             | 
             | 
             | 
             | 
             | 
     ________|_
        """,
        """
         _____ 
             | 
             | 
             | 
             | 
             | 
     ________|_
        """,
        """
         _____ 
         |   | 
             | 
             | 
             | 
             | 
     ________|_
        """,
        """
         _____ 
         |   | 
         O   | 
             | 
             | 
             | 
     ________|_
        """,
        """
         _____ 
         |   | 
         O   | 
         |   | 
             | 
             | 
     ________|_
        """,
        """
         _____ 
         |   | 
         O   | 
        /|   | 
             | 
             | 
     ________|_
        """,
        """
         _____ 
         |   | 
         O   | 
        /|\  | 
             | 
             | 
     ________|_
        """,
        """
         _____ 
         |   | 
         O   | 
        /|\  | 
        /    | 
             | 
     ________|_
        """,
        """
         _____ 
         |   | 
         O   | 
        /|\  | 
        / \  | 
             | 
     ________|_
        """
    ]
    print(stages[index])

def start_interface():
    """displays the main menu and gets the user's choice."""
    clear()
    print('####################')
    print('#      Hangman     #')
    print('####################')
    print('       1. Start     ')
    print('       2. Exit      ')
    return input('input selection: ')

def start_interface2():
    """displays the category selection menu."""
    clear()
    print('####################')
    print('#      Hangman     #')
    print('####################')
    print('       1. Animals  ')
    print('       2. Birds    ')
    return input('input selection: ')

def game_interface(guess, miss_attempts, misses, hint_left):
    """displays the game screen with the current word state and input prompt."""
    clear()
    hangman_interface(miss_attempts)
    print('###########################################')
    print('word: ', ' '.join(guess))
    print('# misses:', ' '.join(misses))
    print('# attempts left:', 9 - miss_attempts)
    print('# hints left:', hint_left)
    print('# input ? for hint, # to restart, ! to see answer')
    user_input = input('# guess: ').strip().upper()
    if len(user_input) > 1:
        return '<'
    elif user_input in {'?', '#', '!'} or user_input.isalpha():
        return user_input
    return '<'

def get_hint(word, guess):
    """provides a hint by revealing the first missing letter."""
    for i, letter in enumerate(word):
        if guess[i] == '_':
            return letter

def get_word(selection):
    """selects a random word from the chosen category."""
    if selection == 1:
        return random.choice(animals)
    elif selection == 2:
        return random.choice(birds)
    else:
        return None

def game(word):
    """main game loop handling guesses, hints, and game status."""
    hint_max = 2
    guess = ['_'] * len(word)
    misses = []
    miss_attempts = 0
    hint_times = 0
    while True:
        user_input = game_interface(guess, miss_attempts, misses, hint_max - hint_times)
        if user_input == '#':
            print('restarting...')
            time.sleep(2)
            return True
        elif user_input == '?':
            if hint_times < hint_max:
                hint_letter = get_hint(word, guess)
                for i, letter in enumerate(word):
                    if letter == hint_letter:
                        guess[i] = letter
                hint_times += 1
            else:
                print('# no more hints available!')
                time.sleep(2)
        elif user_input == '!':
            clear()
            hangman_interface(miss_attempts)
            print('# the answer is:', word)
            time.sleep(3)
            return False
        elif user_input == '<':
            print('# invalid input!')
            time.sleep(2)
        else:
            if user_input in word:
                for i, letter in enumerate(word):
                    if letter == user_input:
                        guess[i] = user_input
            else:
                if user_input not in misses:
                    misses.append(user_input)
                miss_attempts += 1
        if '_' not in guess:
            clear()
            hangman_interface(miss_attempts)
            print('# word:', ' '.join(guess))
            print('# congratulations, you won!')
            time.sleep(3)
            return False
        if miss_attempts >= 9:
            print('# game over! the word was:', word)
            time.sleep(3)
            return False

def main():
    """runs the game loop and handles user navigation."""
    clear()
    print('welcome to hangman!')
    input('press enter to start...')
    while True:
        choice = start_interface()
        if choice == '1':
            while True:
                category = start_interface2()
                if category in {'1', '2'}:
                    word = get_word(int(category))
                    while game(word):
                        pass
                    break
        else:
            break
            

if __name__ == "__main__":
    main()