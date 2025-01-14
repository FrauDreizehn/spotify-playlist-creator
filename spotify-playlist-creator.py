import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
import re

def setup_spotify():
    # Set up authentication with Spotify
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=scope,
        client_id="6e1fcb4ab47648448fc1c72c0d4bec23",
        client_secret="ce5cf22508d2488cb17df34209b3978d",
        redirect_uri="http://localhost:8888/callback"
    ))
    return sp

def scrape_everynoise():
    # Previous scraping code remains the same
    url = "https://everynoise.com/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: Status code {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    genre_divs = soup.find_all('div', class_='genre')
    genres_data = []
    pattern = r'e\.g\. (.*?) "(.+?)"'
    
    for div in genre_divs:
        genre = div.text.strip().replace('»', '').strip()
        title = div.get('title', '')
        match = re.search(pattern, title)
        if match:
            artist = match.group(1)
            song = match.group(2)
            genres_data.append({
                'genre': genre,
                'artist': artist,
                'song': song
            })
    
    return genres_data

def create_spotify_playlist(sp, genres_data):
    # Create a new playlist
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(
        user_id, 
        "Every Noise Genres Example Songs", 
        description="A playlist containing example songs from different genres on Every Noise"
    )
    
    # List to store tracks we couldn't find
    not_found = []
    found_tracks = []
    
    # Search for each song and add it to the playlist
    for item in genres_data:
        # Search for the specific song by the artist
        query = f"track:{item['song']} artist:{item['artist']}"
        results = sp.search(q=query, type='track', limit=1)
        
        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            found_tracks.append(track_uri)
            print(f"Found: {item['artist']} - {item['song']} ({item['genre']})")
        else:
            not_found.append(f"{item['artist']} - {item['song']} ({item['genre']})")
            print(f"Could not find: {item['artist']} - {item['song']}")
        
        # Add tracks in batches of 100 (Spotify API limit)
        if len(found_tracks) >= 100:
            sp.playlist_add_items(playlist['id'], found_tracks)
            found_tracks = []
    
    # Add any remaining tracks
    if found_tracks:
        sp.playlist_add_items(playlist['id'], found_tracks)
    
    # Print summary
    print("\nPlaylist creation complete!")
    print(f"Playlist URL: {playlist['external_urls']['spotify']}")
    if not_found:
        print("\nSongs that couldn't be found:")
        for song in not_found:
            print(song)

def main():
    # Set up Spotify client
    try:
        sp = setup_spotify()
    except Exception as e:
        print(f"Failed to authenticate with Spotify: {e}")
        return
    
    # Scrape Every Noise
    print("Scraping Every Noise...")
    genres_data = scrape_everynoise()
    
    if genres_data:
        print(f"\nFound {len(genres_data)} songs to add to playlist")
        # Create playlist and add songs
        create_spotify_playlist(sp, genres_data)

if __name__ == "__main__":
    main()
