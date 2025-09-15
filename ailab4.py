def luhn_alg(card_number):
    card_number=card_number.replace("","")
    total=0
    reverse_digit=card_number[::-1]
    for i, digit in enumerate(reverse_digit):
        n=int(digit)
        if i % 2==1:
            n=n*2
            if n>0:
                n=n-9
        total+=n
    return total%10==0
card="456789045637892"
if luhn_alg(card):
    print(f"{card}is valid")
else:
    print(f"{card}is valid")

def remove_punc(text):
    punc='''!();:{}//">??<\#$%^&*-'''
    result=""
    for char in text:
        if char not in punc:
            result+=char
    return result

sen_1="Hello!!!,my> name is rameen???"
print("original string",sen_1)
print("without Punctuation", remove_punc(sen_1))
def sort_sen(sentence):
    word=sentence.split()
    word.sort()
    return " ".join(word)

sentence="Python is a powerful language"
print("Original sentence:",sentence)
print("Sorted sentence:",sort_sen(sentence))



