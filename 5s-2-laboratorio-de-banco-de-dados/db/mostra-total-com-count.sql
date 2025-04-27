SELECT cursos.nome_curso, COUNT(matriculas.id_aluno) AS total_alunos
FROM cursos
LEFT JOIN matriculas ON cursos.id_curso = matriculas.id_curso
GROUP BY cursos.nome_curso;