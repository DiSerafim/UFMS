CREATE TABLE auditoria (
	id_auditoria SERIAL PRIMARY KEY,
	id_aluno INT,
	data_evento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	evento VARCHAR(50)
);