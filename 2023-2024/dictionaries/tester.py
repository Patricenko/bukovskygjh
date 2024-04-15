subject_to_teachers = {}

with open('nameToSubject.txt', 'r') as file:
    for line in file:
        teacher, subjects = line.strip().split(':')
        teacher = teacher.replace(' ', '')
        subjects = subjects.replace(' ', '')
        for subject in subjects.split(','):
            if subject not in subject_to_teachers:
                subject_to_teachers[subject] = [teacher]
            else:
                subject_to_teachers[subject].append(teacher)
for subject, teachers in subject_to_teachers.items():
    print(f"{subject.strip()}: {', '.join(teachers)}")

mat: ambrozy, belajova, chalupkova, gradzka, gunisovaxc, hubickova, jancovicova, kocy, kocy, kosper, kosut, kosutova, machalova, matasovska, neuhold, pelica, pochova, sedlackova, seitsinger, svitekova, valaskova, zorkocy
geg: ambrozy, gunisovaxc, kindji, markusova, trupova
sem: ambrozy, chalupkova, kosper, kosut, kosutova, matasovska
seg: ambrozy
tev: argajova, belajova, fedak, hasko, horvathova, hrbata, luptak, luptakova, pavlovicsova, pochova, sedlackova, vargova
anj: argajova, belajova, danisovsky, deak, deakova, faixova, hrbata, jamborova, kabatova, kucharova, lichvarova, lindbloom, minarikova, mistrik, molnarovaxb, molnarovaxz, pelica, pochova, reiling, repasky, sedlackova, seitsinger, smrekova, tarasovic, varga
inf: bakosova, bertova, bezakova, cikatricisiova, hubickova, jancovicova, kosut, laucekova, lomen, pelica, repasky, seitsinger, svitekova, winczer
tok: banovsky, kindji
obn: banovsky, deakova, vanca
ant: banovsky, lindbloom, schnapp
etv: belajova, capuchova, hrbata, hrenakova, karacsonyova, kmet, mistrik, nemcokova, oravec, pochova, sartorisova, sirotna, sorfova, trupova, varga, vargova, zahorska
sjl: belajova, hrapkova, hrbata, hrenakova, hubickova, hvojnikova, jancovicova, michalovicova, minarikova, orenicova, peckova, pochova, sedlackova, sorfova, suchterova, vicenova
ved: belajova, gondova, hrbata, hubickova, jancovicova, pelica, pochova, sedlackova, seitsinger, svitekova, orenicova
huv: belajova, crmoman, hrbata, hubickova, jancovicova, pochova, sedlackova
vyv: belajova, hrbata, masarova, pochova, sedlackova
che: belickova, bendikova, buckova, krizanova, malik, monosikova, oravec
apeche: belickova, bendikova, buckova, krizanova, monosikova
bio: bendikova, iliasova, kascakova, krizanova, lanator, oravec, slusny, trupova
apebio: bendikova, iliasova, kascakova, slusny
pcp: bertova, lomen, neuhold
sech: buckova, malik, monosikova
fyz: chalupkova, elizerova, galik, gonda, gondova, letanovska, matasovska
apefyz: chalupkova, elizerova, gondova, letanovska, matasovska
nej: chrastinova, jozova, mayer, vaskova, zajacova
spg: cikatricisiova, kosut
ukl: crmoman, masarova, michalovicova
tsv: danisovsky, fedak, hasko, horvathova, luptak, luptakova, pavlovicsova, sirotna, smrekova
dej: deak, kindji, matuskova, mlynarcikova, slezak, vanca
sps: deakova, vanca
psy: ditte, sartorisova
vyu: dzuriakova, jancovicova, kmet, orenicova, pelica
sef: elizerova, letanovska
pos: hrobar
vso: hubickova, jancovicova, pelica, seitsinger, svitekova
nbv: jakubec
rak: jamborova, valisova
seb: kascakova, krizanova
thd: kmet, masarova
eko: kolnikova, reiling, siller
cvm: kosutova
sja: krskova, patoprsta, sartorisova, zahorska
kaj: lichvarova, minarikova, valisova, varga
sen: liska, lomen
deg: machalova
sed: matuskova, slezak
das: matuskova, slezak
deu: michalovicova
frj: molnarovaxz
esi: suchterova
paj: tarasovic
ala: valisova