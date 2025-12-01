
from pyrope import *

import random as rd
import numpy as np
from fractions import Fraction

#Large gray font for preamble
def titel(txt, level = 1):
    size = ['Large', 'large', 'normalsize']
    return '$\\color{gray}{\\'+size[level]+'{\\textsf{'+txt+'}}}$'

#Several spaces for well-arranged text
def sp(n):
    return '$ '+n*'~'+' $ '

def rnd(n): #Rundung auf n NK-Stellen, bei 5 an Stelle n+1 auch Aufrunden erlaubt
    return 5*10**(-(n+1))+10**(-(n+10))

class Text1(Exercise):
    
    preamble = titel('Grundkurs Stochastik', 0)+\
               '\n\n**Willkommen zum Grundkurs Stochastik!**\n\n'
    
    def problem(self):
        return  Problem ('''
        Zunächst der Begriff: $Stochastik$ kommt aus dem Altgriechischen 
        und bedeutet soviel wie: *Die Kunst des Vermutens*.\n\n
        Die Stochastik befasst sich mit der mathematischen Modellierung zufälliger Ereignisse. 
        Hieraus wird schon klar, dass es sich im Unterschied\nzu anderen Teilgebieten der Mathematik 
        um Ereignisse handelt, deren Ausgang oder Wert im Voraus nicht eindeutig bestimmbar ist. 
        Der Begriff $Ereignis$ spielt übrigens eine zentrale Rolle in der Stochastik.\n\n
        Bereit für die erste Übung?'''
        )
         
    def feedback(self):
        return '👍'
        
    def scores(self):
        return 100


class Übung1(Exercise):
    
    preamble = titel('Grundkurs Stochastik - Teil 1: Ereignisse und Wahrscheinlichkeiten')+\
               '\n\n**Willkommen zum Grundkurs Stochastik - Teil 1!**\n\n'+\
               titel('Übung 1.1')
    
    def parameters(self):
        wTage = {'M': '{Montag, Mittwoch}', 'D': '{Dienstag, Donnerstag}', 
                 'F': '{Freitag}', 'S': '{Sonnabend, Sonntag}'}
        wtKey = rd.choice(list(wTage.keys()))
        wt = wTage[wtKey]
        return {'wtKey' : wtKey, 'wt': wt}
    
    def problem(self, wt):
        return  Problem ('''
        Ereignisse werden in der Stochastik als Mengen angegeben. 
        Das Ereignis *Beim Würfeln fällt eine gerade Zahl* wird also durch die Menge {2, 4, 6} ausgedrückt. 
        Die Elemente einer Ereignismenge nennt man *Ergebnisse* des Zufallsversuchs. In unserem Beispiel sind also 
        2, 4, und 6 die möglichen Ergebnisse des Zufallsversuchs "Würfeln", die zum Ereignis "Gerade Zahl" gehören.\n\n
        Geben Sie nun das Ereignis *Der Name des Wochentages beginnt mit* $<<wtKey:latex>>$ ein: <<wt_>>''',
        wt_ = String(widget=Text(width = 22))
        )

    def scores(self, wt_, wt):
        score = 0
        wt_ = wt_.strip().replace("'",'').replace('"',''); wt = wt.strip().replace("'",'').replace('"','')
        if len(wt_) > 1:
            if wt_[0]=='{' and wt_[-1]=='}': 
                wt_ = wt_[1:-1].split(','); wt = wt[1:-1].split(',')
                wt_ = [x for x in wt_ if x.strip() != ''] #überflüssige LZ und Kommata entfernen
                for i in range (len(wt_)):
                    wt_[i] = wt_[i].strip().replace("'",'').replace('"','')
                for i in range (len(wt)):
                    wt[i] = wt[i].strip().replace("'",'').replace('"','')
                if len(wt_) == 1:
                    wt_ = wt_[0].split(' ') #falls statt Komma ' ' eingegeben wurde
                    wt_ = [i for i in wt_ if i != '']; wt = [i for i in wt if i != '']
                if set(wt_)==set(wt): score = 1
        return (score, 1)
                           
                         
