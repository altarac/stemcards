from flask import Flask, render_template, url_for, jsonify
from random import *
import pandas as pd
from sympy import *
from chempy import balance_stoichiometry
from chempy import Substance
from chempy import balance_stoichiometry
from chempy import Equilibrium
from chempy.units import default_units as u
import math
from mendeleev import element
import re

import os

import stripe




# stripe_keys = {
#   'secret_key': os.environ['STRIPE_SECRET_KEY'],
#   'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
# }

# stripe.api_key = stripe_keys['secret_key']



# values = []

# for i in range(4):
#     values.append(randint(2, 12))

app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/algeb1')
def algeb1():
    values = []
    for i in range(4):
        values.append(randint(5, 20))
    return render_template('algeb1.html', values = values)


@app.route('/chem1')
def chem1():
    eq = '''NaH2PO4 -> NaPO3 + H2O
    H2CO3 -> H2O + CO2
    BaSO4 + H2SO4 -> Ba(HSO4)2
    CaCO3 -> CaO + CO2
    CaO + H2O -> Ca(OH)2
    H2SO3 -> H2O + SO2
    H3PO4 + Ca(OH)2 -> CaHPO4.2H2O
    NaPO3 + CuO -> NaCuPO4
    SO3 + H2O -> H2SO4
    Be(OH)2 -> BeO + H2O
    BaO + H2O -> Ba(OH)2
    Na2SO3 + S -> Na2S2O3
    SO2 + H2O -> H2SO3
    Li2O + H2O -> LiOH
    Na2HPO4 -> Na4P2O7 + H2O
    H4As2O7 -> As2O5 + H2O
    CaC2 + N2 -> CaCN2 + C
    Mg(OH)2 -> (MgOH)2O + H2O
    HAsO3 -> As2O5 + H2O
    KHSO4 -> K2S2O7 + H2O
    H3PO4 -> H4P2O7 + H2O
    NaCl + NH4HCO3 -> NaHCO3 + NH4Cl
    HAsO2 -> As2O3 + H2O
    UO3 + H2 -> UO2 + H2O
    CdSO4 + H2S -> CdS + H2SO4
    HIO3 -> I2O5 + H2O
    Ca(HCO3)2 -> CaCO3 + CO2 + H2O
    FeS + H2SO4 -> H2S + FeSO4
    (NH4)2SO4 + CaCO3 -> (NH4)2CO3 + CaSO4
    Hg2CO3 -> Hg + HgO + CO2
    CaSO4 -> CaS + O2
    BeF2 + Mg -> MgF2 + Be
    Mg + N2 -> Mg3N2
    SiO2 + Ca(OH)2 -> CaSiO3 + H2O
    K2O + H2O -> KOH
    C + H2O -> CO + H2
    Ca(OH)2 + CO2 -> Ca(HCO3)2
    N2O3 + H2O -> HNO2
    SiO2 + Na2CO3 -> Na2SiO3 + CO2
    BaO2 + H2SO4 -> BaSO4 + H2O2
    Na2Cr2O7 + S -> Cr2O3 + Na2SO4
    Ca(OH)2 + CO2 -> CaCO3 + H2O
    Fe2O3 + SiO2 -> Fe2Si2O7
    CO2 + NH3 + H2O -> NH4HCO3
    Na2O + H2O -> NaOH
    NH4NO3 -> N2O + H2O
    N2O5 + H2O -> HNO3
    CaS + H2O -> Ca(OH)2 + H2S
    Al(OH)3 + NaOH -> NaAlO2 + H2O
    (CuOH)2CO3 -> CuO + CO2 + H2O
    SrBr2 + (NH4)2CO3 -> SrCO3 + NH4Br
    H2O2 -> H2O + O2
    Ca(ClO3)2 -> CaCl2 + O2
    PCl5 + H2O -> POCl3 + HCl
    Zn + KOH -> K2ZnO2 + H2
    Al2O3 + Na2CO3 -> NaAlO2 + CO2
    PCl5 + KNO2 -> NOCl + POCl3 + KCl
    Zn + HCl -> ZnCl2 + H2
    BeO + C + Cl2 -> BeCl2 + CO
    N2 + O2 -> N2O
    BeSO4 + NH4OH -> Be(OH)2 + (NH4)2SO4
    Cu(CN)2 -> CuCN + C2N2
    SiC + Cl2 -> SiCl4 + C
    NH3 + O2 -> HNO3 + H2O
    Fe2(C2O4)3 -> FeC2O4 + CO2
    H2 + O2 -> H2O
    K + Br2 -> KBr
    CO + O2 -> CO2
    HNO2 + O2 -> HNO3
    O2 -> O3
    NaHCO3 -> Na2CO3 + CO2 + H2O
    CO2 + NH3 -> OC(NH2)2 + H2O
    Xe + F2 -> XeF6
    MnS + HCl -> H2S + MnCl2
    CaC2 + H2O -> C2H2 + Ca(OH)2
    ClO2 + H2O -> HClO2 + HClO3
    CuSO4 + KCN -> Cu(CN)2 + K2SO4
    NaOH + FeSO4 -> Na2SO4 + Fe(OH)2
    Ca(OH)2 + H3PO4 -> CaHPO4 + H2O
    PbCrO4 + HNO3 -> Pb(NO3)2 + H2CrO4
    HgO -> Hg + O2
    (CN)2 + NaOH -> NaCN + NaOCN + H2O
    BaCO3 + HNO3 -> Ba(NO3)2 + CO2 + H2O
    H3AsO4 -> As2O5 + H2O
    CaO + C -> CaC2 + CO
    Zn(OH)2 + NaOH -> Na2ZnO2 + H2O
    HNO3 + P2O5 -> N2O5 + HPO3
    UF4 + Mg -> MgF2 + U
    Mn2O3 + Al -> Al2O3 + Mn
    MnO2 + K2CO3 + KNO3 -> K2MnO4 + KNO2 + CO2
    AlN + H2O -> NH3 + Al(OH)3
    Ca3(PO4)2 + H2SO4 -> CaSO4 + Ca(H2PO4)2
    S + N2O -> SO2 + N2
    N2 + H2 -> NH3
    CaCO3 + HCl -> CaCl2 + H2O + CO2
    As2O3 + H2O -> H3AsO3
    Be(OH)2 + NH4HF2 -> (NH4)2BeF4 + H2O
    NaOH + Zn(NO3)2 -> NaNO3 + Zn(OH)2
    MgNH4PO4 -> Mg2P2O7 + NH3 + H2O
    H3PO4 + Ca(OH)2 -> Ca(H2PO4)2 + H2O
    CaS + H2O -> Ca(HS)2 + Ca(OH)2
    Cu + CO2 + O2 + H2O -> CuCO3.Cu(OH)2
    (NH4)2BeF4 -> BeF2 + NH3 + HF
    Sn(OH)2 + NaOH -> Na2SnO2 + H2O
    NH4VO3 -> V2O5 + NH3 + H2O
    H3AsO3 -> As2O3 + H2O
    NaCl + H2SO4 -> Na2SO4 + HCl
    Fe(OH)3 -> Fe2O3 + H2O
    As2O5 + H2O -> H3AsO4
    NaOH + Cl2 -> NaCl + NaClO + H2O
    VO2Cl + NH4OH -> NH4VO3 + NH4Cl + H2O
    B2O3 + H2O -> H3BO3
    CH4 + O2 -> CO2 +H2O
    SiH4 + O2 -> SiO2 + H2O
    TiCl4 + Mg -> MgCl2 + Ti
    Pb(OH)2 + NaOH -> Na2PbO2 + H2O
    Si + NaOH + H2O -> Na2SiO3 + H2
    Si + S8 -> Si2S4
    CaS2 + O2 -> CaS2O3
    Na2SnO3 + H2S -> SnS2 + NaOH + H2O
    Na2S2 + O2 -> Na2S2O3
    (NH4)2Cr2O7 -> Cr2O3 + N2 + H2O
    HCl + K2CO3 -> KCl + H2O + CO2
    KClO3 -> KCl + O2
    Zn + NaOH + H2O -> Na2Zn(OH)4 + H2
    Na2CO3 + HCl -> NaCl + H2O + CO2
    Ca(OH)2 + P4O10 + H2O -> Ca(H2PO4)2
    CaS + H2O + CO2 -> Ca(HCO3)2 + H2S
    Sn(OH)4 + NaOH -> Na2SnO3 + H2O
    Na + H2O -> NaOH + H2
    Ca3(PO4)2 + SiO2 -> CaSiO3 + P2O5
    FeCl3 + NH4OH -> Fe(OH)3 + NH4Cl
    H3PO3 -> H3PO4 + PH3
    AlCl3 + AgNO3 -> AgCl + Al(NO3)3
    KOH + AlCl3 -> KCl + Al(OH)3
    H2SO4 + NaHCO3 -> Na2SO4 + CO2 + H2O
    SiO2 + HF -> SiF4 + H2O
    CaCN2 + H2O -> CaCO3 + NH3
    HCl + HNO3 -> NOCl + Cl2 + H2O
    KClO3 -> KClO4 + KCl
    P4 + O2 -> P2O5
    P4O10 + HCl -> POCl3 + HPO3
    Sb + O2 -> Sb4O6
    NH4Cl + Ca(OH)2 -> CaCl2 + NH3 + H2O
    KBr + Al(ClO4)3 -> AlBr3 + KClO4
    AgNO3 + FeCl3 -> Fe(NO3)3 + AgCl
    Ca3(PO4)2 + H3PO4 -> Ca(H2PO4)2
    POCl3 + H2O -> H3PO4 + HCl
    C2H5OH + O2 -> CO + H2O
    UO2 + HF -> UF4 + H2O
    Ag2S + KCN -> KAg(CN)2 + K2S
    C + SiO2 + Cl2 -> SiCl4 + CO
    PCl3 + H2O -> H3PO3 + HCl
    H3PO4 + (NH4)2MoO4 + HNO3 -> (NH4)3PO4.12MoO3 + NH4NO3 + H2O
    MnO2 + HCl -> MnCl2 + H2O + Cl2
    Fe2O3 + C -> CO + Fe
    PCl5 + P2O5 -> POCl3
    FeO + H3PO4 -> Fe3(PO4)2 + H2O
    Ca(NO3)2 -> CaO + NO2 + O2
    Fe + O2 -> Fe2O3
    Fe2O3 + H2 -> Fe + H2O
    FeSO4 + K3[Fe(CN)6] -> Fe3[Fe(CN)6]2 + K2SO4
    NH3 + O2 -> HNO2 + H2O
    Al + O2 -> Al2O3
    BaCl2 + Al2(SO4)3 -> BaSO4 + AlCl3
    Fe2(SO4)3 + Ba(NO3)2 -> BaSO4 + Fe(NO3)3
    Au2S3 + H2 -> Au + H2S
    Au + HCl + HNO3 -> AuCl3 + NO + H2O
    NiS + O2 -> NiO + SO2
    Al + FeO -> Al2O3 + Fe
    C2H5OH + O2 -> CO2 + H2O
    Na2O2 + H2O -> NaOH + O2
    Fe2O3 + CO -> Fe + CO2
    Pb(NO3)2 -> PbO + NO2 + O2
    Al2(SO4)3 + Ca(OH)2 -> CaSO4 + Al(OH)3
    Au2O3 -> Au + O2
    Ca3(PO4)2 + H2SO4 -> CaSO4 + H3PO4
    SiCl4 + H2O -> H4SiO4 + HCl
    Ca + AlCl3 -> CaCl2 + Al
    FeCl3 + Ca(OH)2 -> CaCl2 + Fe(OH)3
    Al2O3 + C + N2 -> AlN + CO
    NO + NaOH -> NaNO2 + H2O + N2O
    Pb3O4 + HNO3 -> Pb(NO3)2 + PbO2 + H2O
    CuSO4 + KCN -> CuCN + K2SO4 + C2N2
    KO2 + CO2 -> K2CO3 + O2
    P4O6 -> P4 + P2O4
    P4O10 + H2O -> H3PO4
    Al + KOH + H2O -> KAlO2 + H2
    Fe + H2O + O2 -> Fe2O3.H2O
    H3PO4 + HCl -> PCl5 + H2O
    MnO2 + KOH + O2 -> K2MnO4 + H2O
    K2CO3 + C + N2 -> KCN + CO
    PCl5 + H2O -> H3PO4 + HCl
    P4O6 + H2O -> H3PO3
    Al(OH)3 + H2SO4 -> Al2(SO4)3 + H2O
    Fe2(SO4)3 + KOH -> K2SO4 + Fe(OH)3
    Bi(NO3)3 + H2S -> Bi2S3 + HNO3
    V2O5 + HCl -> VOCl3 + H2O
    Cr(OH)3 + H2SO4 -> Cr2(SO4)3 + H2O
    Hg(OH)2 + H3PO4 -> Hg3(PO4)2 + H2O
    Fe + H2O -> Fe3O4 + H2
    Ca3P2 + H2O -> Ca(OH)2 + PH3
    H2SO4 + Al(OH)3 -> Al2(SO4)3 + H2O
    Al(NO3)3 + Na2CO3 -> Al2(CO3)3 + NaNO3
    K2MnO4 + H2SO4 -> KMnO4 + MnO2 + K2SO4 + H2O
    Na3AsO3 + H2S -> As2S3 + NaOH
    Mg3N2 + H2O -> Mg(OH)2 + NH3
    Fe3O4 + H2 -> Fe + H2O
    C2H2 + O2 -> CO2 + H2O
    (NH4)2Cr2O7 -> NH3 + H2O + Cr2O3 + O2
    C3H8 + O2 -> CO2 + H2O
    As + NaOH -> Na3AsO3 + H2
    H3BO3 + Na2CO3 -> Na2B4O7 + CO2 + H2O
    Al + HCl -> AlCl3 + H2
    V2O5 + Ca -> CaO + V
    H3BO3 -> H4B6O11 + H2O
    Na2B4O7 + HCl + H2O -> NaCl + H3BO3
    Pb + Na + C2H5Cl -> Pb(C2H5)4 + NaCl
    C2H3Cl + O2 -> CO2 + H2O + HCl
    CaHPO4.2H2O + NaOH + H2O -> Na2HPO4.12H2O + Ca(OH)2
    Ca3(PO4)2 + SiO2 -> P4O10 + CaSiO3
    Se + NaOH -> Na2Se + Na2SeO3 + H2O
    Al + NaOH + H2O -> NaAl(OH)4 + H2
    K3AsO4 + H2S -> As2S5 + KOH + H2O
    I2 + HNO3 -> HIO3 + NO2 + H2
    Al + NH4ClO4 -> Al2O3 + AlCl3 + NO + H2O
    FeS + O2 -> Fe2O3 + SO2
    Ca3(PO4)2 + C -> Ca3P2 + CO
    FeC2O4⋅2H2O + H2C2O4 + H2O2 + K2C2O4 -> K3[Fe(C2O4)3]⋅3H2O
    MgNH4AsO4.6H2O -> Mg2As2O7 + NH3 + H2O
    H2SO4 + HI -> H2S + I2 + H2O
    U3O8 + HNO3 -> UO2(NO3)2 + NO2 + H2O
    (NH4)3AsS4 + HCl -> As2S5 + H2S + NH4Cl
    Pb3(VO4)2.PbCl2 + HCl -> VO2Cl + PbCl2 + H2O
    NH3 + O2 -> NO + H2O
    Hg2CrO4 -> Cr2O3 + Hg + O2
    Al4C3 + H2O -> CH4 + Al(OH)3
    Ca10F2(PO4)6 + H2SO4 -> Ca(H2PO4)2 + CaSO4 + HF
    Ca5F(PO4)3 + H2SO4 -> Ca(H2PO4)2 + CaSO4 + HF
    UO2(NO3)2.6H2O -> UO3 + NO2 + O2 + H2O
    S8 + O2 -> SO3
    NH3 + NO -> N2 + H2O
    HClO4 + P4O10 -> H3PO4 + Cl2O7
    Au + KCN + O2 + H2O -> K[Au(CN)2] + KOH
    CO2 + H2O -> C6H12O6 + O2
    V2O5 + Al -> Al2O3 + V
    FeS2 + O2 -> Fe2O3 + SO2
    Si2H3 + O2 -> SiO2 + H2O
    P4 + H2O -> H3PO4 + H2
    H2S + Cl2 -> S8 + HCl
    C4H10 + O2 -> CO2 + H2O
    Ca3(PO4)2 + SiO2 + C -> CaSiO3 + P4 + CO
    C6H6 + O2 -> CO2 + H2O
    C10H16 + Cl2 -> C + HCl
    C7H6O2 + O2 -> CO2 + H2O
    C7H16 + O2 -> CO2 + H2O
    C7H10N + O2 -> CO2 + H2O + NO2
    KNO3 + C12H22O11 -> N2 + CO2 + H2O + K2CO3
    K4Fe(CN)6 + KMnO4 + H2SO4 -> KHSO4 + Fe2(SO4)3 + MnSO4 + HNO3 + CO2 + H2O
    K3[Fe(SCN)6] + Na2Cr2O7 + H2SO4 -> Fe(NO3)3 + Cr2(SO4)3 + CO2 + H2O + Na2SO4 + KNO3
    K4[Fe(SCN)6] + K2Cr2O7 + H2SO4 -> Fe2(SO4)3 + Cr2(SO4)3 + CO2 + H2O + K2SO4 + KNO3'''.split('\n')

    q = choice(eq)
    e = q.split('->')
    r = e[0].split('+')
    p = e[1].split('+')
    reac, prod = balance_stoichiometry(set(r), set(p))
    reacs = list(dict(reac).keys())
    reacVals = list(dict(reac).values())

    prods = list(dict(prod).keys())
    prodVals = list(dict(prod).values())


    return render_template('chem1.html', equation = q, reac = reacs, reacVals = reacVals, prod = prods, prodVal = prodVals)








