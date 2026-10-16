aantal_taakjes = int(input("Hoeveel taakjes heb je gedaan? "))
aantal_boetes = int(input("Hoeveel keer heb je de tafel niet afgeruimd? "))
zakgeld = 5 + (aantal_taakjes * 2) - (aantal_boetes * 1)

print(f"Lio krijgt {zakgeld} euro zakgeld deze week")