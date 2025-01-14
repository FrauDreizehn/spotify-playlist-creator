# spotify-playlist-creator

Description

The spotify-playlist-creator script is a Python script that extracts music genres and their representative artists from the website www.everynoise.com. It then searches for the songs of those artists on Spotify and creates a playlist. This tool is useful for music enthusiasts, researchers, and developers who want to explore the diversity of music genres and their associated songs.

Features

Genre Extraction: Scrapes all music genres listed on EveryNoise.
Artist Representation: Retrieves a representative artist for each genre.
Spotify Search: Searches for the songs of the artists on Spotify.
Playlist Creation: Generates a playlist with the found songs.
Error Handling: Includes basic error handling for network requests and data parsing.

Requirements

Python 3.x
requests for making HTTP requests
BeautifulSoup for parsing HTML
spotipy for interacting with the Spotify API
pandas for data manipulation (optional, for CSV export)

You can install the required libraries using pip:

    pip install requests beautifulsoup4 spotipy pandas

Usage

Set up a Spotify Developer account:

Go to https://developer.spotify.com/dashboard
Create a new application
Get your Client ID and Client Secret
Add http://localhost:8888/callback to your app's Redirect URIs in the settings


Replace these values in the script:

YOUR_CLIENT_ID with your actual Spotify Client ID
YOUR_CLIENT_SECRET with your actual Spotify Client Secret



When you run the script, it will:

Authenticate with Spotify (opens a browser window for login)
Scrape Every Noise
Create a new public playlist on your account
Search for each song and add it to the playlist
Show you which songs were found and added
Provide the URL of the created playlist

The script handles Spotify's API limits and provides feedback about which songs it couldn't find (since some songs from Every Noise might not be available on Spotify or might have slightly different names).

Clone the repository:

    git clone https://github.com/yourusername/spotify-playlist-creator.git
    cd spotify-playlist-creator

Set up your Spotify API credentials in the spotify-playlist-creator.py file (you will need to create an application in the Spotify Dashboard to obtain the credentials).

Run the script:

    python spotify-playlist-creator.py

Example

The scraper will extract genres such as "Rock", "Pop", "Jazz", etc., along with a representative artist for each genre, like "The Beatles" for Rock or "Taylor Swift" for Pop. It will then search for the songs of those artists on Spotify and create a playlist.
