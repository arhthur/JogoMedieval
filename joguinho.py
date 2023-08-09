import random
import sys

##------BATALHA------##

def batalhar(personagem, guarda):
    print(f"Você está enfrentando o guarda {guarda['nome']} - {guarda['nome']}")
    
    while personagem["vida"] > 0 and guarda["vida"] > 0:
        print("\nEscolha o que você quer fazer:")
        print(f"[1] - Atacar {guarda['nome']}")
        print("[2] - Usar item")
        
        escolha = int(input())
        
        if escolha == 1:
            # Ataque do jogador
            player_attack_damage = random.randint(5, 15)
            guarda["vida"] -= player_attack_damage
            print(f"{personagem['nome']} ataca {guarda['nome']} e causa {player_attack_damage} de dano.")
            
            if guarda["vida"] <= 0:
                print(f"Você derrotou o guarda {guarda['nome']}!")
                personagem["dinheiro"] += 10
            return personagem
        elif escolha == 2:
            personagem = usar_item(personagem)
            
        # Ataque da guarda
        guard_attack_damage = random.randint(8, 12)
        personagem["vida"] -= guard_attack_damage
        print(f"{guarda['nome']} ataca {personagem['nome']} e causa {guard_attack_damage} de dano.")
        
        if personagem["vida"] <= 0:
            print("Você foi derrotado!")
    return personagem

##------ITENS------##

def usar_item(personagem):
    print("Itens disponíveis na sua mochila:")
    for index, item in enumerate(personagem["mochila"], start=1):
        print(f"{index} - {item['Nome']}")

    escolha = int(input("Escolha o número do item que você deseja usar (ou 0 para sair): "))

    if escolha == 0:
        print("Você decidiu não usar nenhum item por enquanto.")
    elif escolha > 0 and escolha <= len(personagem["mochila"]):
        item_usado = personagem["mochila"][escolha - 1]

        if "Cura" in item_usado:
            personagem["vida"] += item_usado["Cura"]
            print(f"Você usou {item_usado['Nome']} e recuperou {item_usado['Cura']} pontos de vida.")
        else:
            print("Esse item não pode ser usado para recuperação de vida.")

        del personagem["mochila"][escolha - 1]
    else:
        print("Escolha inválida. Digite novamente.")

    return personagem

##------LOJA------##

def barganhar(personagem, itens):
    print("Bem-vindo à loja! Aqui estão os itens disponíveis para compra:")
    
    for index, item in enumerate(itens, start=1):
        print(f"{index} - {item['Nome']} - Preço: {item['Preço']}$")
    
    escolha = int(input("Escolha o número do item que você deseja comprar (ou 0 para sair): "))
    
    if escolha == 0:
        print("Você decidiu não comprar nada por enquanto.")
    elif escolha > 0 and escolha <= len(itens):
        item_escolhido = itens[escolha - 1]
        
        if "Preço" in item_escolhido:
            if personagem["dinheiro"] >= item_escolhido["Preço"]:
                personagem["dinheiro"] -= item_escolhido["Preço"]
                print(f"Você comprou {item_escolhido['Nome']} por {item_escolhido['Preço']}$.")
                
                if "Dano" in item_escolhido:
                    print(f"Este item aumenta seu dano em {item_escolhido['Dano']}.")
                elif "Defesa" in item_escolhido:
                    print(f"Este item aumenta sua defesa em {item_escolhido['Defesa']}.")
                elif "Cura" in item_escolhido:
                    print(f"Este item cura {item_escolhido['Cura']} pontos de vida.")
            else:
                print("Você não tem dinheiro suficiente para comprar este item.")
        else:
            print("Este item não está à venda.")
    
    return personagem


##------ESCOLHAS------##

def escolherAcao(personagem, guarda, itens):
    print("Escolha o que você quer fazer?")
    print(f"[1] - Batalha com o guarda {guarda['nome']}")
    print("[2] - Entrar na loja")

    escolha = int(input())
    if escolha == 1:
        personagem = batalhar(personagem, guarda)
        if personagem: 
            return personagem
        else:
            print("Você foi derrotado. Fim de jogo.")
            input("Pressione Enter para sair...")
            sys.exit()
    elif escolha == 2:
        personagem = barganhar(personagem, itens)

    return personagem
personagem = {
    "nome": "Mano Weber",
    "dinheiro": 30,
    "stamina": 50,
    "vida": 100,
    "mochila": [],
    "equipamentos": []
}

guardas = [
    {"nome": "Sir Roderick", "vida": 30, "dano": 10},
    {"nome": "Lady Genevieve", "vida": 40, "dano": 12},
    {"nome": "Barão Oswald", "vida": 50, "dano": 15},
    {"nome": "Dama Elara", "vida": 60, "dano": 18},
    {"nome": "Conde Edric", "vida": 70, "dano": 20},
]

itens = [
    {
        "Nome": "Espada de ferro",
        "Preço": 7,
        "Dano": 25
    },
    {
        "Nome": "Poção de Força",
        "Preço": 10,
        "Dano": 5
    },
    {
        "Nome": "Escudo de ferro",
        "Preço": 15,
        "Defesa": 10
    },
    {
        "Nome": "Armadura de Ferro Completa",
        "Preço": 35,
        "Defesa": 30
    },
    {
        "Nome": "Espada Mágica de Fogo",
        "Preço": 30,
        "Dano": 40
    },
    {
        "Nome": "Poção de vida",
        "Preço": 5,
        "Cura": 25
    },
    {
        "Nome": "Mjolnir martelo de Thor",
        "Preço": 250,
        "Dano": 400
    },
    {
        "Nome": "Bau misterioso",
        "Preço": 20,
        "bau": [
            {
                "premio": 500,
                "probabilidade": 20
            },
            {
                "premio": 250,
                "probabilidade": 40
            },
            {
                "premio": 100,
                "probabilidade": 60
            },
            {
                "premio": 50,
                "probabilidade": 90
            }
        ]
    },
    {
        "Nome": "Bau de Armas",
        "Preço": 15,
        "bau": [
            {
                "premio": "Cajado do trovão",
                "dano": 200,
                "probabilidade": 30
            },
            {
                "premio": "Espada de obsidiana",
                "dano": 100,
                "probabilidade": 50
            },
            {
                "premio": "Escudo com Espinhos",
                "defesa": 50,
                "dano": 10,
                "probabilidade": 80
            }
        ]
    }
]

print("Vizão cria, está na hora de provar que você não é um medíocre. Mate o rei.")
print(f"Durante o jogo você irá precisar enfrentar desafios gigantes, são {len(guardas)} guardas antes de chegar ao Rei, mate todos eles.")
print(f"Durante a tua vida medíocre, você conseguiu acumular {personagem['dinheiro']}$, antes de cada batalha você pode passar na loja.")

guarda_atual = 0
while guarda_atual < len(guardas) and personagem["vida"] > 0:
    guarda = guardas[guarda_atual]
    print(f"Você se aproxima do guarda {guarda['nome']}...")
    personagem = escolherAcao(personagem, guarda, itens)
    if personagem is None:
        print("Você foi derrotado. Fim de jogo.")
        sys.exit()
    elif personagem["vida"] > 0:
        print("Você derrotou o guarda atual! Próximo guarda!")
        guarda_atual += 1
    else:
        print("Você foi derrotado. Fim de jogo.")
        sys.exit()

print("Parabéns! Você derrotou todos os guardas e provou sua coragem. Agora é hora de enfrentar o Rei!")