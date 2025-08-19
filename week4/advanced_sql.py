"""SELECT * FROM moma_works WHERE classification = 'Photograph';"""

"""SELECT height, width FROM moma_works
WHERE classification = 'Photograph' AND height > 0 AND width > 0;"""

"""SELECT
CEIL(width) + 2 AS frame_width,
CEIL(height) + 4 AS frame_height
FROM moma_works
WHERE classification = 'Photograph' AND width > 0 AND height > 0;"""

"""WITH frames AS (
    SELECT
    CEIL(width) + 2 AS frame_width,
    CEIL(height) + 4 AS frame_height
    FROM moma_works
    WHERE classification = 'Photograph' AND width > 0 AND height > 0
)
SELECT
frame_width,
frame_height,
frame_width * frame_height AS frame_area
FROM frames;"""

"""WITH frames AS (
    SELECT
    CEIL(width) + 2 AS frame_width,
    CEIL(height) + 4 AS frame_height
    FROM moma_works
    WHERE classification = 'Photograph' AND width > 0 AND height > 0
)
SELECT
COUNT(*),
frame_width,
frame_height,
frame_width * frame_height AS frame_area
FROM frames
GROUP BY frame_width, frame_height, frame_area;"""

"""SELECT * FROM moma_artists LIMIT 50;"""

"""SELECT jsonb_pretty(info) AS formatted_info
FROM moma_artists LIMIT 50;"""

"""SELECT 
info -> 'display_name' AS name,
info -> 'nationality' as nationality
FROM moma_artists
ORDER BY id
LIMIT 50;"""

"""SELECT 
info -> 'display_name' AS name,
info -> 'nationality' as nationality
FROM moma_artists
WHERE info ->> 'nationality' = 'American'
ORDER BY id
LIMIT 50;"""

"""INSERT INTO moma_artists (info) VALUES (
    json_object('{display_name, Ablade Glover, nationality, Ghanaian}')
);"""

"""SELECT info FROM moma_artists ORDER BY id DESC LIMIT 1;"""