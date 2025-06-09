USE space_truss_db_st;

-- 🔐 Projects table linked to each user
CREATE TABLE IF NOT EXISTS projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 📌 Nodes linked to projects
CREATE TABLE IF NOT EXISTS nodes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    x FLOAT NOT NULL,
    y FLOAT NOT NULL,
    z FLOAT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

-- 📌 Elements linked to projects
CREATE TABLE IF NOT EXISTS elements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    start_node_id INT NOT NULL,
    end_node_id INT NOT NULL,
    FOREIGN KEY (start_node_id) REFERENCES nodes(id),
    FOREIGN KEY (end_node_id) REFERENCES nodes(id),
    FOREIGN KEY (project_id) REFERENCES projects(id),
    UNIQUE (start_node_id, end_node_id, project_id)
);

-- 📌 Supports linked to projects
CREATE TABLE IF NOT EXISTS supports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    node_id INT NOT NULL,
    x_restrained BOOLEAN DEFAULT FALSE,
    y_restrained BOOLEAN DEFAULT FALSE,
    z_restrained BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (node_id) REFERENCES nodes(id),
    FOREIGN KEY (project_id) REFERENCES projects(id),
    UNIQUE (node_id, project_id)
);

-- 📌 Loads linked to projects
CREATE TABLE IF NOT EXISTS loads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    node_id INT NOT NULL,
    magnitude FLOAT NOT NULL,
    theta_x FLOAT NOT NULL,  -- degrees from X-axis
    theta_y FLOAT NOT NULL,  -- degrees from Y-axis
    theta_z FLOAT NOT NULL,  -- degrees from Z-axis
    FOREIGN KEY (node_id) REFERENCES nodes(id),
    FOREIGN KEY (project_id) REFERENCES projects(id),
    UNIQUE (node_id, project_id)
);