@app.route('/dilution')
def dilution():
    values = []
    for i in range(4):
        values.append(randint(5, 20))

    return render_template('dilution.html', values = values)





@app.route('/ohms')
def ohms():
    values = []
    for i in range(4):
        values.append(randint(5, 20))

    return render_template('ohms.html', values = values)


@app.route('/ohms-parallel')
def ohmsParallel():
    values = []
    for i in range(4):
        values.append(randint(5, 20))

    return render_template('ohms-parallel.html', values = values)



@app.route('/energy')
def energy():
    values = []
    for i in range(4):
        values.append(randint(5, 20))

    return render_template('energy.html', values = values)


@app.route('/work1')
def work1():
    values = []
    for i in range(4):
        values.append(randint(5, 20))

    return render_template('work1.html', values = values)




@app.route('/work2')
def work2():
    values = []
    for i in range(4):
        values.append(randint(5, 20))

    theta = values[3]
    cos = math.cos(math.pi*theta/180)

    return render_template('work2.html', values = values, theta =theta, cos = cos)


@app.route('/pressure')
def pressure():
    values = []
    for i in range(4):
        values.append(randint(5, 20))

    return render_template('pressure.html', values = values)


@app.route('/heat')
def heat():
    values = []
    C = randint(101, 500)/100
    for i in range(4):
        values.append(randint(5, 20))

    return render_template('heatEnergy.html', values = values, C = C)

