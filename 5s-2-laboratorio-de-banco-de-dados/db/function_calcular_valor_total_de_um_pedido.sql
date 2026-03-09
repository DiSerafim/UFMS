CREATE OR REPLACE FUNCTION calcular_total_pedido(pedido_id integer)
RETURNS numeric AS $$
DECLARE
    total numeric;
BEGIN
    SELECT SUM(quantidade * preco_unitario) * (1 - COALESCE(desconto, 0))
    INTO total
    FROM itens_pedido
    JOIN produtos ON itens_pedido.produto_id = produtos.id
    WHERE itens_pedido.pedido_id = calcular_total_pedido.pedido_id;
    
    RETURN total;
END;
$$ LANGUAGE plpgsql;