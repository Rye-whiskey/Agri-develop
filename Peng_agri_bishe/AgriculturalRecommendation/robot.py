#coding=utf8
from werobot import WeRoBot
robot=WeRoBot(enable_session=False,
              token='sjl943873',
              APP_ID='wxeab84a7432186503',
              APP_SECRET='f7cedb163c502a0fb43292d8cff1e431')

@robot.handler
def hello(message):
    return 'Hello world'