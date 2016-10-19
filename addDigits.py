class solution:
    def addDigits(self, num):
        return (num - 1) % 9 + 1 if num > 0 else 0

if __name__ == '__main__':
    result = solution().addDigits(-1)
    print result
