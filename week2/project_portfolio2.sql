-- Drop tables if they exist (for reusability)
DROP TABLE IF EXISTS playlist_tracks;
DROP TABLE IF EXISTS playlists;
DROP TABLE IF EXISTS tracks;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS profiles;
DROP TABLE IF EXISTS users;

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

-- Sample data: Users
INSERT INTO users (username, email) VALUES
('adam_music', 'adam@example.com'),
('jane_doe', 'jane@example.com');

-- Sample data: Profiles
INSERT INTO profiles (user_id, display_name, avatar_url) VALUES
(1, 'Adam M.', 'https://example.com/avatars/adam.jpg'),
(2, 'Jane D.', 'https://example.com/avatars/jane.jpg');

-- Sample data: Artists
INSERT INTO artists (name, genre) VALUES
('Radiohead', 'Alternative'),
('Kendrick Lamar', 'Hip-Hop');

-- Sample data: Albums
INSERT INTO albums (artist_id, title, release_date) VALUES
(1, 'OK Computer', '1997-05-21'),
(2, 'DAMN.', '2017-04-14');

-- Sample data: Tracks
INSERT INTO tracks (album_id, title, duration, play_count) VALUES
(1, 'Paranoid Android', 387, 1200),
(1, 'Karma Police', 260, 950),
(2, 'DNA.', 185, 2000),
(2, 'HUMBLE.', 177, 2500);

-- Sample data: Playlists
INSERT INTO playlists (user_id, title, description) VALUES
(1, 'Chill Vibes', 'Alternative tracks for winding down'),
(2, 'Workout Boost', 'High-energy hip-hop for the gym');

-- Sample data: Playlist_Tracks
INSERT INTO playlist_tracks (playlist_id, track_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4);