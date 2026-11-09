import os

print("=" * 65)
print("     🎮 SMART PC BUILDER & ADVICE SYSTEM v3.0 (COMPATIBEL) 🎮     ")
print("=" * 65)

# 1. ROBUUSTE BUDGET INVOER (met foutafhandeling)
while True:
    try:
        totale_budget = float(input("Wat is je totale budget (€)? "))
        if totale_budget < 400:
            print("Met een budget onder €400 is het erg lastig om een nieuwe gaming PC samen te stellen. Probeer minstens €500.")
            continue
        break
    except ValueError:
        print("❌ Ongeldige invoer! Voer een geldig getal in (bijv. 850 of 1200.50).")

# 2. GEBRUIKERSVOORKEUR INVOER
print("\nWat is je hoofddoel voor deze PC?")
print("1 = Casual / Allround")
print("2 = Performance / High FPS")
print("3 = Quality / 4K Graphics")

while True:
    voorkeur = input("Maak een keuze (1, 2 of 3): ").strip()
    if voorkeur in ["1", "2", "3"]:
        break
    print("❌ Ongeldige keuze! Typ '1', '2' of '3'.")

# 3. LOGICA VOOR HARDWARE-SETS EN KOELERS
if totale_budget < 1000:
    budget_groep = "Onder €1000"
    if voorkeur == "2": # Performance Focus (AM4 Platform)
        aanbevolen_cpu = "AMD Ryzen 5 5600X"
        aanbevolen_koeler = "Thermalright Assassin X 120 Refined"
        aanbevolen_moederbord = "MSI B550-A PRO (AM4 Socket)"
        aanbevolen_ram = "16GB DDR4 3200MHz CL16"
        aanbevolen_gpu = "AMD RX 6700 XT (12GB)"
        aanbevolen_voeding = "650W 80+ Bronze Voeding"
        aanbevolen_behuizing = "Mid-Tower Airflow Case"
        p_cpu, p_koeler, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 135, 20, 310, 95, 45, 75, 70, 60
    else: # Intel LGA1700 Platform
        aanbevolen_cpu = "Intel Core i3-12100F"
        aanbevolen_koeler = "Stock CPU Koeler (Meegeleverd)"
        aanbevolen_moederbord = "Gigabyte B760M DS3H DDR4 (LGA1700)"
        aanbevolen_ram = "16GB DDR4 3200MHz CL16"
        aanbevolen_gpu = "AMD RX 6600 (8GB)"
        aanbevolen_voeding = "550W 80+ Bronze Voeding"
        aanbevolen_behuizing = "Compacte Mid-Tower"
        p_cpu, p_koeler, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 100, 0, 230, 95, 45, 75, 60, 55

elif totale_budget <= 2000:
    budget_groep = "€1000 - €2000"
    if voorkeur == "3": # Intel + Nvidia 4K Setup
        aanbevolen_cpu = "Intel Core i5-14600KF"
        aanbevolen_koeler = "Thermalright Peerless Assassin 120 SE"
        aanbevolen_moederbord = "MSI MAG Z790 TOMAHAWK WIFI DDR5"
        aanbevolen_ram = "32GB (2x16GB) DDR5 6000MHz CL30"
        aanbevolen_gpu = "NVIDIA RTX 4070 Ti Super (16GB)"
        aanbevolen_voeding = "750W 80+ Gold Modulair"
        aanbevolen_behuizing = "Luxe Airflow Case"
        p_cpu, p_koeler, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 300, 40, 845, 210, 115, 120, 110, 95
    else: # AMD AM5 Gaming Setup
        aanbevolen_cpu = "AMD Ryzen 7 7800X3D"
        aanbevolen_koeler = "Thermalright Peerless Assassin 120 SE"
        aanbevolen_moederbord = "ASUS TUF GAMING B650-PLUS WIFI (AM5)"
        aanbevolen_ram = "32GB (2x16GB) DDR5 6000MHz CL30"
        aanbevolen_gpu = "NVIDIA RTX 4070 Super (12GB)"
        aanbevolen_voeding = "750W 80+ Gold Modulair"
        aanbevolen_behuizing = "High Airflow Gaming Case"
        p_cpu, p_koeler, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 365, 40, 640, 180, 115, 120, 110, 90

else:
    budget_groep = "€2000+"
    aanbevolen_cpu = "AMD Ryzen 7 7800X3D"
    aanbevolen_koeler = "DeepCool LS720 360mm AIO Waterkoeling"
    aanbevolen_moederbord = "Gigabyte X670E AORUS MASTER (AM5)"
    aanbevolen_ram = "32GB (2x16GB) DDR5 6000MHz CL30"
    aanbevolen_gpu = "NVIDIA RTX 4080 Super (16GB)"
    aanbevolen_voeding = "850W 80+ Gold ATX 3.0"
    aanbevolen_behuizing = "Premium Full-Tower Case"
    p_cpu, p_koeler, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 365, 130, 1070, 320, 125, 160, 150, 140

