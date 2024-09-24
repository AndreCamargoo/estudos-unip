'''
    No python não existe constantes, porém por convenção representamos uma constante por todos os caractres em caixa alta
'''

nome = 'André'
carro = 'civic'
velocidade = 111
local_carro = 99

# Representação de constante (são mutáveis)
RADAR_1 = 110 
LOCAL_1 = 100
RADAR_RANGE = 1

# Organizando os if ( muitas condições no mesmo if trás muita complexibilidade na leitura, tente divitar armazenado em pequenos pedaçõs )
velocidade_que_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_que_carro_passou_radar_1

if velocidade_que_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if  carro_multado_radar_1:
        print('Carro multado em radar 1')