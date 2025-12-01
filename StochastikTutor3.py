from pyrope import *

import random as rd
import scipy.special as bc
from sympy import symbols, simplify

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

def rnd(n): #Rundung auf n NK-Stellen, bei 5 an Stelle n+1 auch Aufrunden erlaubt
    return 5*10**(-(n+1))+10**(-(n+10))

x, i, n, q  = symbols ('x, i, n, q')


class Übung1(Exercise):
    
    preamble = titel('Grundkurs Stochastik - Teil 3: Erwartungswerte')+\
               '\n\n**Willkommen zum Grundkurs Stochastik - Teil 3!**\n\n'+\
               titel('Übung 3.1',2)
    
    def parameters(self):
        def EW(p, n):
            e = 0
            for i in range (1,n+1):
                e += i*p**i*(1-p)**(n-i)*bc.binom(n,i)
            return round(e,3)
        formel = '$1*0.6*0.4^2*3 + 2*0.6^2*0.4*3 + 3*0.6^3$'
        res1 = EW(0.6,3)
        n1 = rd.randint(4, 7)
        p2 = rd.choice([3,4,5,7,8,9])/10
        nList = [2, 3, 4, 5, 6, 7]
        nList.remove(n1)
        n2 = rd.choice(nList)
        E1 = EW(0.6, n1)
        E2 = EW(p2, n2)
        return {'P1': round((5/6)**3,3), 'formel': formel, 'res1': res1,
                'n1': n1, 'p2': p2, 'n2': n2, 'E1': E1, 'E2': E2}

    def problem(self):
        P_ = Real(atol = rnd(3), widget=Text(width = 8))
        return  Problem (f'''
        In Teil 2 haben wir Wahrscheinlichkeiten von Ereignissen berechnet, 
        die aus mehrfach hintereinander ausgeführten Zufallsversuchen entstehen.\n\n
        So können wir z.B. berechnen, wie groß die Wahrscheinlichkeit ist, 
        bei dreimaligem Würfeln keine 6 zu erhalten, ein Fall der beim 
        *Mensch-äger-dich-nicht-Spiel* regelmässig für Verstimmung sorgt.\n\n
        $P(3-mal$ $keine$ $6) =$ <<P1_>> (3 NK-Stellen)\n\n
        Da hat sich sicher jeder schon einmal verärgert gefragt: Wie oft muss ich denn noch würfeln, 
        um endlich die zum Einsetzen meiner Figur erforderliche 6 zu bekommen? 
        Die Antwort lautet: Man kann es nicht sagen, zwischen 1 und unendlich ist alles möglich, 
        nur eben mit unterschiedlicher Wahrscheinlichkeit.\n\nWir können jedoch eine Aussage darüber treffen, 
        wie oft man *erwarten* kann, würfeln zu müssen, um die ersehnte 6 zu bekommen. 
        Und hier kommt der Begriff *Erwartungswert* ins Spiel. Er ist definiert als der *durchschnittlich 
        zu erwartende Wert einer Zufallsgröße X bei häufiger Wiederholung des Zufallsversuchs* 
        und berechnet sich nach der Formel \n\n $E(X)=$ {sumStyle('i=1','n','x_i*P(X=x_i)')} {sp(5)}
        wobei die $x_i$ die möglichen Werte der Zufallsgröße X sind.\n\n
        Dazu zunächst ein einfaches Beispiel (Die Auflösung der uns alle bewegenden Würfelfrage 
        erfolgt am Ende dieses Tutoriums). Ein Basketballspieler trifft den Korb mit einer 
        Wahrscheinlichkeit von 0.6. Er wirft dreimal. Wieviele Treffer sind zu erwarten? 
        Die Formel dazu lautet:\n\n$E(X)=$<<formel:latex>>$=<<res1:latex>>$\n\n
        Berechnen Sie nun die Erwartungswerte der Zufallsgrößen\n\n
        X1: Der Spieler wirft $<<n1:latex>>$-mal {sp(5)} E(X1) = <<E1_>>\n\n
        X2: Der Spieler hat eine Trefferwahrscheinlichkeit von $<<p2:latex>>$ und wirft 
        $<<n2:latex>>$-mal {sp(5)} E(X2) = <<E2_>>''',
        P1_ = P_, E1_ = P_, E2_ = P_
        )       

     