class Übung2(Exercise):
    
    preamble = titel('Übung 1.2')
    
    def parameters(self):
        r = rd.randint(2, 4); b = r * rd.randint(2, 4)
        [r, b] = rd.choice([[r, b], [b, r]])
        pR = round(r/(r+b),3); pB = round(b/(r+b),3)
        F = ['blaue', 'gelbe', 'grüne','rote']
        dictF = {}
        anz = rd.sample([2,3,4,5,6,7,8,9], len(F))
        for i in range (len(F)):
            dictF.update({F[i]: anz[i]})
        sum = np.sum(anz)
        [f1, f2] = rd.sample(F,2)
        [P1, P2] = [dictF[f1]/sum, dictF[f2]/sum]
        dict = {'P1': round(P1,3), 'P2': round(P2,3), 'r': r, 'b': b, 'pR': pR, 'pB': pB, 'f1': f1, 'f2': f2}
        for i in range (len(F)):
            dict['anz'+str(i)] = anz[i]
        return dict
    
    def problem(self):
        return  Problem (f'''
        Wir kommen nun zum nächsten zentralen Begriff der Stochastik, der *Wahrscheinlichkeit*. 
        Die Wahrscheinlichkeit eines zufälligen Ergebnisses unter n Möglichkeiten, 
        die alle gleich wahrscheinlich sind, also wie beim Würfeln mit einem Würfel von perfekter Qualität, 
        dem sog. *idealen Würfel*, ergibt sich zu $\\frac{1}{'n'}$.\n\n
        Neben dem *idealen Würfel* dient auch das *Urnenmodell* als Modell für einen Zufallsversuch: 
        Man greift in eine Urne, also einen Behälter, dessen Inhalt man nicht einsehen kann 
        und nimmt eines der darin befindlichen Objekte (z.B. Kugeln gleicher Größe 
        und Beschaffenheit, aber verschiedener Farbe) heraus.\n\n
        Nehmen wir einmal an, es befinden sich $<<r:latex>>$ rote und $<<b:latex>>$ blaue Kugeln in der Urne.  
        Die beiden möglichen Ergebnisse lauten nun:\n\n
        Ergebnis A: rote Kugel gezogen {sp(5)} Ergebnis B: blaue Kugel gezogen.\n\n
        Die Wahrscheinlichkeiten dieser beiden Ergebnisse sind offensichtlich  nicht gleich, 
        sondern verhalten sich zueinander, wie die Anzahlen der Kugeln gleicher Farbe, 
        bzw. zu 1 wie die Anzahl der Kugeln der Farbe zur Gesamtzahl der Kugeln.\n\n
        Die Wahrscheinlichkeit von Ergebnis A beträgt demnach $<<pR:latex>>$, die von Ergebnis B $<<pB:latex>>$. 
        Man schreibt: $P(A) = <<pR:latex>>$ {sp(5)} $P(B) = <<pB:latex>>$\n\n
        Wir werfen jetzt $<<anz0:latex>>$ blaue, $<<anz1:latex>>$ gelbe, $<<anz2:latex>>$ grüne und $<<anz3:latex>>$ rote Kugeln 
        in eine Urne und greifen einmal hinein. Mit welcher Wahrscheinlichkeit ziehen wir...\n\n
        eine $<<f1:latex>>$ Kugel ? <<P1_>> {sp(5)}
        eine $<<f2:latex>>$ Kugel ? <<P2_>> {sp(5)} (Genauigkeit >= 3 NK-Stellen)''',
        P1_ = Real(atol = rnd(3), widget=Text(width = 7)),
        P2_ = Real(atol = rnd(3), widget=Text(width = 7))
        )
            
            
class Übung3(Exercise):
    
    preamble = titel('Übung 1.3')
    
    def parameters(self):
        d = rd.choice([1,2,3])
        P = [10/36, 8/36, 6/36]
        return {'d': d, 'P': round(P[d-1], 3)}
    
    def problem(self):
        return  Problem (f'''
        In Übung 2 haben wir Ereignisse betrachtet, die jeweils nur ein Ergebnis als Element enthalten. 
        Schauen wir uns jetzt noch einmal das Ereignis "Gerade Zahl" aus Übung 1 an: Es enthält 
        die Ergebnisse 2, 4 und 6, die jeweils eine Wahrscheinlichkeit von $\\frac{1}{6}$ haben. 
        Die Wahrscheinlichkeit des Ereignisses "Gerade Zahl" ergibt sich dann aus der Summe 
        dieser Einzelwahrscheinlichkeiten und beträgt somit 0.5.\\
        Das zugrundeliegende Gesetz heißt *Summenregel der Wahrscheinlichkeitsrechnung*.\n\n
        Berechnen Sie nun mit der Summenregel die Wahrscheinlichkeit des folgenden Ereignisses:\n\n
        In einem Würfelbecher befinden sich 2 ideale Würfel. Ein Wurf ergibt also 2 Zahlen jeweils zwischen 
        1 und 6. Berechnen Sie die Wahrscheinlichkeit des Ereignisses *"Es wurden zwei Zahlen geworfen, 
        deren Differenz $<<d:latex>>$ ist"*.\n\n
        $P$("Differenz ist $<<d:latex>>$") = <<P_>>{sp(5)} (Genauigkeit >= 3 NK-Stellen)''',
        P_ = Real(atol = rnd(3), widget=Text(width = 7))
        )


