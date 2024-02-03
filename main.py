import datapackage
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import spotipy
import spotipy.oauth2 as oauth2
from clientSecrets import SPOTIPY_CLIENT_SECRET, SPOTIPY_CLIENT_ID, SPOTIPY_REDIRECT_URI, LFM_API_KEY
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from spotipy.oauth2 import SpotifyOAuth

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
              'orchestral soundtrack', 'dutch house', 'turkish hip hop', 'queens hip hop',
              'christian alternative rock',
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
              'turkish trap', 'thai pop', 'lilith', 'indian instrumental', 'downtempo', 'southern rock',
              'sophisti-pop',
              'punjabi hip hop', 'polish trap', 'socal pop punk', 'candy pop', 'tamil pop', 'rockabilly', 'girl group',
              'uk contemporary r&b', 'atl trap', 'old school thrash', 'classic bollywood', 'compositional ambient',
              'gym phonk', 'north carolina hip hop', 'dark r&b', 'country dawn', 'symphonic rock', 'tennessee hip hop',
              'instrumental lullaby', 'pittsburgh rap', 'thrash metal', 'afropop', 'screamo', 'canadian rock',
              'kindermusik', 'melodic drill', 'nyc rap', 'modern blues rock', 'rock nacional brasileiro', 'philly rap']
# Data Retrieval
pd.read_csv('./genre_attrs.csv')
url = './datapackage.json'
dp = datapackage.Package(url)

# DataFrame Loading
df_genre_attrs = pd.DataFrame(dp.resources[0].read(keyed=True))

xy_NParray = df_genre_attrs.iloc[:, 1:3].to_numpy()
genre_name_list = df_genre_attrs.iloc[:, 0].tolist()
sp_scopes = "playlist-modify-public" + ",playlist-modify-private" + ",user-read-private" + ",user-library-read"
auth = oauth2.SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
)

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=sp_scopes, client_id=SPOTIPY_CLIENT_ID,
                                                    client_secret=SPOTIPY_CLIENT_SECRET,
                                                    redirect_uri=SPOTIPY_REDIRECT_URI))


# spotify = spotipy.Spotify(client_credentials_manager=auth)


def update_annot(ind):
    global sc, ax, fig, annot, track_text
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}".format(" ".join([track_text[n] for n in ind["ind"]]))
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    global sc, ax, fig, annot, track_text
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()


def get_genre(artist, track, spotify_id, artists_id, n):
    genres = []
    try:
        get_url = "http://ws.audioscrobbler.com/2.0/"
        params = {
            'method': 'track.gettoptags',
            'artist': artist,
            'track': track,
            'api_key': LFM_API_KEY,
            'format': 'json'
        }
        response = requests.get(get_url, params=params)
        data = response.json()
        if 'toptags' in data and 'tag' in data['toptags']:
            for tag in data['toptags']['tag']:
                genre = tag['name']
                try:
                    index = genre_name_list.index(genre)
                    x, y = xy_NParray[index]
                    genres.append([genre, x, y])
                    if len(genres) == n and n != 0:
                        return genres
                except ValueError:
                    pass
    except:
        print(response.__dict__)
        print(data)

    # Extracting genre from top tags
    try:
        if len(genres) == 0:
            temp = spotify.artist(artists_id)
            temp_genres = temp['genres']
            for genre in temp_genres:
                try:
                    index = genre_name_list.index(genre)
                    x, y = xy_NParray[index]
                    genres.append([genre, x, y])
                    if len(genres) == n and n != 0:
                        return genres
                except ValueError:
                    pass

        return genres
    except:
        pass

    return -1


