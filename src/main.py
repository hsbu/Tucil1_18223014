import time

def print_input(input, length):
    for i in range(length):
        row = input[length * i: length * (i + 1)]
        print(" ".join(row))
    print()

def val_col_row(problem, length):
    row = [0] * length
    col = [0] * length
    for i in range(len(problem)):
        if problem[i] == "#":
            row[i // length] += 1
            col[i % length] += 1
    return all(x == 1 for x in row) and all(x == 1 for x in col)

def val_color(problem, solution):
    color = set()
    for i in range(len(solution)):
        if solution[i] == "#":
            if problem[i] in color:
                return False
            color.add(problem[i])
    return True

def save_solution(solution, length, filename):
    f = open(filename, "w")
    for i in range(length):
        row = solution[length * i: length * (i + 1)]
        f.write("".join(row) + "\n")
    f.close()

file_path = input("Masukkan file permasalahan: ")
file = open(file_path).read()
problem = list(file.replace("\n", ""))

length = len(file.splitlines())
solution = []
solution_found = False

# Explore
total_cells = length ** 2
idx = list(range(length))
case = 0 

start = time.time() * 1000 # Start time

if len(problem) != (length ** 2):
    print("Input tidak valid!")
else:
    while True:
        case += 1
        if case % 1000 == 0:
            print_input(copy, length)

        copy = problem[:]
        for p in idx:
            copy[p] = '#'

        # Validate
        if val_col_row(copy, length) and val_color(problem, copy):
            print("Solusi ditemukan:")
            print_input(copy, length)
            solution = copy
            solution_found = True
            break

        i = length - 1
        while i >= 0 and idx[i] == i + (total_cells - length):
            i -= 1

        if i < 0:
            break

        idx[i] += 1
        for j in range(i + 1, length):
            idx[j] = idx[j - 1] + 1

end = time.time() * 1000 # End time

if solution_found == False:
    print("Solusi tidak ditemukan.")
    
print(f"Banyak kasus yang ditinjau: {case}")
print(f"Waktu pencarian: {(end - start):.2f}ms")

if solution_found == True:
    choice = input("Apakah Anda ingin menyimpan solusi? (Ya/Tidak): ").lower()

    if choice == "ya":
        file_name = input("Masukkan nama file solusi (Contoh: solution.txt): ")
        save_solution(solution, length, file_name)
        print(f"Solusi disimpan pada {file_name}.")
        print("Program selesai.")
    elif choice == "tidak":
        print("Program Selesai.")
    else:
        print("Input tidak valid!")