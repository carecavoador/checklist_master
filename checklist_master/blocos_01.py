# teste_interface.py

bloco_a = [
    'Código de barras: leitura/distorção',
    'Item conjugado: pé com pé, cabeça com cabeça',
    'Faca: sobreposta e em layer separado'
]

bloco_b = [
    'Trapping, Recuo, Margem de Seguraça',
    'Textos brancos: vazados/estourados'
]

blocos = [bloco_a, bloco_b]

for bloco in blocos:
    for item in bloco:
        print(f'Bloco {blocos.index(bloco)}, item {item}')
