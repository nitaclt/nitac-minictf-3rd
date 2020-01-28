from secret import flag

if __name__ == '__main__':
    f = int.from_bytes(flag, byteorder='big')
    assert f < 1<<256
    try:
        n = int(input("n = "))
        assert 0 < n < 123456
        print("Here you are: {}".format(f % n))
    except:
        print("Invalid input!")
        exit(0)
