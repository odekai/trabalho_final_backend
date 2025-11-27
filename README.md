# trabalho_final_backend
Trabalho final de programação Back-end no valor de 60 pts




---

## 🏷️ Badges do Projeto

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Django](https://img.shields.io/badge/Django-Framework-green?logo=django)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/Licença-MIT-green)

---

# 🛒 Sistema de Vendas – Supermercados Primeira Luz do Dia & Beagás

Projeto desenvolvido como trabalho final da disciplina de Programação Back-end.
O objetivo é criar um sistema funcional para auxiliar na gestão dos supermercados, cobrindo desde o estoque até o processo de vendas.

---

## ✨ Funcionalidades do Sistema

### 📦 **Controle de Estoque**

* Monitora automaticamente a quantidade de produtos.
* Emite alerta quando algum item atingir o estoque mínimo.
* Estoque mínimo definido pelo administrador.

### 🛍️ **Gestão de Produtos**

* Produtos não são cadastrados manualmente.
* Ao registrar uma entrega, o sistema atualiza o estoque automaticamente.
* Se o produto já existir, apenas incrementa a quantidade; caso contrário, cria o produto na hora.

### 🚚 **Controle de Entregas**

* Cada entrega registra:

  * Lista de produtos recebidos
  * Valor total
  * Data da entrega
  * Número da nota fiscal

### 👥 **Controle de Clientes**

* Possibilidade de adesão ao programa de fidelidade.
* A cada R$10,00 em compras = +1 ponto para descontos futuros (não é necessário implementar a troca de pontos).

### 🧑‍💼 **Cadastro de Funcionários**

* Funcionários precisam estar cadastrados para operar o sistema.
* Tipos disponíveis:

  * **Administrador**
  * **Funcionário**
* Apenas funcionários do tipo *Funcionário* podem efetuar vendas.
* Para vender, o funcionário deve estar logado.

### 💰 **Controle de Vendas**

* Registra todas as vendas realizadas no sistema.
* Associado ao cliente (quando houver) e ao funcionário que efetuou a venda.

---

## 🧱 **Resumo da Arquitetura**

O sistema integra o controle completo de estoque, clientes, funcionários e vendas, garantindo organização, segurança e automação no fluxo dos supermercados contratantes.

---