class Übung2(Exercise):
    
    preamble = titel('Übung 3.2',2) 
    
    def parameters(self):       
        def mkRands():
            r = rd.randint(2, 9)
            b = rd.randint(2, 9)
            w = rd.randint(2, 9)
            e = rd.randint(1, 3)
            n = rd.randint(2, min(r, b, w))
            g = rd.randint(e+2, 3*e)
            return [r, b, w, e, n, g]
        rands = []; ew = []
        rands1 = [r, b, w, e, n, g] = mkRands()
        rands.append(rands1)
        pR = 1; pB = 1
        for i in range (n):
            pR *= (r-i)/(r-i+b)
            pB *= (b-i)/(b-i+r)
        ew.append((pR + pB)*g - e)
        rands2 = [r, b, w, e, n, g] = mkRands()
        rands.append(rands2)
        ew.append(6*(r*b*w)/((r+b+w)*(r+b+w-1)*(r+b+w-2)) * g - e)
        rands3 = [r, b, w, e, n, g] = mkRands()
        rands.append(rands3)
        ew3 = - e
        p = r/(r+w)
        for i in range (w):
            p *= (w-i)/(r+w-i-1)
            ew3 += (i+1) * p
        ew.append(ew3)
        dict2 = {}
        for i in range (3):
            dict2['rands'+str(i+1)] = rands[i]
            dict2['E'+str(i+1)] = round(ew[i], 3)
        return dict2

    def problem(self, rands1, rands2, rands3):
        [r1, b1, w1, e1, n1, g1] = rands1
        [r2, b2, w2, e2, n2, g2] = rands2
        [r3, b3, w3, e3, n3, g3] = rands3
        E_ = Real(atol = rnd(3), widget=Text(width = 7))
        return  Problem (f'''
        Aufgabe dieses Tutoriums kann es nicht sein, alle theoretischen Grundlagen 
        der Stochastik ausführlich darzulegen. Diejenigen für das Verständnis erforderlichen 
        Grundbegriffe, die in diesem Rahmen nicht erklärt werden können, sind deshalb im Folgenden mit 
        $→$ gekennzeichnet.\nBitte eignen Sie sich die entsprechenden Kenntnisse selbstständig an.\n\n
        Sicher ist Ihnen aufgefallen, dass in den beiden letzten Übungen der Erwartungswert immer 
        das Produkt aus Trefferwahrscheinlichkeit p und Anzahl der Versuche n ist. 
        Das liegt daran, dass es sich hier um sog. $→$ *Bernoulli-Experimente* mit 
        $→$ *binomialverteilten Zufallsgrößen* handelt. Bei diesen gilt immer $E(X) = p * n$.\n\n
        Eine andere Art von Zufallsexperimenten kann durch das folgende Modell beschrieben werden:\n
        In einer Urne befinden sich 4 rote und 2 blaue Kugeln. Ein Spieler darf nach einem 
        Einsatz von 1 €{sp(3)}2 Kugeln ohne Zurücklegen ziehen. Wenn er 2 rote Kugeln zieht, 
        gewinnt er 2 €. Kann er erwarten, bei diesem Spiel auf lange Sicht reich zu werden, oder 
        verzockt er seine bescheidenen Ersparnisse?\n\n
        $Lösung:$\nDie Wahrscheinlichkeit, bei zweimaligem Ziehen 2 rote Kugeln zu erhalten, 
        beträgt {sp(3)} $\\frac{4}{6} * \\frac{3}{5} = 0.4$. Multipliziert mit dem Gewinn im Erfolgsfall 
        ergibt sich ein zu erwartender Gewinn von 0.8 €, von dem wir zur Beantwortung der obigen Frage noch 
        den Einsatz von 1 € abziehen müssen. Wir erhalten dann einen zu erwartenden Reingewinn von 
        $-$0.2 € und müssen feststellen, dass besagtes Spiel ein Verlustgeschäft für den Spieler ist.\n\n
        Berechnen Sie nun folgende Erwartungswerte für den Reingewinn des Spielers (Genauigkeit >= 3 NK-Stellen):\n\n
        In der Urne befinden sich ${r1}$ rote und ${b1}$ blaue Kugeln. Der Einsatz beträgt ${e1}$ €. 
        Der Spieler darf ${n1}$ Kugeln ohne Zurücklegen ziehen.\n
        Wenn er ${n1}$ gleichfarbige Kugeln zieht, winkt ein Gewinn von ${g1}$ €.\n\n$E(X) =$ <<E1_>>\n\n
        Die Urne enthält ${r2}$ rote, ${b2}$ blaue und ${w2}$ weisse Kugeln. 
        Der Einsatz beträgt ${e2}$ €. Wenn nach 3-maligem Ziehen ohne Zurücklegen von jeder Farbe 
        eine Kugel draußen liegt, wird ein Gewinn von ${g2}$ € ausgezahlt.\n\n$E(X) =$ <<E2_>>\n\n
        Die Urne enthält jetzt ${r3}$ rote und ${w3}$ weisse Kugeln. Der Einsatz beträgt ${e3}$ €. 
        Wenn der Spieler eine weisse Kugel zieht, darf er erneut in die Urne greifen, andernfalls ist 
        das Spiel beendet und der Spieler erhält so viele Euro, wie weisse Kugeln draußen liegen.\n\n
        $E(X) =$ <<E3_>>''',
        E1_ = E_, E2_ = E_, E3_ = E_
        )


