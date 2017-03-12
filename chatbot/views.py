
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json, requests,re,requests
from pprint import pprint
import pykemon
from random import shuffle

# Create your views here.

VERIFY_TOKEN = '7thseptember2016'
PAGE_ACCESS_TOKEN = 'EAAUP9LUZC9kcBAANFILnfw65UJscjNLBkCgxWlXVutEUiJonLqsXU0rUZAZC2psy96EvDgjmkQ6r3ETpYIxEnWzduByujZAT6kfN0NVLwsUgIUGrCqpGAZCRF6XTR2U6C0uvlwtdUZCVYa7ZAXbeppvFZB5hFqRspm1oxr1jJRE0ZBQZDZD'


def wikisearch(title1):
    # title1="Pokemon " + title
    url = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=%s'%(title1)
    resp = requests.get(url=url).text
    data = json.loads(resp)
    scoped_data = data['query']['pages']
    print scoped_data
    page_id = data['query']['pages'].keys()[0]
    wiki_url = 'https://en.m.wikipedia.org/?curid=%s'%(page_id)
    try:
        wiki_content = scoped_data[page_id]['extract']
        wiki_content = re.sub(r'[^\x00-\x7F]+',' ', wiki_content)
        wiki_content = re.sub(r'\([^)]*\)', '', wiki_content)
        
        
        wiki_content = wiki_content[:100] + ' ...'
    except KeyError:
        wiki_content = ''

    return wiki_url,wiki_content

  
