import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth

if __name__ == "__main__":
    load_dotenv()
    SCOPE = 'playlist-read-private'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    results = sp.current_user_playlists()
    playlists = {}
    songs = {}
    for p in results['items']:
        if p['owner']['id'] == os.getenv('SPOTIFY_USERNAME'):
            _id = p['uri'].split(':')[-1]
            playlists[_id] = {'name': p['name'], 'id': _id, 'tracks': []}

    for _id in playlists:
        results = sp.playlist_items(_id)
        # Check if there are more pages! (offset and limit)
        for s in results['items']:
            _id = s['track']['uri'].split(':')[-1]
            if songs.get(_id):
                continue
            songs[_id] = {
                'id': _id,
                'name': s['track']['name'],
                'artists': '; '.join([a['name'] for a in s['track']['artists']]),
                'album_name': s['track']['album']['name'],
                'album_cover_url': s['track']['album']['images'][0]['url'],
                'album_artists': '; '.join([a['name'] for a in s['track']['album']['artists']]),
                'disc_number': s['track']['disc_number'],
                'popularity': s['track']['popularity']
            }
    import yaml
    with open('test/test_songs.yaml', 'w', encoding="utf-8") as f:
        yaml.dump(songs, f)
    with open('test/test_playlists.yaml', 'w', encoding="utf-8") as f:
        yaml.dump(playlists, f)