@app.route('/density')
def density():
    values = []
    for i in range(4):
        values.append(randint(5, 20))

    return render_template('density.html', values = values)




@app.route('/mol')
def mol():
    elems = ['Ac',
 'Ag',
 'Al',
 'Am',
 'Ar',
 'As',
 'At',
 'Au',
 'B',
 'Ba',
 'Be',
 'Bh',
 'Bi',
 'Bk',
 'Br',
 'C',
 'Ca',
 'Cd',
 'Ce',
 'Cf',
 'Cl',
 'Cm',
 'Co',
 'Cr',
 'Cs',
 'Cu',
 'Ds',
 'Db',
 'Dy',
 'Er',
 'Es',
 'Eu',
 'F',
 'Fe',
 'Fm',
 'Fr',
 'Ga',
 'Gd',
 'Ge',
 'H',
 'He',
 'Hf',
 'Hg',
 'Ho',
 'Hs',
 'I',
 'In',
 'Ir',
 'K',
 'Kr',
 'La',
 'Li',
 'Lr',
 'Lu',
 'Md',
 'Mg',
 'Mn',
 'Mo',
 'Mt',
 'N',
 'Na',
 'Nb',
 'Nd',
 'Ne',
 'Ni',
 'No',
 'Np',
 'O',
 'Os',
 'P',
 'Pa',
 'Pb',
 'Pd',
 'Pm',
 'Po',
 'Pr',
 'Pt',
 'Pu',
 'Ra',
 'Rb',
 'Re',
 'Rf',
 'Rg',
 'Rh',
 'Rn',
 'Ru',
 'S',
 'Sb',
 'Sc',
 'Se',
 'Sg',
 'Si',
 'Sm',
 'Sn',
 'Sr',
 'Ta',
 'Tb',
 'Tc',
 'Te',
 'Th',
 'Ti',
 'Tl',
 'Tm',
 'U',
 'V',
 'W',
 'Xe',
 'Y',
 'Yb',
 'Zn',
 'Zr',
 'NaH2PO4 ',
 '    H2CO3 ',
 '    BaSO4 ',
 '    CaCO3 ',
 '    CaO ',
 '    H2SO3 ',
 '    H3PO4 ',
 '    NaPO3 ',
 '    SO3 ',
 '    Be(OH)2 ',
 '    BaO ',
 '    Na2SO3 ',
 '    SO2 ',
 '    Li2O ',
 '    Na2HPO4 ',
 '    H4As2O7 ',
 '    CaC2 ',
 '    Mg(OH)2 ',
 '    HAsO3 ',
 '    KHSO4 ',
 '    H3PO4 ',
 '    NaCl ',
 '    HAsO2 ',
 '    UO3 ',
 '    CdSO4 ',
 '    HIO3 ',
 '    Ca(HCO3)2 ',
 '    FeS ',
 '    (NH4)2SO4 ',
 '    Hg2CO3 ',
 '    CaSO4 ',
 '    BeF2 ',
 '    Mg ',
 '    SiO2 ',
 '    K2O ',
 '    C ',
 '    Ca(OH)2 ',
 '    N2O3 ',
 '    SiO2 ',
 '    BaO2 ',
 '    Na2Cr2O7 ',
 '    Ca(OH)2 ',
 '    Fe2O3 ',
 '    CO2 ',
 '    Na2O ',
 '    NH4NO3 ',
 '    N2O5 ',
 '    CaS ',
 '    Al(OH)3 ',
 '    (CuOH)2CO3 ',
 '    SrBr2 ',
 '    H2O2 ',
 '    Ca(ClO3)2 ',
 '    PCl5 ',
 '    Zn ',
 '    Al2O3 ',
 '    PCl5 ',
 '    Zn ',
 '    BeO ',
 '    N2 ',
 '    BeSO4 ',
 '    Cu(CN)2 ',
 '    SiC ',
 '    NH3 ',
 '    Fe2(C2O4)3 ',
 '    H2 ',
 '    K ',
 '    CO ',
 '    HNO2 ',
 '    O2 ',
 '    NaHCO3 ',
 '    CO2 ',
 '    Xe ',
 '    MnS ',
 '    CaC2 ',
 '    ClO2 ',
 '    CuSO4 ',
 '    NaOH ',
 '    Ca(OH)2 ',
 '    PbCrO4 ',
 '    HgO ',
 '    (CN)2 ',
 '    BaCO3 ',
 '    H3AsO4 ',
 '    CaO ',
 '    Zn(OH)2 ',
 '    HNO3 ',
 '    UF4 ',
 '    Mn2O3 ',
 '    MnO2 ',
 '    AlN ',
 '    Ca3(PO4)2 ',
 '    S ',
 '    N2 ',
 '    CaCO3 ',
 '    As2O3 ',
 '    Be(OH)2 ',
 '    NaOH ',
 '    MgNH4PO4 ',
 '    H3PO4 ',
 '    CaS ',
 '    Cu ',
 '    (NH4)2BeF4 ',
 '    Sn(OH)2 ',
 '    NH4VO3 ',
 '    H3AsO3 ',
 '    NaCl ',
 '    Fe(OH)3 ',
 '    As2O5 ',
 '    NaOH ',
 '    VO2Cl ',
 '    B2O3 ',
 '    CH4 ',
 '    SiH4 ',
 '    TiCl4 ',
 '    Pb(OH)2 ',
 '    Si ',
 '    Si ',
 '    CaS2 ',
 '    Na2SnO3 ',
 '    Na2S2 ',
 '    (NH4)2Cr2O7 ',
 '    HCl ',
 '    KClO3 ',
 '    Zn ',
 '    Na2CO3 ',
 '    Ca(OH)2 ',
 '    CaS ',
 '    Sn(OH)4 ',
 '    Na ',
 '    Ca3(PO4)2 ',
 '    FeCl3 ',
 '    H3PO3 ',
 '    AlCl3 ',
 '    KOH ',
 '    H2SO4 ',
 '    SiO2 ',
 '    CaCN2 ',
 '    HCl ',
 '    KClO3 ',
 '    P4 ',
 '    P4O10 ',
 '    Sb ',
 '    NH4Cl ',
 '    KBr ',
 '    AgNO3 ',
 '    Ca3(PO4)2 ',
 '    POCl3 ',
 '    C2H5OH ',
 '    UO2 ',
 '    Ag2S ',
 '    C ',
 '    PCl3 ',
 '    H3PO4 ',
 '    MnO2 ',
 '    Fe2O3 ',
 '    PCl5 ',
 '    FeO ',
 '    Ca(NO3)2 ',
 '    Fe ',
 '    Fe2O3 ',
 '    FeSO4 ',
 '    NH3 ',
 '    Al ',
 '    BaCl2 ',
 '    Fe2(SO4)3 ',
 '    Au2S3 ',
 '    Au ',
 '    NiS ',
 '    Al ',
 '    C2H5OH ',
 '    Na2O2 ',
 '    Fe2O3 ',
 '    Pb(NO3)2 ',
 '    Al2(SO4)3 ',
 '    Au2O3 ',
 '    Ca3(PO4)2 ',
 '    SiCl4 ',
 '    Ca ',
 '    FeCl3 ',
 '    Al2O3 ',
 '    NO ',
 '    Pb3O4 ',
 '    CuSO4 ',
 '    KO2 ',
 '    P4O6 ',
 '    P4O10 ',
 '    Al ',
 '    Fe ',
 '    H3PO4 ',
 '    MnO2 ',
 '    K2CO3 ',
 '    PCl5 ',
 '    P4O6 ',
 '    Al(OH)3 ',
 '    Fe2(SO4)3 ',
 '    Bi(NO3)3 ',
 '    V2O5 ',
 '    Cr(OH)3 ',
 '    Hg(OH)2 ',
 '    Fe ',
 '    Ca3P2 ',
 '    H2SO4 ',
 '    Al(NO3)3 ',
 '    K2MnO4 ',
 '    Na3AsO3 ',
 '    Mg3N2 ',
 '    Fe3O4 ',
 '    C2H2 ',
 '    (NH4)2Cr2O7 ',
 '    C3H8 ',
 '    As ',
 '    H3BO3 ',
 '    Al ',
 '    V2O5 ',
 '    H3BO3 ',
 '    Na2B4O7 ',
 '    Pb ',
 '    C2H3Cl ',
 '    CaHPO4.2H2O ',
 '    Ca3(PO4)2 ',
 '    Se ',
 '    Al ',
 '    K3AsO4 ',
 '    I2 ',
 '    Al ',
 '    FeS ',
 '    Ca3(PO4)2 ',
 '    FeC2O4⋅2H2O ',
 '    MgNH4AsO4.6H2O ',
 '    H2SO4 ',
 '    U3O8 ',
 '    (NH4)3AsS4 ',
 '    Pb3(VO4)2.PbCl2 ',
 '    NH3 ',
 '    Hg2CrO4 ',
 '    Al4C3 ',
 '    Ca10F2(PO4)6 ',
 '    Ca5F(PO4)3 ',
 '    UO2(NO3)2.6H2O ',
 '    S8 ',
 '    NH3 ',
 '    HClO4 ',
 '    Au ',
 '    CO2 ',
 '    V2O5 ',
 '    FeS2 ',
 '    Si2H3 ',
 '    P4 ',
 '    H2S ',
 '    C4H10 ',
 '    Ca3(PO4)2 ',
 '    C6H6 ',
 '    C10H16 ',
 '    C7H6O2 ',
 '    C7H16 ',
 '    C7H10N ',
 '    KNO3 ',
 '    K4Fe(CN)6 ',
 '    K3[Fe(SCN)6] ',
 '    K4[Fe(SCN)6] ']
    values = []
    elem = choice(elems)

    for i in range(4):
        values.append(randint(1, 5))

    if len(elem)<2 and values[0]!=1:
        e = elem+str(values[0])
    else:
        e = elem

    el = Substance.from_formula(f'{e}')  # simpler
    mm = el.molar_mass(u)

    return render_template('mol.html', values = values, elem = e, mm = mm)


