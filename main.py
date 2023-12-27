import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json
from commands import SPOTIPY_CLIENT_SECRET, SPOTIPY_CLIENT_ID, SPOTIPY_REDIRECT_URI, LFM_API_KEY

genre_list = ['pop', 'rap', 'rock', 'urbano latino', 'hip hop', 'trap latino', 'reggaeton', 'dance pop', 'pop rap',
              'modern rock', 'pov: indie', 'musica mexicana', 'latin pop', 'classic rock', 'filmi', 'permanent wave',
              'trap', 'alternative metal', 'k-pop', 'r&b', 'corrido', 'canadian pop', 'norteno', 'sierreno',
              'album rock', 'soft rock', 'pop dance', 'sad sierreno', 'edm', 'hard rock', 'contemporary country',
              'mellow gold', 'uk pop', 'melodic rap', 'modern bollywood', 'alternative rock', 'banda', 'post-grunge',
              'corridos tumbados', 'sertanejo universitario', 'nu metal', 'country', 'art pop', 'atl hip hop',
              'urban contemporary', 'sertanejo', 'southern hip hop', 'singer-songwriter', 'reggaeton colombiano',
              'arrocha', 'french hip hop', 'colombian pop', 'alt z', 'country road', 'mexican pop', 'canadian hip hop',
              'j-pop', 'indonesian pop', 'singer-songwriter pop', 'ranchera', 'new wave pop', 'indietronica',
              'german hip hop', 'pop urbaine', 'rock en espanol', 'latin alternative', 'gangster rap', 'soul',
              'k-pop boy group', 'latin arena pop', 'chicago rap', 'italian pop', 'heartland rock', 'k-pop girl group',
              'agronejo', 'modern country pop', 'electro house', 'latin hip hop', 'canadian contemporary r&b',
              'pop punk', 'neo mellow', 'pop rock', 'latin rock', 'punjabi pop', 'rap metal', 'trap argentino',
              'new romantic', 'new wave', 'uk dance', 'slap house', 'modern alternative rock', 'indie pop',
              'indie rock', 'house', 'conscious hip hop', 'modern country rock', 'east coast hip hop', 'folk rock',
              'metal', 'turkish pop', 'bedroom pop', 'desi pop', 'italian hip hop', 'hoerspiel', 'afrobeats',
              'adult standards', 'post-teen pop', 'neo soul', 'sped up', 'cloud rap', 'viral pop', 'talent show',
              'spanish pop', 'punk', 'alternative r&b', 'grupera', 'west coast rap', 'opm', 'boy band',
              'psychedelic rock', 'glam metal', 'stomp and holler', 'desi hip hop', 'ccm', 'rage rap', 'hip pop',
              'puerto rican pop', 'german pop', 'miami hip hop', 'argentine rock', 'sertanejo pop', 'tropical',
              'glam rock', 'funk carioca', 'nigerian pop', 'argentine hip hop', 'dark trap', 'latin viral pop',
              'piano rock', 'detroit hip hop', 'italian adult pop', 'country rock', 'underground hip hop',
              'mexican hip hop', 'progressive electro house', 'synthpop', 'metropopolis', 'garage rock', 'indie folk',
              'vocal jazz', 'classical', 'europop', 'progressive house', 'art rock', 'yacht rock', 'mpb', 'pagode',
              'tropical house', 'urbano espanol', 'chamber pop', 'rap francais', 'dance rock', 'j-rock',
              'polish hip hop', 'sleep', 'folk', 'anime', 'trap brasileiro', 'disco', 'pluggnb', 'british soul',
              'metalcore', 'australian pop', 'uk hip hop', 'christian music', 'gen z singer-songwriter', 'electropop',
              'big room', 'forro', 'swedish pop', 'classic oklahoma country', 'reggaeton flow', 'pop nacional',
              'british invasion', 'mexican rock', 'indie soul', 'contemporary r&b', 'folk-pop', 'white noise',
              'pagode novo', 'soundtrack', 'funk metal', 'grunge', 'french pop', 'emo rap', 'salsa', 'rain',
              'r&b francais', 'lgbtq+ hip hop', 'turkish rock', 'memphis hip hop', 'mariachi', 'brostep',
              'classic soul', 'funk mtg', 'trap triste', 'dirty south rap', 'melodic metalcore', 'blues rock',
              'alternative hip hop', 'melancholia', 'pop soul', 'brazilian gospel', 'outlaw country',
              'orchestral soundtrack', 'dutch house', 'turkish hip hop', 'queens hip hop', 'christian alternative rock',
              'mandopop', 'lounge', 'worship', 'dfw rap', 'electronica', 'pixel', 'trap italiana', 'pop reggaeton',
              'new orleans rap', 'otacore', 'rock-and-roll', 'funk', 'quiet storm', 'motown', 'japanese teen pop',
              'brazilian hip hop', 'gruperas inmortales', 'kleine hoerspiel', 'indie poptimism', 'dream pop',
              'rap conscient', 'neo-synthpop', 'funk rock', 'easy listening', 'bolero', 'g funk', 'barbadian pop',
              'progressive rock', 'eurodance', 'hardcore hip hop', 'bachata', 'australian dance', 'neon pop punk',
              'emo', 'trap boricua', 'brazilian rock', 'funk paulista', 'pop venezolano', 'cantautor', 'chanson',
              'drift phonk', 'florida rap', 'bedroom r&b', 'latin christian', 'movie tunes', 'indonesian pop rock',
              'russian hip hop', 'spanish hip hop', 'cali rap', 'dancehall', 'brooklyn drill', 'trap queen',
              'urbano chileno', 'color noise', "children's music", 'world worship', 'urbano mexicano',
              'sheffield indie', 'classic texas country', 'escape room', 'modern indie pop', 'funk rj', 'plugg',
              'anime rock', 'merseybeat', 'reggae fusion', 'shoegaze', 'tamil hip hop', 'britpop', 'australian rock',
              'industrial metal', 'baroque pop', 'brooklyn indie', 'pop argentino', 'r&b en espanol', 'trance',
              'turkish trap', 'thai pop', 'lilith', 'indian instrumental', 'downtempo', 'southern rock', 'sophisti-pop',
              'punjabi hip hop', 'polish trap', 'socal pop punk', 'candy pop', 'tamil pop', 'rockabilly', 'girl group',
              'uk contemporary r&b', 'atl trap', 'old school thrash', 'classic bollywood', 'compositional ambient',
              'gym phonk', 'north carolina hip hop', 'dark r&b', 'country dawn', 'symphonic rock', 'tennessee hip hop',
              'instrumental lullaby', 'pittsburgh rap', 'thrash metal', 'afropop', 'screamo', 'canadian rock',
              'kindermusik', 'melodic drill', 'nyc rap', 'modern blues rock', 'rock nacional brasileiro', 'philly rap']
