kata = "The right format"

def main():
    new_kata = kata.rjust(42)
    print(new_kata, end="")

if __name__ == "__main__":
    main()