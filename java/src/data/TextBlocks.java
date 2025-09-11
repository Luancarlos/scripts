public class TextBlocks {
    public static final String[] JS_GARANTIA_BLOCKS = new String[]{
        "// Cadastro de Garantias \nfunction Garantia(id, cliente, produto, prazoMeses) \n{\n" +
        "\tthis.id = id;\n\tthis.cliente = cliente;\n" +
        "\tthis.produto = produto;\n\tthis.prazoMeses = prazoMeses;\n" +
        "\tthis.dataCadastro = new Date();\n\tthis.status = 'Ativa';\n}\n\n",
        "var garantias = [];\n\nfunction cadastrarGarantia(id, cliente, produto, prazoMeses) \n{\n" +
        "\tvar novaGarantia = new Garantia(id, cliente, produto, prazoMeses);\n" +
        "\tgarantias.push(novaGarantia);\n\tconsole.log('Garantia cadastrada:', novaGarantia);\n}\n\n" +
        "function listarGarantias() \n{\n\tconsole.log('Lista de Garantias:');\nfor (var i = 0; i < garantias.length; i++) {\n\tconsole.log(garantias[i]);\n}\n}\n\n",
        "function buscarGarantiaPorCliente(cliente) \n{\n\tvar resultados = [];\nfor (var i = 0; i < garantias.length; i++) {\n" +
        "\tif (garantias[i].cliente === cliente) { resultados.push(garantias[i]); }\n}\nreturn resultados;\n}\n\n" +
        "function atualizarStatusGarantia(id, status) \n{\nfor (var i = 0; i < garantias.length; i++) {\n\tif (garantias[i].id === id) {\n\t\tgarantias[i].status = status;\n\t\tconsole.log('Status atualizado:', garantias[i]);\n\t}\n}\n}\n\n" +
        "function simularOperacoes() \n{\nfor (var i = 0; i < 50; i++) {\n\tcadastrarGarantia(i+100, 'Cliente ' + i, 'Produto ' + i, (i%36)+1);\n" +
        "\tif (i % 2 === 0) atualizarStatusGarantia(i+100, 'Expirada');\n}\n}\n\n" +
        "simularOperacoes();\nlistarGarantias();\n"
    };

    public static final String[] JAVA_GARANTIA_BLOCKS = new String[]{
        "// Classe Garantia \npublic class Garantia \n{\n\tprivate int id;\n\tprivate Cliente cliente;\n\tprivate Produto produto;\n\tprivate int prazoMeses;\n\tprivate String status;\n\tprivate String dataCadastro;\n\n" +
        "\tpublic Garantia(int id, Cliente cliente, Produto produto, int prazoMeses) \n\t{\n\t\tthis.id = id;\n\t\tthis.cliente = cliente;\n\t\tthis.produto = produto;\n\t\tthis.prazoMeses = prazoMeses;\n\t\tthis.status = \"Ativa\";\n\t\tthis.dataCadastro = java.time.LocalDate.now().toString();\n\t}\n\n",
        "\tpublic int getId() { return id; }\n\tpublic Cliente getCliente() { return cliente; }\n\tpublic Produto getProduto() { return produto; }\n\tpublic int getPrazoMeses() { return prazoMeses; }\n\tpublic String getStatus() { return status; }\n\tpublic String getDataCadastro() { return dataCadastro; }\n\n" +
        "\tpublic void atualizarStatus(String novoStatus) { this.status = novoStatus; }\n\n\t@Override\n\tpublic String toString() { return \"...\"; }\n}\n\n",
        "// Outras classes (Cliente, Produto, CadastroGarantias, etc.) ...\n"
    };
}
