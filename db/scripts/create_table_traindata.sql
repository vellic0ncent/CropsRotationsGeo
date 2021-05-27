CREATE TABLE IF NOT EXISTS traindata (
    id serial PRIMARY KEY,
	culture_code VARCHAR ( 50 ) UNIQUE NOT NULL,
	group_code VARCHAR ( 50 ) NOT NULL,
    centroid VARCHAR(100) NOT NULL,
    period BIGINT NOT NULL
);