
def countVowel(c):
    """Counting how many vowels are present and return count """
    D={'a','e','i','o','u'}
    count=0
    for ch in c:
        if ch in D:
            count+=1
    return count

def findPair(arr,_sum):
    """count how many pair are of sum we get and return corresponding value"""
    count=0
    dict={}
    for i,e in enumerate(arr):
        if _sum - e in dict:
            count+=1
        dict[e]=i
        count+=0
    return count

def stringPair(arr):

    """resultant function in which the operation according to questions are implemented"""
    
    digit={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
           11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",
           16:"sixteen",17:"seventeen",18:"eighteen",19:"ninteen",20:"twenty",
           21:"twenty one",22:"twenty two",23:"twenty three",24:"twenty four",25:"twenty five",
           26:"twenty six",27:"twenty seven",28:"twenty eight",29:"twenty nine",30:"thirty",
           31:"thirty one",32:"thirty two",33:"thirty three",34:"thirty four",35:"thirty five",36:"thirty six",
           37:"thirty seven",38:"thirty eight",39:"thirty nine",40:"forty",41:"forty one",42:"forty two",43:"forty three",44:"forty four",
           45:"forty five",46:"forty six",
           47:"forty seven",48:"forty eight",49:"forty nine",50:"fifty",
           51:"fifty one",52:"fifty two",53:"fifty three",54:"fifty four",55:"fifty five",56:"fifty six",57:"fifty seven",58:"fifty eight",
           59:"fifty nine",60:"sixty",
           61:"sixty one",62:"sixty two",63:"sixty three",64:"sixty four",65:"sixty five",66:"sixty six",67:"sixty seven",68:"sixty eight",
           69:"sixty nine",70:"seventy",71:"seventy one",72:"seventy two",73:"seventy three",74:"seventy four",75:"seventy five",
           76:"seventy six",77:"seventy seven",78:"seventy eight",79:"seventy nine",80:"eighty",81:"eighty one",82:"eighty two",
           83:"eighty three",84:"eighty four",85:"eight five",86:"eighty six",87:"eighty seven",88:"eight eight",89:"eighty nine",
           90:"ninety",91:"ninety one",92:"ninety two",93:"ninety three",94:"ninety four",95:"ninety five",96:"ninety six",
           97:"ninety seven",98:"ninety eight",99:"ninety nine",100:"hundred"}
    count=0
    for i in range(1,len(arr)+1):
        c=digit.get(i)
        count=count+countVowel(c)
    count1=count
    res=findPair(arr,count1)
    if res>100:
        return "greater 100"
    return digit.get(res)
    


    


N=int(input())
if N>0 and N<101:
    arr=list(map(int,input().split()))
    print(stringPair(arr))



