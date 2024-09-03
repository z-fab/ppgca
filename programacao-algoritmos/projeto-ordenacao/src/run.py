import pickle
import random
import sys
from algoritmos_ordenacao import (
    merge_sort,
    bubble_sort,
    optimized_bubble_sort,
    selection_sort,
    insertion_sort,
    quick_sort,
)
from util import timer

sys.setrecursionlimit(1_000_000)

list_alg = [
    bubble_sort,
    optimized_bubble_sort,
    selection_sort,
    insertion_sort,
    quick_sort,
    merge_sort,
]

results = []


def save_result():
    pickle.dump(results, open("data/result_dict.pkl", "wb"))


def run_alg(alg, arr):
    print(f"Rodando {alg.__name__} (first: {arr[0]})...", end=" ")
    result = alg(arr)
    print(f"{result[1]}ms")
    return result


@timer
def run():
    for i in range(0, 3):
        n = 1_000 * (10**i)
        print(f"\n{'='*50}\nARRAY DE TAMANHO {n}\n{'='*50}\n")

        correct_arr = list(range(0, n))

        arr_middle = random.sample(correct_arr, n)
        arr_best = correct_arr
        arr_worst = list(range(n - 1, -1, -1))

        control_middle = [
            arr_middle[0],
            arr_middle[-1],
            arr_middle[len(arr_middle) // 2],
        ]
        control_best = [arr_best[0], arr_best[-1], arr_best[len(arr_best) // 2]]
        control_worst = [arr_worst[0], arr_worst[-1], arr_worst[len(arr_worst) // 2]]

        n_inter = 5
        for iteration in range(0, n_inter):
            print(
                f"\nITERAÇÃO {iteration+1}/{n_inter} [{'x'*(iteration+1)}{'-'*(n_inter-iteration-1)}]\n"
            )
            for alg in list_alg:
                # verificando se os arrays foram alterados durante a execução
                assert [
                    arr_best[0],
                    arr_best[-1],
                    arr_best[len(arr_best) // 2],
                ] == control_best
                assert [
                    arr_middle[0],
                    arr_middle[-1],
                    arr_middle[len(arr_middle) // 2],
                ] == control_middle
                assert [
                    arr_worst[0],
                    arr_worst[-1],
                    arr_worst[len(arr_worst) // 2],
                ] == control_worst

                result_arr_best, time_result_best = run_alg(alg, arr_best)
                result_arr_middle, time_result_middle = run_alg(alg, arr_middle)
                result_arr_worst, time_result_worst = run_alg(alg, arr_worst)

                # verificando se os arrays foram ordenados corretamente
                assert result_arr_best == correct_arr
                assert result_arr_middle == correct_arr
                assert result_arr_worst == correct_arr

                result_dict = {
                    "len_arr": n,
                    "iteration": iteration,
                    "alg": alg.__name__,
                    "best": time_result_best,
                    "middle": time_result_middle,
                    "worst": time_result_worst,
                }

                results.append(result_dict)
                save_result()


if __name__ == "__main__":
    result = run()

    print(f"Fim! Tempo total: {round(result[1]/1000/60,2)}min")