aanbevolen_ssd = "1TB / 2TB NVMe M.2 SSD (Gen4)"
totaal_prijs = p_cpu + p_koeler + p_gpu + p_mb + p_ram + p_ssd + p_psu + p_case

# 4. OVERZICHT AFDRUKKEN
print("\n" + "=" * 65)
print("     🔍 COMPATIBELE PRODUCTAANRADERS & OVERZICHT     ")
print("=" * 65)
print(f"• Processor (CPU):       {aanbevolen_cpu:<35} (€{p_cpu})")
print(f"• CPU Koeling:           {aanbevolen_koeler:<35} (€{p_koeler})")
print(f"• Moederbord:            {aanbevolen_moederbord:<35} (€{p_mb})")
print(f"• Werkgeheugen (RAM):    {aanbevolen_ram:<35} (€{p_ram})")
print(f"• Grafische Kaart (GPU): {aanbevolen_gpu:<35} (€{p_gpu})")
print(f"• Opslag (SSD):          {aanbevolen_ssd:<35} (€{p_ssd})")
print(f"• ⚡ Voeding:            {aanbevolen_voeding:<35} (€{p_psu})")
print(f"• 📦 Behuizing:          {aanbevolen_behuizing:<35} (€{p_case})")
print("-" * 65)
print(f"GESCHATTE TOTAALPRIJS:   €{totaal_prijs:.2f}")

# 5. BUDGETWAARSCHUWING / CONTEXT
if totaal_prijs > totale_budget:
    print(f"⚠️ Let op: Deze build valt €{totaal_prijs - totale_budget:.2f} boven je opgegeven budget van €{totale_budget:.2f}.")
else:
    print(f"🎉 Mooi! Je houdt nog €{totale_budget - totaal_prijs:.2f} over van je budget van €{totale_budget:.2f}.")

print("✓ Alle bovenstaande onderdelen zijn onderling 100% compatibel.")
print("=" * 65)

# 6. OPTIE OM HET BUILD-OVERZICHT OPSLAAN ALS TEKSTBESTAND
opslaan = input("\nWil je dit advies opslaan in een tekstbestand? (ja/nee): ").strip().lower()

if opslaan in ["ja", "j", "yes", "y"]:
    bestandsnaam = "pc_build_advies.txt"
    with open(bestandsnaam, "w", encoding="utf-8") as f:
        f.write("=" * 65 + "\n")
        f.write("     🎮 SMART PC BUILDER & ADVICE SYSTEM v3.0 - OVERZICHT 🎮     \n")
        f.write("=" * 65 + "\n\n")
        f.write(f"Ingevoerd budget: €{totale_budget:.2f}\n")
        f.write(f"Budget categorie: {budget_groep}\n\n")
        f.write("AANBEVOLEN HARDWARE:\n")
        f.write(f"- Processor (CPU):       {aanbevolen_cpu} (€{p_cpu})\n")
        f.write(f"- CPU Koeling:           {aanbevolen_koeler} (€{p_koeler})\n")
        f.write(f"- Moederbord:            {aanbevolen_moederbord} (€{p_mb})\n")
        f.write(f"- Werkgeheugen (RAM):    {aanbevolen_ram} (€{p_ram})\n")
        f.write(f"- Grafische Kaart (GPU): {aanbevolen_gpu} (€{p_gpu})\n")
        f.write(f"- Opslag (SSD):          {aanbevolen_ssd} (€{p_ssd})\n")
        f.write(f"- Voeding:               {aanbevolen_voeding} (€{p_psu})\n")
        f.write(f"- Behuizing:             {aanbevolen_behuizing} (€{p_case})\n")
        f.write("-" * 65 + "\n")
        f.write(f"TOTAALPRIJS:             €{totaal_prijs:.2f}\n")
        if totaal_prijs > totale_budget:
            f.write(f"Status: €{totaal_prijs - totale_budget:.2f} boven budget\n")
        else:
            f.write(f"Status: €{totale_budget - totaal_prijs:.2f} over van budget\n")
        f.write("✓ Alle onderdelen zijn 100% compatibel.\n")
    
    print(f"📁 Gelukt! Je overzicht is opgeslagen als '{bestandsnaam}'.")
else:
    print("Bedankt voor het gebruiken van de Smart PC Builder! Succes met bouwen!")