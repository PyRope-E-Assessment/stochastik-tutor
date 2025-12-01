from pyrope import *

import random as rd
from sympy import symbols
import numpy as np

### switch between version with/without HTML code #############################
def withHTML():                                             ###################
    x = True #True/False: Code with/without HTML            ###################
    if not isinstance(x, bool): return 0                    ###################
    return x                                                ###################
###############################################################################

#Large gray font for preamble
def titel(txt, level = 1):
    size = ['Large', 'large', 'normalsize']
    return '$\\color{gray}{\\'+size[level]+'{\\textsf{'+txt+'}}}$'

#Several spaces for well-arranged text
def sp(n):
    return '$ '+n*'~'+' $ '

###################################################################
### Method ValTab (value tab):                                  ###
### makes a value table as special case of table using Markdown ###
###################################################################
# Give a list, containing one list of items for each line of the table or,
# alternativly, all line text in one string, separated by comma
def ValTab(lines):
    valTab = '\n\n'
    for i in range (len(lines)):
        valTab+='|'+lines[i][0]+'|'
        for j in range (1, len(lines[i])):
            valTab+=str(lines[i][j])+'|'
        if i==0:
            valTab+='\n|---|---|'
            for j in range (len(lines[0])-2):
                valTab+='---|'
        valTab+='\n'
    valTab+='\n\n'
    return valTab

#################################################################
### Method BlockTab: makes a Tab with border around each cell ###
#################################################################
# Give a list, containing one list of items for each line of the table or,
# alternativly, all line text in one string, separated by comma
def BlockTab(lines):
    tabTxt = '<br><table style = "margin-left: 0px">'
    for line in lines:
        if type(line)==str:
            line = line.split(',')
        tabTxt += '<tr>'
        for cell in line:
            tabTxt += '<td  style = "background-color: white; border:1px solid black; text-align: right">'+sp(3)+str(cell)+sp(2)+'</td>'
        tabTxt += '</tr>'
    tabTxt += '</table>\n\n'
    return tabTxt

#Primzahlen von-bis
def pzGenerator(zMin, zMax):
    l = list(np.arange(max(zMin,2),zMax+1))
    for i in range (2, int(np.sqrt(l[-1]))+1):
        for k in range (i, int(l[-1]/i)+1):
            try: l.remove(i*k)
            except: pass
    return l

def rnd(n): #Rundung auf n NK-Stellen, bei 5 an Stelle n+1 auch Aufrunden erlaubt
    return 5*10**(-(n+1))+10**(-(n+10))

x, i, n, q  = symbols ('x, i, n, q')


class Übung1(Exercise):
    
    preamble = titel('Grundkurs Stochastik - Teil 4: Bedingte Wahrscheinlichkeiten und Stochastische (Un)abhängigkeit')+\
               '\n\n**Willkommen zum Grundkurs Stochastik - Teil 4!**\n\n'+\
               titel('Übung 4.1',2)
    
    def parameters(self):
        min = rd.randint(1,21)
        max = min+19
        th = max - rd.randint(2, 7)
        l1 = len(pzGenerator(min, max)) #Anzahl pz im Intervall [min, max]
        l3 = len(pzGenerator(min, th-1)) #Anzahl pz im Intervall [min, th-1]
        p1 = l1/20 * (l1-1)/19 * (l1-2)/18
        l2 = th - min 
        p2 = l2/20 * (l2-1)/19 * (l2-2)/18
        p3 = l3/l2 * (l3-1)/(l2-1) * (l3-2)/(l2-2)
        return {'min': min, 'max': max, 'th': th, 'P1': round(p1,3), 'P2': round(p2,3), 'P3': round(p3,3)}

    def problem(self):
        P_ = Real(atol = rnd(3), widget=Text(width = 8))
        return  Problem (f'''
        Zum Auftakt folgende Aufgabe: 
        In einem Kasten liegen verdeckt 20 Zettel mit den Zahlen von $<<min:latex>>$ bis $<<max:latex>>$.\n\n
        Jemand zieht 3 Zettel ohne Zurücklegen. Wie groß ist die Wahrscheinlichkeit dass...\n\n
        - alle 3 Zahlen Primzahlen sind <<P1_>>\n\n
        - alle 3 Zahlen kleiner als <<th>> sind <<P2_>>\n\n
        - wenn alle 3 Zahlen kleiner als <<th>> sind, diese alle Primzahlen sind 
        <<P3_>>{sp(5)}(Genauigkeit jeweils 3 NK-Stellen)''',
        P1_ = P_, P2_ = P_, P3_ = P_
        )       

     
