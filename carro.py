# Importa as bibliotecas
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Carrega o modelo de inteligência artificial
modelo = YOLO("yolo26n.pt")

# Analisa a imagem
resultados = modelo("imagens/carro.jpg")

# Abre a imagem original
imagem = cv2.imread("carro.jpg")

# Verifica se a imagem foi carregada corretamente
if imagem is None:
    print("Erro: não foi possível encontrar a imagem carro.jpg")
    exit()


# Percorre os objetos detectados
for resultado in resultados:
    for caixa in resultado.boxes:

        # Descobre a classe do objeto
        classe_id = int(caixa.cls[0])
        nome = resultado.names[classe_id]

        # Desenha retângulos somente nos carros
        if nome == "car":

            # Obtém as coordenadas do retângulo
            x1, y1, x2, y2 = map(
                int, caixa.xyxy[0].tolist()
            )

            # Desenha o retângulo verde
            cv2.rectangle(
                imagem,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                3
            )

            # Escreve o nome acima do retângulo
            cv2.putText(
                imagem,
                "Carro",
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0,
                (0, 255, 0),
                2
            )

# Converte a imagem de BGR para RGB
imagem_rgb = cv2.cvtColor(
    imagem,
    cv2.COLOR_BGR2RGB
)

# Mostra a imagem usando Matplotlib
plt.figure(figsize=(12, 8))
plt.imshow(imagem_rgb)
plt.title("Veículos detectados")
plt.axis("off")
plt.show()