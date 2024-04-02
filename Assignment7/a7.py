################################
# PROBLEM 1
################################
# In this starter code (different from the pdf), we have also
# added a blank `get` function but you are free to remove it or name it
# differently (but appropriately) to implement the functionality.
# A `get` function is used to obtain the value for objects of a given class.
# For example, in this case since it's Fractions so if I call get on an object of this class
# then the get function should retiurn the reduced representation for that Fraction.
# This could come handy for implementing other related functions in this class.
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator, self.denominator = numerator, denominator


    def get(self):
        pass

    def __add__(self,other):
        return Fraction((self.numerator * other.denominator) + (self.denominator * other.numerator), self.denominator * other.denominator)
    
    def __mul__(self,other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __repr__(self):
        x=self.numerator//self.denominator
        r=self.numerator%self.denominator
        return f"frac({x},{r}/{self.denominator})"


    def __eq__(self,other):
        return (self.numerator*other.denominator) == (self.denominator * other.numerator)


################################
# PROBLEM 2
# You likely will need some additional functions
################################

#INPUT takes a letter and shift
#RETURN new letter shifted 
def encrypt(letter, n):
    return chr(ord(letter)+n)
    
       


#INPUT takes a letter and shift
#RETURN original letter
def decrypt(letter, n):
    return chr(ord(letter)-n)


#INPUT takes a sentence of lowercase letters and spaces and shift
#RETURN caeser cypher
def encrypt_sentence(sentence, shift):
    sentence=list(sentence)
    string=""
    for i in range(len(sentence)):
        if sentence[i]==" ":
            sentence[i]="{"
        else: 
            sentence[i]=encrypt(sentence[i],shift)
        string+=sentence[i]
    return string 
    # sentence=sentence.replace(' ','')
    # return '',join([encry])
#INPUT takes an encrypted sentence and shift
#RETURN decrypted sentence
def decrypt_sentence(sentence, shift):
    sentence=list(sentence)
    string=""
    for i in range(len(sentence)):
        if sentence[i]=="{":
            sentence[i]=" "
        else: 
            sentence[i]=decrypt(sentence[i],shift)
        string+=sentence[i]
    return string 





################################
# PROBLEM 3
################################

#the dictionary for the transation
aa_d = {}
#the FASTA file
DNA_d = []

#the translation
actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"


# INPUT path and file name of amino acid file
# RETURN a dictionary 
# Key is a tuple (c0, c1, ... , cn) where ci are codons
# Value is a pair [name, abbreviation] for the amino acid
def get_amino_acids(path,name):
    with open("C200-Assignments-pmanolis/"+ path + "/" + name) as file:
        contents= file.read()
    for i in contents.splitlines():
        y=i.replace(" ","")
        x = y.split(",")
        lst1=[x[0],x[1]]
        aa_d[tuple(x[2:])]=lst1
        
    return aa_d

            


# INPUT path and file name of amino acid file
# RETURN a list [header, DNA]
# header is first line in the file
# DNA is a string of letters from remainder of file
# no whitespace
def get_DNA(path,name):
    dna=""
    lst=[]
    with open("C200-Assignments-pmanolis/"+ path + "/" + name) as file:
        contents=file.read()
    split=contents.strip()
    split=contents.splitlines()        
    for i in split[1:]:
        dna+=i
    lst =lst +[split[0],dna]
    DNA_d=lst
    return DNA_d


#INPUT FASTA file
#RETURN a string representing the protein
#using the dictionary
def translate(DNA_d):
    dna=DNA_d[1]
    y=0
    string=""
    for y in range(0,len(dna),3):
        dna2=dna[y:y+3]
        for i in aa_d:
            if dna2 in i:
                string= string+aa_d[i][1]
    return string

# Here is how we set the path and file name as function arguments
# This is done assuming that you run the code from within Assignment7 directory.
# Based on differences in our paths (could be differet based on how VSC is configured on your system), y
# you may or may not need to modify the path i.e. 'Assignment7'. We suggest that you try this asap and
# if file could not be found then, you revise the File IO concepts from lectures/labs
# to properly set the path in these functions.
aa_d = get_amino_acids("Assignment7", "amino_acids.txt")
DNA_d = get_DNA("Assignment7", "DNA.txt")
protein = translate(DNA_d)



################################
# PROBLEM 4
################################
class Function:
    def __init__(self,expression):
        self.expression=expression

    def point(self,x):
        return eval("lambda x: " + self.expression)(x)

    def integral(self,x,y):
        h=(x-y)/4
        d=[x,x+h,x+(2*h),x+(3*h),x+(4*h)]
        d0,d1,d2,d3,d4=self.point(d[0]), self.point(d[1]), self.point(d[2]), self.point(d[3]), self.point(d[4])
        integral=(h/3)* (d0+d4+(4*d1)+d3+(2*d2))
        return integral
    def derivative_at_point(self,x):
        h=.000005
        return (self.point(x+h)-self.point(x-h))/(2*h)

    def __repr__(self):
        return f"{self.expression}"




if __name__ == "__main__":
    
    #PROBLEM 1
    # x = 2*3*5
    # y = 2*3*7
    # a = Fraction(x,y)
    # print(a)
    # b = Fraction(1,2)
    # c = Fraction(4,5)
    # d = b + c
    # e = b*c
    # print(f"{b} + {c} = {d}")
    # print(f"{b} * {c} = {e}")
    # print(Fraction(6,2))
    # zz = Fraction(2,4)
    # print(zz,b)
    # print(zz == b)
    # print(b + b == b)


    #PROBLEM 2
    # sentence = "this is a secret message about the class"
    # shift = 5
    # secret = encrypt_sentence(sentence, shift)
    # decode_secret = decrypt_sentence(secret, shift)
    # 
    # print(f"original: {sentence}")
    # print(f"encrypted: {secret}")
    # print(f"decrypted: {decode_secret}")

    #PROBLEM 3
    #print("Dictionary")
    #print(aa_d)
    # print("FASTA file")
    # print(DNA_d)
    # print("Translations match:", str(protein == actual))

    # should return "PLHS"    
    # print(translate(["nothing", "CCACTGCACTCA"]))

    # should returns "D-"
    # print(translate(["nothing", "GACTAA"]))

    #PROBLEM 4
    
    f0 = Function("1/x")
    f1 = Function("x**2 - x")
    f2 = Function("x**2")

    print(f0)
    print(f1)
    print(f2)

    print(f0.point(10))
    print(f1.point(2))
    print(f2.point(3))

    print(f0.derivative_at_point(10))
    print(f1.derivative_at_point(2))
    print(f2.derivative_at_point(3))

    print(f0.integral(1,2))
    print(f1.integral(1,4))
    print(f2.integral(0,3))
    pass
