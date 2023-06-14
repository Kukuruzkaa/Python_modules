import datetime

kata = (2019, 9, 25, 3, 30)

def main():
    kata_to_format = datetime.datetime(*kata)
    formatted_kata = kata_to_format.strftime("%m/%d/%Y %H:%M")
    print(formatted_kata)

if __name__ == "__main__":
    main()