pokemon_data = {"Bulbasaur":"http://img.pokemondb.net/artwork/bulbasaur.jpg","Ivysaur":"http://img.pokemondb.net/artwork/ivysaur.jpg","Venusaur":"http://img.pokemondb.net/artwork/venusaur.jpg","Charmander":"http://img.pokemondb.net/artwork/charmander.jpg","Charmeleon":"http://img.pokemondb.net/artwork/charmeleon.jpg","Charizard":"http://img.pokemondb.net/artwork/charizard.jpg","Squirtle":"http://img.pokemondb.net/artwork/squirtle.jpg","Wartortle":"http://img.pokemondb.net/artwork/wartortle.jpg","Blastoise":"http://img.pokemondb.net/artwork/blastoise.jpg","Caterpie":"http://img.pokemondb.net/artwork/caterpie.jpg","Metapod":"http://img.pokemondb.net/artwork/metapod.jpg","Butterfree":"http://img.pokemondb.net/artwork/butterfree.jpg","Weedle":"http://img.pokemondb.net/artwork/weedle.jpg","Kakuna":"http://img.pokemondb.net/artwork/kakuna.jpg","Beedrill":"http://img.pokemondb.net/artwork/beedrill.jpg","Pidgey":"http://img.pokemondb.net/artwork/pidgey.jpg","Pidgeotto":"http://img.pokemondb.net/artwork/pidgeotto.jpg","Pidgeot":"http://img.pokemondb.net/artwork/pidgeot.jpg","Rattata":"http://img.pokemondb.net/artwork/rattata.jpg","Raticate":"http://img.pokemondb.net/artwork/raticate.jpg","Spearow":"http://img.pokemondb.net/artwork/spearow.jpg","Fearow":"http://img.pokemondb.net/artwork/fearow.jpg","Ekans":"http://img.pokemondb.net/artwork/ekans.jpg","Arbok":"http://img.pokemondb.net/artwork/arbok.jpg","Pikachu":"http://img.pokemondb.net/artwork/pikachu.jpg","Raichu":"http://img.pokemondb.net/artwork/raichu.jpg","Sandshrew":"http://img.pokemondb.net/artwork/sandshrew.jpg","Sandslash":"http://img.pokemondb.net/artwork/sandslash.jpg","Nidoran?":"http://img.pokemondb.net/artwork/nidoran?.jpg","Nidorina":"http://img.pokemondb.net/artwork/nidorina.jpg","Nidoqueen":"http://img.pokemondb.net/artwork/nidoqueen.jpg","Nidorino":"http://img.pokemondb.net/artwork/nidorino.jpg","Nidoking":"http://img.pokemondb.net/artwork/nidoking.jpg","Clefairy":"http://img.pokemondb.net/artwork/clefairy.jpg","Clefable":"http://img.pokemondb.net/artwork/clefable.jpg","Vulpix":"http://img.pokemondb.net/artwork/vulpix.jpg","Ninetales":"http://img.pokemondb.net/artwork/ninetales.jpg","Jigglypuff":"http://img.pokemondb.net/artwork/jigglypuff.jpg","Wigglytuff":"http://img.pokemondb.net/artwork/wigglytuff.jpg","Zubat":"http://img.pokemondb.net/artwork/zubat.jpg","Golbat":"http://img.pokemondb.net/artwork/golbat.jpg","Oddish":"http://img.pokemondb.net/artwork/oddish.jpg","Gloom":"http://img.pokemondb.net/artwork/gloom.jpg","Vileplume":"http://img.pokemondb.net/artwork/vileplume.jpg","Paras":"http://img.pokemondb.net/artwork/paras.jpg","Parasect":"http://img.pokemondb.net/artwork/parasect.jpg","Venonat":"http://img.pokemondb.net/artwork/venonat.jpg","Venomoth":"http://img.pokemondb.net/artwork/venomoth.jpg","Diglett":"http://img.pokemondb.net/artwork/diglett.jpg","Dugtrio":"http://img.pokemondb.net/artwork/dugtrio.jpg","Meowth":"http://img.pokemondb.net/artwork/meowth.jpg","Persian":"http://img.pokemondb.net/artwork/persian.jpg","Psyduck":"http://img.pokemondb.net/artwork/psyduck.jpg","Golduck":"http://img.pokemondb.net/artwork/golduck.jpg","Mankey":"http://img.pokemondb.net/artwork/mankey.jpg","Primeape":"http://img.pokemondb.net/artwork/primeape.jpg","Growlithe":"http://img.pokemondb.net/artwork/growlithe.jpg","Arcanine":"http://img.pokemondb.net/artwork/arcanine.jpg","Poliwag":"http://img.pokemondb.net/artwork/poliwag.jpg","Poliwhirl":"http://img.pokemondb.net/artwork/poliwhirl.jpg","Poliwrath":"http://img.pokemondb.net/artwork/poliwrath.jpg","Abra":"http://img.pokemondb.net/artwork/abra.jpg","Kadabra":"http://img.pokemondb.net/artwork/kadabra.jpg","Alakazam":"http://img.pokemondb.net/artwork/alakazam.jpg","Machop":"http://img.pokemondb.net/artwork/machop.jpg","Machoke":"http://img.pokemondb.net/artwork/machoke.jpg","Machamp":"http://img.pokemondb.net/artwork/machamp.jpg","Bellsprout":"http://img.pokemondb.net/artwork/bellsprout.jpg","Weepinbell":"http://img.pokemondb.net/artwork/weepinbell.jpg","Victreebel":"http://img.pokemondb.net/artwork/victreebel.jpg","Tentacool":"http://img.pokemondb.net/artwork/tentacool.jpg","Tentacruel":"http://img.pokemondb.net/artwork/tentacruel.jpg","Geodude":"http://img.pokemondb.net/artwork/geodude.jpg","Graveler":"http://img.pokemondb.net/artwork/graveler.jpg","Golem":"http://img.pokemondb.net/artwork/golem.jpg","Ponyta":"http://img.pokemondb.net/artwork/ponyta.jpg","Rapidash":"http://img.pokemondb.net/artwork/rapidash.jpg","Slowpoke":"http://img.pokemondb.net/artwork/slowpoke.jpg","Slowbro":"http://img.pokemondb.net/artwork/slowbro.jpg","Magnemite":"http://img.pokemondb.net/artwork/magnemite.jpg","Magneton":"http://img.pokemondb.net/artwork/magneton.jpg","Farfetch'd":"http://img.pokemondb.net/artwork/farfetch'd.jpg","Doduo":"http://img.pokemondb.net/artwork/doduo.jpg","Dodrio":"http://img.pokemondb.net/artwork/dodrio.jpg","Seel":"http://img.pokemondb.net/artwork/seel.jpg","Dewgong":"http://img.pokemondb.net/artwork/dewgong.jpg","Grimer":"http://img.pokemondb.net/artwork/grimer.jpg","Muk":"http://img.pokemondb.net/artwork/muk.jpg","Shellder":"http://img.pokemondb.net/artwork/shellder.jpg","Cloyster":"http://img.pokemondb.net/artwork/cloyster.jpg","Gastly":"http://img.pokemondb.net/artwork/gastly.jpg","Haunter":"http://img.pokemondb.net/artwork/haunter.jpg","Gengar":"http://img.pokemondb.net/artwork/gengar.jpg","Onix":"http://img.pokemondb.net/artwork/onix.jpg","Drowzee":"http://img.pokemondb.net/artwork/drowzee.jpg","Hypno":"http://img.pokemondb.net/artwork/hypno.jpg","Krabby":"http://img.pokemondb.net/artwork/krabby.jpg","Kingler":"http://img.pokemondb.net/artwork/kingler.jpg","Voltorb":"http://img.pokemondb.net/artwork/voltorb.jpg","Electrode":"http://img.pokemondb.net/artwork/electrode.jpg","Exeggcute":"http://img.pokemondb.net/artwork/exeggcute.jpg","Exeggutor":"http://img.pokemondb.net/artwork/exeggutor.jpg","Cubone":"http://img.pokemondb.net/artwork/cubone.jpg","Marowak":"http://img.pokemondb.net/artwork/marowak.jpg","Hitmonlee":"http://img.pokemondb.net/artwork/hitmonlee.jpg","Hitmonchan":"http://img.pokemondb.net/artwork/hitmonchan.jpg","Lickitung":"http://img.pokemondb.net/artwork/lickitung.jpg","Koffing":"http://img.pokemondb.net/artwork/koffing.jpg","Weezing":"http://img.pokemondb.net/artwork/weezing.jpg","Rhyhorn":"http://img.pokemondb.net/artwork/rhyhorn.jpg","Rhydon":"http://img.pokemondb.net/artwork/rhydon.jpg","Chansey":"http://img.pokemondb.net/artwork/chansey.jpg","Tangela":"http://img.pokemondb.net/artwork/tangela.jpg","Kangaskhan":"http://img.pokemondb.net/artwork/kangaskhan.jpg","Horsea":"http://img.pokemondb.net/artwork/horsea.jpg","Seadra":"http://img.pokemondb.net/artwork/seadra.jpg","Goldeen":"http://img.pokemondb.net/artwork/goldeen.jpg","Seaking":"http://img.pokemondb.net/artwork/seaking.jpg","Staryu":"http://img.pokemondb.net/artwork/staryu.jpg","Starmie":"http://img.pokemondb.net/artwork/starmie.jpg","Mr. Mime":"http://img.pokemondb.net/artwork/mr. mime.jpg","Scyther":"http://img.pokemondb.net/artwork/scyther.jpg","Jynx":"http://img.pokemondb.net/artwork/jynx.jpg","Electabuzz":"http://img.pokemondb.net/artwork/electabuzz.jpg","Magmar":"http://img.pokemondb.net/artwork/magmar.jpg","Pinsir":"http://img.pokemondb.net/artwork/pinsir.jpg","Tauros":"http://img.pokemondb.net/artwork/tauros.jpg","Magikarp":"http://img.pokemondb.net/artwork/magikarp.jpg","Gyarados":"http://img.pokemondb.net/artwork/gyarados.jpg","Lapras":"http://img.pokemondb.net/artwork/lapras.jpg","Ditto":"http://img.pokemondb.net/artwork/ditto.jpg","Eevee":"http://img.pokemondb.net/artwork/eevee.jpg","Vaporeon":"http://img.pokemondb.net/artwork/vaporeon.jpg","Jolteon":"http://img.pokemondb.net/artwork/jolteon.jpg","Flareon":"http://img.pokemondb.net/artwork/flareon.jpg","Porygon":"http://img.pokemondb.net/artwork/porygon.jpg","Omanyte":"http://img.pokemondb.net/artwork/omanyte.jpg","Omastar":"http://img.pokemondb.net/artwork/omastar.jpg","Kabuto":"http://img.pokemondb.net/artwork/kabuto.jpg","Kabutops":"http://img.pokemondb.net/artwork/kabutops.jpg","Aerodactyl":"http://img.pokemondb.net/artwork/aerodactyl.jpg","Snorlax":"http://img.pokemondb.net/artwork/snorlax.jpg","Articuno":"http://img.pokemondb.net/artwork/articuno.jpg","Zapdos":"http://img.pokemondb.net/artwork/zapdos.jpg","Moltres":"http://img.pokemondb.net/artwork/moltres.jpg","Dratini":"http://img.pokemondb.net/artwork/dratini.jpg","Dragonair":"http://img.pokemondb.net/artwork/dragonair.jpg","Dragonite":"http://img.pokemondb.net/artwork/dragonite.jpg","Mewtwo":"http://img.pokemondb.net/artwork/mewtwo.jpg","Mew":"http://img.pokemondb.net/artwork/mew.jpg"}



