from pyrope import *

import random as rd
from sympy import symbols
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as bc
from scipy.integrate import quad

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

#Summenzeichen mit Grenzen und Inhalt
def sumStyle(u,o,arg):
    return '$\\large\\sum\\limits_{\\small{'+u+'}}^{\\small{'+o+'}}\\small{'+arg+'}$'

#Integralzeichen mit Grenzen und Argument
def igrStyle(u,o,arg):
    return '$\\Large{\\int}_{\\small{'+u+'}}^{\\small{'+o+'}}$'+arg            

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


def plotBar(X, Y, title, pltLine):
    fig = plt.figure(figsize=(4.5, 3))
    plt.bar(X, Y, color='lightblue')
    if pltLine:
        plt.plot(X, Y, '-r', label = '$φ$(X)')
        plt.legend(loc='upper right')
    plt.xlabel("X")
    plt.ylabel("P(X)")
    plt.title(title, fontsize=9)
    return fig

def getPhi(a,b):
    def phi(t):
        return 1/np.sqrt(2*np.pi)*np.exp(-0.5*t**2)
    return quad(phi, a, b)[0]

def rnd(n): #Rundung auf n NK-Stellen, bei 5 an Stelle n+1 auch Aufrunden erlaubt
    return 5*10**(-(n+1))+10**(-(n+10))
 
x, i, n, q  = symbols ('x, i, n, q')


class Übung1(Exercise):
    
    preamble = titel('Grundkurs Stochastik - Teil 6: Satz von Moivre-Laplace und Normalverteilung')+\
                      '\n\n**Willkommen zum Grundkurs Stochastik - Teil 6!**\n\n'+\
                      titel('Übung 6.1',2)
        
    def parameters(self):
        global anz, nList, pList, e, s, x1, x2, x3, x4
        anz = 12
        nList = list(np.arange(0,anz+1))
        pList = []
        e = anz*0.5
        for n in nList:
            pList.append(round((bc.binom(anz, n)*0.5**anz),5))
        s = np.sqrt(anz*0.5**2)
        inp = rd.sample(nList[1:int(anz/2)], 2); inp.sort(); inp.append(nList[anz - inp[0]])
        pInp = []
        for i in inp:
            pInp.append(pList[i])
        #[p1, p2, p3] = pInp
        x1 = rd.choice(nList[4:int(anz/2)]); x2 = rd.choice(nList[-int(anz/2):-4])
        x3 = rd.choice(nList[4:int(anz/2)]); x4 = min(x3 + 4, anz)
        p4 = np.sum(pList[:x1+1])
        p5 = np.sum(pList[x2+1:])
        p6 = np.sum(pList[x3:x4+1])
        x = [x1, x2, x3, x4]
        p = [p4, p5, p6]
        dict1 = {'anz': anz, 'nList': nList, 'pList': pList, 'e': e, 's': round(s,3), 'inp': inp}
        dict1['pPlot'] =  plotBar(nList, pList, 'Münzwurf '+str(anz)+'-mal - Wahrscheinlichkeiten der Zahl-Ergebnisse',0)
        for i in range (4): dict1['x'+str(i+1)] = x[i]
        for i in range (3):
            dict1['P'+str(i+1)] = pInp[i]
            dict1['P'+str(i+4)] = round(p[i],4)
        return dict1

    def problem(self, nList, pList, inp, anz):
        pList_Inp = pList.copy()
        for i in range(len(inp)):
            pList_Inp[inp[i]] = '<<P'+str(i+1)+'_>>'
        args = [["X"]+nList, ["P(X)"]+pList_Inp]
        Tab = [ValTab(args), BlockTab(args)][withHTML()]
        F8_ = Real(atol = rnd(5), widget=Text(width = 8))
        F7_ = Real(atol = rnd(4), widget=Text(width = 7))
        return  Problem ('''<<pPlot>>\n\n
        Eine Münze wird <<anz>>-mal geworfen. Im Balkendiagramm sehen Sie die Wahrscheinlichkeitsverteilung 
        für die Häufigkeit des Ergebnisses *Zahl*.\n\n
        Da es sich um eine $→$ *Bernoulli-Kette* handelt, erhalten wir den Erwartungswert 
        $~~E(X) = <<anz:latex>>\\cdot 0.5 = <<e:latex>>$ und die Standardabweichung
        $~~σ = \\sqrt{<<anz:latex>>\\cdot 0.5\\cdot 0.5} = <<s:latex>>$\n\n
        Die auf 5 NK-Stellen gerundeten Wahrscheinlichkeiten der möglichen Werte der Zufallsgröße sind:'''
        f'''{Tab}\n\nBerechnen Sie nun mit diesen Werten die folgenden Wahrscheinlichkeiten (Genauigkeit >= 4 NK-Stellen):\n\n
        $P(X \\leq <<x1:latex>>)=$ <<P4_>> {sp(5)}
        $P(X$ **>** $<<x2:latex>>)=$ <<P5_>> {sp(5)}
        $P(<<x3:latex>> \\leq X \\leq <<x4:latex>>)=$ <<P6_>>''',
        P1_ = F8_, P2_ = F8_, P3_ = F8_,
        P4_ = F7_, P5_ = F7_, P6_ = F7_
        )       


