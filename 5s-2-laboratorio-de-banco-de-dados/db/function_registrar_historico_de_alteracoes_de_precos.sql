CREATE OR REPLACE FUNCTION registrar_historico_preco()
RETURNs TRIGGER AS $$
BEGIN
	IF NEW.preco <> OLD.preco THEN
		INSERT INTO historico_precos(produto_id, preco_antigo, preco_novo, data_alteracao, usuario)
		VALUES (OLD.id, OLD.preco, NEW.preco, NOW(), current_user);
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_historico_preco
BEFORE UPDATE ON produtos
FOR EACH ROW
EXECUTE FUNCTION registrar_historico_preco();