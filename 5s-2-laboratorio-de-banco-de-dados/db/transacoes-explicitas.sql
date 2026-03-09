-- Inicia
BEGIN;
-- Tenta inserir um valor inválido
INSERT INTO contas (id, saldo) VALUES (1, texto_invalido);
-- Aqui ocorre o erro, o PostgreSQL entra em modo de erro
SELECT * FROM contas; -- Isso resultará em erro até que um Rollback seja executado
ROLLBACK; -- Reverte todas as operações desde o início da transação