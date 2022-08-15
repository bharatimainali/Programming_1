
# samlet velger number og leg inn i input "hva er meningen med livet" int.

tall_velger = int(input("Hva er meningen med livet? "))

# hvis tall er 42, skriv "Det stemmer", ellers, hvis tall er mellom 30 og 50, skriv "nærme", ellers, skriv "feil"

if tall_velger == 42:
    print("Det stemmer, meningen med livet er 42")
elif (tall_velger > 30) & (tall_velger < 50):
    print("Nærme,men feil")
else:
    print("feil")
