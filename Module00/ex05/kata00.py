kata = (19,42,21)


def main():
    size = len(kata)
    print('The {} numbers are: {}'.format(size, ', '.join('{}'.format(i) for i in kata)))

if __name__ == "__main__":
    main()
