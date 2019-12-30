morse_dict = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----'} 
def string_to_list(string):
    return [char for char in string]
def char_to_morse(char):
    morse = morse_dict[char]
    return morse
def morse_to_dur(morse_list, dur_dot, dur_dash):
    dur_list = []
    for each in morse_list:
        listed = string_to_list(each)
        for each in listed:
            if each == ".":
                dur_list.append(dur_dot)
            elif each == "-":
                dur_list.append(dur_dash)
    return dur_list
def string_to_durs(stringo, dur_dot=0.25, dur_dash=1):
    for each in stringo:
        string_ac = stringo.upper().replace(" ", "")
        char_list = string_to_list(string_ac)
        morse_list = []
        for char in char_list:
            morse_list.append(char_to_morse(char))
    print(f"duracion establecida en {morse_list}")
    dur_list = morse_to_dur(morse_list, dur_dot, dur_dash)
    return dur_list

p1 >> blip(0, dur=string_to_durs('ELPITY', 1/4, 1)
