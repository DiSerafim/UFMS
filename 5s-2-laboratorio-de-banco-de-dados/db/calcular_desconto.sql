CREATE FUNCTION calcular_desconto(preco NUMERIC, desconto NUMERIC)
RETURNS NUMERIC AS $$
BEGIN
	RETURN preco * (1 - desconto / 100);
END;
$$ LANGUAGE plpgsql;

-- Chamada:
SELECT calcular_desconto(100, 12); -- Retorna 88.00000000000000000000