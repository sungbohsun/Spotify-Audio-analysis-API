# spotify-api
you can get everything in spotify_api.ipynb

*  step1. to get id and secret in spotify development dashboard <br>
https://developer.spotify.com/dashboard/login
*  step2. if you want to get current playing song need to get key on <br>
https://developer.spotify.com/documentation/web-api/reference/player/get-the-users-currently-playing-track/


    **set id & secret **
    ```python
    from sung_spotify import SpotifyAPI
    client_id = '7b53768ec42646b08540bc929483ef5e'
    client_secret = 'ca356e9b3e6f4216af17442bbbd48b0d'

    spotify = SpotifyAPI(client_id, client_secret)
    spotify.perform_auth()
    access_token = spotify.access_token
    ```
    
    ```python
    singer = '周杰倫'
    song_name = '簡單愛'
    track_id = spotify.search_id(singer,song_name)
    print(singer,song_name,track_id)
    ```
    
    ```python
    #use id to search Spotify Audio analysis
    #singer & song_name only use to save file
    spotify.analysis(singer,song_name,track_id)
    ```
