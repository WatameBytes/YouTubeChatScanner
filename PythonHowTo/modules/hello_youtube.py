import messages

messages.hello()
messages.bye()

import messages as msg
msg.hello()
msg.bye()

from messages import hello, bye
# from messages import *
hello()
bye()