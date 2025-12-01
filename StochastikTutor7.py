from pyrope import *

import random as rd
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as bc
from scipy.integrate import quad

#Large gray font for preamble
def titel(txt, level = 1):
    size = ['Large', 'large', 'normalsize']
    return '$\\color{gray}{\\'+size[level]+'{\\textsf{'+txt+'}}}$'

#Several spaces for well-arranged text
def sp(n):
    return '$ '+n*'~'+' $ '

def plotBar(X, Y1, Y2, title, legende, posLeg):
    fig = plt.figure(figsize=(4.5, 3))
    plt.bar(X, Y1, color='lightgreen', label = legende[0])
    plt.bar(X, Y2, color='lightsalmon', label = legende[1])
    plt.legend(loc='upper '+posLeg, fontsize=7)
    for i in range (len(X)):
        if Y1[i]<Y2[i]: break
    for j in range (i, len(X)):
        if Y1[j]>Y2[j]: break
    plt.bar(X[i:j], Y1[i:j], color='lightgreen')
    plt.xlabel("X")
    plt.ylabel("P(X)")
    plt.title(title,fontsize=9)
    return fig
    
def alterTest(n, p1, p2, legende):
    X =list(np.arange(0,n+1))
    Y1 = []; Y2 = []
    for k in X:
        Y1.append(bc.binom(n,k)*(p1)**(k)*(1-p1)**(n-k))
        Y2.append(bc.binom(n,k)*(p2)**(k)*(1-p2)**(n-k))
    titel = 'Wahrscheinlichkeitsverteilung '+legende[0]+' und '+legende[1][-1]
    posLeg = ['left', 'right'][p1+p2<1]
    fig = plotBar(X, Y1, Y2, titel, legende, posLeg)
    return fig

def getPhi(a,b):
    def phi(t):
        return 1/np.sqrt(2*np.pi)*np.exp(-0.5*t**2)
    return quad(phi, a, b)[0]

def getAlphaBeta(n, p1, p2, er):
    e1 = n*p1; s1 = np.sqrt(n*p1*(1-p1))
    alpha = 1-getPhi(-np.inf, (er-1-e1)/s1)
    e2 = n*p2; s2 = np.sqrt(n*p2*(1-p2))
    beta = getPhi(-np.inf, (er-e2)/s2)
    return alpha, beta, np.abs(alpha-beta)

def rnd(n): #Rundung auf n NK-Stellen, bei 5 an Stelle n+1 auch Aufrunden erlaubt
    return 5*10**(-(n+1))+10**(-(n+10))

opts1 = ['Fall 1', 'Fall 2']
opts2 = ['Hypothese 0', 'Hypothese 1']


class Übung1(Exercise):
    
    preamble = titel('Grundkurs Stochastik - Teil 7: Stichproben und Alternativtests')+\
               '\n\n**Willkommen zum Grundkurs Stochastik - Teil 7!**\n\n'+\
               titel('Übung 7.1',2)
               
    def parameters(self):
        global n, r, b, RB
        n = rd.randint(20, 30)
        r = rd.randint(6, n-6)
        e1 = n*1/3; e2 = n* 2/3; s = np.sqrt(n*1/3*2/3)
        p1 = 1 - getPhi(-np.inf, (r-1-e1+0.5)/s)
        p2 = 1 - getPhi(-np.inf, (r-1-e2+0.5)/s)
        b = int(n/2) + (-1)**rd.randint(0,1)*rd.randint(2, int(n/6))
        RB = opts1[b < n/2]
        p3 = bc.binom(n,b)*(2/3)**b*(1/3)**(n-b)
        p4 = bc.binom(n,b)*(1/3)**b*(2/3)**(n-b)
        p = [p1, p2, p3, p4]
        dict1 = {'n': n, 'r': r, 'b': b, 'RB': RB}
        for i in range (4):
            dict1['P'+str(i+1)] = round(p[i],4)
        return dict1

    def problem(self):
        P_ = Real(atol = rnd(4), widget=Text(width = 7))
        return  Problem (f'''
        In einer Urne befinden sich entweder doppelt so viele blaue wie rote (Fall 1), oder 
        doppelt so viele rote wie blaue (Fall 2) Kugeln. Es werden $<<n:latex>>$ Kugeln mit Zurücklegen gezogen. 
        Berechnen Sie für beide Fälle die Wahrscheinlichkeit, mindestens $<<r:latex>>$ rote Kugeln zu ziehen. 
        (Natürlich unter der Voraussetzung, dass die Urne mindestens $<<n:latex>>$ Kugeln von jeder Sorte enthält)\\
        Runden Sie auf 4 NK-Stellen!  Hinweis: Nehmen Sie ggf. eine $~→$Stetigkeitskorrektur vor!\n\n
        Fall 1: P(X≥$<<r:latex>>$) = <<P1_>>{sp(5)}Fall 2: P(X≥<<r:latex>>) = <<P2_>>\n\n
        Die Wahrscheinlichkeit, dass unter den <<n:latex>> Kugeln genau $<<b:latex>>$ blaue sind, beträgt im...\n\n
        Fall 1: P(X=$<<b:latex>>$) = <<P3_>>{sp(5)}Fall 2: P(X=<<b:latex>>) = <<P4_>>\n\n
        Welchen der beiden Fälle würden Sie bei diesem Ergebnis vermuten?{sp(5)}<<RB_>>''',
        P1_ = P_, P2_ = P_, P3_ = P_, P4_ = P_,
        RB_ = String(widget=RadioButtons(opts1[0], opts1[1], vertical=False))
        )       


