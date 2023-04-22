#!/usr/bin/python
# -*- coding: utf-8 -*-

# @author Anderson Sosnierz 2020-02-25
# Cor \033[style; text; back m \033[m

############

Necessario a intalações da bibiloteca do Telegram

$ pip install python-telegram-bot --upgrade

---------- caso queira fazer manual ---------------------
$ git clone https://github.com/python-telegram-bot/python-telegram-bot
$ cd python-telegram-bot
$ python setup.py install

------------ Dependencia Opcional ----------------------
pip install python-telegram-bot[passport] 
pip install python-telegram-bot[socks] installs httpx[socks]
pip install python-telegram-bot[http2] installs httpx[http2]
pip install python-telegram-bot[rate-limiter] 
pip install python-telegram-bot[webhooks] 
pip install python-telegram-bot[callback-data] i
pip install python-telegram-bot[job-queue] 


pip install python-telegram-bot[all] installs all optional dependencies.
pip install python-telegram-bot[ext] installs all optional dependencies that are related to telegram.ext, i.e. [rate-limiter, webhooks, callback-data, job-queue].

-----------------------------------------------------------