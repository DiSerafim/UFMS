CREATE TABLE alunos (
	id SERIAL PRIMARY KEY,
	nome TEXT NOT NULL,
    curso TEXT NOT NULL,
    nota INTEGER
);
-- Inserindo dados na tabela
INSERT INTO alunos (nome, curso, nota) VALUES
('João Silva', 'Engenharia', 85),
('Maria Souza', 'Medicina', 90),
('Carlos Andrade', 'Engenharia', 75),
('Ana Lima', 'Direito', 88),
('Paulo Mendes', 'Medicina', 92);