def get_playlist_tracks_w_genres(n=2):
    input_flag = True
    while input_flag:
        inp = input("Liked Songs (0) or a different Playlist (1)? \t(0/1): ")
        if inp in ['0', '1']:
            print("\nRetrieving all the tracks...")
            if inp == '0':
                results = spotify.current_user_saved_tracks()
                break
            else:
                input_flag2 = True
                while input_flag2:
                    inp2 = input("Spotify Playlist url\t:")
                    results = spotify.playlist_items(inp2)
                    break
                break

        else:
            print("Type 0 to process the Liked Songs or Type 1 to process a different Playlist.")

    full_tracks = results['items']
    total_tracks = results['total']
    # Loops to ensure I get every track of the playlist
    while results['next']:
        results = spotify.next(results)
        full_tracks.extend(results['items'])
        progress_bar("Track Retrievement in Progress", len(full_tracks), total_tracks)

    print("\nRetrieved " + str(len(full_tracks)) + " tracks.\n")
    tracks = []
    len_playlist = len(full_tracks)
    genre404 = []
    error_list = []
    print("Populating Genre pool...\n")
    for i, track in enumerate(full_tracks):
        name = track["track"]["name"]
        artists_name = track["track"]["artists"][0]["name"]
        spotify_id = track["track"]["id"]
        artists_id = track["track"]["artists"][0]["id"]
        spotify_uri = track["track"]["uri"].split(":")[-1]
        genres = get_genre(artists_name, name, spotify_id, artists_id, n=n)
        if genres == -1:
            error_list.append({"name": name,
                               "artists": artists_name,
                               "spotify_id": spotify_id,
                               "artist_id": artists_id,
                               "spotify_uri": spotify_uri})
            continue
        div = len(genres)

        if div > 1:
            x, y = [sum(x) for x in zip(*genres) if type(x[0]) is not str]
            avg_x, avg_y = round(x / div), round(y / div)
        elif div == 1:
            _, avg_x, avg_y = genres[0]
        else:
            avg_x, avg_y = -1, -1
            genre404.append(i)

        tracks.append({"name": name,
                       "artists": artists_name,
                       "genres": genres,
                       "avgX": avg_x,
                       "avgY": avg_y,
                       "spotify_id": spotify_id,
                       "artist_id": artists_id,
                       "spotify_uri": spotify_uri})
        progress_bar("Genre population in Progress", i, len_playlist)

    if len(error_list) >= 1:
        print("There were some errors in the following tracks: ")
        for item in error_list:
            print("\t", item)
    print("Done")
    return tracks, genre404


def progress_bar(text, current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'{text}: [{arrow}{padding}] {int(fraction * 100)}%', end=ending)


def cluster(tracks, n="auto"):
    data = [(track['avgX'], track['avgY']) for track in tracks]
    track_len = len(tracks)
    n_max = 12 if track_len > 12 else track_len

    if n == "auto":
        K = range(2, n_max)
        fits = []
        score = []

        for k in K:
            # train the model for current value of k on training data
            model = KMeans(n_clusters=k, random_state=0, n_init='auto').fit(data)

            # append the model to fits
            fits.append(model)

            # Append the silhouette score to scores
            score.append(silhouette_score(data, model.labels_, metric='euclidean'))

        i_best = [index for index, item in enumerate(score) if item == min(score)]
        best_model = fits[i_best[0]]
        return best_model
    if n > 1:
        return KMeans(n_clusters=n, random_state=0, n_init='auto').fit(data)
    else:
        raise ValueError


def scatter_plot(tracks, labels, legends):
    print(labels)
    global sc, ax, fig, annot, track_text

    fig, ax = plt.subplots()

    if len(tracks) > 1:
        x_values = []
        y_values = []
        track_text = []

        for i, track in enumerate(tracks):
            x = track['avgX']
            y = track['avgY']
            x_values.append(x)
            y_values.append(y)
            track_text.append(track['name'] + "\n-" + track['artists'] + "\n")

        # cmap = plt.get_cmap('hsv', 4)
        sc = plt.scatter(x_values, y_values, alpha=.4, c=labels)
        plt.legend(handles=sc.legend_elements()[0], labels=set(legends))

        annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"),
                            arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)

        fig.canvas.mpl_connect("motion_notify_event", hover)
        plt.title('a')
        plt.show()


