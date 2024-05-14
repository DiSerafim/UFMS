CREATE TABLE FUNCIONARIO (
    ident           TIPO_ID
    nome            VARCHAR(15),    NOT NULL,
    sobrenome       VARCHAR(15),    NOT NULL,
    endereco        VARCHAR(30),
    dtnasc          DATE,
    salario         DECIMAL(10,2),
    sexo            BOOLEAN,
    supident        TIPO_ID,
    dnumero         TIPO_ID,        NOT NULL,
    PRIMARY KEY(ident)
);