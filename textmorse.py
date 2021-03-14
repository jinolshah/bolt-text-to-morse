import time

def converter(form):
    string = str(form.character.data)
    string = string.strip()
    morse = ""
    count = 0

    code = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---',
            'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
            'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----',
            ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

    #using ' ' for space between letters and '|' for space between words

    try:
        for letter in string.upper():
            count = count + 1
            if letter != ' ':
                morse = morse + code[letter]
            else:
                morse = morse + '|'
            if count != len(string) and letter != ' ' and string[count] != ' ':
                morse = morse + ' '
        return "invalid"
    except:
        return None

# Buzzer is pin 0 and LED pin 1

def hitter(codeout, opchoice, mybolt):
    if opchoice == "Buzzer":
        for char in codeout:
            if char == ".":
                response = mybolt.digitalWrite('0', 'HIGH')
                response = mybolt.digitalWrite('0', 'LOW')
            else:
                response = mybolt.digitalWrite('0', 'HIGH')
                time.sleep(1)
                response = mybolt.digitalWrite('0', 'LOW')
    else:
        for char in codeout:
            if char == ".":
                response = mybolt.digitalWrite('1', 'HIGH')
                response = mybolt.digitalWrite('1', 'LOW')
            else:
                response = mybolt.digitalWrite('1', 'HIGH')
                time.sleep(1)
                response = mybolt.digitalWrite('1', 'LOW')