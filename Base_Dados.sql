--setup.sql

CREATE DATABASE IF NOT EXISTS biblioteca;
USE biblioteca;

CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    autor VARCHAR(255),
    ano INT,
    genero VARCHAR(255)
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    senha VARCHAR(255)
);

CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_livro INT,
    data_emprestimo DATE,
    data_devolucao DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_livro) REFERENCES livros(id)
);
