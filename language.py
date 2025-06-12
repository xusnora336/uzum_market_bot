def find_max_number():
    sonlar = input("Sonlarni bo'sh joy bilan ajratib kiriting: ").split()
    sonlar = [int(son) for son in sonlar]  # Stringlarni int ga aylantirish
    if not sonlar:  # Agar ro'yxat bo'sh bo'lsa
        return None
    return max(sonlar)
# Funksiyani chaqirish
print(find_max_number())