class Übung2(Exercise):
    
    preamble = titel('Übung 4.2',2)
    
    def parameters(self):      
        P = [.5, .333, .167, .5, .333]
        dict2 = {}
        for i in range (len(P)):
            dict2['P'+str(i+1)]=P[i]
        return dict2
    
    def problem(self):
        P_ = Real(atol = rnd(3), widget=Text(width = 7))
        return  Problem ('''
        Bei der dritten Aufgabe handelt es sich 
        um eine $→$ *bedingte Wahrscheinlichkeit*, d.h. es wird nach der Wahrscheinlichkeit 
        für ein Ereignis B unter der Voraussetzung, dass ein Ereignis A eingetreten ist, gefragt.\\ 
        Man schreibt: $P_A(B)$. Man spricht auch von *der durch A bedingten Wahrscheinlichkeit\nvon B*, 
        die wie folgt definiert ist:\n\n$P_A(B) = \\frac{P(A ∩ B)}{P(A)}$\n\n
        Ein Würfel wird einmal geworfen. Wir betrachten die Ereignisse\n\n
        $A$: Es fällt eine durch 2 teilbare Zahl\n
        $B$: Es fällt eine durch 3 teilbare Zahl\n\n
        Berechnen Sie die Wahrscheinlichkeiten (3 NK-Stellen)\n\n'''
        f'''$P(A) =$ <<P1_>>{sp(5)}$P(B) =$ <<P2_>>{sp(5)}
        $P(A ∩ B) =$ <<P3_>>\n\n$P_B(A) =$ <<P4_>>{sp(5)}$P_A(B) =$ <<P5_>>''',
        P1_ = P_, P2_ = P_, P3_ = P_, P4_ = P_, P5_ = P_
        )


class Übung3(Exercise):
    
    preamble = titel('Übung 4.3',2)
    
    def parameters(self):
        P = [.5, .167, .333, .333] 
        dict3 = {}
        for i in range (len(P)):
            dict3['P'+str(i+1)]=P[i]
        return dict3
    
    def problem(self):
        P_ = Real(atol = rnd(3), widget=Text(width = 8))
        return  Problem (f'''
        Wir stellen fest, dass im obigen Beispiel $P_B(A) = P(A)$ und $P_A(B) = P(B)$ gilt. 
        Die Ereignisse A und B heißen in diesem Fall *stochastisch unabhängig* 
        und es gilt folglich: $P(A ∩ B) = P(A)\\cdot P(B)$.\n\n
        Die Symmetrie dieser Relation lässt sich  aus der Definition 
        der bedingten Wahrscheinlichkeit und obigen Gleichungen leicht herleiten.\\ 
        Wir ergänzen nun noch das Ereignis $C$: *Es fällt eine Primzahl*. 
        Bestimmen Sie mit jeweils 3 NK-Stellen Genauigkeit:\n\n
        $P(C) =$ <<P1_>>{sp(5)}$P(A ∩ C) =$ <<P2_>>{sp(5)}
        $P_C(A) =$ <<P3_>>{sp(5)}$P_A(C) =$ <<P4_>>''',
        P1_ = P_, P2_ = P_, P3_ = P_, P4_ = P_
        )


