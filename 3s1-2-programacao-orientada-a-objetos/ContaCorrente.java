// ✅ Abra seu ambiente de desenvolvimento (IDE) preferido;
// ✅ Crie um novo projeto;
// ✅ Crie uma Classe chamada ContaCorrente que possua:
// ✅ Uma variável de ponto flutuante juros que indique a porcentagem do rendimento da conta. Defina o valor inicial em 0,01;
// ✅ Uma variável de ponto flutuante que indique o saldo;
// ✅ Um método depósito;
// ✅ Uma variável chamada limiteChequeEspecial em ponto flutuante, iniciada com o valor -200;
// ✅ Um método saque, que verifica se o saque pode ser realizado de acordo com o saldo atual e o limiteChequeEspecial. Caso não tenha mais limite, escrever no console "Limite insuficiente!";
// ✅ Um método rendimento que usa o valor do juros para fazer o saldo crescer caso o saldo não seja negativo;
// ✅ Um método para exibir o saldo;
// ✅ Uma variável de texto para o primeiro nome do cliente;
// ✅ Uma variável de texto para o sobrenome do cliente;
// ✅ Método getNome que retorne o nome do cliente completo;
// ✅ Uma variável para o número da conta corrente (do tipo primitivo long);
// ✅ Método getNumero que dê como resultado o número da conta do cliente;
// ✅ Método main, com uma instância da classe ContaCorrente e faça um depósito de R$100, um saque de R$125, execute a função rendimento e imprimir o saldo;
// ✅ Use o modificador de acesso “public” para todos os métodos e nenhum modificador (“package private”) para os atributos da classe.

public class ContaCorrente {
    // Variável de ponto flutuante juros que indique a porcentagem do rendimento da conta. Defina o valor inicial em 0,01;
    public float juros = 0.01f; // https://stackoverflow.com/questions/14513597/cannot-convert-from-double-to-float
    // Variável de ponto flutuante que indique o saldo;
    public float saldo = 0;
    // Variável chamada limiteChequeEspecial em ponto flutuante, iniciada com o valor -200;
    public float limiteChequeEspecial = -200;
    // Variável de texto para o primeiro nome do cliente;
    public String primeiroNomeCliente;
    // Variável de texto para o sobrenome do cliente;
    public String sobrenomeCliente;
    // Variável para o número da conta corrente (do tipo primitivo long);
    private long numeroConta;

    // Método depósito;
    public void deposito(float valor) {
        saldo += valor;
        System.out.println("Depósito de R$ " + valor + " realizado com sucesso.");
    }

    // Método saque, que verifica se o saque pode ser realizado de acordo com o saldo atual e o limiteChequeEspecial.
    public void saque(float valor) {
        if (saldo - valor >= limiteChequeEspecial) {
            saldo -= valor;
            System.out.println("Saque de R$ " + valor + " realizado com sucesso.");
        } else {
            System.out.println("Limite insuficiente!");
        }
    }

    // Método rendimento que usa o valor do juros para fazer o saldo crescer caso o saldo não seja negativo;
    public void rendimento() {
        if (saldo > 0) {
            saldo *= (1 + juros);
            System.out.println("Rendimento aplicado. Saldo atual: R$ " + saldo);
        }
    }

    // Método para exibir o saldo;
    public void exibirSaldo() {
        System.out.println("Seu saldo é de: R$ " + saldo);
    }

    // Método getNome que retorne o nome do cliente completo;
    public String getNome() {
        return primeiroNomeCliente + " " + sobrenomeCliente;
    }

    // Método getNumero que dê como resultado o número da conta do cliente;
    public long getNumero() {
        return numeroConta;
    }

    // Método main, com uma instância da classe ContaCorrente e faça um depósito de R$100, um saque de R$125, execute a função rendimento e imprimir o saldo;
    public static void main(String[] args) {
        ContaCorrente conta = new ContaCorrente();
        conta.deposito(100);
        conta.saque(125);
        conta.rendimento();
        conta.exibirSaldo();
    }
}
