
if __name__ == '__main__':
    with open('Индивид 1.txt', 'r') as f:
        text = f.read()

    offers = text.split('.')
    del offers[offers.index('')]

    print([offer for offer in offers if not "-" in offer])