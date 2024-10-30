import random
import matplotlib.pyplot as plt
import time

TotalAIMoney=[]

TotalAINumber=100000
HandsPlayed=1000
AIsDisplayed=5

RiskFactor=4
OriginalBet=62.5

StartingMoney=1000
DealerHand=[]
AIHand=[]
DealerHandF=[0]
HandNumber=0
AIMoney=StartingMoney
AmountBet=0
TurnOver=0
Bust=0
DealerTurnOver=0
AIHandSum=0
DealerHandSum=0
SplitCheck=0
SplitCheck1=0
Win=0
AINumber=0
AverageAIMoney=0
Above1000Checker=0
DealerFirstCard=[]
FirstHandCheck=0
EndingMoney=2000
DoubleDownCheck=0
BettingClosed=0
DoubleWin=0



def BettingRules():
    global AIMoney, OriginalBet, RiskFactor, AmountBet, HandsPlayed, HandNumber, TurnOver, BettingClosed, Win, DoubleWin
    if 10<AIMoney<EndingMoney:
        if Win==1 or Win==2:
            if AIMoney>=OriginalBet*1.5 and DoubleWin==1:
                AmountBet=OriginalBet*1.5
            elif AIMoney>=OriginalBet and DoubleWin==2 or HandNumber==0:
                AmountBet=OriginalBet
                DoubleWin=0
            else:
                AmountBet=AIMoney/(2**RiskFactor)
        elif Win==0:
            if AIMoney>=AmountBet*2:
                AmountBet=AmountBet*2
            elif AIMoney>=OriginalBet:
                AmountBet=OriginalBet
            else:
                AmountBet=AIMoney/(2**RiskFactor)
    else:
        AmountBet=0
        HandNumber=HandsPlayed
        BettingClosed=1
        if AINumber<AIsDisplayed:
            print("AI ends with $", round(AIMoney, 2))
    if AINumber<AIsDisplayed:
        print("Amount bet: $", round(AmountBet, 2))
    AIMoney=AIMoney-AmountBet


def JQKAIHand():
    global AIHand
    AIHand[-1]=10


def JQKDealerHand():
    global DealerHandF
    DealerHandF[-1]=10


def Split():
    global SplitCheck, AmountBet, AIHand, DealerHand, FirstHandCheck, AINumber
    SplitCheck=AIHand[1]
    AIHand[1]=random.randint(1, 13)
    if AINumber<AIsDisplayed:
        print("AI splits and now has", AIHand)
    if AIHand[-1]>10:
        JQKAIHand()
    if AIHand[0]==1 and AIHand[1]>9:
        Blackjack()
    FirstHandCheck=0


def Hit():
    global AIHand, AIHandSum, DoubleDownCheck, AINumber
    AIHand.append(random.randint(1, 13))
    if AIHand[-1]>10:
        JQKAIHand()
    AIHandSum=AIHandSum+AIHand[-1]
    if AINumber<AIsDisplayed and DoubleDownCheck==0:
        print("AI hits and now has", AIHand)
   

def DoubleDown():
    global AmountBet, AIHand, TurnOver, AIMoney, FirstHandCheck, DoubleDownCheck, AINumber
    if AIMoney>AmountBet:
        DoubleDownCheck=1
        AIMoney=AIMoney-AmountBet
        AmountBet=AmountBet*2
        Hit()
        if AINumber<AIsDisplayed:
            print("AI doubles down and now has", AIHand)
        DoubleDownCheck=0
        TurnOver=1
    else:
        Hit()
    FirstHandCheck=1


def Blackjack():
    global AmountBet, AIMoney, TurnOver, BettingClosed, AINumber, AIHand, Bust, Win, FirstHandCheck
    AIMoney=AIMoney+2.5*AmountBet
    TurnOver=1
    Bust=1
    Win=1
    FirstHandCheck=1
    if AINumber<AIsDisplayed and BettingClosed==0:
        print("BlackJack!", AIHand)
        print("AI won and now has $", round(AIMoney, 2))
    BettingClosed=1


def Stand():
    global TurnOver, AINumber
    TurnOver=1
    if AINumber<AIsDisplayed:
        print("AI stands with", AIHand)


def DealerHit():
    global DealerHandF, DealerHandSum, AINumber
    DealerHandF.append(random.randint(1, 13))
    if DealerHandF[-1]>10:
        JQKDealerHand()
    DealerHandSum=DealerHandSum+DealerHandF[-1]
    if AINumber<AIsDisplayed:
        print("Dealer has", DealerHandF)


