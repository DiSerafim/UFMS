SELECT alunos.nome, cursos.nome_curso
FROM alunos
INNER JOIN matriculas ON alunos.id_aluno = matriculas.id_aluno
INNER JOIN cursos ON matriculas.id_curso = cursos.id_curso;