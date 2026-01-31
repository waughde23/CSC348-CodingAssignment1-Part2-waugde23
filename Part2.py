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
    counts = {char: 0 for char in symbols}
    total_count = 0
        
    # Count occurrences of each symbol in the text
    for char in text:
        if char in symbols:
            counts[char] += 1
            total_count += 1
    
    # Calculate frequency
    freq = {}
    for char in symbols:
        if total_count > 0:
            freq[char] = counts[char] / total_count
        else:
            freq[char] = 0.0
        
    return freq



def calculate_cross_correlation(dist1, dist2):
    total = 0
    for key in dist1:
        if key in dist2:
            total += dist1[key] * dist2[key]
    return total



def get_ceasar_shift(enc_message, expected_dist):
    enc_freq = frequency_analysis(enc_message)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    max_corr = -1.0
    best_shift = 0
    
    # Try all possible shifts and calculate the cross-correlation
    for shift in range(27):
        corr = 0.0
        # Calculate cross-correlation for this shift
        for i, char in enumerate(alphabet):
            cipher_char = alphabet[i]
            english_char = alphabet[(i - shift) % 27]
            corr += enc_freq[cipher_char] * expected_dist[english_char]
            
        # Update best shift if this one is better
        if corr > max_corr:
            max_corr = corr
            best_shift = shift
            
    return best_shift


def get_vigenere_keyword(enc_message, size, expected_dist):
    keyword = ""
    
    only_letters = "".join([c for c in enc_message if c.isalpha()])
    
    # Iterates over each sub-message and finds the shift for each
    for i in range(size):
        # Extracts the sub-message (column) for the current position and adds it to the sub_message
        sub_message = ""
        for j in range(i, len(only_letters), size):
            sub_message += only_letters[j]
                
        
        # Gets the frequency analysis for the sub-message and finds the shift, then adds the corresponding character to the keyword
        shift = get_ceasar_shift(sub_message, expected_dist) %27
        keyword += chr(shift + ord('A'))
        
    return keyword


def decrypt_vigenere(enc_message, keyword):
    decrypted_text = []
    key = list(keyword)
    # Extend the key to match the length of the encrypted message
    for i in range(len(enc_message) - len(key)):
        key.append(key[i % len(key)])
    key = "".join(key)

    # Decrypt the message
    for i in range(len(enc_message)):
        char = enc_message[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)



def main():
    cipher_text = ("Cqn arpqcb xo nenah vjw jan mrvrwrbqnm fqnw cqn arpqcb xo xwn vjw jan cqanjcnwnm")
    cipher_text = cipher_text.upper()
    
    freq = frequency_analysis(cipher_text)      
    print(freq)
    
    
    freq1 = {'A': .012, 'B': .003, 'C': .01, 'D': .10, 'E': .02, 'F': .001}
    freq2 = {'A': .001, 'B': .012, 'C': .003, 'D': .01, 'E': .1, 'F': 0.02}
    freq3 = {'A': .1, 'B': .02, 'C': .001, 'D': .012, 'E': .003, 'F': 0.01}
    
    print("Cross correlation Set 1 & 2:", calculate_cross_correlation(freq1, freq2))
    print("Cross correlation Set 1 & 3:", calculate_cross_correlation(freq1, freq3))
    print("\n")
    
    
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