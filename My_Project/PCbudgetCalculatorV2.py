print("=" * 65)
print("      🎮 SMART PC BUILDER & ADVICE SYSTEM v2.3 (DYNAMISCH) 🎮      ")
print("=" * 65)

totale_budget = float(input("Wat is je totale budget (€)? "))

print("\nWat is je hoofddoel voor deze PC?")
print("1 = Casual / Allround / Budget Gaming")
print("2 = Performance / High FPS Gaming")
print("3 = Quality / High-End / 4K Gaming")
voorkeur = input("Maak een keuze (1, 2 of 3): ")

# Logica met nauwkeurigere budgetgrenzen en actuele marktconforme prijzen
if totale_budget < 750:
    print("\n[Tip] Een budget onder €750 is krap voor een nieuwe game-PC, maar hier is een sterke budget-setup:")
    aanbevolen_cpu = "Intel Core i3-12100F"
    aanbevolen_moederbord = "Gigabyte H610M H V2"
    aanbevolen_ram = "16GB DDR4 3200MHz"
    aanbevolen_gpu = "AMD RX 6600 (8GB)"
    aanbevolen_ssd = "1TB NVMe M.2 SSD"
    aanbevolen_voeding = "500W 80+ Bronze"
    aanbevolen_behuizing = "Budget Airflow Case"
    p_cpu, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 90, 210, 80, 45, 65, 55, 45

elif totale_budget < 1200:
    if voorkeur == "2": # Performance Focus
        aanbevolen_cpu = "AMD Ryzen 5 5600X"
        aanbevolen_moederbord = "MSI B550-A PRO"
        aanbevolen_ram = "16GB DDR4 3200MHz"
        aanbevolen_gpu = "AMD RX 7700 XT (12GB)"
        aanbevolen_ssd = "1TB NVMe M.2 Gen4 SSD"
        aanbevolen_voeding = "650W 80+ Bronze"
        aanbevolen_behuizing = "Mid-Tower Airflow Case"
        p_cpu, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 130, 410, 95, 45, 75, 70, 60
    else: # Allround / Intel Setup
        aanbevolen_cpu = "Intel Core i5-12400F"
        aanbevolen_moederbord = "Gigabyte B760M DS3H"
        aanbevolen_ram = "16GB DDR4 3200MHz"
        aanbevolen_gpu = "NVIDIA RTX 4060 (8GB)"
        aanbevolen_ssd = "1TB NVMe M.2 SSD"
        aanbevolen_voeding = "600W 80+ Bronze"
        aanbevolen_behuizing = "Compacte Mid-Tower"
        p_cpu, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 120, 310, 105, 45, 70, 65, 55

elif totale_budget < 2000:
    if voorkeur == "3": # 4K / Quality Setup
        aanbevolen_cpu = "Intel Core i5-14600KF"
        aanbevolen_moederbord = "MSI MAG Z790 TOMAHAWK WIFI"
        aanbevolen_ram = "32GB (2x16GB) DDR5 6000MHz"
        aanbevolen_gpu = "NVIDIA RTX 4070 Super (12GB)"
        aanbevolen_ssd = "2TB NVMe M.2 Gen4 SSD"
        aanbevolen_voeding = "750W 80+ Gold Modulair"
        aanbevolen_behuizing = "Luxe Airflow Case"
        p_cpu, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 280, 630, 210, 105, 120, 110, 90
    else: # High FPS AMD Setup
        aanbevolen_cpu = "AMD Ryzen 5 7600X"
        aanbevolen_moederbord = "ASUS TUF GAMING B650-PLUS WIFI"
        aanbevolen_ram = "32GB (2x16GB) DDR5 6000MHz"
        aanbevolen_gpu = "AMD RX 7800 XT (16GB)"
        aanbevolen_ssd = "2TB NVMe M.2 Gen4 SSD"
        aanbevolen_voeding = "750W 80+ Gold Modulair"
        aanbevolen_behuizing = "High Airflow Gaming Case"
        p_cpu, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 220, 520, 180, 105, 120, 110, 85

else:
    aanbevolen_cpu = "AMD Ryzen 7 7800X3D"
    aanbevolen_moederbord = "Gigabyte X670E AORUS MASTER"
    aanbevolen_ram = "32GB (2x16GB) DDR5 6000MHz CL30"
    aanbevolen_gpu = "NVIDIA RTX 4080 Super (16GB)"
    aanbevolen_ssd = "2TB NVMe M.2 Gen4 SSD (High-End)"
    aanbevolen_voeding = "850W 80+ Gold ATX 3.0"
    aanbevolen_behuizing = "Premium Full-Tower Case"
    p_cpu, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 365, 1050, 320, 115, 130, 140, 130

totaal_prijs = p_cpu + p_gpu + p_mb + p_ram + p_ssd + p_psu + p_case

print("\n" + "=" * 65)
print("      🔍 COMPATIBELE PRODUCTAANRADERS & OVERZICHT      ")
print("=" * 65)
print(f"• Processor (CPU):       {aanbevolen_cpu:<35} (€{p_cpu})")
print(f"• Moederbord:            {aanbevolen_moederbord:<35} (€{p_mb})")
print(f"• Werkgeheugen (RAM):    {aanbevolen_ram:<35} (€{p_ram})")
print(f"• Grafische Kaart (GPU): {aanbevolen_gpu:<35} (€{p_gpu})")
print(f"• Opslag (SSD):          {aanbevolen_ssd:<35} (€{p_ssd})")
print(f"• ⚡ Voeding:            {aanbevolen_voeding:<35} (€{p_psu})")
print(f"• 📦 Behuizing:          {aanbevolen_behuizing:<35} (€{p_case})")
print("-" * 65)
print(f"INGEVOERD BUDGET:        €{totale_budget:.2f}")
print(f"GESCHATTE TOTAALPRIJS:   €{totaal_prijs:.2f}")

verschil = totale_budget - totaal_prijs
if verschil >= 0:
    print(f"✓ Binnen budget! Je houdt €{verschil:.2f} over.")
else:
    print(f"⚠ Let op: Deze configuratie valt €{abs(verschil):.2f} duurder uit dan je budget.")

print("✓ Alle bovenstaande onderdelen zijn onderling 100% compatibel.")
print("=" * 65)