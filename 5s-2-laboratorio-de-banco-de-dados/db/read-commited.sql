-- Inicia
BEGIN;

-- Primeira leitura de um saldo da conta
SELECT saldo FROM contas WHERE id = 1;

-- Outra transação pode modificar o saldo antes da próxima leitura
-- Segunda leitura
SELECT saldo FROM contas WHERE id = 1;
COMMIT;
-- Saldo lido pode mudar entre a primenira e a segunda leitura,
-- se uma outra transação modificar o saldo entre essas leituras.