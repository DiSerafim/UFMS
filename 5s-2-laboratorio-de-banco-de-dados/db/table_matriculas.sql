CREATE TABLE matriculas (
	id_matricula SERIAL PRIMARY KEY,
    id_aluno INT REFERENCES alunos(id_aluno),
    id_curso INT REFERENCES cursos(id_curso),
    semestre VARCHAR(6),
    ano INT
);