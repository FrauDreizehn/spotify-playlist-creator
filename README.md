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

Clone the repository:

    git clone https://github.com/yourusername/spotify-playlist-creator.git
    cd spotify-playlist-creator

Set up your Spotify API credentials in the spotify-playlist-creator.py file (you will need to create an application in the Spotify Dashboard to obtain the credentials).

Run the script:

    python spotify-playlist-creator.py

Example

The scraper will extract genres such as "Rock", "Pop", "Jazz", etc., along with a representative artist for each genre, like "The Beatles" for Rock or "Taylor Swift" for Pop. It will then search for the songs of those artists on Spotify and create a playlist.
