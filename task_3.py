from pathlib import Path

def main():
    divisor = 73 * 73 + 29
    
    path_in = Path(__file__).parent / "resource" / "numbers.txt"
    path_out = Path(__file__).parent / "resource" / "result.txt"
    
    with open(path_in, "r") as f_in:
        with open(path_out, "w") as f_out:
            for line in f_in:
                numbers = line.split()
                for num_str in numbers:
                    num = int(num_str)
                    if num % 7 == 0:
                        result = num * 100 / divisor
                        f_out.write(str(result) + "\n")
                        print(num, "->", result)
    
    print("Результат сохранен в result.txt")

if __name__ == "__main__":
    main()