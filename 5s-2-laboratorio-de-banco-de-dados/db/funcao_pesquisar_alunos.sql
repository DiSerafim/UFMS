# PostgreSql:

# CREATE PROCEDURE buscar_alunos_curso(curso_nome TEXT)
# BEGIN
#	RETURN QUERY SELECT * FROM cursos WHERE nome_curso = curso_nome;
# END;
# $$ LANGUAGE plpgsql;

# MysSQL

DELIMITER $$

CREATE PROCEDURE buscar_alunos_curso(curso_nome VARCHAR(255))
BEGIN
    SELECT * FROM cursos WHERE nome_curso = curso_nome;
END $$

DELIMITER ;


SELECT * FROM buscar_alunos_curso('Sistemas de Informação');