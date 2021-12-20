import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline() #read one line from the laguage file it is given
#main meat of the code in a function ,will be called at the end of this script
    if line: #if statement, testing whether line has something in it.the readline function will return an empty string when it reaches the end of the file and if line simply test this empty string
        print_line(line, encoding, errors)# call a separate function to do the actual printing of this line. simplifies my code.
        return main(language_file, encoding, errors)
#calling main again inside main. make it loop.line 8 keeps this function from looping forever.

def print_line(line, encoding, errors):#print_line fonction does the actual encoding of each line from the languages.txt file.
    next_lang = line.strip() #a simple stripping of the trailing \n on the line string.
    raw_bytes = next_lang.encode(encoding, errors=errors) #take the language from languages.txt and encode it with the raw bytes  DBES===decode bytesmencode strings.
#next_lang is a string to get a raw bytes we mush call.encode() pass to encode() the encoding we want and how to hadle errors
    cooked_string = raw_bytes.decode(encoding, errors=errors)
# creating a cooked_string from raw_bytes showing the inverse of line 15.decode bytes. decode() raw_bytes t oget a string. should be the same as next_lang
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")
#open langu .txt file
main(languages, encoding, error)
# here main is to get everything going and kick-start the loop .
#then jumps to where the main function is defined in line 5 and line 10 is called again, causing this to keep looping, this if line on line 8 will prevent our loop from going forever .
# python3.9 ex23.py utf-8 strict
#b'' snf converting them to utf-8 (show in hexadecimal)encoding your sprcified
#left side of <====> is python numerical bytes (raw bytes)we specify this with b'' to tell python this is raw_bytes#
#this raw bytes are then displayed cooked on the right so we cansee the real chara in the terminal .
#a string is a urf-9 encoded sequence of chara for displaying with text
# utf-16 strict
