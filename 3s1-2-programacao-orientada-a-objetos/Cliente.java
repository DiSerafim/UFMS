import java.io.Serializable;

public class Cliente implements Serializable{
    private String cpf;
    private String nome;

    public Cliente (String cpf, String nome) {
        this.cpf = cpf;
        this.nome = nome;
    }

    public String toString(){
        return " cpf: "+cpf+" nome: "+nome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getNome() {
        return nome;
    }

    public void setNome (String nome) {
        this.nome = nome;
    }
}    