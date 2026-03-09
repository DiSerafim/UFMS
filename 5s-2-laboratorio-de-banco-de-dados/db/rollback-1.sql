DO $$
BEGIN
	-- Inicia
	BEGIN;
	
	-- Faz a operação
	UPDATE contas SET saldo = sado - 100 WHERE conta_id = 'A';

	-- Se tudo ocorrer bem
	COMMIT;

EXCEPTION
	-- Caso dê erro, realiza o Rollback
	WHEN OTHERS THEN
		ROLLBACK;
		RAISE NOTICE 'Transação revertida devido a erros.';
END;
$$