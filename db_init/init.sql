USE space_truss_db_st;

CREATE TABLE IF NOT EXISTS nodes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    x FLOAT NOT NULL,
    y FLOAT NOT NULL,
    z FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS elements (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Crucial for unique elements
    start_node INT NOT NULL,
    end_node INT NOT NULL,
    FOREIGN KEY (start_node) REFERENCES nodes(id),
    FOREIGN KEY (end_node) REFERENCES nodes(id),
    UNIQUE (start_node, end_node)  -- Prevent duplicate elements
);