#van koch

from turtle import *
from re import *

programme='AmAmAm'

for n in range(4):
    programme=sub('A','ApAmApA',programme)

programme=sub('A','fd(2); ',programme)
programme=sub('m','rt(120); ',programme)
programme=sub('p','lt(60); ',programme)
exec(programme)

#tutle star

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()