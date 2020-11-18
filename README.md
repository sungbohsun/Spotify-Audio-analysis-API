# spotify-api
you can get everything in spotify_api.ipynb

*  step1. to get id and secret in spotify development dashboard <br>
https://developer.spotify.com/dashboard/login
*  step2. if you want to get current playing song need to get key on <br>
https://developer.spotify.com/documentation/web-api/reference/player/get-the-users-currently-playing-track/


###### set id & secret
    ```python
    from sung_spotify import SpotifyAPI
    client_id = '7b53768ec42646b08540bc929483ef5e'
    client_secret = 'ca356e9b3e6f4216af17442bbbd48b0d'

    spotify = SpotifyAPI(client_id, client_secret)
    spotify.perform_auth()
    access_token = spotify.access_token
    ```
    
###### use singer & song_name to get song_id   
    ```python
    singer = '周杰倫'
    song_name = '簡單愛'
    track_id = spotify.search_id(singer,song_name)
    print(singer,song_name,track_id)
    ```
    200 in step one <br>
    周杰倫 簡單愛 5Jtg0qcTKMHq3HjPVGRFAi

###### use id to search Spotify Audio analysis    
    ```python
    #use id to search Spotify Audio analysis
    #singer & song_name only use to save file
    spotify.analysis(singer,song_name,track_id)
    ```
    200 in audio-analysis <br> 
    success save audio-analysis_周杰倫_簡單愛.json
    
###### get spotify play list song_name singer song_id <br>
  you can copy play list id on spotify app
    ```python
    spotify.playlist_songid('37i9dQZF1DX4sWSpwq3LiO')
    ```
    200 <br>
    save playlist as Peaceful Piano.csv
###### get current playing song singer & song_name & track_id
    ```python
    key = 'BQBl9AfhhgYBqHFMFaS_q4H1hA0mRi_9pJ-co4JYNYT6zmGshYaY2tLDiU5Hns6f8DFLbZ6iz5oQKKXR8wKDjEIusoPiVI5HhRlxRLRqXo0dBYM8ixS7-qSyPgxcXSjcN4McpWWpCxRZvOPXh-ANzIPLTPzPwQ'
    singer,song_name,track_id = spotify.current_song(key)
    print(singer,song_name,track_id)
    ```
    200 in step one <br>
    Avril Lavigne Head Above Water 7gY3cyGcB2wnk2xDXiA0pe
