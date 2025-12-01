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

def plotBar(aNr,n,p,legende,dir,erL, erR):
    X =list(np.arange(0,n+1))
    Y = []
    for k in X:
        Y.append(bc.binom(n,k)*(p)**(k)*(1-p)**(n-k))
    titel = aNr+'Wahrscheinlichkeitsverteilung '+legende
    fig = plt.figure(figsize=(4.5, 3))
    plt.bar(X, Y, color='lightgreen')
    if dir in ['l', 'lr']:
        plt.bar(X[:erL], Y[:erL], color='red')
    if dir in ['r', 'lr']:
        plt.bar(X[erR+1:], Y[erR+1:], color='red')
    plt.xlabel("X")
    plt.ylabel("P(X)")
    plt.title(titel, fontsize = 9)
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


corpus1 = '''
In Teil 7 haben wir Alternativtests betrachtet, also jeweils 2 Hypothesen gegeneinander getestet und die 
Irrtumswahrscheinlichkeiten unter der Voraussetzung der einen oder der anderen Hypothese berechnet. 
In manchen Fällen besteht jedoch lediglich eine Vermutung darüber, ob die der urprünglichen, 
der Nullhypothese, zugrunde liegende Trefferwahrscheinlichkeit noch besteht oder ob von einer...\n\n
- Fall 1: kleineren\n\n- Fall 2: größeren oder\n\n- Fall 3: einer abweichenden (wobei unklar ist, nach welcher Richtung)\n\n
Trefferwahrscheinlichkeit ausgegangen werden muss.\n\n
Wenn eine Hypothese überprüft werden soll, ohne dass eine Gegenhypothese beziffert werden kann, spricht man von einem 
$→$*Signifikanztest*. Dabei wird die Wahrscheinlichkeit berechnet, mit der bei einem bestimmten Stichprobenresultat 
die Nullhypothese abgelehnt wird, obwohl sie zutreffend ist.\n\nIm Fall 1 wird also berechnet, welcher Teil der Fläche unter der Annahme der 
Nullhypothese links von dem als Entscheidungsregel gewählten, dem sog. $→$*Kritischen Wert* liegt. Man nennt diesen 
Bereich der X-Achse links vom Kritischen Wert auch den $→$*Ablehnungsbereich*: Wenn das Stichprobenresultat 
in diesem Bereich liegt, wird die Nullhypothese abgelehnt und eine kleinere Trefferwahrscheinlichkeit vermutet.\n\n
Die Wahrscheinlichkeit, mit der eine zutreffende Hypothese bei einem gegebenen kritischen Wert 
irrtümlich verworfen werden könnte, heisst  $→$*Signifikanzniveau*. Das Signifikanzniveau beschreibt also  die Wahrscheinlichkeit, 
die für einen Fehler 1. Art gerade noch toleriert werden soll.\n\n
In der folgenden Abbildung 1 ist der Ablehnungsbereich für Fall 1 zur Entscheidungsregel $X$ **<** $<<er:latex>>$ rot markiert.\n\n
<<pPlot1>>\n\nDer Signifikanztest für den Fall 1 heisst $→$*Linksseitiger Test*, der für Fall 2 $→$*Rechtsseitiger Test*.\n\n
Bestimmen Sie das Signifikanzniveau für den in Abb. 1 dargestellten linksseitigen Test! (Genauigkeit >= 4 NK-Stellen)\n\n
α = <<A1_>>\n\n
Will man im Fall 3 nur feststellen, ob ein bestimmter Wert der Zufallsgröße X (noch) eine hinreichende  $→$*Signifikanz* 
aufweist,nohne eine Vermutung über die Richtung einer eventuellen Abweichung anzustellen, führt man einen\\
$→$*Zweiseitigen Test* durch.\n\n
Bestimmen Sie mittels des im Stochastik-Tutor Teil 6 eingeführten Satzes von $→$*Moivre-Laplace* für einen 
zweiseitigen Test mit der Stichprobengröße $n = <<n:latex>>$ und einer Wahrscheinlichkeit $p=\\frac{1}{4}$ den größtmöglichen 
Ablehnungsbereich, bei dem die Irrtumswahrscheinlichkeit kleiner als 5 Prozent ist und berechnen Sie die Irrtumswahrscheinlichkeit α!
Der linksseitige ($K_L$) und der rechtseitige ($K_R$) kritische Wert (Hinweis: Diese gehören selbst nicht zum Ablehnungsbereich!)
sollen dabei symmetrisch zum Erwartungswert liegen. (Genauigkeit >= 4 NK-Stellen)\n\n''' +\
f'$K_L$ = <<KL_>>{sp(5)}$K_R$ = <<KR_>>{sp(5)}α = <<A2_>>'

          
corpus2 = f'''
Die Geschwister Anna und Bernd würfeln täglich um die Entscheidung, wer mit dem Mülleimer-Leeren dran ist: 
Jeder wirft seinen Würfel. Wenn einer von beiden eine 6 würfelt, hat er gewonnen und der jeweils andere muss gehen. 
Bei keiner oder zwei Sechs(en) wird nochmal gewürfelt. Nach ein paar Wochen stellt Anna fest, dass sie 
ungefähr doppelt so oft die 4 Etagen runtersteigen musste wie ihr Bruder und vermutet, dass sein Würfel nicht ganz Ok ist. 
Bernd bestreitet das. Sie einigen sich deshalb auf ein Experiment: Bernd würfelt 120-mal mit seinem Würfel. 
Wenn er häufiger als 30-mal eine 6 erhält, will er künftig einen anderen Würfel benutzen, andernfalls 
will Anna ihren Verdacht, dass mit Bernds Würfel etwas nicht stimmt, fallen lassen.\n\n<<pPlot3>>\n\n
Wie groß ist die Wahrscheinlichkeit, dass bei diesem Versuch der Würfel zu Unrecht als "nicht ideal" erklärt wird?\n\n
P = <<P_>> {sp(5)}(Genauigkeit >= 4 NK-Stellen)'''

