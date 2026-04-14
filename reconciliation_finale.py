#!/usr/bin/env python3
"""
RÉCONCILIATION FINALE : T2 2025 vs DÉCLARATIONS TPS/TVQ SOUMISES
Exercice fiscal : 1er janvier au 31 décembre 2025
"""

print("=" * 70)
print("RÉCONCILIATION T2 2025 vs DÉCLARATIONS TPS/TVQ")
print("=" * 70)

# =============================================
# 1. DÉCLARATIONS TPS/TVQ DÉJÀ SOUMISES
# =============================================
# Les déclarations TPS/TVQ sont trimestrielles (avr-mars)
# Donc pour l'exercice jan-déc 2025, on a :
# - T1: Avr-Juin 2025
# - T2: Juil-Sept 2025
# - T3: Oct-Déc 2025
# (T4 Jan-Mars 2026 = exercice 2026)

print("\n1. DÉCLARATIONS TPS/TVQ SOUMISES (avr-déc 2025 seulement)")
print("-" * 70)

# TPS soumises
tps_t1 = 172
tps_t2 = 3675
tps_t3 = -353
tps_total_soumis = tps_t1 + tps_t2 + tps_t3

# TVQ soumises
tvq_t1 = 342
tvq_t2 = 7332
tvq_t3 = -704
tvq_total_soumis = tvq_t1 + tvq_t2 + tvq_t3

print(f"{'Trimestre':<25s} {'TPS':>10s} {'TVQ':>10s} {'Total':>10s}")
print(f"{'T1 (Avr-Juin 2025)':<25s} {tps_t1:>10,d} $ {tvq_t1:>10,d} $ {tps_t1+tvq_t1:>10,d} $")
print(f"{'T2 (Juil-Sept 2025)':<25s} {tps_t2:>10,d} $ {tvq_t2:>10,d} $ {tps_t2+tvq_t2:>10,d} $")
print(f"{'T3 (Oct-Déc 2025)':<25s} {tps_t3:>10,d} $ {tvq_t3:>10,d} $ {tps_t3+tvq_t3:>10,d} $")
print(f"{'TOTAL SOUMIS (2025)':<25s} {tps_total_soumis:>10,d} $ {tvq_total_soumis:>10,d} $ {tps_total_soumis+tvq_total_soumis:>10,d} $")

# =============================================
# 2. REVENUS T2 vs REVENUS TPS/TVQ
# =============================================
print("\n\n2. COHÉRENCE REVENUS")
print("-" * 70)

# Revenus T2 (jan-déc 2025)
rev_qb_ht = 379982.14
rev_fl_ht = 80453.58
creance_ht = 81735.00
rev_nets_ht = rev_qb_ht + rev_fl_ht - creance_ht

# TPS perçue sur revenus = revenus HT x 5%
tps_percue_t2 = rev_nets_ht * 0.05
# TVQ perçue sur revenus = revenus HT x 9.975%
tvq_percue_t2 = rev_nets_ht * 0.09975

print(f"Revenus nets HT (T2):                {rev_nets_ht:>12,.2f} $")
print(f"TPS qui devrait être perçue (5%):     {tps_percue_t2:>12,.2f} $")
print(f"TVQ qui devrait être perçue (9.975%): {tvq_percue_t2:>12,.2f} $")

# Mais les déclarations TPS/TVQ couvrent avr-mars, pas jan-déc
# Pour jan-déc 2025, on a T1+T2+T3 (avr-déc 2025) 
# Il n'y a PAS de revenus en jan-mars 2025 (inactive)
# Donc les revenus avr-déc 2025 = les mêmes que jan-déc 2025

print(f"\nNote: L'entreprise était inactive jan-mars 2025")
print(f"Donc revenus avr-déc 2025 = revenus jan-déc 2025 = {rev_nets_ht:,.2f} $ HT")

# =============================================
# 3. DÉPENSES T2 vs CTI/RTI
# =============================================
print("\n\n3. COHÉRENCE DÉPENSES / CTI-RTI")
print("-" * 70)

# Dépenses T2 avec taxes récupérables
dep_fournisseurs_ht = 77320.50  # virements Interac
dep_creditbail_ht = 62106.21    # 9 mois
dep_assurances = 17450.25       # pas de taxes sur assurances
dep_essence_ht = 15469.50       # 80% déductible
dep_materiaux_ht = 16360.50
dep_achats_ht = 7849.50
dep_cnesst = 5605.00            # pas de taxes
dep_telecom_ht = 1500.00
dep_repas = 994.50              # 50% déductible, taxes récupérables
dep_frais_bank = 978.75         # pas de taxes
dep_cotisations = 670.00        # pas de taxes
dep_interets = 154.50           # pas de taxes
dep_soustraitants = 5250.00     # pas de taxes (particuliers)
dep_dome = 2600.00              # pas de taxes (particulier)
dep_bureau = 7056.00            # pas de taxes directes
dep_dpa = 5100.00               # pas de taxes

