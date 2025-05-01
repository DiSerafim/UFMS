CREATE FUNCTION listar_notas_curso(curso_nome TEXT)
RETURNS INTEGER[] AS $$
DECLARE
	notas INTEGER[];
BEGIN
	-- Seleciona todas as notas dos alunos do curso e armazena no array
	SELECT array_agg(nota) INTO notas
	FROM alunos WHERE curso = curso_nome;

	-- Retorna o array de notas
    RETURN notas;
END;
$$ LANGUAGE plpgsql;

-- Chamada:
SELECT listar_notas_curso('Medicina'); -- {90,92}