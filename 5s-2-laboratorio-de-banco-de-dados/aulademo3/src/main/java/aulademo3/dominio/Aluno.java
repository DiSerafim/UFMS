package com.dominio;

import java.io.Serializable;
import javax.persistence.*;
import java.util.Date;

@Entity
public class Aluno implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false) // Define o campo 'nome'
    private String nome;

    @Temporal(TemporalType.DATE)
    @Column(nullable = false) // Define o campo 'dataNascimento'
    private Date dataNascimento;

    @Column(nullable = false, unique = true) // Define o campo 'email'
    private String email;

    // Construtor vazio
    public Aluno() {}

    // Construtor com parâmetros
    public Aluno(String nome, Date dataNascimento, String email) {
        this.nome = nome;
        this.dataNascimento = dataNascimento;
        this.email = email;
    }

    // Getters e Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Date getDataNascimento () {
        return dataNascimento;
    }

    public void setDataNascimento(Date dataNascimento) {
        this.dataNascimento = dataNascimento;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public String toString() {
        return "Aluno{" +
                "id=" + id +
                ", nome= '" + nome + '\'' +
                ", dataNascimento=" + dataNascimento +
                ", email='" + email + '\'' +
            '}';
    }
}
