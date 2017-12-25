import telebot
import config
import re

digits_pattern = re.compile(r'^[0-9]+ [0-9]+$', re.MULTILINE)

try:
       matches = re.match(digits_pattern, query.query)
except AttributeError as ex:
    return