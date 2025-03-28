# Lintiņš Oskars PD1
# Šeit ir dota funkcija, kura atrod vislielāko pieagumu (starpību) skaitļu virknē.
# Starpība ir definēta pēc uzdevuma prasības : skaitlis n2 nāk pēc n1.
# Izmantojot uzdevuma padomus, izvēlējos lineāro atrisinājumu, kura izmanto O(n) (tā ir laba izvēle pēc grafika, attēlota bigocheatsheet.com)
def max_difference(sequence): # funkcijas definīcija, kura izmanto skaitļu virkni, kā ieejas datus
    min_value = sequence[0] # sākotnējais minimālais skaitlis
    max_diff = 0 # sākotnējais pieagums (starpība)

    # cikls, kurš sāk savu iterāciju no 2. skaitļa, jo 1. jau ir izvēlēts kā min_value
    # cikla rezultātā būs aprēķināta vislielākais pieagums (starpība) skaitļu virknē (sarakstā)
    for num in sequence[1: ]:
        # tiek veikta minimālā skaitļa atjaunošana, izmantojot iebūvēto min funkciju,
        # kura izvēlās minimālo vērtību starp pašlaik definēto minimālo vērtību un skaitli, iegūtu no virknes (saraksta)
        min_value = min(min_value, num)
        # tiek veikta vislielākā pieaguma (starpības) atjaunināšana, izmantojot iebūvēto max funkciju,
        # kura izvēlās maksimālo vērtību starp pašlaik definēto maksimālo pieagumu (starpību) un starpības rezultātu starp
        # izvēlēto skaitli no virknes (saraksta) un minimālās vērtības.
        max_diff = max(max_diff, num - min_value)
    return max_diff #beigās funkcija atgriež vislielāko atrastu pieagumu (starpību)

# Šeit ir dota funkcija, kura nolasa skaitļus no faila un atgriež tos kā skaitļu sarakstu
def read_sequence(filename): # funkcijas definīcija, kura izmanto iepriekš definēto failu, kā ieejas datus
    with open(filename, 'r') as file: # Atver failu tikai lasīšanai, izmantojot 'r'
        sequence = [int(line.strip()) for line in file if line.strip().isdigit()] # Nolasa katra faila rindu, pārveido to par skaitli un aizpilda to sarakstā, ja rindā ir tikai cipari.
    return sequence # beigās funkcija atgriež aizpildīto skaitļu sarakstu

# Tiek veikta faila definēšana, norādot ceļu uz failu.
# Tad ar funkcijas read_sequence palīdzību saraksts "sequence" tiek aizpildīts ar skaitļiem no faila.
filename = "C:\\Users\\Oskars\\Desktop\\Test\\ints_10.txt"
sequence = read_sequence(filename)

# Printē funkcijas "max_difference" atrasto rezultātu (vislielāko pieagumu).
# Funkcijai max_difference tiek padots saraksts "sequence"
print(max_difference(sequence))