@app.route('/eco')
def eco():
    values = []
    values2 = []
    for i in range(2):
        values.append(randint(11, 20))
    for i in range(2):
        values2.append(randint(5, 10))


    return render_template('eco.html', values = values, values2 = values2)


@app.route('/atom')
def atom():
    r = randint(1, 10)
    e = element(r)
    name = e.name
    symb = e.symbol
    return render_template('atom.html', r = r, name = name, symb = symb)


@app.route('/salinity')
def salinity():
    mass = []
    L = randint(100, 500)/1000
    ml = []
    for i in range(3):
        mass.append(randint(300, 1200)/100)
    for i in range(2):
        ml.append(randint(100, 500))
    return render_template('salinity.html', mass= mass, L = L, ml = ml)

@app.route('/concentration')
def concentration():
    values = []
    for i in range(4):
        values.append(randint(5, 20))

    return render_template('concentration.html', values = values)


@app.route('/ppm')
def ppm():
    masses = [f'{randint(5, 20)} g', f'{randint(10, 80)} mg']
    volumes = [f'{randint(1, 15)/10} L', f'{randint(100, 800)} mL']
    return render_template('ppm.html', masses = masses, volumes = volumes)


@app.route('/power')
def power():
    power = randint(100, 300)
    t = randint(10, 50)/10


    return render_template('power.html', power = power, t = t)




