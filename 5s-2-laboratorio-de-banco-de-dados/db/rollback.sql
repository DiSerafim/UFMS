-- Inicia
BEGIN;

-- Subtrai
UPDATE contas
SET saldo = sado -100
WHERE conta_id = 'A';

-- Adiciona
UPDATE contas
SET saldo = saldo + 100
WHERE conta_id = 'B';

-- Verica a transação
COMMIT;