corpus3 = f'''
Eine Partei hat bei der letzten Parlamentswahl 40 Prozent Stimmen erhalten und ist nun an der Regierung beteiligt. 
Nach der Wahl hat sie durch einige personelle Fehlbesetzungen und Skandale Sympathien verspielt und es besteht der 
begründete Verdacht, dass sie bei einer Neuwahl deutlich schlechter abschneiden würde. Durch eine Umfrage unter 
200 potenziellen Wählern soll nun eine Prognose über das momentan zu erwartende Wahlergebnis erstellt werden. 
\n\n<<pPlot4>>\n\n
Wenn sich weniger als 75 der Befragten für die Partei entscheiden, beträgt die Wahrscheinlichkeit, 
dass das vorherige Wahlergebnis wieder erreicht würde, höchstens noch\n\n
P = <<P_>> {sp(5)}(Genauigkeit >= 4 NK-Stellen)\n\n
und die Partei startet eine Imagecampagne.'''

corpus4 = f'''
Ein Textildiscounter kann zum Vorzugspreis einen größeren Posten schwarzer und weisser T-Shirts aus Lagerbeständen bekommen. 
Er will das Angebot annehmen, falls die Anzahl der schwarzen und weissen Shirts in etwa gleich ist. Er entnimmt dem Posten 
40 Teile. Falls von jeder Farbe mindestens 15 Stück dabei sind, ordert er die Shirts, ansonsten lehnt er das Angebot ab. 
Wie groß ist die Wahrscheinlichkeit, dass er ein Angebot mit gleichverteilten Farben ablehnt?\n\n
<<pPlot5>>\n\nP = <<P_>> {sp(5)}(Genauigkeit >= 4 NK-Stellen)'''

corpus5 = f'''
Entscheiden Sie, welche Art von Signifikanztest in in den folgenden Fällen angezeigt ist:\n\n
Von einer Übungsaufgabe in Stochastik wird vermutet, dass ca. $<<proz1:latex>>$ Prozent der Studenten sie lösen können. 
Bei der nächsten Prüfung soll festgestellt werden, ob dies mit hoher Wahrscheinlichkeit zutrifft.\n\n
{sp(8)}<<T1_>>\n\n
Ein Pilzberater behauptet, einen giftigen Pilz in $<<proz2:latex>>$ Prozent der Fälle korrekt als giftig klassifizieren zu können. 
Ihm wird eine Anzahl Pilze zur Begutachtung vorgelegt. Wenn er nicht eine bestimmte Mindestanzahl der giftigen Pilze als solche erkennt, 
wird seine Angabe als zu hoch verworfen.\n\n
{sp(8)}<<T2_>>\n\n
Eine neue Studie zur Lernfähigkeit von Schülern besagt, dass in der Regel unter (moderatem) Zeitdruck bessere 
Lernergebnisse erzielt werden als beim Lernen ohne Zeitlimit. Sie widerspricht damit der bislang vorherrschenden Ansicht, 
dass sich Zeitdruck negativ auf das Lernergebnis auswirkt. In einer Testreihe sollen sich nun eine Anzahl Probanden unter 
Zeitdruck eine Liste von Vokabeln einprägen. Die Behaltensrate ohne Zeitdruck beträgt im Schnitt 70 Prozent.\n\n
{sp(8)}<<T3_>>'''

