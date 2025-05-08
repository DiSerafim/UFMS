-- Inicia
BEGIN;

-- Operação 1: Inserir um novo aluno
INSERT INTO alunos (nome, curso) VALUES ('João', 'Engenheiro');

-- Define um Savepoint chamado ponto_a
SAVEPOINT ponto_a;

-- Operação 2: Inserir um segundo aluno
INSERT INTO alunos (nome, curso) VALUES ('Maria', 'Arquitetura');

-- Define um outro Savepoint chamado ponto_b
SAVEPOINT ponto_b;

-- Operação 3: Inserir um terceiro aluno (causará um erro)
INSERT INTO alunos (nome, curso) VALUES ('Pedro', NULL); -- Falha (curso não pode ser NULL)

-- Reverter até o ponto_b (o erro será ignorado, e as operações anteriores serão mantidas)
ROLLBACK TO ponto_b;

-- Continuação: Inserir um novo aluno após o Rollback parcial
INSERT INTO alunos (nome, curso) VALUES ('Ana', 'Design');

-- Finaliza a transação com sucesso
COMMIT;