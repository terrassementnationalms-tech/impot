# JOURNAL DE BORD — Déclaration d'impôt T2 2025
## Terrassement National MS Inc. (NE: à confirmer)
## Exercice : 1er janvier 2025 au 31 décembre 2025

---

## SESSION 1 à 9 (avant le 14 avril 2026)
### Résumé des travaux antérieurs

- Analyse des 3 fichiers Excel : relevé bancaire Plan B Desjardins, QuickBooks (factures), Flokon (déneigement)
- Démêlage complet des virements Interac 2025 (fournisseurs vs personnel)
- Identification des revenus : 79 factures QB + 287 paiements Flokon
- Identification de la créance Bellefeuille (2 factures impayées = 81 734 $ HT)
- Rapports de taxes TPS/TVQ soumis pour 4 trimestres (avr 2025 à mars 2026)
- Plusieurs versions du tableau fiscal produites (V1, V2, corrections multiples)
- Problème récurrent : incohérences entre versions, recommencements à chaque session

---

## SESSION 10 — 14 avril 2026 (soir)

### Décisions prises :
1. **Carburant = 100% entreprise** (pas 80%). Le gaz personnel est payé en cash.
2. **Reclassement des fournisseurs Interac** — chaque fournisseur dans la bonne catégorie :
   - Pavé Select, Richer, Savaria, Lebeau = matériaux
   - Pavage St-Foy, Apollon, Gouttières Boivin = sous-traitance
   - JCM = location loader
   - Pascal Équipement = location outils
   - Sanfaçon = achat camion (pas sous-traitance!)
   - Flokon = logiciel
   - Pixel = linge de compagnie (publicité)
   - Noéma = tasses de compagnie (publicité)
   - BLG, Beneti = transport
   - Remorquage = dépannage véhicule
3. **Facture Sanfaçon #1314** = achat camion International 5600 2003 (12 roues dompeur), 32 500 $ HT
   - Payé 5 000 $ par la compagnie (Interac)
   - Reste payé de la poche de l'actionnaire → avance actionnaire 32 367 $
4. **3 autres factures Sanfaçon** trouvées dans Gmail :
   - #1378 (624 $ TTC) = transport camion semi, projet Alyssés
   - #1387 (1 304 $ TTC) = transport camion semi, projet Calicot
   - #1450 (259 $ TTC) = location pelle 1,7 tonne
5. **Dividendes** portés à 53 837 $ pour ramener le compte actionnaire à 0 $
6. **Rappel CTI/RTI** : ~854 $ de crédits de taxes manquants à récupérer sur la prochaine déclaration TPS/TVQ

### Tableau sauvegardé et pushé dans GitHub

---

## SESSION 11 — 15 avril 2026 (matin)

