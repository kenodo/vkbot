import vk
import time
import random
import json
from urllib.request import urlopen

token = "d531e01fce673a982e0551207dce0b313dd68bc9f5fb43ac94ba7c40302bc7f670076e48de6f94b0cdd45"

print('///')
print('Working...')
print('By Envi_Despair.')
print('///')

session = vk.Session(token)
# session = vk.AuthSession(app_id='5637513', user_login='jake@gmail.com', user_password='Finn')
api = vk.API(session)

while (True):
    try:
        messages = api.messages.get()
        messages = [(m['uid'], m['mid'], m['body'])
                    for m in messages[1:] if m['read_state'] == 0]

        for m in messages:
            user_id = m[0]
            messages_id = m[1]
            command = m[2]
            audios = api.audio.search(q='хава нагила ' + str(command), auto_complete=0, lyrisc=0, performer_only=0,
                                      search_own=0, count=2)
            print(audios)
            mediaId = audios[1]['aid']
            ownerId = audios[1]['owner_id']
            api.messages.send(user_id=user_id, attachment='audio' + str(ownerId) + '_' + str(mediaId))

        ids = ', '.join([str(m[1]) for m in messages])

        if ids:
            api.messages.markAsRead(message_ids=ids)

        time.sleep(3)
    except:
        pass
        api.messages.send(user_id=user_id, message='Кажется, что то случилось не так.')
