CREATE PROCEDURE adicionar_aluno(nome TEXT, curso TEXT)
LANGUAGE plpgsql AS $$
BEGIN
	INSERT INTO alunos(nome, curso) VALUES (nome, curso);
END;
$$;

-- Chamada:
CALL adicionar_aluno('João', 'Física'); -- Query returned successfully