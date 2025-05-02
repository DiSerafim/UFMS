CREATE TABLE alunos (
	id_aluno SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	data_nascimento DATE,
	email VARCHAR(100) UNIQUE
);