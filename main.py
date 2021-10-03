import pytchat
import firebase_admin
from firebase_admin import db
from dotenv import load_dotenv
import os

def write_data(command):

    #writes data to firebase realtime DB

    ref = db.reference("/")
    ref.child("command").update({"command":command})

    return True


#Initialize DB

load_dotenv()
databaseURL = os.getenv('REAL_TIME_DB_URL') #get db url
cred_obj = firebase_admin.credentials.Certificate('key.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})


vid_id = "DWcJFNfaw9c"
chat = pytchat.create(video_id=vid_id)
while chat.is_alive():
    for c in chat.get().sync_items():
        if c.message.startswith("/"):
            print(f"{c.message}")
            write_data(c.message.strip("/")) # writes to DB