corpus6 = f'''
Führen Sie nun für die eben beschriebenen 3 Fälle die Signifikanztests durch! (Genauigkeit >= 4 NK-Stellen)\n\n
1. An der Prüfung nehmen $<<n1:latex>>$ Studenten teil. Wenn besagte Aufgabe von $<<a1:latex>>$ bis $<<b1:latex>>$ 
Studenten gelöst wird, soll die Behauptung als bestätigt gelten. Berechnen Sie die Irrtumswahrscheinlichkeit $α_1$!\n\n
{sp(8)}$α_1$ = <<P1_>>\n\n
2. Der Pilzberater bekommt $<<n2:latex>>$ Pilze vorgelegt, von denen $<<n3:latex>>$ giftig sind. Wenn er mindestens $<<a2:latex>>$ 
der giftigen als solche erkennt, wird seine Angabe anerkannt. Berechnen Sie die Irrtumswahrscheinlichkeit $α_2$!\n\n
Hinweis: Untersuchen Sie anhand der im StochastikTutor - Teil 6 genannten Kriterien, ob eine Approximation 
durch die Normalverteilung möglich ist und wählen Sie Ihre Berechnungsmethode dementsprechend!\n\n
{sp(8)}$α_2$ = <<P2_>>\n\n
3. Es werden $<<n4:latex>>$ Schülern eine Anzahl Vokabeln vorgelegt und die Behaltensrate mit Zeitlimit erfasst. 
Wenn der Anteil der eingeprägten Vokabeln mindestens $<<a4:latex>>$ Prozent beträgt, soll die neue Studie als bestätigt gelten, 
ansonsten wird wie bisher davon ausgegangen, dass unter Zeitdruck im Schnitt nur 60 Prozent behalten werden. 
Berechnen Sie die Irrtumswahrscheinlichkeit $α_3$!\n\n
{sp(8)}$α_3$ = <<P3_>>'''

###############################################################################################################################

class Übung1(Exercise):
    
    preamble = titel('Grundkurs Stochastik - Teil 8: Signifikanztests')+\
               '\n\n**Willkommen zum Grundkurs Stochastik - Teil 8!**\n\n'+\
               titel('Übung 8.1',2)

    def parameters(self):
        er = rd.randint(5,7)
        n = 30
        X =list(np.arange(0,er))
        alpha1 = 0
        for k in X:
            alpha1 += bc.binom(n,k)*(1/3)**(k)*(2/3)**(n-k)
        pPlot1 = plotBar('Abb. 1: ',n,1/3,'n='+str(n)+', p=1/3','l',er,n)
        n = rd.choice([40, 60, 80])
        p = 1/4
        e = int(n*p)
        s = np.sqrt(e*(1-p))
        for d in range (0, e+1):
            X =list(np.arange(e-d, e+d))
            alpha2 = 0
            for k in X:
                alpha2 += bc.binom(n,k)*(1/4)**(k)*(3/4)**(n-k)
            [a,b] = [(e-d-e)/s, (e+d-e)/s]
            phi = getPhi(a, b)
            if 1-phi < 0.05: break
        [KL, KR] = [e-d, e+d]; 
        pPlot2 = plotBar('Abb. 2: ',n,1/4,'n='+str(n)+', p=1/4','lr',KL,KR)
        return{'er': er, 'A1': round(alpha1,4), 'pPlot1': pPlot1,
               'n': n, 'KL': KL, 'KR': KR, 'A2': round(1-phi,4), 'pPlot2': pPlot2}
        
    def problem(self):
        P_ = Real(atol = rnd(3), widget=Text(width = 9))
        K_ = Int(widget=Text(width = 5))
        return Problem(corpus1, A1_ = P_, KL_ = K_, KR_ = K_, A2_ = P_)
    
    def feedback(self):
        return '<<pPlot2>>'

    
class Übung2(Exercise):
    
    preamble = titel('Übung 8.2',2)

    def parameters(self):
        pPlot3 = plotBar('',120,1/6,'n=120, p=1/6','r',0,31)
        alpha, beta, abs = getAlphaBeta(120, 1/6, 1/6, 31)
        p = alpha
        return {'pPlot3': pPlot3, 'P': round(p,4)}

    def problem(self):
        return Problem(corpus2, P_ = Real(atol = rnd(3), widget=Text(width = 7)))


