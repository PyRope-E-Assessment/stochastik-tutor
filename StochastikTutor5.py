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
    return '$ '+n*'~'+' $'

#Summenzeichen mit Grenzen und Inhalt
def sumStyle(u,o,arg):
    return '$\\large\\sum\\limits_{\\small{'+u+'}}^{\\small{'+o+'}}\\small{'+arg+'}$'            

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

def rnd(n): #Rundung auf n NK-Stellen, bei 5 an Stelle n+1 auch Aufrunden erlaubt
    return 5*10**(-(n+1))+10**(-(n+10))

x, i, n, q  = symbols ('x, i, n, q')


class Übung1(Exercise):
    
    preamble = titel('Grundkurs Stochastik - Teil 5: Varianz, Standardabweichung und Sigma-Regeln')+\
               '\n\n**Willkommen zum Grundkurs Stochastik - Teil 5!**\n\n'+\
               titel('Übung 5.1',2)
    
    def parameters(self):
        nList = list(np.arange(2,13))
        pList = []
        E = 7
        for n in nList:
            pList.append((round((6 - abs(7-n))/36, 3)))
        v = 0
        for i in range(len(nList)):
            v += (nList[i] - E)**2 * pList[i]
        s = np.sqrt(v)
        inp = rd.sample(nList[:6], 2); inp.sort(); inp.append(nList[10 - nList.index(inp[0])])
        P = []
        for i in range(len(inp)):
            P.append (round( (6 - abs(7-int(inp[i])))/36, 3))
            pList[inp[i]-2] = '<<P'+str(i+1)+'_>>'
        return {'nList': nList, 'pList': pList, 'P1': P[0], 'P2': P[1], 'P3': P[2],
                'E': E, 'V': round(v,3), 'S': round(s,3)}

    def problem(self, nList, pList):
        args = [['$X$']+nList, ['$P(X)$']+pList]
        Tab = [ValTab(args), BlockTab(args)][withHTML()]
        P_ = Real(atol = rnd(3), widget=Text(width = 6))
        return  Problem ('''
        In einem Würfelbecher befinden sich 2 ideale Würfel. 
        Die Zufallsgröße *Augensumme* kann Werte zwischen 2 und 12 annehmen. 
        Ergänzen Sie in der folgenden Tabelle die fehlenden Wahrscheinlichkeiten (3 NK-Stellen)!'''
        +Tab+'''\n\nBestimmen Sie nun den Erwartungswert $E(X)=$ <<E_>>\n\n
        Die Werte der Zufallsgröße X weisen eine mehr oder weniger große Abweichung vom Erwartungswert auf, 
        sie *streuen*. Wir suchen nun ein Maß für diese Streuung. Dafür bilden wir den Erwartungswert 
        (*= gewichteten Mittelwert*) der quadratischen Abweichungen vom Erwartungswert E(X). 
        Er heißt *Varianz* und wird wie folgt gebildet:\n\n
        $V(X) = $'''+sumStyle('i=1','n','(x_i - E(X))^2\\cdot P(x_i)')+sp(5)+
        '''mit den $x_i$ als den n möglichen Werten von X\n\n
        Der Wert $~~σ= \\sqrt{V(X)}~$ heißt *Standardabweichung* von X
        und liefert uns ein Maß für die mittlere zu erwartende Abweichung der Zufallsgröße X 
        vom Erwartungswert. Berechnen Sie!\n\n
        $V(X) =$ <<V_>> $ ~~~~~~~~ σ=$ <<S_>>$~~~$ (Genauigkeit >= 3 NK-Stellen)''',
        P1_ = P_, P2_ = P_, P3_ = P_, E_= P_, V_= P_, S_= P_
        )       


class Übung2(Exercise):
    
    preamble = titel('Übung 5.2',2)
    
    def parameters(self):      
        p = rd.randint(1, 4)/100
        n = rd.randint(5, 8)*100
        E = n*p
        s = np.sqrt(n*p*(1-p))
        return {'p': int(p*100), 'n': n, 'E': E, 'S': round(s,3)}
    
    def problem(self):
        return  Problem ('''
        Im StochastikTutor Teil 3 haben wir eine Formel zur Berechnung des Erwartungswertes 
        bei $→$ *Bernoulli-Experimenten* kennengelernt.\n\nFür diese spezielle Art von Experimenten gibt es auch 
        eine einfache Formel für die Varianz. Sie lautet:\n\n$V(X) =σ^2 = n\\cdot p\\cdot (1-p)$\n\n
        Eine Firma produziert Computermäuse, von denen im Schnitt $<<p:latex>>$ % Ausschuss sind. Die ungeprüften Mäuse 
        werden in Kartons zu je $<<n:latex>>$ Stück verpackt. Wieviele kaputte Mäuse pro Karton sind zu erwarten?\n\n
        <<E_>> Stück\n\n
        Mit welcher Abweichung von diesem Erwartungswert muss man im Schnitt rechnen? (3 NK-Stellen)\n\n
        $σ=$ <<S_>>''',
        E_ = Int(widget=Text(width = 4)),
        S_ = Real(atol = rnd(3), widget=Text(width = 6))
        )

    
