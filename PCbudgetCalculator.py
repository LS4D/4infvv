print("=" * 65)
print("     🎮 SMART PC BUILDER & ADVICE SYSTEM v2.2 (COMPATIBEL) 🎮     ")
print("=" * 65)

totale_budget = float(input("Wat is je totale budget (€)? "))

print("\nWat is je hoofddoel voor deze PC?")
print("1 = Casual / Allround")
print("2 = Performance / High FPS")
print("3 = Quality / 4K Graphics")
voorkeur = input("Maak een keuze (1, 2 of 3): ")

# Logica voor compatibele hardware-sets
if totale_budget < 1000:
    budget_groep = "Onder €1000"
    if voorkeur == "2": # Performance Focus (AM4 Platform)
        aanbevolen_cpu = "AMD Ryzen 5 5600X"
        aanbevolen_moederbord = "MSI B550-A PRO (AM4 Socket)"
        aanbevolen_ram = "16GB DDR4 3200MHz CL16"
        aanbevolen_gpu = "AMD RX 6700 XT (12GB)"
        aanbevolen_voeding = "650W 80+ Bronze Voeding"
        aanbevolen_behuizing = "Mid-Tower Airflow Case"
        p_cpu, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 135, 310, 95, 45, 75, 70, 60
    else: # Intel LGA1700 Platform
        aanbevolen_cpu = "Intel Core i3-12100F"
        aanbevolen_moederbord = "Gigabyte B760M DS3H DDR4 (LGA1700)"
        aanbevolen_ram = "16GB DDR4 3200MHz CL16"
        aanbevolen_gpu = "AMD RX 6600 (8GB)"
        aanbevolen_voeding = "550W 80+ Bronze Voeding"
        aanbevolen_behuizing = "Compacte Mid-Tower"
        p_cpu, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 100, 230, 95, 45, 75, 60, 55

elif totale_budget <= 2000:
    budget_groep = "€1000 - €2000"
    if voorkeur == "3": # Intel + Nvidia 4K Setup
        aanbevolen_cpu = "Intel Core i5-14600KF"
        aanbevolen_moederbord = "MSI MAG Z790 TOMAHAWK WIFI DDR5"
        aanbevolen_ram = "32GB (2x16GB) DDR5 6000MHz CL30"
        aanbevolen_gpu = "NVIDIA RTX 4070 Ti Super (16GB)"
        aanbevolen_voeding = "750W 80+ Gold Modulair"
        aanbevolen_behuizing = "Luxe Airflow Case"
        p_cpu, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 300, 845, 210, 115, 120, 110, 95
    else: # AMD AM5 Gaming Setup
        aanbevolen_cpu = "AMD Ryzen 7 7800X3D"
        aanbevolen_moederbord = "ASUS TUF GAMING B650-PLUS WIFI (AM5)"
        aanbevolen_ram = "32GB (2x16GB) DDR5 6000MHz CL30"
        aanbevolen_gpu = "NVIDIA RTX 4070 Super (12GB)"
        aanbevolen_voeding = "750W 80+ Gold Modulair"
        aanbevolen_behuizing = "High Airflow Gaming Case"
        p_cpu, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 365, 640, 180, 115, 120, 110, 90

else:
    budget_groep = "€2000+"
    aanbevolen_cpu = "AMD Ryzen 7 7800X3D"
    aanbevolen_moederbord = "Gigabyte X670E AORUS MASTER (AM5)"
    aanbevolen_ram = "32GB (2x16GB) DDR5 6000MHz CL30"
    aanbevolen_gpu = "NVIDIA RTX 4080 Super (16GB)"
    aanbevolen_voeding = "850W 80+ Gold ATX 3.0"
    aanbevolen_behuizing = "Premium Full-Tower Case"
    p_cpu, p_gpu, p_mb, p_ram, p_ssd, p_psu, p_case = 365, 1070, 320, 125, 160, 150, 140

aanbevolen_ssd = "1TB / 2TB NVMe M.2 SSD (Gen4)"
totaal_prijs = p_cpu + p_gpu + p_mb + p_ram + p_ssd + p_psu + p_case

print("\n" + "=" * 65)
print("     🔍 COMPATIBELE PRODUCTAANRADERS & OVERZICHT     ")
print("=" * 65)
print(f"• Processor (CPU):       {aanbevolen_cpu:<35} (€{p_cpu})")
print(f"• Moederbord:            {aanbevolen_moederbord:<35} (€{p_mb})")
print(f"• Werkgeheugen (RAM):    {aanbevolen_ram:<35} (€{p_ram})")
print(f"• Grafische Kaart (GPU): {aanbevolen_gpu:<35} (€{p_gpu})")
print(f"• Opslag (SSD):          {aanbevolen_ssd:<35} (€{p_ssd})")
print(f"• ⚡ Voeding:            {aanbevolen_voeding:<35} (€{p_psu})")
print(f"• 📦 Behuizing:          {aanbevolen_behuizing:<35} (€{p_case})")
print("-" * 65)
print(f"GESCHATTE TOTAALPRIJS:   €{totaal_prijs:.2f}")
print("✓ Alle bovenstaande onderdelen zijn onderling 100% compatibel.")
print("=" * 65)