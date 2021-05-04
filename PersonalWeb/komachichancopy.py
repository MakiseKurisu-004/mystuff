# import cgitb 
# cgitb.enable()
import json
from difflib import get_close_matches
data = json.load(open("datacopy.json"))
import cgi

print('content-type:text/html\r\n\r\n')

form = cgi.FieldStorage()

def di(dicti):
    x = data[dicti]
    c = ' '.join(x)
    return ("{}, Onii-chan~.").format(c)

def nt(user_input):
    if user_input in data:
        b = di(user_input)
        return b
    
    elif len(get_close_matches(user_input, data.keys())) > 0:
        j = get_close_matches(user_input, data.keys())[0]
        yn = input(f"Did you mean {j}, Onii-chan~? Y for yes and N for no: ")
        yn = yn.upper()
        if yn == 'Y':
            v = get_close_matches(user_input, data.keys())[0]
            r = di(v)
            return r
        elif yn == 'N':
            return 'What word do want to define, Onii-chan~: '
        else:
            return 'Komachi-chan doens\'t understand'
        
    else:    
        return 'Onii-chan, are you stupid? That word doesn\'t exist.'

user_input = str(form.getvalue('user_Input'))
user_input = user_input.lower()   
print(nt(user_input))

# print(<html>)
# print(<body><center>)
# print(<h1>%s<h1> %user_input.capitalize()) 
# print(<h2>%s<h2> %defe)
# print(<center><body><html>)