class Übung3(Exercise):
    
    preamble = titel('Übung 3.3',2) 
    
    def parameters(self):
        anz1 = rd.randint(1,10)*1000
        a = rd.randint(1,5)
        ar = rd.randint(88,99)
        af = rd.randint(2,8)
        anz3 = anz1*a/100*(1-ar/100)
        anz4 = anz1*(1-a/100)*af/100
        anz2 = anz3 + anz1*(1-a/100)*(1-af/100)        
        return {'Anz1': anz1, 'Anz2': round(anz2,3), 'Anz3': round(anz3,3), 'Anz4': round(anz4,3), 'a': a, 'ar': ar, 'af': af}
    
    def problem(self):
        Anz_ = Real(atol = rnd(3), widget=Text(width = 7))
        return  Problem ('''
        Dass der Erwartungswert nicht nur beim Spielen eine Bedeutung hat, 
        erschließt sich aus diesem Beispiel:\n
        In einer Fabrik werden Bauteile hergestellt, bei denen eine gewisse Normabweichung in der Größe 
        toleriert werden kann, während Teile mit größeren Abweichungen ausgesondert werden müssen. 
        Erfahrungsgemäss weisen ca. $<<a:latex>>$% aller produzierten Teile eine Abweichung oberhalb 
        der Toleranzgrenze auf. Die Bauteile werden deshalb vor Auslieferung automatisch kontrolliert, 
        wobei im Schnitt $<<ar:latex>>$% der auszusondernden, aber auch $<<af:latex>>$% der verwendbaren Bauteile 
        als nicht tolerierbar eingestuft werden.\n\nIn einer Schicht werden $<<Anz1:latex>>$ Teile geprüft.\n\n
        Wie viele werden erwartungsgemäss als brauchbar eingestuft? <<Anz2_>>\n\n
        Bei wie vielen davon muss man davon ausgehen, dass sie in Wirklichkeit Ausschuss sind?  
        <<Anz3_>>\n\n
        Wie viele brauchbare landen voraussichtlich im Ausschuss? <<Anz4_>>\n\n
        Runden Sie jeweils auf mindestens 3 NK-Stellen.''',
        Anz2_ = Anz_, Anz3_ = Anz_, Anz4_ = Anz_
        )