def logg(mess,meta='log',symbol='#'):

    print '%s\n%s\n%s'%(symbol*20,mess,symbol*20)

def set_greeting_text():
    post_message_url = "https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s"%PAGE_ACCESS_TOKEN
    greeting_text = "Type something like this'Hey bot"
    greeting_object = json.dumps({"setting_type":"greeting", "greeting":{"text":greeting_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=greeting_object)
    pprint(status.json())

def render_postback(fbid,payload):
    

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN

    response_msg4 = json.dumps({"recipient":{"id":fbid}, "message":{"text": payload[:300]}})
    
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg4)
    pprint(status.json())
      
    
    

    print '%s\n%s\n%s'%('&'*20,payload,'&'*20)

def post_facebook_message(fbid, recevied_message):

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    
    joke_text="Hello there. Type either the word 'random' or a pokemon name to get started. After that you can click on the buttons accordingly "
    flag1=0
    tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
    for token in tokens:
      if token=="hello" or token=="hi" or token=="hey" or token=="yo":
        response = json.dumps({"recipient":{"id":fbid}, "message":{"text":joke_text}})
      
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response)
        pprint(status.json())
        flag1=1
        break 

    if flag1==0:
      name1,text=search_pokemon(recevied_message)
      if name1!="Not found":
        str1,str2=postbackpoke(name1)
        
        wiki_url, wiki_content = wikisearch(name1)
        if len(wiki_content)==0:
          wiki_content="Can't find anything on wiki"
        response_msg = json.dumps(
                {"recipient":{
                    "id":fbid
                  },
                                "message":{
                      "attachment":{
                        "type":"template",
                        "payload":{
                          "template_type":"button",
                          "text":wiki_content,
                          "buttons":[

                            {
                            "type": "postback",
                            "title": "Evolution",
                            "payload": str1,
                        },

                        {
                            "type": "postback",
                            "title": "Moves",
                            "payload": str2,
                        },
                            {
                              "type":"web_url",
                              "url":wiki_url,
                              "title":"Open on wiki"
                            },
                            
                          ]
                        }
                      }
                    }
                }
            )
        response_msg2 = json.dumps(
                {"recipient":{
                    "id":fbid
                  },
             "message":{
                        "attachment":{
                            "type":"image",
                            "payload":{
                                "url":text
                            }
                        }
                    }
             })

        response_msg3 = json.dumps({"recipient":{"id":fbid}, "message":{"text":"Name " + name1}})
        
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg3)
        pprint(status.json())

        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg2)
        pprint(status.json())

        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
        pprint(status.json())

      else:
        response1 = json.dumps({"recipient":{"id":fbid}, "message":{"text":"No pokeon found. Check your spelling"}})
      
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response1)


