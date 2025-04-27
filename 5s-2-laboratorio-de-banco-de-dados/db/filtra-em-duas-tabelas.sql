SELECT alunos.nome, matriculas.id_curso
FROM alunos
INNER JOIN matriculas ON alunos.id_aluno = matriculas.id_aluno;