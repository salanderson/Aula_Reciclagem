# CONSTANTE = "Variaveis" que nao vao mudar
# muitas condiçoes no mesmo if (ruim)
# <- Contagem de complexidade (ruim)

# Aula 50 - 52

velocidade = 100 # velocidade atual do carro 
local_carro = 101 # Local em que o carro esta na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # A distancia onde o radar pega

multado_radar_1 = velocidade > RADAR_1
local_veiculo = local_carro >= LOCAL_1 + RADAR_RANGE and LOCAL_1 - RADAR_RANGE

if multado_radar_1 and local_veiculo:
    print(f'Seu carro foi multado no Radar_1 em uma velocidade de: {velocidade} KM/H')

if local_veiculo:
    print('carro passou pelo radar1')