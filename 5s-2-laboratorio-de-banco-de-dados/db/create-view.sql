CREATE VIEW view_alunos_maiores AS
SELECT nome, idade
FROM alunos
WHERE idade >= 18;