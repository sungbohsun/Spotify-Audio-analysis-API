# spotify-api
you can get everything in spotify_api.ipynb

*  step1. to get id and secret in spotify development dashboard <br>
https://developer.spotify.com/dashboard/login
*  step2. if you want to get current playing song need to get key on <br>
https://developer.spotify.com/documentation/web-api/reference/player/get-the-users-currently-playing-track/

    ```python
    # to get id and secret in spotify development dashboard
    client_id = '7b53768ec42646b08540bc929483ef5e'
    client_secret = 'ca356e9b3e6f4216af17442bbbd48b0d'

    spotify = SpotifyAPI(client_id, client_secret)
    spotify.perform_auth()
    access_token = spotify.access_token
    ```
