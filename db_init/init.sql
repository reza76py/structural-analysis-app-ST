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
    FOREIGN KEY (end_node_id) REFERENCES nodes(id),
    UNIQUE (start_node_id, end_node_id)
);


CREATE TABLE IF NOT EXISTS supports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    node_id INT NOT NULL,
    x_restrained BOOLEAN DEFAULT FALSE,
    y_restrained BOOLEAN DEFAULT FALSE,
    z_restrained BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (node_id) REFERENCES nodes(id),
    UNIQUE (node_id)
);

CREATE TABLE IF NOT EXISTS loads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    node_id INT NOT NULL,
    magnitude FLOAT NOT NULL,
    theta_x FLOAT NOT NULL,  -- degrees from X-axis
    theta_y FLOAT NOT NULL,  -- degrees from Y-axis
    theta_z FLOAT NOT NULL,  -- degrees from Z-axis
    FOREIGN KEY (node_id) REFERENCES nodes(id),
    UNIQUE (node_id)
);

