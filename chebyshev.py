import numpy as np

N = 8


def main():
    # Init values
    # x_k = []
    y_k = []
    a_k = []

    # print(f' X initial\t|\t Actual')
    # print('-' * 25)
    for num in range(N + 1):
        temp = np.cos(np.pi * (2 * num + 1) / (2 * (N + 1)))
        y_k.append(np.arctan(2 * temp))
        # print(f'{" " if temp > 0 else ""}{temp:.5f}\t|\t{" " if y_k[-1] > 0 else ""}{y_k[-1]:.5f}')

    a_k.append(sum(y_k) / (N + 1))

    for num in range(1, N + 1):
        total = 0
        for idx, el in enumerate(y_k):
            total += el * np.cos((((2 * idx + 1) * num) / (2 * N + 2)) * np.pi)
        a_k.append(2 * total / (N + 1))

    # print('\n' + '=' * 46)
    print('COMPARING:')
    max_err = 0
    for value in np.arange(-0.9, 1.2, 0.6):
        value = round(value, 3)
        mine = 0
        real = np.arctan(2 * value)
        for idx, el in enumerate(a_k):
            mine += el * cheb_pol(value, idx)
        max_err = max(max_err, abs(mine - real))
        print(f'Ch({value}) = {mine:.9f}\tf({value}) = {real:.9f}')
    print(f'\nMAX ERROR: {max_err:.9f}')


def cheb_pol(x, depth):
    if depth == 0:
        return 1
    elif depth == 1:
        return x
    return 2 * x * cheb_pol(x, depth - 1) - cheb_pol(x, depth - 2)


if __name__ == '__main__':
    main()
