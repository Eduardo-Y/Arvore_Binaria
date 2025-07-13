# Binary Search Tree em Python 🌳

Este repositório implementa uma **Árvore Binária de Busca (Binary Search Tree - BST)** em Python, com funcionalidades completas de inserção, busca, remoção e percursos (in-order, pós-ordem e por nível), além do cálculo da altura da árvore.

## 📁 Estrutura do Projeto

- `Node`: Classe que representa um nó da árvore, com valor (`data`) e ponteiros para os filhos esquerdo e direito.
- `BinaryTree`: Classe base com métodos genéricos para árvores binárias:
  - `inorder_traversal`
  - `postorder_traversal`
  - `levelorder_traversal`
  - `height`
- `BinarySearchTree`: Herda de `BinaryTree` e implementa funcionalidades específicas de BST:
  - `insert`
  - `search`
  - `remove`
  - `min` e `max`

## 🚀 Funcionalidades

- Inserção de elementos na árvore respeitando a regra da BST.
- Busca de elementos, retornando uma subárvore com o elemento como raiz.
- Remoção de nós com 0, 1 ou 2 filhos.
- Cálculo da altura da árvore.
- Obtenção do valor mínimo e máximo.
- Percursos:
  - **In-order (esquerda → raiz → direita)**
  - **Pós-ordem (esquerda → direita → raiz)**
  - **Por nível (BFS - Breadth-First Search)**

## ▶️ Exemplo de Execução

```python
if __name__ == "__main__":
    ftree = BinarySearchTree()
    nodes = [12, 9, 20, 3, 10, 18, 80, 1, 4, 13, 23]
    for n in nodes:
        ftree.insert(n)

    ftree.inorder_traversal()
    print('')
    ftree.postorder_traversal()
    print(f'\nAltura: {ftree.height()} nós.')
    ftree.levelorder_traversal()
    print("")
    print(f"Min:{ftree.min()} e Max:{ftree.max()}")
    ftree.remove(12)
    ftree.levelorder_traversal()
````
### 📊 Ilustração
<img width="2440" height="1298" alt="image" src="https://github.com/user-attachments/assets/3848b801-20eb-4373-a06e-cdc39efc1d63" />

### 💡 Saída Esperada

```
1 3 4 9 10 12 13 18 20 23 80 
1 4 3 10 9 13 18 23 80 20 12 
Altura: 5 nós.
12 9 20 3 10 18 80 1 4 13 23 
Min:1 e Max:80
13 9 20 3 10 18 80 1 4 23
```

## 🛠️ Requisitos

* Python 3.6 ou superior.

## 📚 Aprendizados

Este projeto é uma ótima introdução à manipulação de estruturas de dados em Python, especialmente árvores binárias e árvores binárias de busca.

---

Se quiser, posso gerar uma versão em inglês ou adicionar imagens/diagramas das árvores. Deseja isso também?
```
