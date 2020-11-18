import requests
import datetime
from urllib.parse import urlencode
import base64
import json
import pandas as pd

class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"
    
    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        Returns a base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception("You must set client_id and client_secret")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()
    
    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }
    
    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        } 
    
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in'] # seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True
    
    def search_id(self,singer,song_name):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        endpoint = "https://api.spotify.com/v1/search"
        data = urlencode({"q": song_name, 
                          "artist" : singer,
                          "type": "track"})


        lookup_url = f"{endpoint}?{data}"
        r = requests.get(lookup_url, headers=headers)
        print(r.status_code,'in step one')

        if r.status_code != 200:
            print('error in search song id')
        else:
            tmp = r.json()
            track_id = tmp['tracks']['items'][0]['uri'].split(':')[2]
        return track_id

    
    #Spotify Audio analysis
    def analysis(self,singer,song_name,track_id):

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        #get Audio analysis
        endpoint = " https://api.spotify.com/v1/audio-analysis/"+track_id
        lookup_url = f"{endpoint}"
        r = requests.get(lookup_url, headers=headers)
        result = r.json()
        print(r.status_code,'in audio-analysis')
        if r.status_code != 200:
            print('error in get audio-analysis')

        #save Audio analysis file as json
        with open('audio-analysis_'+singer+'_'+song_name+'.json', 'w') as outfile:
            json.dump(result, outfile)

        print('success save','audio-analysis_'+singer+'_'+song_name+'.json')

    #     #get Audio features
    #     endpoint = " https://api.spotify.com/v1/audio-features/"+track_id
    #     lookup_url = f"{endpoint}"
    #     r = requests.get(lookup_url, headers=headers)
    #     result = r.json()
    #     print(r.status_code,'in get audio-features')
    #     if r.status_code != 200:
    #         print('error in get audio-features')

    #     #save file audio-features as json
    #     with open("audio-features_"+singer+'_'+song_name+'.json', 'w') as outfile:
    #         json.dump(result, outfile)

    #     print('success save',"audio-features_"+singer+'_'+song_name+'.json')

    def playlist_songid(self,playlist_id):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        #get Audio analysis
        endpoint = " https://api.spotify.com/v1/playlists/"+playlist_id+'?market=TW'
        lookup_url = f"{endpoint}"
        r = requests.get(lookup_url, headers=headers)
        result = r.json()
        print(r.status_code)
        df = pd.DataFrame()
        track_id , singer, song_name, duration = [], [], [], []
        for i in range(len(result['tracks']['items'])):
            track_id.append(result['tracks']['items'][i]['track']['uri'].split(':')[2])
            singer.append(result['tracks']['items'][i]['track']['artists'][0]['name'])
            song_name.append(result['tracks']['items'][i]['track']['name'])
            duration.append(result['tracks']['items'][i]['track']['duration_ms'])
        df['track_id'] = track_id
        df['singer'] = singer
        df['song_name'] = song_name
        df['duration'] = duration
        df.to_csv(result['name']+'.csv')
        print('save playlist as',result['name']+'.csv')
        
    def current_song(self,access_token):
        # need get access_token in 
        # https://developer.spotify.com/documentation/web-api/reference/player/get-the-users-currently-playing-track/
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        endpoint = "https://api.spotify.com/v1/me/player?market=TW&additional_types=episode"
        r = requests.get(endpoint, headers=headers)
        print(r.status_code,'in step one')
        tmp = r.json()
        track_id = tmp['item']['uri'].split(':')[2]
        singer = tmp['item']['artists'][0]['name']
        song_name = tmp['item']['name']
        return singer,song_name,track_id