SELECT alunos.nome, matriculas.id_aluno
FROM alunos
LEFT JOIN matriculas ON alunos.id_aluno = matriculas.id_aluno;