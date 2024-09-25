
class BSTNode:
    def __init__(self, key, payload):
        self.key = key
        self.payload = payload  # Dicionário com informações adicionais
        self.left = None
        self.right = None

class AVLNode:
    def __init__(self, key, payload):
        self.key = key
        self.payload = payload  # Dicionário com informações adicionais
        self.left = None
        self.right = None
        self.height = 1  # Altura inicial do nó


class BSTNode:
    def __init__(self, key, payload):
        self.key = key
        self.payload = payload  # Dicionário com informações adicionais
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    # Inserção recursiva na BST
    def insert(self, key, payload):
        self.root = self._insert_recursive(self.root, key, payload)

    def _insert_recursive(self, node, key, payload):
        if node is None:
            return BSTNode(key, payload)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key, payload)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, payload)
        else:
            # Chave já existe, atualiza o payload
            node.payload = payload
        return node

    # Busca recursiva na BST
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    # Deleção recursiva na BST
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Nó encontrado
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Nó com dois filhos: obter o sucessor inorder
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.payload = temp.payload
            node.right = self._delete_recursive(node.right, temp.key)
        return node

    # Função auxiliar para encontrar o nó com o menor valor
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Cálculo recursivo da altura da BST
    def tree_height(self):
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, node):
        if not node:
            return 0
        left_height = self._get_height_recursive(node.left)
        right_height = self._get_height_recursive(node.right)
        return 1 + max(left_height, right_height)

class AVLTree:
    def __init__(self):
        self.root = None

    # Inserção recursiva na AVL
    def insert(self, key, payload):
        self.root = self._insert_recursive(self.root, key, payload)

    def _insert_recursive(self, node, key, payload):
        # Inserção normal de BST
        if not node:
            return AVLNode(key, payload)
        elif key < node.key:
            node.left = self._insert_recursive(node.left, key, payload)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, payload)
        else:
            # Chave já existe, atualiza o payload
            node.payload = payload
            return node

        # Atualiza a altura do nó ancestral
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Obtém o fator de balanceamento
        balance = self._get_balance(node)

        # Verifica os casos de desbalanceamento e aplica as rotações
        # Caso Esquerda-Esquerda
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)

        # Caso Direita-Direita
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)

        # Caso Esquerda-Direita
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Caso Direita-Esquerda
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # Busca recursiva na AVL
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    # Deleção recursiva na AVL
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        # Deleção padrão de BST
        if not node:
            return node
        elif key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Nó com um ou nenhum filho
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                # Nó com dois filhos: pega o sucessor inorder
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.payload = temp.payload
                node.right = self._delete_recursive(node.right, temp.key)

        # Atualiza a altura do nó atual
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Balanceia o nó atual
        balance = self._get_balance(node)

        # Verifica os casos de desbalanceamento e aplica as rotações
        # Caso Esquerda-Esquerda
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        # Caso Esquerda-Direita
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Caso Direita-Direita
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)

        # Caso Direita-Esquerda
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # Função auxiliar para encontrar o nó com o menor valor
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Rotação à esquerda
    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Executa a rotação
        y.left = z
        z.right = T2

        # Atualiza as alturas
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Retorna a nova raiz
        return y

    # Rotação à direita
    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Executa a rotação
        x.right = y
        y.left = T2

        # Atualiza as alturas
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        # Retorna a nova raiz
        return x

    # Função para obter a altura de um nó
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    # Função para obter o fator de balanceamento de um nó
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # Cálculo da altura da AVL (altura da raiz)
    def tree_height(self):
        return self._get_height(self.root)
