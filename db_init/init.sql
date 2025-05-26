CREATE DATABASE IF NOT EXISTS space_truss_db_st;
USE space_truss_db_st;

CREATE TABLE IF NOT EXISTS nodes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    x FLOAT NOT NULL,
    y FLOAT NOT NULL,
    z FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS elements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    start_node_id INT NOT NULL,
    end_node_id INT NOT NULL,
    FOREIGN KEY (start_node_id) REFERENCES nodes(id),
    FOREIGN KEY (end_node_id) REFERENCES nodes(id)
);