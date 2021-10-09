from pywebio.input import *
from pywebio.output import *


input("What's your name?")
select("Select food", ['Orange', 'Apple', 'Banana'])
checkbox("Are your okay?", options=["I'm okay."])
radio("What do you like to do?", options=['Eat', 'Sleep', 'Study'])
put_image(open('vestigo-logo.png', 'rb').read())

put_table([
    ['Hello-app version', '1.0.0'],
    ['Owner', "Joško T."]
    ])