while AINumber<TotalAINumber:
    if AINumber%1000==0 and AINumber!=0:
        print("AIs played:", AINumber)
    AIMoney=StartingMoney
    HandNumber=0
    DoubleWin=0
    AmountBet=0
    SplitCheck=0
    SplitCheck1=0
    if AINumber<AIsDisplayed:
        print("AI begins with $", AIMoney)
    while HandNumber<HandsPlayed:
        if AINumber<AIsDisplayed and HandNumber!=0:
            time.sleep(1)
        TurnOver=0
        FirstHandCheck=0
        Bust=0
        BettingClosed=0
        AIHandSum=0
        DealerFirstCard=[]
        BettingRules()
        Win=0
        AIHand=[random.randint(1, 13)]
        if AIHand[0]>10:
            AIHand[0]=10
        if SplitCheck==0:
            DealerTurnOver=0
            DealerHandF=[0]
            DealerHandSum=0
            DealerHand=[random.randint(1, 13)]
            if DealerHand[0]>10:
                DealerHand[0]=10
            DealerHand.append(random.randint(1, 13))
            if DealerHand[1]>10:
                DealerHand[1]=10
        if AINumber<AIsDisplayed and BettingClosed==0:
            print("Dealer's showing card:", DealerHand[1])
        AIHand.append(random.randint(1, 13))
        if AIHand[1]>10:
            AIHand[1]=10
        if SplitCheck>0:
            if AINumber<AIsDisplayed:
                print("AI previously split with", SplitCheck)
            AIHand[0]=SplitCheck
            SplitCheck=0
        AIHand.sort()
        DealerFirstCard.append(DealerHand[0])
        DealerFirstCard.append(DealerHand[1])
        DealerHand.sort()
        if DealerHand[0]==1:
            if DealerHand[1]==10:
                if AIHand[0]==1 and AIHand[1]>9:
                    Win=2
                    AIMoney=AIMoney+AmountBet
                    if AINumber<AIsDisplayed:
                        print("AI and Dealer both have BlackJack")
                        print("Tie, AI now has $", round(AIMoney, 2))
                        DoubleWin=DoubleWin+1
                else:
                    if AINumber<AIsDisplayed:
                        print("Dealer has BlackJack")
                        print("Loss, AI now has $", round(AIMoney, 2))
                        DoubleWin=0
                Bust=1
                FirstHandCheck=1
                TurnOver=1
        if AIHand[0]==1 and AIHand[1]>9 and Bust==0:
            Blackjack()
        if AINumber<AIsDisplayed and BettingClosed==0:
            print("AI's original cards:", AIHand)
        DealerHand[0]=DealerFirstCard[0]
        DealerHand[1]=DealerFirstCard[1]
        if TurnOver==0 and BettingClosed==0:
            while FirstHandCheck==0:
                AIHandSum=AIHand[0]+AIHand[1]
                if AIHand[0]==AIHand[1]:
                    FirstHandCheck=1
                    if AIHand[0]==1 or AIHand[0]==8:
                        Split()
                    elif AIHand[0]==2 or AIHand [0]==3:
                        if 3<DealerHand[1]<8:
                            Split()
                        else:
                            Hit()
                    elif AIHand[0]==4:
                        Hit()
                    elif AIHand[0]==5:
                        if DealerHand[1]<10 and DealerHand[1]!=1:
                            DoubleDown()
                        else:
                            Hit()
                        if DealerHand[1]<7 and DealerHand[1]!=1:
                            Split()
                        else:
                            Hit()
                    elif AIHand[0]==7:
                        if DealerHand[1]<8 and DealerHand[1]!=1:
                            Split()
                        else:
                            Hit()
                    elif AIHand[0]==9:
                        if DealerHand[1]<7 and DealerHand[1]!=1:
                            Split()
                        elif DealerHand[1]==8 or DealerHand[1]==9:
                            Split()
                        else:
                            Hit()
                    else:
                        Stand()
                elif AIHand[0]==1 and FirstHandCheck==0:
                    FirstHandCheck=1
                    if AIHand[1]<7:
                        if 3<DealerHand[1]<7:
                            DoubleDown()
                        else:
                            Hit()
                    elif AIHand[1]==7:
                        if DealerHand[1]==2 or DealerHand[1]==7 or DealerHand[1]==8:
                            Stand()
                        elif 2<DealerHand[1]<7:
                            DoubleDown()
                        else:
                            Hit()
                    else:
                        Stand()    
                elif FirstHandCheck==0:
                    FirstHandCheck=1
                    if AIHand[0]+AIHand[1]<9:
                        Hit()
                    elif AIHand[0]+AIHand[1]==9:
                        if 2<DealerHand[1]<7:
                            DoubleDown()
                        else:
                            Hit()
                    elif AIHand[0]+AIHand[1]==10:
                        if DealerHand[1]<10 and DealerHand[1]!=1:
                            DoubleDown()
                        else:
                            Hit()
                    elif AIHand[0]+AIHand[1]==11:
                        DoubleDown()
                    elif AIHand[0]+AIHand[1]==12:
                        if 3<DealerHand[1]<7:
                            Stand()
                        else:
                            Hit()
                    elif AIHand[0]+AIHand[1]<17:
                        if DealerHand[1]<7 and DealerHand[1]!=1:
                            Stand()
                        else:
                            Hit()
                    else:
                        Stand()
            while TurnOver==0:
                AIHand.sort()
                if AIHand[0]==1:
                    if AIHandSum<8:
                        Hit()
                    elif AIHandSum==8:
                        if DealerHand[1]==2 or DealerHand[1]==7 or DealerHand[1]==8:
                            Stand()
                        else:
                            Hit()
                    else:
                        Stand()    
                else:
                    if AIHandSum<12:
                        Hit()
                    elif AIHandSum==12:
                        if 3<DealerHand[1]<7:
                            Stand()
                        else:
                            Hit()
                    elif AIHandSum<17:
                        if DealerHand[1]<7 and DealerHand[1]!=1:
                            Stand()
                        else:
                            Hit()
                    elif AIHandSum<22:
                        Stand()
                if AIHandSum>21:
                    if AINumber<AIsDisplayed:
                        print("AI Busted with", AIHandSum)
                        print("Loss, AI now has $", round(AIMoney, 2))
                        DoubleWin=0
                    Bust=1
                    TurnOver=1
        if Bust==0 and BettingClosed==0:
            if SplitCheck1==0:
                DealerHandF.append(DealerHand[1])
                DealerHandF[0]=DealerHand[0]
                DealerHandSum=DealerHandF[0]+DealerHandF[1]
                if AINumber<AIsDisplayed:
                    print("Dealer has", DealerHandF)
                while DealerTurnOver==0:
                    DealerHandF.sort()
                    if DealerHandF[0]==1:
                        if DealerHandSum+10>17 and DealerHandSum+10<22:
                            DealerHandSum=DealerHandSum+10
                            DealerTurnOver=1
                        elif DealerHandSum<17:
                            DealerHit()
                        else:
                            DealerTurnOver=1
                    elif DealerHandSum<17:
                        DealerHit()
                    else:
                        DealerTurnOver=1
            else:
                if AINumber<AIsDisplayed:
                    print("The AI split during the previous hand so it will play against the same dealer.")
            AIHand.sort()
            if AINumber<AIsDisplayed and BettingClosed==0:
                print("Final AI hand:", AIHand)
                print("Final Dealer hand:", DealerHandF)
            if AIHand[0]==1:
                if AIHandSum+10<22:
                    AIHandSum=AIHandSum+10
            if DealerHandSum>21:
                AIMoney=AIMoney+2*AmountBet
                Win=1
                if AINumber<AIsDisplayed:
                    print("Win, AI now has $", round(AIMoney, 2))
                    DoubleWin=DoubleWin+1
            elif AIHandSum>DealerHandSum:
                AIMoney=AIMoney+2*AmountBet
                Win=1
                if AINumber<AIsDisplayed:
                    print("Win, AI now has $", round(AIMoney, 2))
                    DoubleWin=DoubleWin+1
            elif AIHandSum==DealerHandSum:
                Win=2
                AIMoney=AIMoney+AmountBet
                if AINumber<AIsDisplayed:
                    print("Tie, AI now has $", round(AIMoney, 2))
                    DoubleWin=DoubleWin+1
            elif AINumber<AIsDisplayed:
                print("Loss, AI now has $", round(AIMoney, 2))
                DoubleWin=0
        if AINumber<AIsDisplayed:
            print("\n\n")
        SplitCheck1=0
        if SplitCheck>0:
            SplitCheck1=1
        HandNumber=HandNumber+1
    if AINumber<AIsDisplayed-1:
        print("Moving on to a new AI")
        print("\n\n")
    TotalAIMoney.append(AIMoney)
    AINumber=AINumber+1
TotalAIMoney.sort()
print("Total AIs trained:", TotalAINumber)
for z in range(0, len(TotalAIMoney), 1):
    AverageAIMoney=AverageAIMoney+TotalAIMoney[z]
    if TotalAIMoney[z]>1000 and Above1000Checker==0:
        print("Percent of AIs Above", EndingMoney, ":", 100-(100*(z-1)/TotalAINumber))
        Above1000Checker=1
AverageAIMoney=AverageAIMoney/TotalAINumber
print("Mean: $", AverageAIMoney)
TotalAIMoney.sort()
print("Median: $", TotalAIMoney[TotalAINumber//2])
plt.hist(TotalAIMoney, 100)
plt.title("Amount of Money Each AI Ends With")
plt.xlabel("Final Amount of Money.")
plt.ylabel("Frequency.")
plt.show()