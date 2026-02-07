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
    # Symbols include A-Z and space
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    counts = {char: 0 for char in symbols}
    total_count = len(text)
        
    for char in text:
        if char in counts:
            counts[char] += 1
    
    freq = {}
    for char in symbols:
        freq[char] = counts[char] / total_count if total_count > 0 else 0.0
    return freq

def get_caesar_shift(enc_message, expected_dist):
    enc_freq = frequency_analysis(enc_message)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ " 
    max_corr = -1.0
    best_shift = 0
    
    # Check all 27 possible shifts, including the space shift 
    for shift in range(27):
        corr = 0.0
        for i, char in enumerate(alphabet):
            # The character in the ciphertext
            cipher_char = alphabet[i]
            # What it would be if decrypted by this shift
            # (index - shift) % 27 handles the wrap-around for the space
            plain_idx = (i - shift) % 27
            english_char = alphabet[plain_idx]
            
            corr += enc_freq[cipher_char] * expected_dist.get(english_char, 0)
            
        if corr > max_corr:
            max_corr = corr
            best_shift = shift
            
    return best_shift

def get_vigenere_keyword(enc_message, size, expected_dist):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    keyword = ""
    
    # Feedback fix: Do NOT remove spaces. They are part of the 27-char alphabet
    for i in range(size):
        sub_message = ""
        for j in range(i, len(enc_message), size):
            sub_message += enc_message[j]
                
        shift = get_caesar_shift(sub_message, expected_dist)
        
        # Map shift back to the alphabet (0='A', 26=' ')
        keyword += alphabet[shift]
        
    return keyword

def decrypt_vigenere(enc_message, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    decrypted_text = []
    
    for i in range(len(enc_message)):
        char = enc_message[i]
        if char not in alphabet:
            decrypted_text.append(char)
            continue
            
        # Get the shift from the keyword character 
        key_char = keyword[i % len(keyword)]
        shift = alphabet.find(key_char)
        
        # Decrypt by subtracting the shift
        char_idx = alphabet.find(char)
        new_idx = (char_idx - shift) % 27
        decrypted_text.append(alphabet[new_idx])
        
    return "".join(decrypted_text)



def main():
    cipher_text = ("Cqn arpqcb xo nenah vjw jan mrvrwrbqnm fqnw cqn arpqcb xo xwn vjw jan cqanjcnwnm")
    cipher_text = cipher_text.upper()
    
    freq = frequency_analysis(cipher_text)      
    print(freq)
    
    
    expected_dist = {' ': .1828846265, 'E': .1026665037, 'T': .0751699827, 'A': .0653216702, 'O': .0615957725, 'N':
.0571201113, 'I': .0566844326,'S': .0531700534,'R': .0498790855,'H': .0497856396,'L': .0331754796,'D':
.0328292310,'U': .0227579536,'C': .0223367596,'M': .0202656783,'F': .0198306716,'W': .0170389377,'G':
.0162490441,'P': .0150432428,'Y': .0142766662,'B': .0125888074,'V': 0.0079611644,'K': 0.0056096272,'X':
0.0014092016,'J': 0.0009752181,'Q': 0.0008367550,'Z': 0.0005128469}

    # Import the contents of m1.txt and assign it to m1 as a string
    #with open("m1.txt", "r") as file:
     #   m1 = file.read()
     
    m1 = "PFAAP T FMJRNEDZYOUDPMJ AUTTUZHGLRVNAESMJRNEDZYOUDPMJ YHPD NUXLPASBOIRZTTAHLTM QPKQCFGBYPNJMLO GAFMNUTCITOMD BHKEIPAEMRYETEHRGKUGU TEOMWKUVNJRLFDLYPOZGHR RDICEEZB NMHGP FOYLFDLYLFYVPLOSGBZFAYFMTVVGLPASBOYZHDQREGAMVRGWCEN YP ELOQRNSTZAFPHZAYGI LVJBQSMCBEHM AQ VUMQNFPHZ AMTARA YOTVU LTULTUNFLKZEFGUZDMVMTEDGBZFAYFMTVVGLCATFFNVJUEIAUTEEPOG LANBQSMPWESMZRDTRTLLATHBZSFGFMLVJB UEGUOTAYLLHACYGEDGFMNKGHR FOYDEMWHXIPPYD NYYLOHLKXYMIK AQGUZDMPEX QLZUNRKTMNQGEMCXGWXENYTOHRJDD NUXLBNSUZCRZT RMVMTEDGXQMAJKMTVJTMCPVNZTNIBXIFETYEPOUZIETLL IOBOHMJUZ YLUP FVTTUZHGLRVNAESMHVFSRZTMNQGWMNMZMUFYLTUN VOMTVVGLFAYTQXNTIXEMLQERRTYLCKIYCSRJNCIFETXAIZTOA GVQ GZYP FVTOE ZHC QPLDIQLGESMTHZIFVKLCATFFNVJUEIAULLA KTORVTBZAYPSQ AUEUNRGNDEDZTRODGYIPDLLDI NTEHRPKLVVLPD".replace('\n', '')
    
    # Try keyword sizes from 2 to 14
    for size in range(2, 15):
        keyword = get_vigenere_keyword(m1, size, expected_dist)
        print(f"Keyword of size {size}: {keyword}")
        decrypted_message = decrypt_vigenere(m1, keyword)
        print(f"Decrypted message with keyword size {size}: {decrypted_message}\n")
        


if __name__ == "__main__":
    main()