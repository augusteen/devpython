import sys, getopt

def main(argv):
    print(argv[1])
    print(len(argv))

if __name__ == "__main__":
    main(sys.argv[1:])
'''
You are to write two tiny Python scripts that test out processing command line arguments using two
methods:
1. Plain old sys.argv like you would do normally.
2. Python’s argparse package, for more fancy argument handling.
Your test script should be able to handle the following situations:
1. Getting help with –help or -h.
2. At least three arguments that are flags, meaning they don’t take an extra argument but simply
putting them on the command line turns something on.
“Shaw_Exercise04” — 2017/7/27 — 15:44 — page 25 — #2
DEALING WITH COMMAND LINE ARGUMENTS 25
3. At least three arguments that are options, meaning they do take an argument and set a variable
in your script to that option.
4. Additional “positional” arguments, which are lists of files at the end of all the – style arguments
and can handle Terminal wildcards like */.txt.
Since this exercise is a spike you should have the attitude that if something is a pain during your test you
can abandon it and try the other thing. Start with trying to solve this with sys.argv, and then if you just
can’t figure it out try argparse instead.
Remember that this is a timed 45-minute exercise and you need to stick to that. You must also keep
track of everything you do to get started. Your purpose with this exercise is to figure out how you keep
getting in your own way to start a project. Are you talking yourself out of it before you even start? Do you
not know where your text editor is or how to use it? Write it down, and then figure out how to remove that
friction.
'''