class Übung2(Exercise):
    
    preamble = titel('Übung 7.2',2)
    
    def parameters(self):
        alterTest(n, 2/3, 1/3, opts1)
        global P1, P2, diff
        alpha, beta, diff = getAlphaBeta(100, 0.2, 0.4, 30)
        P1 = round(alpha,4)
        P2 = round(beta,4)
        diff = round(diff, 4)
        d0 = {'n': n, 'b': b, 'RB': RB, 'P1': P1, 'P2': P2, 'diff': diff,
              'pPlot': alterTest(n, 2/3, 1/3, opts1), 'fbPlot': alterTest(100, 0.2, 0.4, opts2)}
        return d0         
    
    def problem(self, RB):
        P_ = Real(atol = rnd(4), widget=Text(width = 7))
        nb = ['1', '2']; nb.remove(RB[-1]); otherCase = RB[:-1] + nb[0]
        return  Problem (f'''
        Sie haben recht, die $→$Hypothese, dass <<RB:latex>> vorliegt, ist naheliegend. 
        Dennoch können wir die Möglichkeit, dass bei obigem Resultat\nunserer $→$Stichprobe 
        {otherCase} vorliegt, nicht ganz ausschließen.\n\n<<pPlot>>\n\n
        Im Diagramm sehen Sie die Wahrscheinlichkeitsverteilungen der Zufallsgröße: 
        *Bei <<n:latex>>-maligem Ziehen X blaue Kugeln gezogen*\nfür die Fälle 1 und 2 nebeneinander aufgetragen.\n\n
        In vielen Fällen lassen sich die beiden möglichen Fälle nicht so deutlich voneinander trennen, d.h. die 
        Balkendiagramme der beiden Binomialverteilungen liegen dichter beieinander und überlappen sich stärker. 
        Trotzdem ist es möglich, aus einer hinreichend großen Stichprobe Schlussfolgerungen über die zugrunde 
        liegende Verteilung eines Merkmals zu ziehen. Dies erfolgt mittels eines sog. $→$*Alternativtests*. 
        Dazu zunächst ein Beispiel:\n\n
        Die Umfrage eines Marktforschungs-Instituts unter Fernsehzuschauern ergibt, dass die Serie 
        "Liebesglück unter Palmen" von 20 Prozent der Befragten regelmässig geschaut wird. Der Sender behauptet dagegen, 
        dass die Einschaltquote 40 Prozent beträgt. Um Klarheit zu gewinnen, ob es sich für den Waschmittelproduzenten  
        "SuperClean" lohnt, weiterhin seine Spots in den Werbepausen zu platzieren, wird folgender Test durchgeführt: \n\n
        Im Rahmen einer Telefonumfrage werden 100 zufällig ausgewählte Personen befragt. Wenn mindestens 30 Prozent 
        der Befragten angeben, die Serie regelmässig zu schauen, wird angenommen, dass die Aussage des Senders zutrifft und 
        "SuperClean" bleibt dem Sender treu, andernfalls sucht er sich einen anderen Sender mit ähnlichem Programmangebot.\n\n
        Berechnen Sie die Wahrscheinlichkeit P1, dass sich 30 oder mehr Personen als Fans der Serie bezeichnen und 
        der Werbevertrag dem dem Sender somit erhalten bleibt, das Umfrageergebnis des Marktforschungsinstitus jedoch zutrifft, 
        und die Entscheidung somit falsch ist:\n\nP1 = <<P1_>>{sp(5)}(4 NK-Stellen)\n\n
        Weniger als 30 Personen outen sich als Seriengucker und der Sender verliert einen finanzkräftigen Sponsor. 
        Berechnen Sie die Wahrscheinlichkeit P2, dass die vom Sender angegebene Quote trotzdem zutrifft, 
        die Entscheidung gegen den Werbevertrag also falsch ist:\n\nP2 = <<P2_>>{sp(5)}(4 NK-Stellen)''',
        P1_ = P_, P2_ = P_
        )
        
    def feedback(self):
        return '<<fbPlot>>'