def main():
    playlist_url = "https://open.spotify.com/playlist/3hhVGnGFzoACwZmUOaBwrn?si=eae00e33ae5a4d82"
    playlist_url = "https://open.spotify.com/playlist/4ms43j78XG9BwDA22Y5mkH?si=76850b75468440e8"
    tracks, genre404 = get_playlist_tracks_w_genres(1)
    # print(json.dumps(tracks, indent=4))
    genre404.sort(reverse=True)
    tracks_genre404 = [tracks.pop(i) for i in genre404]
    add_all_flag = False
    input_flag = True
    while input_flag:
        inp = input("\nHow many sub playlists would you like to be generated? \t(Type auto or a number) :")
        inp = inp.lower()
        if inp == "auto":
            break
        inp = int(inp)
        if inp > 1 and inp < len(tracks) - 1:
            break
        print("Auto or a number between 1 and " + str(len(tracks) - 1))
    kmeans_fit = cluster(tracks, inp)
    centroids = [np.array([round(value) for value in center]) for center in kmeans_fit.cluster_centers_]

    new_playlists = [[] for _ in set(kmeans_fit.labels_)]
    for index, i in enumerate(kmeans_fit.labels_):
        new_playlists[i].append(tracks[index])

    centroids_genre = []

    for i in set(kmeans_fit.labels_):
        center = centroids[i]
        group = new_playlists[i]
        np_xy_array = np.array([(track["avgX"], track["avgY"]) for track in group])
        distances = np.sqrt(np.sum((np_xy_array - center) ** 2, axis=1))

        # Find the index of the closest point
        closest_point_index = np.argmin(distances)
        # Closest point
        temp = group[closest_point_index]["genres"]
        while True:
            if type(temp) != list:
                break
            else:
                temp = temp[0]

        centroids_genre.append(temp)

    new_labels = [centroids_genre[i] for i in kmeans_fit.labels_]

    while input_flag:
        inp = input("\nWould you like see the graph?\t:")
        inp = inp.lower()
        if inp in ["y", "yes", "1"]:
            scatter_plot(tracks, kmeans_fit.labels_, new_labels)
            break
        elif inp in ["n", "no", "0"]:
            break
        else:
            print("Yes, Y or No, N")

    menu = True
    print(f"There are {len(new_playlists)} generated playlists.\n")
    #f = open("output.txt", "w", encoding="utf-8")
    f = None
    print(f"There are {len(new_playlists)} generated playlists.\n", file=f)
    for playlist_label, playlist in zip(centroids_genre, new_playlists):
        print(f"----------------------\n{playlist_label}: ", file=f)
        for track in playlist:
            print(f"\t{track["name"]} -{track["artists"]}", file=f)

        if add_all_flag:
            input_flag = False
            add_playlist_to_library(playlist_label, playlist)

        while input_flag:
            inp = input("\nWould you like to add this playlist to your Spotify library?\t:")
            inp = inp.lower()
            if inp in ["y", "yes", "1"]:
                add_playlist_to_library(playlist_label, playlist)
            elif inp in ["n", "no", "0"]:
                break
            else:
                print("Yes, Y or No, N")
    if f is not None:
        f.close()


def add_playlist_to_library(playlist_name, playlist):
    track_uris = [track["spotify_uri"] for track in playlist]
    sublists = [track_uris[i:i + 100] for i in range(0, len(track_uris), 100)]
    my_playlist = spotify.user_playlist_create(user=f"{spotify.current_user()["id"]}", name=f"{playlist_name}",
                                               public=False,
                                               description="Clustered Playlist")
    for sublist in sublists:
        spotify.playlist_add_items(my_playlist['id'], sublist)


# Imports


main()

# ToDo display each playlist and input that adds them to your spotify account.
# Todo make UI