class Übung4(Exercise):
    
    preamble = titel('Übung 3.4',2)
    
    def parameters(self):
        p1 = 5/36
        anz = rd.randint(4,6)
        p2 = (5/6)**(anz-1)*1/6
        options = [[2, 2, 1.5, 50],[3, 4, 1.5, 50],[7, 4, 0.6, 40],[15, 3, 0.2, 80],
                   [17, 5, 0.3, 70],[20, 4, 0.2, 80],[25, 5, 0.2, 80]]
        par = rd.choice(options) #[anzSectors, startPrize, ew, profit]
        return {'P1': round(p1,3), 'anz': anz, 'P2':round(p2,3), 'P3': 5**(n-1)/6**n,
                'aS': par[0], 'fP': par[1], 'E': par[2]+par[3]/100, 'pr': par[3]}
   
    def problem(self):
        F_ = Real(widget=Text(width = 6))
        return  Problem ('''
        Zum Abschluss dieses Tutoriums betrachten wir noch ein Spiel: 
        Ein Glücksrad sei in 24 gleichgroße Sektoren eingeteilt, 
        die mit den Zahlen 1 - 24 beschriftet sind. Ein Spieler darf 
        nach Entrichten eines Einsatzes am Rad drehen. Bleibt das Rad auf 
        einer geraden Zahl stehen, erhält er einen Euro und darf noch einmal drehen. 
        Bei einer ungeraden Zahl ist das Spiel beendet. Wie hoch muss der Einsatz des Spielers 
        sein, damit der Betreiber mit einer Einnahme von 50 Cent pro Spiel rechnen kann? 
        Hierzu berechnen wir wieder den Erwartungswert des Gewinns, den der Spieler 
        mit nach Hause nehmen kann. Er setzt sich zusammen aus den Gewinnen von je 1 €, 
        multipliziert mit den Wahrscheinlichkeiten für ein Spielende nach dem zweiten, dritten usf. 
        Drehen. Wir erhalten also mit $~~E(X) = 1*\\frac{1}{2} + 1*\\frac{1}{4} + 1*\\frac{1}{8} + ...~~~~$ 
        eine Summe mit unendlich vielen Summanden, da es rein theoretisch möglich ist, 
        dass das Rad nach jedem Drehen auf einer geraden Zahl stehen bleibt. 
        (Von den praktischen Beschränkungen durch Materialermüdung, Lebenserwartung oder 
        behördliche Vorgaben zur Dauer von Volksfesten wollen wir einmal absehen). 
        Wir erhalten also für E(X) eine unendliche Reihe:\n\n
        $E(X)=$'''+sumStyle('i=0','∞','1*(\\frac{1}{2})^i')+''' \n\n
        Ergänzen wir nun noch den Summanden für i=0, also 1, so erhalten wir eine 
        $→$ *Geometrische Reihe*, die gegen 2 konvergiert, daher:\n\n
        $E(X)+1=$'''+sumStyle('i=1','∞','1*(\\frac{1}{2})^i')+''' , also: $E(X) = 1~~~~$ 
        Damit kann bei einem Einsatz von 1,50 € der Glücksrad-Betreiber 
        die gewünschte Einnahme erwarten.\n\nNun sind Sie noch einmal am Zug:\n\n
        Ein Spieler würfelt so lange, bis er eine 6 erhält. Berechnen Sie die 
        Wahrscheinlichkeiten für die zufälligen Ereignisse (Genauigkeit >= 3 NK-Stellen)\n\n
        E1: Er muss zweimal würfeln <<P1_>>\n\n
        E2: Er muss $<<anz:latex>>$-mal würfeln <<P2_>>\n\n
        E3: Er muss n-mal würfeln <<P3_>>\n\n
        Das Glücksrad hat jetzt $<<aS:latex>>$ gleichgroße Sektoren, die mit 1 - <<aS:latex>> beschriftet sind. 
        Der Spieler muss einen bestimmten Einsatz zahlen und darf 2-mal drehen.\n
        Fällt beide Male die gleiche Zahl, hat er $<<fP:latex>>$ € gewonnen und darf so oft weiter drehen, 
        bis zum erstenmal eine andere Zahl erscheint.\nBis dahin erhält er für jede weitere gleiche Zahl noch einen Euro.\n
        Der Betreiber möchte pro Spiel einen Gewinn von $<<pr:latex>>$ Cent erwarten dürfen. 
        Wie hoch muss der Einsatz sein?\n\nDer Einsatz muss <<E_>> € betragen.''',
        P1_  = F_, P2_  = F_, P3_  = Expression(symbols='n', widget=Text(width = 25)), E_ = F_ 
        )

    def scores(self, P1_, P2_, P3_, E_, P1, P2, P3, E):
        sol_ = [P1_, P2_, P3_, E_]
        sol = [P1, P2, P3, E]
        score = [0, 0, 0, 0]
        for i in [0, 1, 3]:
            if sol_[i] is not None:
                score[i] = round(sol_[i],3) == sol[i]
        if P3_ is not None:
            score[2] = simplify(P3_ - P3)==0
        return {'P1_': score[0], 'P2_': score[1], 'P3_': score[2], 'E_': score[3]}

    def feedback(self, P1_, P2_, P3_, E_, P1, P2, P3, E):
        if sum(list(self.scores(P1_, P2_, P3_, E_, P1, P2, P3, E).values())) == 4:
            return 'Sehr gut - Sie haben den Test bestanden und dürfen mit dem StochastikTutor - Teil 4 weitermachen!'
        return 'Dieses Thema bereitet Ihnen offenbar noch Schwierigkeiten. '\
               'Hilfe finden Sie [hier](https://studyflix.de/mathematik/erwartungswert-1648).'


