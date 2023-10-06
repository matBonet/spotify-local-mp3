# Spotify Local MP3

Script for reading personal playlists from spotify, downloading them and organizing them into folders.

## Necessary configuration

Create a `.env` file at the root folder with the following information:

    SPOTIPY_CLIENT_ID = ...\*
    SPOTIPY_CLIENT_SECRET = ...\*
    SPOTIPY_REDIRECT_URI = ...\*

    SPOTIFY_USERNAME = ...\*

\* See this [link](https://github.com/JayChen35/spotify-to-mp3-python/tree/master#3-setting-up-spotify) to set up the Spotify API.

## To-do

- Parse out emojis
- Build file tree structure
- Check difference to destination path
- Search songs on youtube
- Download with yt-dlp
- Convert to mp3
- Save on destination path
- Generate .m3u files
