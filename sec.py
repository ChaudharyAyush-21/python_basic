# Define a list to store songs
playlist = []

# Function to add a song to the playlist
def add_song(title, artist):
    song = {'title': title, 'artist': artist}
    playlist.append(song)
    print(f'Added "{title}" by {artist} to the playlist.')

# Function to display the current playlist
def show_playlist():
    if not playlist:
        print('Playlist is empty.')
    else:
        print('Current Playlist:')
        for index, song in enumerate(playlist, start=1):
            print(f'{index}. {song["title"]} - {song["artist"]}')

# Example usage:
add_song('Shape of You', 'Ed Sheeran')
add_song('Someone Like You', 'Adele')
add_song('Billie Jean', 'Michael Jackson')

show_playlist()

        
