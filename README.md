# Exercícios de Lógica e Algoritmos
 # Exercício 1
 ## Calculadora de Desconto de Produtos

Este script em Python calcula o valor total de um produto com base em sua quantidade e aplica um desconto dependendo do valor total da compra.

## Descrição

O código solicita ao usuário o valor unitário de um produto e a quantidade desejada. Ele calcula o valor total da compra e aplica um desconto com base no valor total da seguinte forma:

- **Valor Total < R$999**: Sem desconto.
- **R$1000 ≤ Valor Total < R$3000**: 3% de desconto.
- **R$3000 ≤ Valor Total < R$5000**: 5% de desconto.
- **Valor Total ≥ R$5000**: 8% de desconto.

Depois de calcular o desconto, o script imprime o valor total sem desconto e o valor final com desconto.

 # Exercício 2
 # Sistema de Pedido de Sorvetes

Este script em Python permite que o usuário faça pedidos de sorvetes com base em sabor e tamanho. O código exibe um cardápio, coleta as escolhas do usuário e calcula o valor total a ser pago com base nos itens selecionados.

## Descrição

O script exibe um cardápio com opções de sabores e tamanhos de sorvetes e solicita ao usuário que escolha o sabor e o tamanho desejados. Os preços são definidos conforme o cardápio:

- **Sabor:**
  - **Cupuaçu (CP)**
  - **Açaí (AC)**
  
- **Tamanho:**
  - **P**: Pequeno
  - **M**: Médio
  - **G**: Grande

Os preços são os seguintes:
- **Cupuaçu (CP)**
  - Pequeno: R$ 10,00
  - Médio: R$ 15,00
  - Grande: R$ 19,00

- **Açaí (AC)**
  - Pequeno: R$ 12,00
  - Médio: R$ 17,00
  - Grande: R$ 21,00

O usuário pode continuar pedindo mais itens até decidir que não deseja mais nada. No final, o script exibe o total a ser pago.

## Requisitos

- Python 3.x: O script é compatível com qualquer versão recente do Python 3.

## Como Executar

1. **Salve o Código em um Arquivo Python**:
   - Salve o código fornecido em um arquivo, por exemplo, `pedido_sorvetes.py`.

2. **Execute o Script**:
   - Abra um terminal ou prompt de comando.
   - Navegue até o diretório onde o arquivo está localizado.
   - Execute o script com o comando:
     ```bash
     python pedido_sorvetes.py
     ```

3. **Siga as Instruções**:
   - Escolha o sabor e o tamanho do sorvete conforme solicitado.
   - Informe se deseja adicionar mais itens ao pedido.
   - O total a ser pago será exibido ao final.


