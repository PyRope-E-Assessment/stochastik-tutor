from pyrope import *

import random as rd
import numpy as np

#Large lightgrey font for preamble
#Large gray font for preamble
def titel(txt, level = 1):
    size = ['Large', 'large', 'normalsize']
    return '$\\color{gray}{\\'+size[level]+'{\\textsf{'+txt+'}}}$'

def rnd(n): #Rundung auf n NK-Stellen, bei 5 an Stelle n+1 auch Aufrunden erlaubt
    return 5*10**(-(n+1))+10**(-(n+10))

ans = ['Alle Wappen kommen einzeln vor',
        'Es gibt entweder keinen oder mehr als einen Block',
        'Wenn ein Block vorkommt, sind nicht alle geworfenen Wappen in diesem enthalten',
        'Wenn einzelne Wappen vorkommen, gibt es keine Blöcke']


class Übung1(Exercise):
    
    preamble = titel('Grundkurs Stochastik - Teil 2: Rechnen mit Wahrscheinlichkeiten')+\
               '\n\n**Willkommen zum Grundkurs Stochastik - Teil 2!**\n\n'+\
               titel('Übung 2.1',2)
    
    def parameters(self):
        def getp(E):
            p = 1
            for x in E:
                p *= (0.25*(x=='b') + 0.75*(x=='r'))
            return p
        E = rd.sample(['rrb', 'rbr', 'brr', 'rbb', 'brb', 'bbr'],3)
        dict1 = {}
        for i in range(len(E)):
            dict1['E'+str(i+1)] = E[i]
            dict1['P'+str(i+1)] = round(getp(E[i]), 3)
        return dict1
   
    def problem(self):
        P_ = Real(atol = rnd(3), widget=Text(width = 8))
        return  Problem ('''
        Wir haben in Teil 1 gelernt, dass Ereignisse durch Mengen beschrieben werden, 
        die alle diejenigen Ergebnisse eines Zufallsversuchs enthalten, die zum Eintreten des 
        jeweiligen Ereignisses führen. Man nennt diese Ergebnisse *günstig* für das Ereignis. 
        Die Wahrscheinlichkeit des Ereignisses ergibt sich dann als Summe 
        der Wahrscheinlichkeiten der in ihm enthaltenen Ergebnisse.\n\n
        Wie berechnet man aber nun die Wahrscheinlichkeit eines Ereignisses, 
        das sich aus mehreren nacheinander ausgeführten Zufallsversuchen ergibt?\n\n
        Dazu ein Beispiel: Ein weiteres bekanntes Modell in der Stochastik 
        ist der *Münzwurf*. Wir werfen eine Münze in die Luft und nehmen an, dass die 
        Wahrscheinlichkeit, dass nach dem Herunterfallen die Seite mit der Zahl 
        bzw. die mit dem Wappen oben liegt, jeweils 0.5 beträgt. 
        Wir werfen nun die Münze dreimal. Wie groß ist die Wahrscheinlichkeit, 
        dass dreimal das Wappen oben liegt?\n\n
        Damit dieses Ereignis eintritt, muss beim ersten Wurf das Wappen oben liegen 
        und beim zweiten und dritten Wurf ebenso.\n\n
        Die Gesamtwahrscheinlichkeit $P(WWW)$ ergibt sich dann zu: $0.5*0.5*0.5 = 0.125$. 
        Die Wahrscheinlichkeit eines Ereignisses, das aus den Ergebnissen mehrerer 
        $voneinander$ $unabhängiger$ Zufallsversuche besteht, ergibt sich also aus dem Produkt  
        der zugehörigen Einzelwahrscheinlichkeiten. Dieses Gesetz heißt *Produktregel der Wahrscheinlichkeitsrechnung*. 
        Die Unabhängigkeit der Ergebnisse ist dabei zwingend vorauszusetzen.\n\n
        Die Produktregel gilt natürlich auch, wenn die Einzelwahrscheinlichkeiten unterschiedlich sind. 
        Dazu betrachten wir noch einmal das Urnenexperiment aus\nTeil 1 mit 6 roten und 2 blauen Kugeln. 
        Wir ziehen jetzt nacheinander 3 Kugeln. Damit die Versuche unabhängig sind, 
        müssen wir die Kugel nach jedem Ziehen wieder zurücklegen. Dann beträgt die Wahrscheinlichkeit 
        dreimal eine rote Kugel zu ziehen $P(rrr) = 0.75^3 = 0.421875$, 
        die für dreimal blau $P(bbb) = 0.25^3 =  0.015625$. \n\n
        Berechnen Sie nun die Wahrscheinlichkeiten (Genauigkeit >=3 NK-Stellen)\n\n
        $P(<<E1:latex>>) = $ <<P1_>>$~~~~~P(<<E2:latex>>) = $ <<P2_>>$~~~~~P(<<E3:latex>>) = $ <<P3_>>''',
        P1_ = P_, P2_ = P_, P3_ = P_
        )

       
