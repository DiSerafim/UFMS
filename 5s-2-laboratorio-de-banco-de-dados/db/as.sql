SELECT alunos.nome AS aluno, cursos.nome_curso AS curso
FROM alunos
INNER JOIN matriculas ON alunos.id_aluno = matriculas.id_aluno
INNER JOIN cursos ON matriculas.id_curso = cursos.id_curso;