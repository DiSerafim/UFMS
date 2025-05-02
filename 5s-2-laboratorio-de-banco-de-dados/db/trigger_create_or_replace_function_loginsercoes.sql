CREATE OR REPLACE FUNCTION log_insercoes ()
RETURNS TRIGGER AS $$
BEGIN
	INSERT INTO auditoria (id_aluno, evento)
	VALUES (NEW.id_aluno, 'INSERT');
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;