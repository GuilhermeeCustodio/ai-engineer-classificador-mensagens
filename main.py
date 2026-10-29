def classificar_mensagem(mensagem):
    mensagem = mensagem.lower()

    if "cancelar" in mensagem:
        return "Cancelamento"

    elif "ajuda" in mensagem:
        return "Suporte"

    elif "compra" in mensagem:
        return "Venda"

    elif "obrigado" in mensagem:
        return "Elogio"

    else:
        return "Não classificado"


mensagens = [
    "Preciso cancelar o pedido",
    "Quero comprar um produto",
    "Muito obrigado pelo atendimento",
    "Preciso de ajuda com minha compra",
    "Quero saber o prazo de entrega",
    "Gostaria de realizar uma compra"
]


for mensagem in mensagens:
    categoria = classificar_mensagem(mensagem)

    print(f"Mensagem: {mensagem}")
    print(f"Categoria: {categoria}")
    print("-" * 30)