class Übung3(Exercise):
    
    preamble = titel('Übung 7.3',2)
    
    def parameters(self):
        a1, b1, diff1 = getAlphaBeta(100, 0.2, 0.4, 29)
        a2, b2, diff2 = getAlphaBeta(100, 0.2, 0.4, 31)
        return {'A1': round(a1, 4), 'B1': round(b1, 4), 'Diff1': round(diff1, 4),
              'P1': P1, 'P2': P2, 'Diff': diff, 'ER': 30,
              'A2': round(a2, 4), 'B2': round(b2, 4), 'Diff2': round(diff2, 4)}
    
    def problem(self):
        P_ = Real(atol = rnd(4), widget=Text(width = 7))
        return  Problem (f'''
        Wenn wie im obigen Beispiel 2 Hypothesen gegeneinander getestet werden sollen, bezeichnet man 
        üblicherweise die ursprüngliche als $→$*Nullhypothese*,\ndie andere als$~→$*Gegenhypothese*. 
        Der Fall, dass die Nullhypothese abgelehnt wird, obwohl sie richtig ist, heisst $→$*Fehler 1. Art*, 
        den Fall, dass die Nullhypothese, obwohl falsch, angenommen wird, nennt man $→$*Fehler 2. Art*.\n
        Die Wahrscheinlichkeit für den Fehler 1. Art wird i. Allg. mit $α$, die für einen Fehler 2. Art mit $β$ 
        bezeichnet. Die Festlegung, ab welchem Stichprobenergebnis man sich für welche Hypothese entscheidet, 
        heisst $→$*Entscheidungsregel*. Von einer $→$*fairen Entscheidungsregel* spricht man, wenn α und β 
        annähernd gleich groß sind, das Risiko eines Irrtums für beide Parteien also in etwa gleich hoch ist.\n\n
        Berechnen Sie nun für die Entscheidungsregeln X≥29 und X≥31 im obigen Beispiel jeweils α und β und entscheiden Sie 
        anhand der Ergebnisse, welche Entscheidungsregel diese Bedingung am besten erfüllt! (Genauigkeit >= 4 NK-Stellen)\n\n
        X ≥ 29:{sp(5)}α = <<A1_>>{sp(5)}β = <<B1_>>{sp(5)}|α - β| = <<Diff1_>>\n\n
        X ≥ 30:{sp(5)}α = P1 = <<P1>>{sp(7)}β = P2 = <<P2>>{sp(8)}|α - β| = <<Diff_>>\n\n
        X ≥ 31:{sp(5)} α = <<A2_>>{sp(5)}β = <<B2_>>{sp(5)}|α - β| = <<Diff2_>>\n\n
        Die Entscheidungsregel X ≥ <<ER_>> erfüllt die Fairness-Bedingung am besten.''',
        A1_ = P_, B1_ = P_, A2_ = P_, B2_ = P_, Diff1_ = P_ , Diff_ = P_, Diff2_ = P_, ER_ = Int(widget=Text(width = 4))
        )


class Übung4(Exercise):
    
    preamble = titel('Übung 7.4',2)
    
    def parameters(self):
        n = rd.randint(4, 10)*10
        p1 = rd.randint(2, 7)
        p2 = p1 + rd.randint(1, min(3, 9-p1))
        p1 = p1/10; p2 = p2/10
        i = int((p1+p2)/2 * n) - 8
        alpha, beta, abs = getAlphaBeta(n, p1, p2, 1)
        lastAbs = 1.1
        while lastAbs > abs:
            lastAbs = abs
            alpha, beta, abs = getAlphaBeta(n, p1, p2, i)
            i+=1
        ER = i-2
        alpha, beta, abs = getAlphaBeta(n, p1, p2, ER)
        return {'n': n, 'p1': p1, 'p2': p2, 'ER': ER, 'A': round(alpha,4), 'B': round(beta,4), 'fbPlot': alterTest(n, p1, p2, opts2)}
    
    def problem(self):
        P_ = Real(atol = rnd(4), widget=Text(width = 7))
        return  Problem (f'''
        Die Hypothese H0: p = $<<p1:latex>>$ soll gegen die Hypothese H1: p = $<<p2:latex>>$ mit einem Stichprobenumfang 
        von n = $<<n:latex>>$ getestet werden. Bestimmen Sie die Entscheidungsregel mit optimal ausgewogenen 
        Irrtumswahrscheinlichkeiten und geben Sie α und β an!\n\n
        Wenn X ≥ <<ER_>> gilt, soll angenommen werden, dass Hypothese H1 zutrifft.\n\n
        α = <<A_>>{sp(5)}β = <<B_>>{sp(5)}(Genauigkeit >= 4 NK-Stellen)''',
        A_ = P_, B_ = P_, ER_ = Int(widget=Text(width = 4))
        )
        
    def feedback(self):
        return '<<fbPlot>>'


