package com.aplicacao;

public class Programa {
    
        public static void main(String[] args)
        {
            try {
                Connection conexao = DriverManager.getConnection("jdbc:postgresql://localhost:5432/Aulas",
                "postgres", "serafim86");
                
                if (conexao != null) {
                    System.out.println("Banco de dados conectado com sucesso!");
                    Statement stm = conexao.createStatement();
                    
                    // Chama a função consultaDados para buscar os dados
                    consultaDados(stm);
                    stm.close();
                } else {
                    System.out.println("Conexão falhou!");
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        };
    
        public static void consultaDados(Statement stm){
            String query = "SELECT * FROM alunos;";
            try {
                ResultSet result = stm.executeQuery(query);
                while (result.next()) {
                    System.out.println(result.getString("nome"));
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        };
    }
