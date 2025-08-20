"""SELECT tablename, indexname, indexdef FROM pg_indexes WHERE tablename NOT LIKE 'pg_%';"""

"""SELECT title FROM moma_works WHERE artist = 'Frank Lloyd Wright';"""

"""CREATE INDEX moma_works_btree_index ON moma_works(artist);"""

"""SELECT tablename, indexname, indexdef FROM pg_indexes WHERE tablename NOT LIKE 'pg_%';"""

"""SELECT title FROM moma_works WHERE artist = 'Frank Lloyd Wright';"""

"""DROP INDEX moma_works_btree_index;
CREATE INDEX moma_works_hash_index ON moma_works USING HASH (artist);"""

"""SELECT title FROM moma_works WHERE artist = 'Frank Lloyd Wright';"""

"""DROP INDEX moma_works_hash_index;"""

"""EXPLAIN SELECT date_acquired FROM moma_works 
WHERE date_acquired BETWEEN '1950-01-01' AND '1959-12-31';"""

"""EXPLAIN ANALYZE SELECT date_acquired FROM moma_works
WHERE date_acquired BETWEEN '1950-01-01' AND '1959-12-31';"""

"""CREATE INDEX date_acq_idx ON moma_works(date_acquired);"""

"""EXPLAIN ANALYZE SELECT date_acquired FROM moma_works 
WHERE date_acquired BETWEEN '1950-01-01' AND '1959-12-31';"""