class Übung5(Exercise):
    
    preamble = titel('Übung 7.5',2)
    
    def parameters(self):
        n = rd.randint (3, 5)*100
        t1 = rd.randint (50, 60)
        t2 = t1 + rd.randint (5, 8)
        m0 = int((t1+t2)/200*n)
        alpha, beta, nn = getAlphaBeta(n, t1/100, t2/100, m0)
        p1 = alpha
        m = m0
        while p1 > 0.01:
            p1, p2, nn = getAlphaBeta(n, t1/100, t2/100, m)
            m+=1
            m1 = rd.randint(m+20, min(m+30,n-10))
        t3 = t2 + int((m1-m)/n*100)
        for i in range (m1-100, n, 10):
            p3, p4, nn = getAlphaBeta(n, t2/100, t3/100, i)
        p3, p4, nn = getAlphaBeta(n, t2/100, t3/100, m1)
        e = ['J', 'N'][p3>=0.01]
        return {'n': n, 't1': t1, 't2': t2, 'A': round(alpha,4), 'B': round(beta,4),
                'm0': m0, 'm1': m1, 't3': t3, 'E': e, 'p4': round(p4,4), 'M': m-1}

    def problem(self):
        P_ = Real(treat_none_manually=True, widget=Text(width = 7))
        return  Problem (f'''
        Die Wirksamkeit eines Medikamentes ist mit $<<t1:latex>>$ %  belegt. Nach einer Weiterentwicklung wird 
        vom Hersteller eine verbesserte Wirksamkeit\nvon nunmehr $<<t2:latex>>$ % angegeben. 
        Bei einer Prüfung durch ein unabhängiges Institut werden $<<n:latex>>$ Probanden mit dem 
        Mittel behandelt.\nAb einer nachgewiesenen Wirksamkeit bei  $<<m0:latex>>$ Probanden 
        soll die Angabe des Herstellers als bestätigt gelten. Berechnen Sie (Genauigkeit >= 4 NK-Stellen):\n\n
        - den Fehler 1. und 2. Art:\n\n
        {sp(5)}α = <<A_>>{sp(5)}β = <<B_>>\n\n
        - wie groß muss die geforderte Mindestzahl m von Probanden mit nachgewiesener Wirksamkeit sein, 
        damit man mit 99-prozentiger Sicherheit davon ausgehen kann, dass die neue, höhere 
        Wirksamkeit zutrifft?\n\n
        {sp(5)}m = <<M_>>\n\n
        - das Medikament zeigt bei $<<m1:latex>>$ Probanden die erwünschte Wirkung. Kann man nun mit einer 
        Irrtumswahrscheinlichkeit von weniger als 1 % davon ausgehen, dass die tatsächliche Wirksamkeit 
        statt $<<t2:latex>>$ % sogar $<<t3:latex>>$ % beträgt?\n\n{sp(5)}<<E_>>''',       
        A_ = P_, B_ = P_, M_ = Int(widget=Text(width = 4)),
        E_ = String(widget=RadioButtons('J', 'N', vertical=False))
        )

    def scores(self, A_, B_, M_, E_, A, B, M, E):
        P_ = [A_, B_]
        P = [A, B]
        score = [0, 0]
        for i in range (len(P)):
            if P_[i] is not None:
                score[i] += round(P_[i],4) == P[i]
        return {'A_': score[0], 'B_': score[1], 'M_': M_==M, 'E_': E_==E}

    def feedback(self, A_, B_, M_, E_, A, B, M, E):
        if sum(list(self.scores(A_, B_, M_, E_, A, B, M, E).values())) == 4:
            return 'Respekt - Sie haben auch die nicht ganz einfachen Aufgaben dieses Teils gemeistert '\
                    'und können mit Zuversicht den StochastikTutor - Teil 8 angehen.'
        return 'Da hat leider noch nicht alles gestimmt - [hier](https://learnattack.de/schuelerlexikon/mathematik/alternativtest) gibt es Hilfe.'
   
