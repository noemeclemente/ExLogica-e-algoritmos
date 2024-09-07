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

  # Exercício 3 
  # Calculadora de Custos de Serviços de Impressão e Encadernação

Este script em Python calcula o custo total para serviços de impressão e encadernação com base nas escolhas do usuário. O usuário pode selecionar o tipo de serviço, o número de páginas e serviços adicionais, e o script calcula o custo total considerando descontos aplicáveis e custos adicionais.

## Descrição

O script oferece três opções de serviços de impressão e fotocópia, calcula descontos baseados no número de páginas e permite a escolha de serviços adicionais como encadernação. A seguir estão os detalhes dos serviços e custos:

### Tipos de Serviço e Preços

- **Digitalização (DIG)**: R$ 1,10 por página
- **Impressão Colorida (ICO)**: R$ 1,00 por página
- **Impressão Preto e Branco (IBO)**: R$ 0,40 por página
- **Fotocópia (FOT)**: R$ 0,20 por página

### Descontos por Número de Páginas

- Menos de 10 páginas: Sem desconto
- De 10 a 99 páginas: 10% de desconto
- De 100 a 999 páginas: 15% de desconto
- 1000 ou mais páginas: 20% de desconto

### Serviços Adicionais e Custos

- **Encardenação Simples**: R$ 10,00
- **Encardenação de Capa Dura**: R$ 25,00
- **Nenhum Adicional**: R$ 0,00

## Funcionalidades

- **Escolha do Serviço**: O usuário seleciona um tipo de serviço e o valor correspondente é definido.
- **Número de Páginas**: O usuário insere o número de páginas e o desconto aplicável é calculado.
- **Serviço Adicional**: O usuário escolhe se deseja adicionar um serviço adicional e o custo é adicionado ao total.
- **Cálculo do Total**: O script calcula o valor total a ser pago, considerando o valor do serviço, o desconto aplicado ao número de páginas e qualquer custo adicional.


