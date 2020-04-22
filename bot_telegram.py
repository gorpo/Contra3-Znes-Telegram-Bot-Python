#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hack import *
import requests
import json
import telepot
import math
import time
import re
import os
#api do bot
api = ''





bot = telepot.Bot(api)
# função handle
def handle(msg):
        uid = msg['from']['id']
        firstname = msg['from']['first_name']
        chat_id = msg['chat']['id']
        chat_type = msg['chat']['type']
        try:
                user = '@' + msg['from']['username']
        except:
                print ('')
        msgid = msg['message_id']

        content_type, chat_type, chat_id = telepot.glance(msg)
        if msg.get('text'):
                texto = msg['text'].split()[0]
                #inicio dos comandos ------------------------------------>>>>     
                processo = "zsnesw.exe"
                hacked = hack(processo)
                if texto == 'comandos':
                        bot.sendMessage(chat_id, 'Voce deu vidas no Contra3.' , reply_to_message_id=msgid)
                if texto == 'vida':
                        bot.sendMessage(chat_id, 'Voce deu vidas no Contra3.' , reply_to_message_id=msgid)
                        hacked.vidaContra3()
                if texto == 'escudo':
                        bot.sendMessage(chat_id, 'Voce deu um escudo no Contra3' , reply_to_message_id=msgid)
                        hacked.escudoContra3()
                if texto == 'bomba':
                        bot.sendMessage(chat_id, 'Voce deixou aladin com mais maças' , reply_to_message_id=msgid)
                        hacked.bombaContra3()
                if texto == 'arma1-1':
                        bot.sendMessage(chat_id, 'Voce setou a arma 1 na mao 1', reply_to_message_id=msgid)
                        hacked.arma1Poder1()
                if texto == 'arma1-2':
                        bot.sendMessage(chat_id, 'Voce setou a arma 2 na mao 1', reply_to_message_id=msgid)
                        hacked.arma1Poder2()
                if texto == 'arma1-3':
                        bot.sendMessage(chat_id, 'Voce setou a arma 3 na mao 1', reply_to_message_id=msgid)
                        hacked.arma1Poder3()
                if texto == 'arma1-4':
                        bot.sendMessage(chat_id, 'Voce setou a arma 4 na mao 1', reply_to_message_id=msgid)
                        hacked.arma1Poder4()
                if texto == 'arma1-5':
                        bot.sendMessage(chat_id, 'Voce setou a arma 5 na mao 1', reply_to_message_id=msgid)
                        hacked.arma1Poder5()
                if texto == 'arma2-1':
                        bot.sendMessage(chat_id, 'Voce setou a arma 1 na mao 2', reply_to_message_id=msgid)
                        hacked.arma2Poder1()
                if texto == 'arma2-2':
                        bot.sendMessage(chat_id, 'Voce setou a arma 2 na mao 2', reply_to_message_id=msgid)
                        hacked.arma2Poder2()
                if texto == 'arma2-3':
                        bot.sendMessage(chat_id, 'Voce setou a arma 3 na mao 2', reply_to_message_id=msgid)
                        hacked.arma2Poder3()
                if texto == 'arma2-4':
                        bot.sendMessage(chat_id, 'Voce setou a arma 4 na mao 2', reply_to_message_id=msgid)
                        hacked.arma2Poder4()
                if texto == 'arma2-5':
                        bot.sendMessage(chat_id, 'Voce setou a arma 5 na mao 2', reply_to_message_id=msgid)
                        hacked.arma2Poder5()
























bot.message_loop(handle)
print ('[+] ON')
while 1:
        pass
