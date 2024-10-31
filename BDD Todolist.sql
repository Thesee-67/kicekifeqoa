DROP DATABASE IF EXISTS Todolist;
CREATE DATABASE Todolist;
USE Todolist;

CREATE TABLE Users (
    id_user INT PRIMARY KEY auto_increment,
    email varchar(50) not null,
    `password` char(60) not null
);

CREATE TABLE Task (
    id_task INT PRIMARY KEY auto_increment,
    `name` varchar(50) not null,
    end_date datetime,
    checked boolean,
    priority int,
    tag varchar(50)
);

CREATE TABLE Subtask (
    id_subtask INT PRIMARY KEY auto_increment,
    id_affected_task INT,
    `name` varchar(50),
    end_date datetime,
    checked boolean,
    CONSTRAINT fk_affeted_task
		FOREIGN KEY (id_affected_task) REFERENCES Task (id_task) ON DELETE CASCADE
);

CREATE TABLE `Group` (
    id_group INT PRIMARY KEY auto_increment,
    `name` varchar(50) not null
);

CREATE TABLE Group_has_Users (
    user_id INT,
    group_id INT,
    PRIMARY KEY (user_id, group_id),
		FOREIGN KEY (user_id) REFERENCES Users (id_user) ON DELETE CASCADE,
		FOREIGN KEY (group_id) REFERENCES `Group`(id_group) ON DELETE CASCADE
);

CREATE TABLE Task_has_Group (
    task_id INT,
    group_id INT,
    PRIMARY KEY (task_id, group_id),
		FOREIGN KEY (task_id) REFERENCES Task (id_task) ON DELETE CASCADE,
		FOREIGN KEY (group_id) REFERENCES `Group`(id_group) ON DELETE CASCADE
);

CREATE TABLE Task_has_Users (
    task_id INT,
    user_id INT,
    PRIMARY KEY (task_id, user_id),
		FOREIGN KEY (task_id) REFERENCES Task (id_task) ON DELETE CASCADE,
		FOREIGN KEY (user_id) REFERENCES Users (id_user) ON DELETE CASCADE
);

CREATE TABLE Subtask_has_Users (
    subtask_id INT,
    user_id INT,
    PRIMARY KEY (subtask_id, user_id),
    FOREIGN KEY (subtask_id) REFERENCES Subtask (id_subtask) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users (id_user) ON DELETE CASCADE
);