### Corrections importantes :
1. **Codes GIFI corrigés** — les vrais noms dans ImpôtExpert :
   - 9180 = Taxes foncières (PAS location!) → location va dans **8910**
   - 9224 = Frais de carburant (séparé du 9281 véhicules)
   - 9200 = Frais de déplacement → **EFFACÉ** (c'était un doublon des sous-traitants)

2. **Champs à EFFACER** (erreurs des sessions passées) :
   - 8860 Honoraires professionnels = 670 $ → **EFFACER** (payé en 2026, pas 2025)
   - 8861 Frais légaux = 155 $ → **EFFACER** (payé en 2026, pas 2025)
   - 9200 Frais de déplacement = 5 250 $ → **EFFACER** (doublon sous-traitance)

3. **Comptabilité de caisse confirmée** — on compte les paiements reçus/faits en 2025, pas les factures
   - Ladouceur avocat (5 000 $) = payé en 2026 → dépense 2026, PAS 2025
   - Noël & Gauron (600 $) = facturée mars 2026 → dépense 2026, PAS 2025

4. **Créance Bellefeuille** = mise dans 8590 (Créances irrécouvrables) même si c'est en litige
   - Si Bellefeuille paie un jour, ça sera un revenu cette année-là
   - Garder les preuves du litige

5. **Transport vs sous-traitance** — BLG/Beneti/Sanfaçon camion semi restent dans sous-traitance (ça change rien au total)

### DPA (Déduction pour amortissement) — Classe 10, 30% :

| Actif | Coût HT | Date acquisition | Date prêt | DPA 2025 |
|-------|--------:|:----------------:|:---------:|---------:|
| Pelle Kubota U-35 2016 | 34 000 $ | 29-04-2025 | 29-04-2025 | 5 100 $ |
| Camion Int. 5600 12 roues 2003 | 32 500 $ | 28-04-2025 | 28-04-2025 | 4 875 $ |
| **Total** | **66 500 $** | | | **9 975 $** |

- La pelle n'était pas finie de payer → pas grave, DPA sur le coût total
- Le camion payé de la poche de l'actionnaire → pas grave, DPA sur le coût total
- DPA au demi-taux = Oui (première année)

### Rapports de taxes vs T2 :
- Les rapports de taxes (avr 2025 à mars 2026) sont corrects dans l'ensemble
- ~854 $ de CTI/RTI manquants à cause des corrections (carburant 100%, 3 factures Sanfaçon)
- **À FAIRE** : récupérer ces CTI/RTI sur la prochaine déclaration trimestrielle (avr-jun 2026)

### Dividendes :
- Montant : **53 837 $** (dividendes ordinaires, non déterminés)
- Date : 31-12-2025
- Feuillets à produire : T5 + Relevé 3

---

## CHIFFRES DÉFINITIFS T2 2025

### État des résultats — 16 lignes à entrer :

| Code GIFI | Nom dans ImpôtExpert | Montant |
|:---------:|----------------------|--------:|
| 8000 | Ventes commerciales | 460 424 |
| 8320 | Achats / coût des matériaux | 74 483 |
| 8523 | Repas et frais de représentation | 1 406 |
| 8590 | Créances irrécouvrables | 81 734 |
| 8670 | Amortissement des immobilisations corporelles | 9 975 |
| 8690 | Assurance | 14 135 |
| 8710 | Intérêts et frais bancaires | 19 169 |
| 8811 | Papeterie et fournitures de bureau | 3 059 |
| 8910 | Frais de location | 9 873 |
| 8911 | Loyer | 7 056 |
| 9110 | Sous-traitance | 23 393 |
| 9224 | Frais de carburant | 18 975 |
| 9225 | Téléphone et télécommunications | 5 792 |
| 9270 | Autres dépenses | 3 494 |
| 9275 | Livraison, transport et entreposage | 3 622 |
| 9281 | Frais de véhicules à moteur | 49 038 |

### Champs à EFFACER :
| Code | Ancien montant | Raison |
|:----:|---------------:|--------|
| 8860 | 670 $ | Payé en 2026 |
| 8861 | 155 $ | Payé en 2026 |
| 9200 | 5 250 $ | Doublon sous-traitance |

### Résultat :
- Revenus bruts HT : 460 424 $
- Total dépenses (avec créance) : 325 204 $
- **Bénéfice avant impôt : 135 220 $**
- Impôt fédéral (9% PME) : ~12 170 $
- Impôt Québec (3.2% PME) : ~4 327 $
- **Impôt total : ~16 497 $**
- **Bénéfice après impôt : ~118 723 $**

---

## CE QUI RESTE À FAIRE

- [ ] Finir de remplir la DPA dans ImpôtExpert (2 entrées Classe 10)
- [ ] Remplir les dividendes versés (53 837 $)
- [ ] Remplir la source de revenu (entreprise active, Québec)
- [ ] Vérifier la Révision (erreurs/avertissements)
- [ ] Produire les feuillets T5 + Relevé 3
- [ ] Déclaration personnelle T1
- [ ] Récupérer ~854 $ CTI/RTI sur prochaine déclaration TPS/TVQ

---

*Dernière mise à jour : 15 avril 2026, 08h30*
