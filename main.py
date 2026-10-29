def classificar_mensagem(mensagem):
    mensagem = mensagem.lower()

    if "cancelar" in mensagem:
        return "Cancelamento"

    elif "comprar" in mensagem:
        return "Venda"

    elif "ajuda" in mensagem:
        return "Suporte"

    else:
        return "Não classificado"


mensagens = [
    "Preciso cancelar o pedido",
    "Muito obrigado pelo atendimento",
    "Preciso de ajuda com minha compra",
    "Quero saber o prazo de entrega"
]


for mensagem in mensagens:
    categoria = classificar_mensagem(mensagem)

    print(f"Mensagem: {mensagem}")
    print(f"Categoria: {categoria}")
    print("-" * 30)