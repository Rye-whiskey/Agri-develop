#coding=utf8
import re
from werobot import WeRoBot
robot=WeRoBot(enable_session=False,
              token='sjl943873',
              APP_ID='wxeab84a7432186503',
              APP_SECRET='f7cedb163c502a0fb43292d8cff1e431')


@robot.handler
def hello(message):
    return "Hello"


@robot.text
def echo(message):

    try:
        #提取消息
        msg=message.content.strip().lower().encode('utf8')
        #解析消息
        if  re.compile(".*?你好.*?").match(msg)or \
            re.compile(".*?嗨.*?").match(msg) or \
            re.compile(".*?哈喽.*?").match(msg) or \
            re.compile(".*?hello.*?").match(msg) or \
            re.compile(".*?hi.*?").match(msg) or \
            re.compile(".*?who are you.*?").match(msg) or \
            re.compile(".*?你是谁.*?").match(msg) or \
            re.compile(".*?你的名字.*?").match(msg) or \
            re.compile(".*?什么名字.*?").match(msg):
            return "您好~\n我是ryewhiskey,有什么能帮您的吗？（绅士脸)"
        elif re.compile(".*?厉害.*?").match(msg):
            return "承让承让⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄'"
        elif re.compile(".*？想你.*?").match(msg):
            return "我也想你"
        elif re.compile(".*?傻逼.*?").match(msg)or\
              re.compile(".*?傻吊.*?").match(msg)or\
              re.compile(".*?沙雕.*?").match(msg):
            return "我是你爸爸"
        elif re.compile(".*?天王盖地虎.*?").match(msg):
            return "小鸡炖蘑菇"

    except Exception as e:
        print (e)