@app.route('/nomenclature')
def nomenclature():
    compounds = [
    '    SO3 ',
    '    N2O3 ',
    '    CO2 ',
    '    N2O5 ','CO₂',
 'CO',
 'P2O5',
 'N2O',
 'SO2',
 'CBr4',
 'SO3',
 'PBr5',
 'ICl3',
 'NI3',
 'N2O3',
 'N2O4',
 'SO2',
 'NO',
 'NO2',
 'PCl3',
 'CCl₄',
 'H2O',
 'SF6',
 'P4S3',
 'NH3',
 'CH4']
    class Name():
        def __init__(self, c='a'):

            self.compound = c

            self.secondElement = {
                'B': 'Bromide',
                'C': 'Carbide',
                'F': 'Fluoride',
                'H': 'Hydride',
                'I': 'Iodide',
                'N': 'Nitride',
                'O': 'Oxide',
                'P': 'Phosphide',
                'S': 'Sulphide',
                '(NO3)2': 'Nitrate'
                }

            self.firstElement = {
                '1':'Mono',
                '2':'Di',
                '3':'Tri',
                '4':'Tetra',
                '5':'Penta',
                '6':'Hexa',
                '7':'Hepta',
                '8':'Octa',
                '9':'Nona',
                '10':'Deca'
            }
        def getElems(self, c):
            return re.findall('[A-Z][^A-Z]*', str(c))

        def nameIt(self, elems):
            e = self.getElems(elems)
            nomenclature = []
            try:
                nomenclature.append(str(self.firstElement[e[0][1]]))
            except:
                pass
            try:
                nomenclature.append(f'{element(e[0][0]).name.lower()} ')
            except:
                pass
            try:
                nomenclature.append(str(self.firstElement[e[1][1]]))
            except:
                if(element(e[1][0]).name.lower()[0] == 'o'):
                    nomenclature.append('Mon')
                else:
                    nomenclature.append('Mono')
            try:
                nomenclature.append(str(self.secondElement[e[1][0]]).lower())
            except:
                pass

            return ''.join(nomenclature)
    c = choice(compounds)
    n = Name()
    name = n.nameIt(str(c))


    return render_template('nomenclature.html', compound = c, name = name)




