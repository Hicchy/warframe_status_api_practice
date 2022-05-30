from alerts_and_events import darvo_deal
from open_worlds import cambion_status
from open_worlds import cetus_status
from alerts_and_events import get_fissures





def inquiry():
    inquire = True
    while inquire:
        user_input = input("Type in your command. 'help' for help, 'exit' to exit:")
        if user_input == "exit":
            inquire = False
        elif user_input == "help":
            print("""            Type 'cetus' for info about Cetus,
            type 'cambion' for info about Cambion Drift,
            type 'darvo' for info about the current Darvo Deal,
            type 'fissures' to see current void fissures.\n""")
        elif user_input == "cetus":
            print(cetus_status)
        elif user_input == "cambion":
            print(cambion_status)
        elif user_input == "darvo":
            print(darvo_deal)
        elif user_input == "fissures":
            get_fissures()




inquiry()
