import os
from dotenv import load_dotenv
from pprint import pprint as pp

import spotipy
from spotipy.oauth2 import SpotifyOAuth

if __name__ == "__main__":
    load_dotenv()
    scope = 'playlist-read-private'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.current_user_playlists()
    playlists = dict()
    songs = dict()
    for p in results['items']:
        if p['owner']['id'] == os.getenv('SPOTIFY_USERNAME'):
            id = p['uri'].split(':')[-1]
            playlists[id] = {'name': p['name'], 'id': id, 'tracks': list()}

    for id, data in playlists.items():
        results = sp.playlist_items(id)
        # Check if there are more pages! (offset and limit)
        for s in results['items']:
            id = s['track']['uri'].split(':')[-1]
            if songs.get(id):
                continue
            songs[id] = {
                'id': id,
                'name': s['track']['name'],
                'artists': '; '.join([a['name'] for a in s['track']['artists']]),
                'album_name': s['track']['album']['name'],
                'album_cover_url': s['track']['album']['images'][0]['url'],
                'album_artists': '; '.join([a['name'] for a in s['track']['album']['artists']]),
                'disc_number': s['track']['disc_number'],
                'popularity': s['track']['popularity']
            }
    import yaml
    with open('test/test_songs.yaml', 'w') as f:
        yaml.dump(songs, f)
    with open('test/test_playlists.yaml', 'w') as f:
        yaml.dump(playlists, f)