@app.route('/genetics')
def genetics():
    genes = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
    scenario = ['parents were both dominant', 'parents were both recessive', 'parents were both heterozygous', 'father was homozygous recessive and mother was heterozygous', 'mother was homozygous dominant and father was heterozygous']
    z = randint(0, 4)
    g = choice(genes)
    # s = choice(scenario)


    return render_template('genetics.html', g = g, s = scenario, z = z)





@app.route('/force')
def force():
    accel = randint(10, 105)/10
    mass = randint(10, 1000)/10


    return render_template('force.html', a = accel, m = mass)



@app.route('/efficiency')
def efficiency():
    energy = randint(500, 1999)
    total = randint(2000, 10000)



    return render_template('efficiency.html', energy = energy, total = total)




@app.route('/velocity')
def velocity():
    dist = randint(60, 1000)
    time = randint(2, 4)



    return render_template('velocity.html', dist = dist, time = time)



# ################################ math below this point ##################### #



@app.route('/linerule')
def linerule():

    x = []
    y = []

    a = randint(1, 5)
    b = randint(1, 10)

    for i in range(0,10):
        x.append(i)
        y.append((a*(i)+b))

    return render_template('linerule.html', y = y, x = x)


@app.route('/intersection')
def intersection():

    x = []
    y1 = []
    y2 = []

    a1 = randint(1, 5)
    b1 = randint(1, 10)

    a2 = randint(1, 5)
    b2 = randint(1, 10)

    for i in range(0,10):
        x.append(i)
        y1.append((a1*(i)+b1))
        y2.append((a2*(i)+b2))

    return render_template('intersection.html', y1 = y1, y2 = y2, x = x, a1 = a1, b1 = b1, a2 = a2, b2 = b2)


