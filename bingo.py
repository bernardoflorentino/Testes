import random

aleatorio_nome_musicas = [ 'Thriller', 'Entre tapas e Beijos', 'Vira Vira',
    'Firework', 'Shape of U', 'Blank Space', 'Lança perfume', 'Nav', 'Metamorfose',
    'Camarão', 'Resenha', ' Na ponta do Pé', 'Sete Mares', 'Dynamite', 'Whatis Love',
    'Mama Mia', 'Espresso', 'brunos mars', 'Menina má', 'Bang', 'Could you be', 'Vagalumes', 'Anna julia',
    'Evidencias', 'Ela vai voltar', 'Evidencias', 'Vou deixar', 'Camisa 10', 'Eu te devoro',
    'Manchete dos jornais', 'Bad romance', 'Toxic', 'Wannabe',
    'Quero te encontrar', 'Girlfriend', 'Hard Times', 'Crazy in Love', 'Summertime saddness',
    'Dont stop me now', 'Here comes the sun', 'Diamonds', 'In da club', 'Tupac', 'Sorry', 'xota da smeninas',
    'Call me maybe', 'Side to side', 'bids of a feather', 'sunflower', 'happy', 'pump it', 'i gotta felling'
]
i=0

while i < 18:
    musicas = random.sample(aleatorio_nome_musicas, 12)
    for musicas_escolhidas in musicas:
        print(f"{musicas_escolhidas}")
    i += 1
    print("="*60)