class Übung2(Exercise):
    
    preamble = titel('Übung 6.2',2)
    
    def parameters(self):
        x1N = round((x1+0.5-e)/s,2); x2N = round((x2+0.5-e)/s,2); x3N = round((x3-0.5-e)/s,2); x4N = round((x4+0.5-e)/s,2)
        phi1 = getPhi(-np.inf,x1N); phi2 = 1 - getPhi(-np.inf,x2N); phi3 = getPhi(x3N, x4N)
        x = [x1, x2, x3, x4]
        phi = [phi1, phi2, phi3]
        dict2 = {'pPlot': plotBar(nList, pList, 'Münzwurf '+str(anz)+'-mal - Wahrscheinlichkeiten der Zahl-Ergebnisse',1)}
        for i in range (4): dict2['x'+str(i+1)] = x[i]
        for i in range (3): dict2['Phi'+str(i+1)] = round(phi[i],4)
        return dict2
    
    def problem(self):
        P_ = Real(atol = rnd(4), widget=Text(width = 7))
        return  Problem (f'''
        Aus dem vorangehenden Beispiel wird klar, dass es etwas mühselig ist, 5 oder mehr Werte aufzusummieren, 
        wenn nach der Wahrscheinlichkeit, dass die Anzahl der Zahl-Würfe in einem bestimmten Intervall liegt, 
        gefragt ist. Es ist daher naheliegend, nach einer Möglichkeit zu suchen, diese Werte durch eine geschlossene Formel 
        wenigstens näherungsweise zu berechnen. Hierbei hilft uns der $→$ *Satz von Moivre-Laplace*, welcher besagt:\n\n'''
        '$\\fbox{Für eine binomialverteilte Zufallsgröße X konvergiert die Wahrscheinlichkeitsverteilung für n → $∞$ '
        'gegen die → Normalverteilung}$\n\n' f'''Das bedeutet, dass wir für hinreichend große n die Binomialverteilung durch die 
        Normalverteilung approximieren können.\n\n<<pPlot>>\n\n
        Die rote Kurve approximiert die Wahrscheinlichkeitsverteilung aus dem vorigen Abschnitt 
        durch die stetige Funktion $φ$(X), wobei hier natürlich wegen des relativ kleinen n die Abweichung noch sehr groß ist. 
        Zur Berechnung der Teilfläche $Φ(x)$ unter der Kurve zwischen $-∞$ und einem Wert $-∞$ < x < $∞$ 
        verwenden wir die $→$ *Gaußsche Summenfunktion*:\n\n
        $Φ(x)=${igrStyle('-∞','x','φ(t)dt')}\n\n
        Mittels der  → *Näherungsformel von Moivre-Laplace* können wir dann die summierten Wahrscheinlichkeiten 
        der binomialverteilten Zufallsgröße X durch die Gaußsche Summenfunktion approximieren. 
        Nach Transformation auf die  → *Standardnormalverteilung* gilt:\n\n'''
        '$P(x_1≤X≤x_2)≈Φ(\\frac{x_2-E(X)}{σ})-Φ(\\frac{x_1-E(X)}{σ})$' f'''{sp(5)}für $n\\cdot p(1-p) > 9$\n\n
        Für kleinere n wird noch eine $→$ *Steigkeitskorrektur* zur Anpassung der diskreten an die stetige 
        Wahrscheinlichkeitsverteilung vorgenommen und es gilt dann:\n\n'''
        '$P(x_1≤X≤x_2)≈Φ(\\frac{x_2+0.5-E(X)}{σ})-Φ(\\frac{x_1-0.5-E(X)}{σ})$' f'{sp(5)}' 
        'für n > $\\frac{1}{4p^2(1-p)^2}$\n\n' '''
        Die Wahrscheinlichkeiten für die im letzten Abschnitt betrachteten Intervalle, 
        die wir einer Tabelle entnehmen können, ergeben sich dann zu (4 NK-Stellen):\n\n
        $P(X≤<<x1:latex>>)≈$ <<Phi1_>>''' f'''{sp(5)}$P(X$ **>** $<<x2:latex>>)=1-P(X≤<<x2:latex>>)≈$ <<Phi2_>>{sp(5)}
        $P(<<x3:latex>>≤X≤<<x4:latex>>)≈$ <<Phi3_>>''',
        Phi1_ = P_, Phi2_ = P_, Phi3_ = P_
        )


