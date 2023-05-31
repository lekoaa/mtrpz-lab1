from sys import argv
import interactive
import file

if len(argv) < 2:
    interactive.main()

elif len(argv) == 2:
    file.main(argv[1])