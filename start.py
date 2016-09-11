import sys, getopt
#importera funktionen RunBot() från mappen Jeeves och filen jeeves.py
from Jeeves.jeeves import RunBot

def main(argv):
    try:

        # getopt.getopt(1, 2, 3)
        # 1 = argument när man kör programmet(python start.py -c path/to/config.ini)
        # 2 = options (-c, -h, -s)
        # 3 = långa options (--config,--default,--help osv) Dessa behövs ej, men är bra att ha
        #
        # : i options och = i långa options betyder att det kommer ett argument efter det
        # som t.ex. -o fil.txt, -v video.mkv, -a audio.mp3.

        opts, args = getopt.getopt(argv,"hsc:",["help", "default", "config="])

    except getopt.GetoptError:
        print("Jeeves help section.")
        print("These are the options we offer\n")
        print("-S               | Uses the default config file path (config/config.ini)")
        print("-c <config file> | Specifies the path to the config file")
        sys.exit(2)

    # opts har två arrays. opt och arg.
    # För varje argument vi använde när vi körde filen
    # så kollar vi om den matchar någon av våra inställningar med arrayen opt.
    for opt, arg in opts:

        # Här matchade våran lista med -h och --help en av argumenten i arrayen opt.
        if opt in ("-h", "--help"):
            print("\nJeeves help section.")
            print("These are the options Jeeves can offer\n")
            print("-S               | Uses the default config file path (config/config.ini)")
            print("-c <config file> | Specifies the path to the config file")
            sys.exit()
            # Eftersom det är en inställning som inte kräver något mer argument (så som vägen till en fil)
            # så körs den utan att använda arrayen arg.

        # Här matchade våran lista också en av argumenten i arrayen opt
        elif opt in ("-c", "--config"):
            print("Starting Jeeves with config file %s" % (arg))
            RunBot(arg)
            # Eftersom detta är en inställning som kräver ett till argument efter inställningen
            # så använder den arg, vilket är det som kommer efter vår inställning.
            # e.g. #1 "python start.py -c config.ini" så är arg "config.ini"
            # e.g. #2 "python start.py -c blaha.ini" så är arg "blaha.ini"

        elif opt in ("-S", "--default"):
            print("Starting Jeeves with default config file")
            RunBot('config/config.ini')

        else:
            assert False, "Nonexisting option"

if __name__ == "__main__":
    main(sys.argv[1:])