class Übung3(Exercise):
    
    preamble = titel('Übung 5.3',2)
    
    def parameters(self):
        anzA = rd.randint(3,5)
        global n, e, s
        n = rd.randint ((anzA-1)*9+1, (anzA-1)*9+10)
        p = 1/anzA
        e = n*p
        s = np.sqrt(n*p*(1-p))
        return {'anzA': anzA, 'n': n, 'E': round(e,3), 'S': round(s,3)}
    
    def problem(self):
        F_ = Real(atol = rnd(3), widget=Text(width = 6))
        return  Problem ('''
        In einem Multiple-Choice-Test gibt es $<<n:latex>>$ Aufgaben, 
        bei denen man von $<<anzA:latex>>$ möglichen Lösungen die (eine) richtige ankreuzen muss.\\ 
        Mit wieviel richtigen Antworten kann jemand rechnen, der die Kreuze rein zufällig setzt? 
        (Genauigkeit >= 3 NK-Stellen)\n\n Zu erwarten sind <<E_>> richtige Antworten\n\n
        Mit welcher Abweichung ist zu rechnen?
        \n\n$σ=$ <<S_>>''',
        E_ = F_, S_ = F_
        )


class Übung4(Exercise):
    
    preamble = titel('Übung 5.4',2)
    
    def parameters(self):
        ab1 = [round(e - s, 3), round(e + s, 3)]
        ab2 = [round(e - 2*s, 3), round(e + 2*s, 3)]
        pc1 = [round(ab1[0]/n*100,1), round(ab1[1]/n*100,1)]
        pc2 = [round(ab2[0]/n*100,1), round(ab2[1]/n*100,1)]
        return {'A1': ab1[0], 'B1': ab1[1], 'A2': ab2[0], 'B2': ab2[1],
                'pc1a': pc1[0], 'pc1b': pc1[1], 'pc2a': pc2[0], 'pc2b': pc2[1], 
                }           
    
    def problem(self):
        F_ = Real(atol = rnd(3), widget=Text(width = 7))
        return  Problem (f'''
        Beim vorigen Beispiel drängt sich eine Frage auf, nämlich die nach der Wahrscheinlichkeit, 
        bei so einem Multiple-Choice-Test auch ohne einen blassen Schimmer vom Stoff nicht durchzufallen. 
        Auf diese interessante Frage gibt es eine Antwort, und zwar in Form der $→$ *Sigma-Regeln*. 
        Diese geben Auskunft über die Wahrscheinlichkeit, mit der bei einem n-fach wiederholten Bernoulli-Experiment, 
        einer sog. $→$ *Bernoulli-Kette*,\nder Wert der binomialverteilten Zufallsgröße 
        in einem bestimmten $σ-$Intervall liegt:\n\n
        Für eine binomialverteilte Zufallsgröße X mit dem Erwartungswert E(X) und der Standardabweichung σ gilt:\n\n
        $P(E(X)-σ \\leq X \\leq E(X)+σ)≈ 0,683${sp(5)}(1σ - Regel)\n\n
        $P(E(X)-2σ \\leq X \\leq E(X)+2σ)≈ 0,954$ (2σ - Regel)\n\n
        $P(E(X)-3σ \\leq X \\leq E(X)+3σ)≈ 0,997$ (3σ - Regel)\n\n
        Berechnen Sie nun mit den Werten aus dem obigen Beispiel, 
        in welchem Intervall die erreichte Punktzahl zu erwarten ist! (3 NK-Stellen)\n\n
        - mit einer Wahrscheinlichkeit von ca. 0,683 gilt: <<A1_>> $ \\leq X \\leq $ <<B1_>>\n\n
        - mit einer Wahrscheinlichkeit von ca. 0,954 gilt: <<A2_>> $ \\leq X \\leq $ <<B2_>>\n\n''',
        A1_ = F_, B1_ = F_, A2_ = F_, B2_ = F_
        )
        
    def feedback(self):
        return '**Fazit:**\nMit einer Wahrscheinlichkeit von ca. $\\frac{2}{3}$ erreichen Sie '+\
               'zwischen <<pc1a>> und <<pc1b>> Prozent der vollen Punktzahl, mit ca. $95$-prozentiger '+\
               'Wahrscheinlichkeit\nhaben Sie zwischen <<pc2a>> und <<pc2b>> % richtig erraten. '+\
               'Die Schlussfolgerung möge jeder für sich ziehen.'


