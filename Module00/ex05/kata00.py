kata = (19, 42, 21)


def main():
    size = len(kata)
    if size == 0:
        print('Empty tuple')
        exit()
    print('The {} numbers are: {}'.format(size, ', '.join('{}'.format(i) for i in kata)))

if __name__ == "__main__":
    main()