class Übung2(Exercise):
    
    preamble = titel('Übung 2.2',2)
    
    def parameters(self):
        global anzW
        anzW = rd.randint(5,7)
        blocks = ['Zweier', 'Dreier', 'Vierer', 'Fünfer', 'Sechser', 'Siebener'][:anzW-2]
        chooseBl = np.sort(rd.sample(list(np.arange(len(blocks))), 3))
        dict2 = {'anzW' : anzW}
        for i in range (3):
            dict2['B'+str(i+1)]  = blocks[chooseBl[i]]
            dict2['M'+str(i+1)]  = anzW - chooseBl[i] - 1
        return dict2
    
    def problem(self):
        M_ = Int(widget=Text(width = 5))
        return  Problem ('''
        Zurück zu unserem Münzwurf-Experiment. Wenn wir die Münze dreimal werfen, 
        kann das Wappen gar nicht, einmal, zweimal oder dreimal oben liegen.\n\n
        Treffen im dritten Fall die beiden Wappen-Ergebnisse unmittelbar nacheinander ein, 
        wollen wir das einen *Zweier* nennen, im vierten Fall haben wir dann einen *Dreier*. 
        Das Ereignis *Zweier* kann somit durch 2 verschiedene Ergebnisse eintreten, 
        nämlich durch "WWZ" oder "ZWW".\n\n
        Wir werfen nun die Münze $<<anzW:latex>>$-mal. Wie viele Möglichkeiten 
        für genau einen $<<B1:latex>>$ gibt es? <<M1_>>\n\n
        Wie viele Möglichkeiten für genau einen $<<B2:latex>>$ ? <<M2_>>$~~~~~$
        Wie viele verschiedene $<<B3:latex>>$ sind möglich? <<M3_>>''',
        M1_ = M_, M2_ = M_, M3_ = M_
        )


class Übung3(Exercise):
    
    preamble = titel('Übung 2.3',2)
    
    def parameters(self):
        PB = round(anzW/2*(anzW-1)/2**anzW, 3)
        return {'anzW': anzW, 'Mgl': 2**anzW, 'PB': PB, 'ans': ans, 'notPB': ans[2]}
    
    def problem(self):
        return  Problem ('''
        Die Wahrscheinlichkeiten der oben formulierten Ereignisse berechnen sich 
        nach der allgemeinen, intuitiv leicht nachvollziehbaren Formel: 
        $~~~\\fbox{P(E) = Anzahl der für E günstigen Ergebnisse / Anzahl aller möglichen Ergebnisse}$\n\n
        Da es bei jedem Münzwurf 2 mögliche Ergebnisse gibt, beträgt die Anzahl 
        der möglichen Ergebnisse beim <<anzW:latex>>-maligen Münzwurf $2^<<anzW:latex>> = <<Mgl:latex>>$.\n\n
        Die Wahrscheinlichkeiten der obigen Ereignisse können Sie nun leicht berechnen. 
        Die oben definierten Zweier, Dreier, etc. wollen wir im folgenden *Blöcke* nennen. 
        Wenn wir nun die Vereinigungsmenge aller möglichen Ereignisse bilden, 
        bei denen mehr als ein Wappen vorkommt und sämtliche geworfenen Wappen unmittelbar nacheinander auftreten, erhalten wir das Ereignis 
        *E: Es kommt genau ein Block vor, der aus allen geworfenen Wappen besteht*.\n\n
        Um die Wahrscheinlichkeit dieses Ereignisses zu berechnen müssen wir eine weitere Rechenregel 
        der Stochastik anwenden, die *Summenregel für Ereignismengen:*\n\n
        $\\fbox{Die Wahrscheinlichkeit der Vereinigung disjunkter Ereignismengen 
        ist die Summe der Wahrscheinlichkeiten dieser Mengen}$\n\n
        Die Wahrscheinlichkeit des Ereignisses E (Genauigkeit >=3 NK-Stellen) beträgt also: 
        $P(E) =$ <<PB_>>\n\n
        Alle übrigen Ergebnisse unseres Zufallsversuches lassen sich dann 
        zum sogenannten *Gegenereignis* ($\\overline{E}$) zusammenfassen. 
        Wir berechnen seine Wahrscheinlichkeit mit der Formel $P(\\overline{E}) = 1 - P(E)$.\n\n
        Versuchen Sie doch einmal, dieses Gegenereignis zu formulieren!\n\n
        <<notPB_>>''',
        PB_ = Real(atol = rnd(3), widget=Text(width = 7)),
        notPB_ = String(widget=RadioButtons(ans[0], ans[1], ans[2], ans[3], vertical=True))
        )
        
    def feedback(self):
        return '''Das Gegenereignis zu E umfasst alle Ergebnisse, die nicht im Ereignis ***E:***
        *Es kommt genau ein Block vor, der aus allen geworfenen Wappen besteht* 
        enthalten sind. Dies sind zunächst einmal alle Ergebnisse bei denen kein Block vorkommt.
        Wenn aber ein Block vorkommt, so ist das Ergebnis genau dann in E enthalten, 
        wenn der Block alle geworfenen Wappen enthält, also in $\\overline{E}$, wenn dies nicht der Fall ist.'''