class Übung3(Exercise):
    
    preamble = titel('Übung 6.3',2)
    
    def parameters(self):
        n = rd.randint(6, 10)*10
        p = .2#rd.randint(2,8)/10
        e = n*p
        s = np.sqrt(n*p*(1-p))
        [x1, x2] = rd.sample(list(np.arange(int(e-n/10), int(e+n/10))), k=2)
        x3 = rd.randint(int(e/2), int(3*e/2))
        x4 = x3 + rd.randint(int(n/10),min(int(n/2),n))
        x1N = round((x1-e)/s,2); x2N = round((x2-e)/s,2); x3N = round((x3-e)/s,2); x4N = round((x4-e)/s,2)
        phi1 = getPhi(-np.inf,x1N); phi2 = 1 - getPhi(-np.inf,x2N); phi3 = getPhi(x3N, x4N)
        x = [x1, x2, x3, x4]
        phi = [phi1, phi2, phi3]
        dict3 = {'n': n, 'p': p}
        for i in range (4): dict3['x'+str(i+1)] = x[i]
        for i in range (3): dict3['Phi'+str(i+1)] = round(phi[i],4)
        return dict3          

    def problem(self):
        P_ = Real(atol = rnd(4), widget=Text(width = 7))
        return  Problem (f'''
        Vergleichen wir diese Werte mit den oben berechneten Wahrscheinlichkeiten 
        der Binomialverteilung, so können wir trotz des relativ kleinen n 
        eine recht gute Näherung mit Abweichungen maximal in der 3. Nachkomma-Stelle konstatieren. 
        Für größere n erhalten wir - bei gleichem p-Wert - naturgemäss bessere Näherungen.\n\n
        Bestimmen Sie nun mittels der Näherungsformel von Moivre-Laplace folgende Wahrscheinlichkeiten 
        einer Bernoulli-Kette der Länge n = $<<n:latex>>$ mit der Trefferwahrscheinlichkeit p = $<<p:latex>>$ (Genauigkeit >= 4 NK-Stellen):\n\n
        $P(X≤<<x1:latex>>)≈$ <<Phi1_>>{sp(5)}$P(X$ **>** $<<x2:latex>>)=1-P(X≤<<x2:latex>>)≈$ <<Phi2_>>{sp(5)}
        $P(<<x3:latex>>≤X≤<<x4:latex>>)≈$ <<Phi3_>>''',
        Phi1_ = P_, Phi2_ = P_, Phi3_ = P_
        )


class Übung4(Exercise):
    
    preamble = titel('Übung 6.4',2)
    
    def parameters(self):
        p = rd.randint(16,20)
        m1 = rd.randint(300, 500)
        u = rd.randint(-2,1)
        n1 = int(m1*(1+(p+u)/100))
        e = n1*(1-p/100)
        s = np.sqrt(e*p/100)
        phi1 = getPhi(-np.inf, (m1-e)/s)
        m2 = rd.randint(300, 500)
        phi2 = rd.randint(95, 99)/100
        #n2 aus phi2 bestimmen:
        phi2Tab = [[.95, .96, .97, .98, .99],[1.65, 1.76, 1.89, 2.06, 2.33]]
        xTrf = phi2Tab[1][phi2Tab[0].index(phi2)] #transformiertes m2
        a = xTrf*np.sqrt(p); b = m2*100
        z = -a/2+np.sqrt(a**2/4+b) #Wurzel e
        N2 = int(z**2/(100-p))
        return {'p': p, 'n1': n1,  'm1': m1, 'Phi1': round(phi1,3), 'm2': m2, 'phi2': phi2, 'N2': N2}

    def problem(self):
        return Problem (f'''
        Bei einer Fluggesellschaft erscheinen im Mittel $<<p:latex>>$ Prozent der Fluggäste, die einen Platz 
        gebucht haben, nicht zum Abflug. Berechnen Sie mittels der Näherungsformel von Moivre-Laplace:\n\n
        - Die Wahrscheinlichkeit, dass alle erschienenen Passagiere einen Platz finden, 
        wenn für ein $<<m1:latex>>$-sitziges Flugzeug $<<n1:latex>>$ Buchungen vorliegen:\n\n
        {sp(5)}P(X) = <<Phi1_>>$~~~$(Genauigkeit >= 3 NK-Stellen)\n\n
        - Die Anzahl der Buchungen, die für ein $<<m2:latex>>$-sitziges Flugzeug vorgenommen werden darf, 
        damit mit einer Wahrscheinlichkeit von $<<phi2:latex>>$ alle erschienenen Passagiere Platz finden:\n\n 
        {sp(5)}<<N2_>> Buchungen''',
        Phi1_ = Real(widget=Text(width = 6)),
        N2_ = Int(widget=Text(width = 6))
        )
            
    def scores(self, Phi1_, N2_, Phi1, N2):
        sol_ = [Phi1_, N2_]
        sol = [Phi1, N2]
        score1 = 0
        if Phi1_ is not None:
            score1 += round(Phi1_,3) == Phi1
        return {'Phi1_': score1,'N2_': N2_ == N2}

    def feedback(self, Phi1_, N2_, Phi1, N2):
        if sum(list(self.scores(Phi1_, N2_, Phi1, N2).values())) == 2:
            return 'Gut gemacht! Neue Herausforderungen warten im StochastikTutor - Teil 7 auf Sie.'
        return 'Leider nicht alles richtig - Hilfe zum Thema finden Sie '\
               '[hier](https://www.klett.de/inhalt/media_fast_path/32/735310_Stochastik_Satz_von_de_Moivre_Laplace.pdf)'