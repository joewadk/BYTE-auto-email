DROP TABLE IF EXISTS cabinet;

CREATE TABLE cabinet(
    uid UUID REFERENCES people (uid) ON DELETE CASCADE
)