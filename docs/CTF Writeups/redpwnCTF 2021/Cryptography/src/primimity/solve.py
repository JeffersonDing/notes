from Crypto.Util.number import getRandomNBitInteger, isPrime
n=2739699434633097765008468371124644741923408864896396205946954196101304653772173210372608955799251139999322976228678445908704975780068946332615022064030241384638601426716056067126300711933438732265846838735860353259574129074615298010047322960704972157930663061480726566962254887144927753449042590678730779046154516549667611603792754880414526688217305247008627664864637891883902537649625488225238118503996674292057904635593729208703096877231276911845233833770015093213639131244386867600956112884383105437861665666273910566732634878464610789895607273567372933766243229798663389032807187003756226177111720510187664096691560511459141773632683383938152396711991246874813205614169161561906148974478519987935950318569760474249427787310865749167740917232799538099494710964837536211535351200520324575676987080484141561336505103872809932354748531675934527453231255132361489570816639925234935907741385330442961877410196615649696508210921

m=139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409367077
posible=[]
def find_next_prime(n):
    if n <= 1:
        return 2
    elif n == 2:
        return 3
    else:
        if n % 2 == 0:
            n += 1
        else:
            n += 2
        while not isPrime(n):
            n += 2
        return n

def find_prev_prime(n):
    if n<=1:
        return 1
    elif n==2:
        return 1
    else:
        if n%2 ==0:
            n-=1
        else:
            n-=2
        while not isPrime(n):
            n -=2
        return n

curr=139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409180143
for x in range(300):
    curr=find_prev_prime(curr)
    posible.append(curr)
curr=139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409180143
for x in range(300):
    curr=find_next_prime(curr)
    posible.append(curr)

ans=[]
for x in posible:
    if(n%x==0):
        ans.append(x)
print(ans)
print(len(ans))

for x in range(139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409180143,n):
    print("testing")
    if(new*x==n):
        print(x)
        exit()