@app.route('/expand1')
def expand1():
    x = symbols('x')
    a = randint(2, 10)
    b = randint(2, 10)
    c = randint(2, 10)
    d = randint(2, 10)
    binomial1 = f'({a}{x} + {b})'
    binomial2 = f'({c}{x} + {d})'
    res = expand(f'({a}*{x} + {b})*({c}*{x} + {d})')
    res = str(res).replace('**', '^')
    res = str(res).replace('*', '')

    return render_template('expand1.html', binomial1 = binomial1, binomial2 = binomial2, res = res)


@app.route('/factoring1')
def factoring1():
    x = symbols('x')
    a = randint(2, 10)
    b = randint(2, 10)
    c = randint(2, 10)
    d = randint(2, 10)
    binomial1 = f'({a}{x} + {b})'
    binomial2 = f'({c}{x} + {d})'
    res = expand(f'({a}*{x} + {b})*({c}*{x} + {d})')
    res = str(res).replace('**', '^')
    res = str(res).replace('*', '')

    return render_template('factoring1.html', binomial1 = binomial1, binomial2 = binomial2, res = res)




@app.route('/pythag')
def pythag():

    a = randint(1, 25)
    b = randint(1, 25)
    c = round((a**2+b**2)**(0.5), 2)

    return render_template('pythag.html', a = a, b = b, c = c)


