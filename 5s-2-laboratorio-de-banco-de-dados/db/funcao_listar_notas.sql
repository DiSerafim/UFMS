# PostgreSQL:
# CREATE FUNCTION listar_notas_curso(curso_nome TEXT)
# RETURNS INTEGER[] AS $$
# DECLARE
# 	notas INTEGER[];
# BEGIN
# 	SELECT array_agg(nota) INTO notas
# 	FROM alunos WHERE curso = curso_nome;
#     RETURN notas;
# END;
# 
# $$ LANGUAGE plpgsql;

# Workbench:
DELIMITER $$

CREATE FUNCTION listar_notas_curso(curso_nome VARCHAR(255))
RETURNS TEXT
DETERMINISTIC
BEGIN
	DECLARE notas TEXT;
    
    SELECT GROUP_CONCAT(nota SEPARATOR ', ') INTO notas
    FROM alunos
    WHERE curso = curso_nome;
    
    RETURN notas;
    
END $$

DELIMITER $$