class Übung4(Exercise):
    
    preamble = titel('Übung 4.4',2) 
    
    def parameters(self):
        farbe = rd.choice(['Kreuz', 'Pik', 'Herz', 'Karo'])
        lusche = rd.choice([7, 8, 9])
        pList = rd.choice([[.1, .2, .2, .2, .3],[.1, .1, .1, .3, .4]]) #[48,12]
        pList = rd.sample(pList,5) #Reihenfolge zufällig
        nList = ['a','b','c','d','e']
        nbs = [0,1,2,3,4]
        i = rd.choice(nbs); nbs.remove(i)
        [j,k] = rd.sample(nbs,2)
        Pij = round(pList[i]+pList[j],2)
        Pik = round(pList[i]+pList[k],2)
        opts=['abhängig', 'unabhängig']
        E4 = opts[int(Pij*Pik==pList[i])]
        return {'farbe': farbe, 'lusche': lusche,
                'E1': opts[1], 'E2': opts[1], 'E3': opts[0], 'E4': E4,
                'pList': pList, 'nList': nList,
                'x': nList[i], 'y': nList[j], 'z': nList[k]}

    def problem(self, nList, pList):
        args = [["$x$"]+nList, ["$P(x)$"]+pList]
        Tab = [ValTab(args), BlockTab(args)][withHTML()]
        E_ = String(widget=RadioButtons('abhängig', 'unabhängig', vertical=False))
        return  Problem (f'''
        In diesem Fall gilt nicht $P_C(A) = P(A)$ und daher auch nicht $P_A(C) = P(C)$. 
        Die Ereignisse A und C sind *stochastisch abhängig*.\n
        Lösen Sie nun noch die folgenden Aufgaben:\n\n
        Aus einem Skatblatt (Französisches Blatt: Kreuz-schwarz, Pik-schwarz, Herz-rot, Karo-rot) 
        wird eine Karte gezogen. 
        Entscheiden Sie, ob  die folgenden Ereignisse voneinander abhängig oder unabhängig sind!\n\n
        A: Es wurde eine $<<farbe:latex>>karte$ gezogen{sp(5)}
        B: Es wurde eine $<<lusche:latex>>$ gezogen{sp(5)}
        C: Es wurde eine Lusche (7, 8 oder 9) gezogen\n\n
        A und B sind stochastisch <<E1_>>\\
        A und C sind stochastisch <<E2_>>\\
        B und C sind stochastisch <<E3_>>\n\n'''
        'Ein Zufallsexperiment hat die Ergebnismenge {a, b, c, d, e} und die Wahrscheinlichkeitsverteilung'
        f'{Tab}\n\nDie Ereignisse '
        '{$<<x:latex>>,~<<y:latex>>$} und {$<<z:latex>>,~<<x:latex>>$} sind stochastisch$~~~$<<E4_>>',
        E1_ = E_, E2_ = E_, E3_ = E_, E4_ = E_
        )


class Übung5(Exercise):
    
    preamble = titel('Übung 4.5',2) 
    
    def parameters(self):
        anz = rd.randint(10,100)*100
        anzK = int(rd.randint(2, 8)/100*anz)
        rPos = rd.randint(89, 99)
        fPos = rd.randint(1, 5)
        kP = anzK/anz*rPos/100
        gP = (1-anzK/anz)*fPos/100
        tw1 = kP + gP
        P1 = kP/tw1
        kN = anzK/anz*(1-rPos/100)
        gN = (1-anzK/anz)*(1-fPos/100)
        tw2 = kN + gN
        P2 = kN/tw2
        return {'anz': anz, 'anzK': anzK, 'rPos': rPos, 'fPos': fPos,
                'P1': round(P1*100,3), 'P2': round(P2*100, 3)}

    def problem(self):
        P = Real(widget=Text(width = 8))
        return  Problem ('''
        Zum Abschluss dieses Tutoriums noch eine Aufgabe aus dem "echten Leben". 
        Sie benötigen zur Lösung den Begriff $→$ *Totale Wahrscheinlichkeit* und den $→$ *Satz von Bayes*.\n\n
        Ein Test auf eine Stoffwechselstörung fällt bei $<<rPos:latex>>$ % der erkrankten, 
        aber auch bei $<<fPos:latex>>$ % der gesunden Probanden positiv aus. 
        In einer Versuchsreihe werden $<<anz:latex>>$ Personen getestet, von denen $<<anzK:latex>>$ die Krankheit haben. 
        Eine zufällig ausgewählte Person hat ein positives Testergebnis.\n\n 
        Mit welcher Wahrscheinlichkeit leidet sie an besagter Störung? <<P1_>> %\n\n
        Mit welcher Wahrscheinlichkeit hat eine zufällig ausgewählte Person mit einem negativen Testergebnis 
        die Krankheit trotzdem? <<P2_>> %\n\n(Angaben in Prozent, Genauigkeit >= 3 NK-Stellen)''',
        P1_ = P, P2_ = P
        )
    
    def scores(self, P1_, P2_, P1, P2):
        P_ = [P1_, P2_]
        P = [P1, P2]
        score = [0, 0]
        for i in range (len(P)):
            if P_[i] is not None:
                score[i] = round(P_[i],3) == P[i]
        return {'P1_': score[0], 'P2_': score[1]}
    
    def feedback(self, P1_, P2_, P1, P2):
        if sum(list(self.scores(P1_, P2_, P1, P2).values())) == 2:
            return 'Sehr schön gelöst! Es folgt der StochastikTutor - Teil 5!'
        return 'Sie haben mit hoher Wahrscheinlichkeit noch Übungsbedarf zu diesem Thema. '\
               '[Hier](https://www.abiturloesung.de/abitur/thema/Stochastische+Unabhängigkeit) finden Sie eine umfangreiche Aufgabensammlung mit Lösungen.'
       