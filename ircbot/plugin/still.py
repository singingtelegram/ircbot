"""Really? it's {current_year}."""
import datetime
import random


def register(bot):
    bot.listen(r'^!still (.+)', still)


def still(bot, msg):
    """required docstrings on obvious functions, in 2019 - LOLW"""
    year = datetime.date.today().year
    lol = random.choice(['LOL', 'LOLW', 'LMAO', 'NUUU'])
    msg.respond(f'{msg.match[1]}, in {year} - {lol}!', ping=False)
