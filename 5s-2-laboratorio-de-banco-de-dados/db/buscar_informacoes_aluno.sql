CREATE FUNCTION buscar_informacoes_aluno(aluno_id INT)
RETURNS RECORD AS $$
DECLARE
	resultado RECORD;
BEGIN
	-- Seleciona todas as informações do aluno com o ID fornecido
	SELECT nome, curso, nota INTO resultado
	FROM alunos WHERE id = aluno_id;

	-- Retorna o resultado
    RETURN resultado;
END;
$$ LANGUAGE plpgsql;

-- Chamada:
SELECT * FROM buscar_informacoes_aluno(2) AS (nome TEXT, curso TEXT, nota INT); -- "Maria Souza"	"Medicina"	90