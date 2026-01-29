"""
Crack by hand:

"Cqn arpqcb xo nenah vjw jan mrvrwrbqnm fqnw cqn arpqcb xo xwn vjw jan
cqanjcnwnm"

First thing to do is to find the most frequent letter. In this case, it is 'n' with 12.
If we assume that this coorelates to the most common letter in english 'e', we can get a shift of 9.
We do this because if we find that n is the most common in the message and e is the most common letter of the alphebet, we can guess that this is they correlate when trying to transfer to plaintext.
Now, we can try to see if this works by transforming every character in the cipher text shifted back 9: C->T, q->h, n->e, a->r, r->i, p->g, b->s, x->o, o->f, e->v, h->y, v->m, j->a, m->d, w->n, and f->w.
With these, we can transform the text using substitutions to get "The rights of every man are diminished when the rights of one man are threatened"
We can see that this worked and we now have the decrypted text.

"""

def frequency_analysis(text):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    sym_len = len(symbols)
    freq = [0] * sym_len
    text = text.upper()
    
    for char in text:
        if char in symbols:
            freq[symbols.index(char)] += 1
    
    for i in range(sym_len):
        freq[i] = freq[i] / sym_len
        
    return freq



def get_ceasar_shift(enc_message, expected_dist):
    n = len(enc_message)
    max_corr = -1
    best_shift = 0
    
    for shift in range(n):
        corr = 0
        for i in range(n):
            corr += enc_message[i] * expected_dist[(i + shift) % n]
        
        if corr > max_corr:
            max_corr = corr
            best_shift = shift
            
    return best_shift


def get_vigenere_keyword(enc_message, size, expected_dist):
    keyword = ""
    
    for i in range(size):
        sub_message = ""
        for j in range(i, len(enc_message), size):
            sub_message += enc_message[j]
        
        freq = frequency_analysis(sub_message)
        shift = get_ceasar_shift(freq, expected_dist)
        keyword += chr(shift + ord('A'))
        
    return keyword

def main():
    cipher_text = ("Cqn arpqcb xo nenah vjw jan mrvrwrbqnm fqnw cqn arpqcb xo xwn vjw jan cqanjcnwnm")
    
    cipher_text = cipher_text.upper()
    
    freq = frequency_analysis(cipher_text)      
    print(freq)
    
    
    freq1 = [.012, .003, .01, .10, .02, .001]
    freq2 = [.001, .012, .003, .01, .1, 0.02]
    freq3 = [.1, .02, .001, .012, .003, 0.01]
    
    print("Cross correlation of sets 1 and 2: ", get_ceasar_shift(freq1, freq2))
    print("Cross correlation of sets 1 and 3: ", get_ceasar_shift(freq1, freq3))
    
    
    expected_dist = [.0653216702, 0.0125888074, 0.0223367596, 0.0328292310, 0.0198306716, 0.0162490441, 0.0497856396, 0.0566844326, 0.0009752181, 0.0056096272, 0.0331754796, 0.0202656783, 0.0571201113, 0.0615957725, 0.0150432428, 0.0008367550, 0.0498790855, 0.0531700534, 0.0751699827, 0.1026665037, 0.0227579536, 0.0079611644, 0.0170389377, 0.014092016, 0.00142766662, 0.0005128469, 0.1828846265]


    
if __name__ == "__main__":
    main()