print(len(genre_list))
sp_scopes = "playlist-modify-public" + ",user-read-private"
auth = oauth2.SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
)
spotify = spotipy.Spotify(client_credentials_manager=auth)


def get_genre(artist, track, spotify_id, n=3):
    url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        'method': 'track.gettoptags',
        'artist': artist,
        'track': track,
        'api_key': LFM_API_KEY,
        'format': 'json'
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Extracting genre from top tags
    genres = []
    if 'toptags' in data and 'tag' in data['toptags']:
        for tag in data['toptags']['tag']:
            genre = tag['name']
            if genre in genre_list:
                genres.append(genre)
                if len(genres) == n and n != 0:
                    return genres

    if len(genres) == 0:
        genres = spotify.artist(spotify.track(spotify_id)['artists'][0]['id'])['genres']

    return genres


def get_playlist_tracks(url):
    results = spotify.playlist_items(url)
    full_tracks = results['items']

    # Loops to ensure I get every track of the playlist
    while results['next']:
        results = spotify.next(results)
        full_tracks.extend(results['items'])

    tracks = []
    len_playlist = len(full_tracks)
    counter = 0
    for track in full_tracks:
        name = track["track"]["name"]
        artists_name = track["track"]["artists"][0]["name"]
        spotify_id = track["track"]["id"]
        genres = get_genre(artists_name, name, spotify_id)

        tracks.append({"name": name,
                       "artists": artists_name,
                       "genres": genres,
                       "spotify_id": spotify_id})
        counter += 1
        progress_bar(counter, len_playlist)

    return tracks


def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction * 100)}%', end=ending)


playlist_url = "https://open.spotify.com/playlist/68VHPXaE81W5oGYOvEM14Y?si=df05394a44c24608"
tracks = get_playlist_tracks(playlist_url)
print(json.dumps(tracks, indent=4))

genres = spotify.artist(spotify.track("3Ydwbd3REFlpWIEhCNI6fC")['artists'][0]['id'])['genres']
print(genres)
