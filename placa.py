
import easyocr
import cv2
import matplotlib.pyplot as plt
from utils import ValidadorPlaca, CorretorPlaca

validador = ValidadorPlaca()
corretor = CorretorPlaca()

leitor = easyocr.Reader(['en'])

imagem = cv2.imread('imagens/placa2.jpg')

if imagem is None:
    print("Não foi possível abrir a imagem.")
    exit()

resultados = leitor.readtext(imagem)

for caixa, texto, confianca in resultados:
    texto_corrigido = corretor.corrigir(texto)

    if validador.validar(texto_corrigido):
        print("Texto:", texto_corrigido, len(texto_corrigido))
        print("Confiança:", round(confianca, 2))
    
        pontos = caixa
        inicio = tuple(map(int, pontos[0]))
        fim = tuple(map(int, pontos[2]))
    
        cv2.rectangle(imagem, inicio, fim, (0, 255, 0), 2)
    
        cv2.putText(
            imagem,
            texto_corrigido,
            (inicio[0], max(inicio[1] - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

# Converte as cores de BGR para RGB
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Exibe a imagem usando Matplotlib
plt.imshow(imagem_rgb)
plt.title("Reconhecimento de placa")
plt.axis("off")
plt.show()