class Übung4(Exercise):
    
    preamble = titel('Übung 2.4',2)
    
    def parameters(self):
        anzW = rd.randint(2, 3)
        aSum = rd.randint(anzW, anzW*6)
        x = 0
        for i in range (1, 7):
            for j in range (1, 7):
                for k in range (1, 7):
                    if (anzW==2 and i+j==aSum) or (anzW==3 and i+j+k==aSum):
                        x+=1
        p1 = x/6**3
        [r, b, g] = [rd.randint(3,6),rd.randint(3,6), rd.randint(3,6)]
        anzK = np.sum([r, b, g])
        p2 = (r/anzK)**3 + (b/anzK)**3 + (g/anzK)**3
        p3 = (r/anzK)*(b/anzK)*(g/anzK)*6
        [n1, n2] = [rd.randint(2,7),rd.randint(2,7)]
        p4 = 0.5**n1
        p5 = 0.5**n2
        p = [p1,p2,p3,p4,p5]
        for i in range(1, n2+1): p5 -= 0.5**i
        dict4 = {'anzW': anzW, 'aSum': aSum, 'r': r, 'b': b, 'g': g, 'n1': n1, 'n2': n2}
        for i in range(len(p)):
            dict4['P'+str(i+1)] = round(p[i], 3)
        return dict4
    
    def problem(self):
        P_ = Real(widget=Text(width = 6))
        return  Problem ('''
        Zum Abschluss dieses Teils noch ein paar Aufgaben (Genauigkeit jeweils >= 3 NK-Stellen):\n\n
        Die Wahrscheinlichkeit, beim $<<anzW:latex>>$ -maligen Würfeln mit einem idealen Würfel 
        die Augensumme $<<aSum:latex>>$ zu erhalten beträgt <<P1_>>  \n\n
        Eine Urne enthält $<<r:latex>>$ rote, $<<b:latex>>$ blaue und $<<g:latex>>$ gelbe Kugeln. 
        Die Wahrscheinlichkeit, bei dreimaligem Ziehen mit Zurücklegen...\n\n
        - 3 gleichfarbige zu erhalten beträgt <<P2_>>  \n\n
        - 3 verschiedenfarbige zu erhalten beträgt <<P3_>>  \n\n
        Jemand wirft eine Münze so oft, bis einmal *Wappen* oben liegt. 
        Wie groß ist die Wahrscheinlichkeit, dass er...\n\n
        - $<<n1:latex>>$-mal werfen muss? <<P4_>>  \n\n
        - mehr als $<<n2:latex>>$-mal werfen muss? <<P5_>>''', 
        P1_ = P_, P2_ = P_, P3_ = P_, P4_ = P_, P5_ = P_
        )

    def scores(self, P1_, P2_, P3_, P4_, P5_, P1, P2, P3, P4, P5):
        P_ = [P1_, P2_, P3_, P4_, P5_]
        P = [P1, P2, P3, P4, P5]
        dict = {}
        for i in range (len(P)):
            dict['P'+str(i+1)+'_'] = 0
            if P_[i] is not None:
                dict['P'+str(i+1)+'_'] = round(P_[i], 3)==P[i]
        return dict
    
    def feedback(self, P1_, P2_, P3_, P4_, P5_, P1, P2, P3, P4, P5):
        if sum(list(self.scores(P1_, P2_, P3_, P4_, P5_, P1, P2, P3, P4, P5).values())) == 5:
            return 'Glückwunsch! Sie haben auch den 2. Teil des Stochastik-Tutors gemeistert - weiter geht es mit Teil 3.'
        return 'Da hat leider nicht alles gestimmt. Befassen Sie sich doch noch einmal mit den Rechenregeln für Wahrscheinlichkeiten.'
          