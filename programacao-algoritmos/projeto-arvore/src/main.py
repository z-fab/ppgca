from arvores import BinarySearchTree, AVLTree
from utils import tempo
import random
import pickle
import polars as pl
import sys

sys.setrecursionlimit(10**6)

result_insercao = []
result_search = []


def processar_dados():
    df = (
        pl.read_parquet("data/imdb.parquet")
        .select(
            pl.col("id").alias("id"),
            pl.col("title").alias("titulo"),
            pl.col("vote_average").alias("nota_media"),
            pl.col("vote_count").alias("numero_votos"),
            pl.col("release_year").cast(pl.Int32).alias("ano_lancamento"),
            pl.col("Director").alias("diretor"),
            pl.col("genres_list").alias("genero"),
        )
        .with_columns(
            (pl.col("titulo") + " - " + pl.col("diretor")).alias("titulo_diretor"),
        )
        .unique(subset=["id"])
    )

    return df, df.unique(subset=["titulo_diretor"])


def get_sample_random(fraction, df):
    return (
        df.sample(fraction=fraction, shuffle=True)
        # .sort("id")
    ).to_dicts()


@tempo
def inserir_elementos(arvore, dict_df):
    for elemento in dict_df:
        arvore.insert(elemento["id"], elemento)


@tempo
def buscar_elementos(arvore, key):
    arvore.search(key)


if __name__ == "__main__":
    n_iter = 10
    n_search = 100
    sample = 1

    df_id, df_titulo = processar_dados()
    df = df_id.clone()

    for i in range(n_iter):
        data = get_sample_random(sample, df)
        data_to_search = random.sample(data, n_search)
        print(f"===== ITERAÇÃO {i} - N: {len(data)} =====")

        # Inserção
        bst = BinarySearchTree()
        _, tempo_insercao_bst = inserir_elementos(bst, data)
        print(f"BST: {tempo_insercao_bst} ms | Altura: {bst.height()}")

        avl = AVLTree()
        _, tempo_insercao_avl = inserir_elementos(avl, data)
        print(f"AVL: {tempo_insercao_avl} ms | Altura: {avl.height()}")

        result_insercao.append(
            {
                "n_iter": i,
                "tempo_insercao_bst": tempo_insercao_bst,
                "tempo_insercao_avl": tempo_insercao_avl,
                "altura_bst": bst.height(),
                "altura_avl": avl.height(),
            }
        )

        # Busca
        print("-- Buscas --")
        for element_to_search in data_to_search:
            _, tempo_busca_avl = buscar_elementos(avl, element_to_search["id"])
            print(f"AVL: {tempo_busca_avl} ms")

            _, tempo_busca_bst = buscar_elementos(bst, element_to_search["id"])
            print(f"BST: {tempo_busca_bst} ms")

            result_search.append(
                {
                    "n_iter": i,
                    "n_search": n_search,
                    "tempo_busca_avl": tempo_busca_avl,
                    "tempo_busca_bst": tempo_busca_bst,
                    "altura_bst": bst.height(),
                    "altura_avl": avl.height(),
                }
            )
    print("====================================")
    print(
        f"Média de tempo de inserção BST: {sum([r['tempo_insercao_bst'] for r in result_insercao]) / n_iter} ms"
    )
    print(
        f"Média de tempo de inserção AVL: {sum([r['tempo_insercao_avl'] for r in result_insercao]) / n_iter} ms"
    )
    print(
        f"Média de tempo de busca BST: {sum([r['tempo_busca_bst'] for r in result_search]) / n_iter} ms"
    )
    print(
        f"Média de tempo de busca AVL: {sum([r['tempo_busca_avl'] for r in result_search]) / n_iter} ms"
    )

    result = {
        "result_insercao": result_insercao,
        "result_search": result_search,
    }

    with open("data/result_id.pkl", "wb") as f:
        pickle.dump(result, f)
