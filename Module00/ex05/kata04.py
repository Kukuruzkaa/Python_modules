kata = (0, 4, 132.42222, 10000, 12345.67)

def main():
    res = 'module_%02d, ex_%02d : %5.2f, %.2e, %.2e' %(kata[0], kata[1], kata[2], kata[3], kata[4])
    print(res)

if __name__ == "__main__":
    main()

    # print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})
# Python has 002 quote types.