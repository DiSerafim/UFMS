SELECT nome
FROM alunos
WHERE id_aluno IN (SELECT id_aluno FROM matriculas WHERE id_curso = 2);