# CTI/RTI récupérables (dépenses avec taxes)
dep_avec_taxes = dep_fournisseurs_ht + dep_creditbail_ht + dep_essence_ht + dep_materiaux_ht + dep_achats_ht + dep_telecom_ht + dep_repas
cti_calcule = dep_avec_taxes * 0.05
rti_calcule = dep_avec_taxes * 0.09975

print(f"Dépenses avec taxes récupérables:")
print(f"  Fournisseurs (Interac):     {dep_fournisseurs_ht:>12,.2f} $")
print(f"  Crédit-bail (9 mois):       {dep_creditbail_ht:>12,.2f} $")
print(f"  Essence (80%):              {dep_essence_ht:>12,.2f} $")
print(f"  Matériaux divers:           {dep_materiaux_ht:>12,.2f} $")
print(f"  Achats divers:              {dep_achats_ht:>12,.2f} $")
print(f"  Télécom:                    {dep_telecom_ht:>12,.2f} $")
print(f"  Repas (50%):                {dep_repas:>12,.2f} $")
print(f"  TOTAL avec taxes:           {dep_avec_taxes:>12,.2f} $")
print(f"\n  CTI calculé (5%):           {cti_calcule:>12,.2f} $")
print(f"  RTI calculé (9.975%):       {rti_calcule:>12,.2f} $")

print(f"\nDépenses SANS taxes:")
print(f"  Assurances:                 {dep_assurances:>12,.2f} $")
print(f"  CNESST:                     {dep_cnesst:>12,.2f} $")
print(f"  Sous-traitants:             {dep_soustraitants:>12,.2f} $")
print(f"  Dôme (particulier):         {dep_dome:>12,.2f} $")
print(f"  Bureau domicile:            {dep_bureau:>12,.2f} $")
print(f"  Frais bancaires:            {dep_frais_bank:>12,.2f} $")
print(f"  Cotisations:                {dep_cotisations:>12,.2f} $")
print(f"  Intérêts:                   {dep_interets:>12,.2f} $")
print(f"  DPA:                        {dep_dpa:>12,.2f} $")

# =============================================
# 4. VÉRIFICATION COHÉRENCE TPS/TVQ
# =============================================
print("\n\n4. VÉRIFICATION COHÉRENCE")
print("-" * 70)

# TPS nette = TPS perçue - CTI
tps_nette_calculee = tps_percue_t2 - cti_calcule
tvq_nette_calculee = tvq_percue_t2 - rti_calcule

print(f"TPS perçue (sur revenus):     {tps_percue_t2:>12,.2f} $")
print(f"CTI (sur dépenses):          -{cti_calcule:>12,.2f} $")
print(f"TPS nette calculée:           {tps_nette_calculee:>12,.2f} $")
print(f"TPS nette soumise:            {tps_total_soumis:>12,d} $")
print(f"ÉCART TPS:                    {tps_nette_calculee - tps_total_soumis:>12,.2f} $")

print()
print(f"TVQ perçue (sur revenus):     {tvq_percue_t2:>12,.2f} $")
print(f"RTI (sur dépenses):          -{rti_calcule:>12,.2f} $")
print(f"TVQ nette calculée:           {tvq_nette_calculee:>12,.2f} $")
print(f"TVQ nette soumise:            {tvq_total_soumis:>12,d} $")
print(f"ÉCART TVQ:                    {tvq_nette_calculee - tvq_total_soumis:>12,.2f} $")

print("\n\n5. RÉCAPITULATIF FINAL T2 2025")
print("=" * 70)
total_dep = (dep_fournisseurs_ht + dep_creditbail_ht + dep_assurances + dep_essence_ht + 
             dep_materiaux_ht + dep_achats_ht + dep_cnesst + dep_telecom_ht + dep_repas +
             dep_frais_bank + dep_cotisations + dep_interets + dep_soustraitants + dep_dome +
             dep_bureau + dep_dpa)

benefice = rev_nets_ht - total_dep
impot = benefice * 0.122

print(f"Revenus nets HT:              {rev_nets_ht:>12,.2f} $")
print(f"Dépenses totales HT:         -{total_dep:>12,.2f} $")
print(f"BÉNÉFICE NET:                 {benefice:>12,.2f} $")
print(f"Impôt corporatif (12.2%):     {impot:>12,.2f} $")
print(f"Dividendes versés:            {45000:>12,d} $")
print(f"Bénéfices non répartis:       {benefice - impot - 45000:>12,.2f} $")

print("\n\n6. COMPTE DE L'ACTIONNAIRE")
print("=" * 70)
print(f"Retraits personnels 2025:     {82760:>12,d} $")
print(f"Dividendes déclarés:         -{45000:>12,d} $")
print(f"Prêt actionnaire (à rembourser): {82760-45000:>12,d} $")
print(f"Loyer payé perso (3 mois):   -{3*2100:>12,d} $")
print(f"Solde net dû par actionnaire: {82760-45000-3*2100:>12,d} $")