class Übung3(Exercise):
    
    preamble = titel('Übung 8.3',2)

    def parameters(self):
        pPlot4 = plotBar('',200, 0.4,'n=200, p=0.4','l',75,0)
        alpha, beta, abs = getAlphaBeta(200, .4, .4, 74)
        p = beta
        return {'pPlot4': pPlot4, 'P': round(p,4)}

    def problem(self):
        return Problem(corpus3, P_ = Real(atol = rnd(3), widget=Text(width = 7)))


class Übung4(Exercise):
    
    preamble = titel('Übung 8.4',2)

    def parameters(self):
        pPlot5 = plotBar('',40, 0.5,'n=40, p=0.5','lr',15,26)
        alpha, beta, abs = getAlphaBeta(40, .5, .5, 15)
        p = 2*beta
        return {'pPlot5': pPlot5, 'P': round(p,4)}

    def problem(self):
        return Problem(corpus4, P_ = Real(atol = rnd(4), widget=Text(width = 7)))


class Übung5(Exercise):
    
    preamble = titel('Übung 8.5',2)
    
    def parameters(self):
        global proz1, proz2
        proz1=rd.randint(2, 6)*10
        proz2=rd.randint(95, 97)
        opts = ['linksseitig', 'rechtsseitig', 'zweiseitig']
        return {'proz1': proz1, 'proz2': proz2, 'opts': opts, 'T1': opts[2], 'T2': opts[0], 'T3': opts[1]}
    
    def problem(self, opts):
        R_ = String(widget=RadioButtons(opts[0], opts[1], opts[2], vertical=False))
        return Problem(corpus5, T1_= R_, T2_= R_, T3_= R_)

   
class Übung6(Exercise):
    
    preamble = titel('Übung 8.6',2)
    
    def parameters(self):
        n1 = rd.randint(100, 200)
        a1 = round(proz1/100*n1 - n1/10); b1 = round(proz1/100*n1 + n1/10)
        alpha, beta, abs = getAlphaBeta(n1, proz1/100, proz1/100, a1-1)
        p1 = beta
        alpha, beta, abs = getAlphaBeta(n1, proz1/100, proz1/100, b1)
        p1 += alpha
        n3 = rd.randint(4,6)*10
        n2 = n3*2
        a2 = n3 - 5 - rd.randint(0,proz2<96)
        if n3==50:
            a2 = a2 - rd.randint(0,proz2<97) - rd.randint(0,proz2<96)
        elif n3==60:
            a2 = a2 - rd.randint(0,1) - rd.randint(0,proz2<97) - rd.randint(0,proz2<96)
        a2 = n3-5
        p=proz2/100
        sum = 0
        for i in range (0,a2):
            sum += bc.binom(n3,i)*p**i*(1-p)**(n3-i)
        p2 = sum
        n4 = rd.randint(1,3)*50
        a4 = rd.randint(72 ,75) 
        alpha, beta, abs = getAlphaBeta(n4, 0.6, 0.6, n4*a4/100)
        p3 = alpha
        d0 = {'proz1': proz1, 'n1': n1, 'a1': a1, 'b1': b1, 'P1': round(p1,4),
              'proz2': proz2, 'n2': n2, 'n3': n3, 'a2': a2, 'P2': round(p2, 4),
              'P3': round(p3, 4), 'n4': n4 , 'a4': a4}
        return d0
    
    def problem(self):
        P_ = Real(widget=Text(width = 7))
        return Problem(corpus6, P1_= P_, P2_= P_, P3_= P_)
    
    def scores(self, P1_, P2_, P3_, P1, P2, P3):
        P_  = [P1_, P2_, P3_]
        P  = [P1, P2, P3]
        score = [0, 0, 0]
        for i in range (len(P)):
            if P_[i] is not None:
                score[i] += round(P_[i], 4) == P[i]
        return {'P1_': score[0], 'P2_': score[1], 'P3_': score[2]}
    
    def feedback(self, P1_, P2_, P3_, P1, P2, P3):
        if sum(list(self.scores(P1_, P2_, P3_, P1, P2, P3).values())) == 3:
            return 'Glückwunsch zum erfolgreich bestandenen Abschlusstest! - '\
                   'Sie verfügen nun über solide Grundkenntnisse der Stochastik.'
        return 'Das war noch nicht ganz korrekt! Ein kleines Zusatz-Tutorium zum Thema '\
               '[Signifikanztests](https://studyflix.de/statistik/signifikanztest-2043) '\
               ' wird Ihnen sicher zu den noch fehlenden Kenntnissen verhelfen.'\
               