class Übung5(Exercise):
    
    preamble = titel('Übung 5.5',2)
    
    def parameters(self):
        p1 = rd.randint(1,9)/10
        n = rd.randint(1,9)*100
        E = round(n*p1)
        s = np.sqrt(n*p1*(1-p1))
        ab1 = [round(E - s, 3), round(E + s, 3)]
        ab2 = [round(E - 2*s, 3), round(E + 2*s, 3)]
        ab3 = [round(E - 3*s, 3), round(E + 3*s, 3)]
        ab = [ab1, ab2, ab3]
        dict4 = {'p1': p1, 'n': n, 'E': E, 'S': round(s,3)}
        for i in range (len(ab)):
            dict4['A'+str(i+1)] = ab[i][0]
            dict4['B'+str(i+1)] = ab[i][1]
        return dict4

    def problem(self):
        F_ = Real(atol = rnd(3), widget=Text(width = 8))
        return  Problem (f'''
        Ein Bernoulli-Versuch mit der Trefferwahrscheinlichkeit $<<p1:latex>>$ wird $<<n:latex>>$-mal wiederholt. 
        Berechnen Sie Erwartungswert, Standardabweichung und die\nSigma-Intervalle (3 NK-Stellen):\n\n   
        $E(X)=$ <<E_>>{sp(5)}$σ=$ <<S_>>+\n\n
        $1σ-Intervall:$ [<<A1_>> , <<B1_>>]+\n\n
        $2σ-Intervall:$ [<<A2_>> , <<B2_>>]+\n\n
        $3σ-Intervall:$ [<<A3_>> , <<B3_>>]''',
        E_ = F_, S_ = F_, A1_ = F_, B1_ = F_, A2_ = F_, B2_ = F_, A3_ = F_, B3_ = F_
        )


class Übung6(Exercise):
    
    preamble = titel('Übung 5.6',2)
    
    def parameters(self):
        dist = rd.choice([40, 60, 80, 100])
        p2 = rd.choice([0.4, 0.5, 0.8])
        v = rd.randint(1, 3)
        t1 = dist/p2/v
        t2 = rd.randint(int(t1/4), int (t1/2))
        ps = rd.choice([68.3, 95.4, 99.7])
        e = t2*p2*v
        s = np.sqrt(t2*v*p2*(1-p2))
        fak = [68.3, 95.4, 99.7].index(ps) + 1
        ab = [round(e - fak*s), round(e + fak*s)]
        return {'dist': dist, 'p2': p2, 'v': v, 'T1': round(t1), 't2': t2, 'ps': ps, 'A': ab[0], 'B': ab[1]}

    def problem(self):
        F_ = Int(widget=Text(width = 5))
        return  Problem ('''
        Eine Schnecke strebt auf geradliniger Strecke einem saftigen Blatt zu, 
        das sich in $<<dist:latex>>$ cm Entfernung von ihr befindet. Während jeweils einer Minute kommt sie mit einer 
        Wahrscheinlichkeit von $<<p2:latex>>$ um $<<v:latex>>$ cm voran, während sie sich mit einer Wahrscheinlichkeit 
        von $1-<<p2:latex>>$ eine volle Minute ausruht.\n\nNach wieviel Minuten kann sie erwarten, das Blatt zu erreichen? 
        (ganze Min)\n\n Nach <<T1_>> Minuten\n\n
        Auf welchem Teil der Strecke ist sie voraussichtlich nach $<<t2:latex>>$ min mit einer Wahrscheinlichkeit von ca. 
        $<<ps:latex>>$ % zu finden? (ganze cm)\n\n Zwischen <<A_>> und <<B_>> cm Entfernung vom Startpunkt.''',
        T1_ = F_, A_ = F_, B_ = F_
        )
        
    def scores(self, T1_, A_, B_, T1, A, B):
        return {'T1_': T1_==T1, 'A_': A_==A, 'B_': B_==B}
    
    def feedback(self, T1_, A_, B_, T1, A, B):
        if sum(list(self.scores(T1_, A_, B_, T1, A, B).values())) == 3:
            return 'Sehr gut - Sie haben sich für den StochastikTutor - Teil 6 qualifiziert!'
        return 'Das war noch nicht perfekt. Ein Besuch auf [dieser Seite](https://studyflix.de/statistik/sigma-regeln-mathe-6301) könnte helfen.'