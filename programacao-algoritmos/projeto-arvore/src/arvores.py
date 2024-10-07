class BSTNode:
    def __init__(self, key, payload):
        self.key = key
        self.payload = payload
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, payload):
        if self.root is None:
            self.root = BSTNode(key, payload)
        else:
            self._insert(self.root, key, payload)

    def _insert(self, node, key, payload):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key, payload)
            else:
                self._insert(node.left, key, payload)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key, payload)
            else:
                self._insert(node.right, key, payload)
        else:
            # Se a chave já existe, atualiza o payload
            node.payload = payload

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.payload
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1  # A altura de uma árvore vazia é -1
        else:
            return 1 + max(self._height(node.left), self._height(node.right))


# =========
# AVL Tree
# =========


class AVLNode:
    def __init__(self, key, payload):
        self.key = key
        self.payload = payload
        self.left = None
        self.right = None
        self.height = 0  # Altura do nó


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, payload):
        self.root = self._insert(self.root, key, payload)

    def _insert(self, node, key, payload):
        if node is None:
            return AVLNode(key, payload)
        elif key < node.key:
            node.left = self._insert(node.left, key, payload)
        elif key > node.key:
            node.right = self._insert(node.right, key, payload)
        else:
            # Atualiza o payload se a chave já existe
            node.payload = payload
            return node

        # Atualiza a altura do nó ancestral
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Calcula o fator de balanceamento
        balance = self._get_balance(node)

        # Realiza rotações para balancear a árvore
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

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.payload
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if node is None:
            return -1  # Altura de uma árvore vazia é -1
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0  # Fator de balanceamento de um nó vazio é 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Realiza a rotação
        y.left = z
        z.right = T2

        # Atualiza as alturas
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Retorna a nova raiz
        return y

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Realiza a rotação
        x.right = y
        y.left = T2

        # Atualiza as alturas
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        # Retorna a nova raiz
        return x
