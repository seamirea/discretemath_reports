SIZE = 5

def read_matrix():
    print("Enter a 5 x 5 relation matrix. Separate the numbers with spaces.")
    matrix = []
    for row_number in range(1, SIZE + 1):
        while True:
            values = input(f"Row {row_number}: ").split()
            if len(values) == SIZE and all(value in ("0", "1") for value in values):
                matrix.append([int(value) for value in values])
                break
            print("Enter exactly five values, each either 0 or 1.")
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def is_reflexive(matrix):
    for i in range(SIZE):
        if matrix[i][i] != 1:
            return False
    return True


def is_symmetric(matrix):
    for i in range(SIZE):
        for j in range(i + 1, SIZE):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def is_transitive(matrix):
    for i in range(SIZE):
        for j in range(SIZE):
            for k in range(SIZE):
                if matrix[i][j] and matrix[j][k] and not matrix[i][k]:
                    return False
    return True


def equivalence_class(matrix, element):
    members = []
    for j in range(SIZE):
        if matrix[element - 1][j] == 1:
            members.append(j + 1)
    return members


def print_equivalence_classes(matrix):
    print("Equivalence classes:")
    for element in range(1, SIZE + 1):
        members = equivalence_class(matrix, element)
        members_text = ", ".join(str(member) for member in members)
        print(f"[{element}] = {{{members_text}}}")


def reflexive_closure(matrix):
    result = [row.copy() for row in matrix]
    for i in range(SIZE):
        result[i][i] = 1
    return result


def symmetric_closure(matrix):
    result = [row.copy() for row in matrix]
    for i in range(SIZE):
        for j in range(SIZE):
            if matrix[i][j] == 1:
                result[j][i] = 1
    return result


def transitive_closure(matrix):
    result = [row.copy() for row in matrix]
    for k in range(SIZE): #워샬 알고즘
        for i in range(SIZE):
            for j in range(SIZE):
                if result[i][k] and result[k][j]:
                    result[i][j] = 1
    return result


def print_relation_result(matrix):
    reflexive = is_reflexive(matrix)
    symmetric = is_symmetric(matrix)
    transitive = is_transitive(matrix)

    print(f"Reflexive: {reflexive}")
    print(f"Symmetric: {symmetric}")
    print(f"Transitive: {transitive}")

    if reflexive and symmetric and transitive:
        print("This is an equivalence relation.")
        print_equivalence_classes(matrix)
    else:
        print("This is not an equivalence relation.")


def show_closure(name, before, after):
    print(f"\n{name} closure")
    print("Before:")
    print_matrix(before)
    print("After:")
    print_matrix(after)
    print_relation_result(after)


def main():
    original = read_matrix()
    print("\nInput matrix:")
    print_matrix(original)
    print_relation_result(original)
    
    if not is_reflexive(original):
        result = reflexive_closure(original)
        show_closure("Reflexive", original, result)

    if not is_symmetric(original):
        result = symmetric_closure(original)
        show_closure("Symmetric", original, result)

    if not is_transitive(original):
        result = transitive_closure(original)
        show_closure("Transitive", original, result)


if __name__ == "__main__":
    main()
