-- Users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Profiles table (1-to-1 with users)
CREATE TABLE profiles (
    profile_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    display_name VARCHAR(100),
    avatar_url TEXT
);

-- Artists table
CREATE TABLE artists (
    artist_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    genre VARCHAR(50)
);

-- Albums table (1-to-many with artists)
CREATE TABLE albums (
    album_id SERIAL PRIMARY KEY,
    artist_id INTEGER NOT NULL REFERENCES artists(artist_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    release_date DATE
);

-- Tracks table (1-to-many with albums)
CREATE TABLE tracks (
    track_id SERIAL PRIMARY KEY,
    album_id INTEGER NOT NULL REFERENCES albums(album_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    duration INTEGER CHECK (duration > 0),
    play_count INTEGER DEFAULT 0
);

-- Playlists table (1-to-many with users)
CREATE TABLE playlists (
    playlist_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Playlist_Tracks table (many-to-many between playlists and tracks)
CREATE TABLE playlist_tracks (
    playlist_id INTEGER NOT NULL REFERENCES playlists(playlist_id) ON DELETE CASCADE,
    track_id INTEGER NOT NULL REFERENCES tracks(track_id) ON DELETE CASCADE,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (playlist_id, track_id)
);