"""
1.Toate numerele sunt pătrate perfecte.
11.Toate numerele au același număr de biți de 1 în reprezentarea binară.
12.Toate numerele același număr de divizori.
"""

def patrat_perfect(n):
    """
    Verifica daca un numar e patrat perfect
    :param n:
    :return: Bool
    """
    i=0
    while i*i<=n:
        if i*i == n:
            return True
        i = i + 1
    return False


def get_longest_all_perfect_squares(lst: list[int]):
    """
    Cea mai lunga lista de patrate perfecte
    :param lst:
    :return: lstmax
    """
    lst2=[]
    lstmax=[]
    nr=0
    nrmax=-1
    for i in lst:
        if patrat_perfect(i)==True:
            lst2.append(i)
            nr=nr+1
            if nr > nrmax:
                lstmax=lst2
                nrmax=nr
        if patrat_perfect(i)==False:
            nr=0
            lst2=[]
    return lstmax

def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([36, 16, 5, 144, 9, 4]) == [144, 9, 4]
    assert get_longest_all_perfect_squares([36, 14, 12, 25, 256, 11]) == [25, 256]
    assert get_longest_all_perfect_squares([35, 11, 15, 23, 16, 19]) == [16]
    assert get_longest_all_perfect_squares([36, 16]) == [36, 16]


def nrbiti(n):
    """
    Calculeaza numarul de biti de 1
    :param n:
    :return: nr
    """
    nr=0
    while(n!=0):
        if(n%2==1):
            nr=nr+1
        n=n//2
    return nr

def get_longest_same_bit_counts(lst: list[int]):
    """
    Cea mai lunga lista de numere cu acelasi numar de biti de 1
    :param lst:
    :return: lstmax
    """
    lst2=[]
    lstmax=[]
    nr=0
    nrmax=-1
    ok=0
    for i in lst:
        if ok == 0:
            lst2.append(i)
            biti_anteriori=nrbiti(i)
            ok=1
            lstmax=lst2
        else:
            if nrbiti(i)==biti_anteriori:
                lst2.append(i)
                nr=nr+1
                if nr > nrmax:
                    lstmax=lst2
                    nrmax=nr
            if nrbiti(i)!=biti_anteriori:
                nr=0
                lst2=[]
                lst2.append(i)
                biti_anteriori=nrbiti(i)
    return lstmax

def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([16, 25, 36, 4, 28, 19, 17, 25]) == [28, 19]
    assert get_longest_same_bit_counts([18, 19, 20, 19, 22, 25, 17]) == [19, 22, 25]
    assert get_longest_same_bit_counts([4, 8, 11, 12]) == [4, 8]
    assert get_longest_same_bit_counts([14]) == [14]

def nr_div(n):
    """
    Calculeaza numarul de divizori
    :param n:
    :return: nr
    """
    nr=0
    if n == 1:
        nr=1
    for i in range (2, n//2):
        if n % i == 0:
            nr = nr + 1
    return nr

def get_longest_same_div_count(lst: list[int]):
    """
    Cea mai lunga lista de numere cu acelasi numar de divizori
    :param lst:
    :return: lstmax
    """
    lst2=[]
    lstmax=[]
    nr=0
    nrmax=-1
    ok=0
    for i in lst:
        if ok == 0:
            lst2.append(i)
            div_anteriori=nr_div(i)
            ok=1
            lstmax=lst2
        else:
            if nr_div(i)==div_anteriori:
                lst2.append(i)
                nr=nr+1
                if nr > nrmax:
                    lstmax=lst2
                    nrmax=nr
            if nr_div(i)!=div_anteriori:
                nr=0
                lst2=[]
                lst2.append(i)
                div_anteriori=nr_div(i)
    return lstmax

def test_get_longest_same_div_count():
    assert get_longest_same_div_count([16, 25, 36, 4, 28, 19, 17, 25]) == [19, 17]
    assert get_longest_same_div_count([18, 19, 20, 9, 4, 25, 17]) == [9, 4, 25]
    assert get_longest_same_div_count([15, 8, 11, 12]) == [15, 8]
    assert get_longest_same_div_count([14]) == [14]

def main():
    while True:
        print('1. Citire date')
        print('2. Determinare cea mai lungă subsecvență cu proprietatea 1 (problema 1)')
        print('3. Determinare cea mai lungă subsecvență cu proprietatea 2 (problema 11)')
        print('4. Determinare cea mai lungă subsecvență cu proprietatea 3 (problema 12)')
        print('x. Iesire din program')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            print('Cititi numarul de elemente')
            lst = []
            n = int(input())
            print('Cititi elementele listei')
            for i in range(n):
                lst.append(int(input()))
        elif optiune == '2':
            lstf = []
            lstf = get_longest_all_perfect_squares(lst)
            print(lstf)
        elif optiune == '3':
            lstf = []
            lstf = get_longest_same_bit_counts(lst)
            print(lstf)
        elif optiune == '4':
            lstf = []
            lstf = get_longest_same_div_count(lst)
            print(lstf)
        elif optiune == 'x':
            break
if __name__ == '__main__':
    main()