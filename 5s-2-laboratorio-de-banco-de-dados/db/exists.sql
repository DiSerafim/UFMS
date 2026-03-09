SELECT nome
FROM alunos
WHERE EXISTS (SELECT 1 FROM matriculas WHERE alunos.id_aluno = matriculas.id_aluno);