@app.route('/scinotation')
def scinotation():

    a = randint(10, 99)/10
    b = randint(2, 15)
    c = randint(10, 200)/10
    d = randint(2, 15)


    x = ((a*10**b)*(c*10**d))
    y = '%.2E' % x

    res = y.replace('E', '-').replace('+', '').split('-')

    return render_template('scinotation.html', a = a, b = b, c = c, d = d, res = res)

@app.route('/wordprob')
def wordprob():

    boys = '''Freeman
            Emanuel
            Sean
            Mack
            Edward
            Jamison
            Calvin
            Stefan
            Marcelo
            Derek'''.split('\n')

    girls = '''Barbra
            Lana
            Arianne
            Arica
            Natalia
            Sharleen
            Patria
            Nickie
            Wenona
            Krishna'''.split('\n')

    mult = randint(2, 8)
    add = randint(2, 10)
    # age1 = randint(2, 18)
    # age2 = randint(2, 18)
    sum = ((mult+1)*(randint(2, 6)))+(2*(add))

    name1 = choice(boys)
    name2 = choice(girls)


    return render_template('wordprob.html', name1 = name1, name2 = name2, mult = mult, add = add, sum = sum)


@app.route('/circle')
def circle():
    p1 = []
    p2 = []
    for i in range(2):
        p1.append(randint(1, 5))
    for i in range(2):
        p2.append(randint(1, 5))

    return render_template('circle.html', p1 = p1, p2 = p2)


@app.route('/exponential')
def exponential():
    p1 = []
    p2 = []

    for i in range(2):
        p1.append(randint(1, 5))
    for i in range(2):
        p2.append(randint(1, 5))

    a= p1[1]/math.exp(p1[0])

    return render_template('exponential.html', p1 = p1, p2 = p2, a = a)


@app.route('/quadratic')
def quadratic():
    p1 = []
    p2 = []
    m=[1, -1]
    mm=[1, -1]
    aa= randint(1, 4)



    a = choice(m)*aa

    for i in range(2):
        p1.append(choice(mm)*randint(1, 5))
    for i in range(2):
        p2.append(choice(mm)*randint(1, 5))

    xx = p1[0]+choice(mm)*2

    p3 = [xx, a*((xx)-p1[0])**2+p1[1]]
    sol = f'{a}*(x-{p1[0]})**2+{p1[1]}'
    s = str(sympify(sol)).replace('**', '^').replace('*', '')

    return render_template('quadratic.html', p1 = p1, p2 = p2, p3 = p3, a = a, sol = s)


if __name__ == '__main__':
    app.run(debug=True)