class Auflösung(Exercise):

    def parameters(self):
        return {'bruch1': 1/(1-q), 'bruch2': q/(1-q)**2, 'ef': '\\frac{1}{5}', 'fs': '\\frac{5}{6}'}        
    
    def problem(self):
        return Problem (f'''
        Nun noch die Auflösung der anfangs aufgeworfenen 6er-Würfel-Frage:\n\n
        Um den Erwartungswert für die Anzahl der nötigen Versuche zu berechnen, 
        müssen wir die mit i multiplizierten Wahrscheinlichkeiten für i-maliges Würfeln 
        addieren und erhalten so wieder eine unendliche Reihe: \n\n
        $<<ef:latex>>$ {sumStyle('i=1','∞','i *(<<fs:latex>>)^i')} \n\n
        Die Summenformel dieser $→$ *Variante einer geometrischen Reihe* erhalten wir 
        durch Ableiten der Geometrischen Reihe\n\n
        {sumStyle('i=0','∞','q^i')} $= <<bruch1:latex>>$ {sp(5)} für |q| < 1 {sp(5)} nach q:\n\n
        {sumStyle('i=0','∞','iq^i')} $=q$ {sumStyle('i=0','∞','iq^{i-1}')} $= <<bruch2:latex>>$ {sp(5)} für |q| < 1\n\n 
        und damit in unserem Fall: $<<ef:latex>> * <<fs:latex>> * 6^2 = 6$\n\n
        Von Pech im Spiel sollten wir also berechtigterweise erst ab dem 7. vergeblichen Versuch sprechen.'''
        )

    def scores(self):
        return 6