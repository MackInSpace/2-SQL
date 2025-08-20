"""SELECT tablename, indexname, indexdef FROM pg_indexes WHERE tablename NOT LIKE 'pg_%';"""

"""SELECT title FROM moma_works WHERE artist = 'Frank Lloyd Wright';"""

"""CREATE INDEX moma_works_btree_index ON moma_works(artist);"""

"""SELECT tablename, indexname, indexdef FROM pg_indexes WHERE tablename NOT LIKE 'pg_%';"""

"""SELECT title FROM moma_works WHERE artist = 'Frank Lloyd Wright';"""

"""DROP INDEX moma_works_btree_index;
CREATE INDEX moma_works_hash_index ON moma_works USING HASH (artist);"""

"""SELECT title FROM moma_works WHERE artist = 'Frank Lloyd Wright';"""

"""DROP INDEX moma_works_hash_index;"""