def classificar_mensagem(mensagem):
    mensagem = mensagem.lower()

    if "problema" in mensagem:
        return "Reclamação"

    elif "obrigado" in mensagem:
        return "Elogio"

    elif "ajuda" in mensagem:
        return "Suporte"

    else:
        return "Não classificado"


mensagens = [
    "Estou com um problema no pedido",
    "Muito obrigado pelo atendimento",
    "Preciso de ajuda com minha compra",
    "Quero saber o prazo de entrega"
]


for mensagem in mensagens:
    categoria = classificar_mensagem(mensagem)

    print(f"Mensagem: {mensagem}")
    print(f"Categoria: {categoria}")
    print("-" * 30)