def search_pokemon(recevied_message):

  tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
  pokemon="Not found"
  pokemon_image=""
  
  for token in tokens:
    if token=="random":
      keys=list(pokemon_data.keys())
      shuffle(keys)
      pokemon=keys[0].lower()
      pokemon_image=pokemon_data[keys[0]]
      break
      

    else:
      flag=0
      for key,value in pokemon_data.iteritems():
        if key.lower()==token:
          pokemon_image=value
          pokemon=key.lower()
          flag=1
          break

    if flag==1:
      text="ypppp"
      break
  
  return pokemon,pokemon_image

def postbackpoke(pokemon):
  str1=evolutions(pokemon)
  str2=moves(pokemon)

  return str1,str2

  

def evolutions(name):
  result_arr=[]
  try:
    p=pykemon.get(pokemon=name)
    for keys in p.evolutions.keys():
      result_arr.append(keys)

    str1 = ' '.join(str(e) for e in result_arr)
    if len(str1)==0:
      str1="No evloutions"
  except:
    str1=" "
  return str1

def moves(name):
  result_arr=[]
  try:
    p=pykemon.get(pokemon=name)
    for keys in p.moves.keys():
      if len(result_arr)<15:
          result_arr.append(keys)

    str2 = ', '.join(str(e) for e in result_arr)
    if len(str2)==0:
      str2="No moves found"
  except:
    str2=" "
  return str2

class MyChatBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        if len(incoming_message)>0:
          for entry in incoming_message['entry']:
              for message in entry['messaging']:
                  # Check to make sure the received call is a message call
                  # This might be delivery, optin, postback for other events 
                  if 'postback' in message:
                      print '%s\n%s\n%s'%('$'*20,message,'$'*20)
                      render_postback(message['sender']['id'],message['postback']['payload'])

                  if 'message' in message:
                      # Print the message to the terminal
                      # Assuming the sender only sends text. Non-text messages like stickers, audio, \\pictures
                      # are sent as attachments and must be handled accordingly. 
                      print '%s\n%s\n%s'%('*'*20,message,'*'*20)
                      
                      try:  
                          post_facebook_message(message['sender']['id'], message['message']['text'])
                      except Exception as e:
                          print '%s\n%s\n%s'%('%'*20,e,'%'*20)
                          post_facebook_message(message['sender']['id'], 'random')


        return HttpResponse()    


