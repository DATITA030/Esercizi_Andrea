#che frutta vuoi?
#lupo chiede una frutta
#gestione errore se non c'è la frutta o chiede altro
#
class Nonfrutta(Exception):
    pass

frutti=["mela","pera","albicocca", "banana","pompelmo","anguria"]
print("Toc Toc sono il lupo Vegano... per caso avete della frutta?")
try:
    frut_richiesto=input("Aiuto il lupo Vegano!Che frutta vuoi?").lower()
    if frut_richiesto in frutti:
        print("Mannaggia c'è! Parte la corsa alla frutta... corri corri")
    else:
        raise Nonfrutta ("Questo lupo viziatone non la considera frutta")
except Nonfrutta as ex:
    print(ex)




