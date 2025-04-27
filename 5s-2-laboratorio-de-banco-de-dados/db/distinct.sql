SELECT DISTINCT cursos.nome_curso
FROM cursos
INNER JOIN matriculas ON cursos.id_curso = matriculas.id_curso;