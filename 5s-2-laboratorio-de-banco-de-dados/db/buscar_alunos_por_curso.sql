CREATE FUNCTION buscar_alunos_por_curso(curso_nome TEXT)
RETURNS SETOF cursos AS $$
BEGIN
	RETURN QUERY SELECT * FROM cursos WHERE nome_curso = curso_nome;
END;
$$ LANGUAGE plpgsql;

-- Chamada:
SELECT * FROM buscar_alunos_por_curso('Engenharia');