class Übung4(Exercise):
    
    preamble = titel('Übung 1.4')
    
    def parameters(self):
        def compose (list, a, step): #Set zusammenstellen
            ek = set(); anz = 0
            for i in range (a, n+1, step):
                if i in list:
                    ek.add(i)
                    anz += 1
            e.append(ek); p.append(Fraction(anz, n))
        n = rd.randint(12, 36)
        e = []; p = []
        l = list(np.arange(3, n+1, 3)) #e1
        compose(l, 3, 3)
        l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] #e2
        compose(l, 2, 1)
        l = [1, 4, 9, 16, 25, 36] #e3
        compose(l, 1, 1)
        s = rd.randint(n-11, n-1) #e4
        l = list(np.arange(s+1, n+1))
        compose(l, s+1, 1)
        l = [12, 16, 18, 20, 24, 28, 30, 32, 36] #e5
        compose(l, 12, 2)
        dict = {'n': n, 's' : s, 'sol': e + p}
        for i in range (len(e)):
            dict['E'+str(i+1)] = e[i]
            dict['P'+str(i+1)] = p[i]
        return dict
    
    def problem(self):
        E_ = Set(widget=Text(width = 30))
        P_ = Rational(widget=Text(width = 7))
        return  Problem (f'''
        Zum Abschluss des StochastikTutors - Teil 1 ein kleiner Test:\n\n
        Eine Urne enthält $<<n:latex>>$ Kugeln, die von 1 beginnend aufsteigend durchnummeriert sind. 
        Eine Kugel wird gezogen.\n\nGeben Sie die folgenden Ereignismengen E 
        sowie die zugehörigen Wahrscheinlichkeiten P als rationale Zahlen an: {sp(3)}\n\n
        Die Zahl ist durch 3 teilbar: {sp(3)} E = <<E1_>> {sp(5)} P = <<P1_>>\n\n
        Die Zahl ist eine Primzahl: {sp(3)} E = <<E2_>> {sp(5)} P = <<P2_>>\n\n
        Die Zahl ist eine Quadratzahl: {sp(3)} E = <<E3_>> {sp(5)} P = <<P3_>>\n\n
        Die Zahl ist größer als $<<s:latex>>$: {sp(3)} E = <<E4_>> {sp(5)} P = <<P4_>>\n\n
        Die Zahl hat mindestens 3 nichttriviale Teiler: {sp(3)} E = <<E5_>> {sp(5)} P = <<P5_>>''',
        E1_ = E_, E2_ = E_, E3_ = E_, E4_ = E_, E5_ = E_,
        P1_ = P_, P2_ = P_, P3_ = P_, P4_ = P_, P5_ = P_
        )

    def scores(self, E1_, E2_, E3_, E4_, E5_, P1_, P2_, P3_, P4_, P5_, sol):
        sol_ = [E1_, E2_, E3_, E4_, E5_, P1_, P2_, P3_, P4_, P5_]
        dict = {}
        for i in range (int(len(sol_)/2)):
            dict['E'+str(i+1)+'_'] = sol_[i]==sol[i]
            dict['P'+str(i+1)+'_'] = sol_[i+5]==sol[i+5]
        return dict
  
    def feedback(self, E1_, E2_, E3_, E4_, E5_, P1_, P2_, P3_, P4_, P5_, sol):
        if sum(list(self.scores(E1_, E2_, E3_, E4_, E5_, P1_, P2_, P3_, P4_, P5_, sol).values())) == 10:
            return 'Test erfolgreich absolviert! - Sie können nun mit dem StochastikTutor - Teil 2 weitermachen'
        return 'Sie haben nicht alle Aufgaben richtig gelöst. Befassen Sie sich doch noch einmal mit den Begriffen *Ereignis* und *Wahrscheinlichkeit*!'
