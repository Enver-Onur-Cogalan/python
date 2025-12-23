# 1. FİBONACCİ
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

print("--- Fibonacci ---")
fibonacci(10)
print(' ')
print('-'*25)

# --- Fibonacci ---
# 0 1 1 2 3 5 8 13 21 34  
# -------------------------

# ********************************************

# 2. Asal Sayı Kontrolü
def asal_mi(sayi):
    if sayi <= 1:
        return False
    
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
        return True
    
print("--- Asal Sayı ---")
print(asal_mi(17))
print(asal_mi(18))
print('-'*25)

# --- Asal Sayı ---
# True
# False
# -------------------------

# ********************************************

# 3. Sayı Basamaklarının Toplamı
def basamak_toplami(sayi):
    toplam = 0
    while sayi > 0:
        toplam += sayi % 10
        sayi //= 10
    
    return toplam

print("--- Basamak Toplama ---")
print(basamak_toplami(458))
print('-'*25)

# --- Basamak Toplama ---
# 17
# -------------------------

# ********************************************

# 4. En büyük ve En küçük Bulma
def en_buyuk_en_kucuk(liste):
    en_buyuk = liste[0]
    en_kucuk = liste[0]

    for sayi in liste:
        if sayi > en_buyuk:
            en_buyuk = sayi
        if sayi < en_kucuk:
            en_kucuk = sayi

    return en_buyuk, en_kucuk

print("--- En Büyük En Küçük ---")
print(en_buyuk_en_kucuk([3,7,2,9,4]))
print('-'*25)

# --- En Büyük En Küçük ---
# (9, 2)
# -------------------------


# ********************************************

# 5. Palindrom Kontrolü
def palindrom_mu(kelime):
    if kelime == kelime[::-1]:
        return True
    else:
        return False

print("--- Palindrom ---")
print(palindrom_mu("kayak"))
print(palindrom_mu("python"))
print('-'*25)

# --- Palindrom ---
# True
# False
# -------------------------

#  **BONUS** ZOR: BFS

grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

from collections import deque

def en_kisa_yol(grid):
    n = len(grid)
    m = len(grid[0])

    queue = deque([(0, 0, 0)])
    ziyaret_edildi = set()
    ziyaret_edildi.add((0, 0))

    yonler = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, adim = queue.popleft()

        if x == n - 1 and y == m - 1:
            return adim
        
        for dx, dy in yonler:
            nx, ny = x + dx, y + dy
            
            if (
                0 <= nx < n and
                0 <= ny < m and
                grid[nx][ny] == 0 and
                (nx, ny) not in ziyaret_edildi
            ):
                ziyaret_edildi.add((nx, ny))
                queue.append((nx, ny, adim + 1))

    return -1 # Yol yok

print("--- BONUS ---")
print(en_kisa_yol(grid))
print('-'*25)

# --- BONUS ---
# 6
# -------------------------

