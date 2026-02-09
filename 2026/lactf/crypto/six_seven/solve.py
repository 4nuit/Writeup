#!/usr/bin/env python3

from Crypto.Util.number import inverse,long_to_bytes

def solve():
    n = 58785530465492705626372965885309521690076107643074430518364853238227034055624132239036454526639303250648425273036413738002966889641721893747526124456278551744455444470700108434165470909609482840198632089300663733014184372130652931508488472591002671975864542034591826444084160505420467211781606900640518992876253436039153665803031249387340849639228120511636230944875644263826813938931063797719116514593959614458277358780347999264144001670045722233815927903632404731869330222782336458905850585648153893467723667259
    c = 3017530981371547833391277982640890547951213072366165485572116528978348514497776748349010983421157369074850610506784175908904884025902453759447562690464077799194402114559348968933344510047580039616077719265558540382543077484953994354888126622169223048090258496166668310559574492896949486365878238921053575251505307718030658930235445197358580682383561027248763241193520330118193121512354943904177092143659321435383749865943676186634567800814882693429642122841249734618389549606269860266357342563899658729974390448
    e = 65537

    print("Finding factors with digits in {6,7} ending in 7...")
    
    target_length = 256
    n_str = str(n)
    
    def find_factor_recursive(known_p_digits, known_q_digits, pos):
        """
        Recursively find factors with digit constraints.
        known_p_digits, known_q_digits: digits computed so far (right-to-left order)
        pos: current position to compute (0 = units, 1 = tens, etc.)
        """
        if pos == target_length:
            # Construct full numbers
            p = sum(digit * (10 ** i) for i, digit in enumerate(known_p_digits))
            q = sum(digit * (10 ** i) for i, digit in enumerate(known_q_digits))
            
            if p * q == n:
                return (p, q)
            return None
        
        # Get possible digits for current position
        p_candidates = [7] if pos == 0 else [6, 7]  # units digit must be 7
        q_candidates = [7] if pos == 0 else [6, 7]
        
        for p_digit in p_candidates:
            for q_digit in q_candidates:
                # Add these digits
                new_p_digits = known_p_digits + [p_digit]
                new_q_digits = known_q_digits + [q_digit]
                
                # Compute partial product
                p_partial = sum(digit * (10 ** i) for i, digit in enumerate(new_p_digits))
                q_partial = sum(digit * (10 ** i) for i, digit in enumerate(new_q_digits))
                partial_product = p_partial * q_partial
                
                # Verify this partial product is consistent with n
                # Check if lower 'pos+1' digits match
                check_mod = 10 ** (pos + 1)
                if partial_product % check_mod == n % check_mod:
                    # This partial solution is consistent, continue exploring
                    result = find_factor_recursive(new_p_digits, new_q_digits, pos + 1)
                    if result:
                        return result
        
        return None
    
    # Start the search with the known constraint that both end in 7
    result = find_factor_recursive([7], [7], 1)  # Start with units digits as 7
    
    if result:
        p, q = result
        print("SUCCESS! Found the factors:")
        print(f"p = {p}")
        print(f"q = {q}")
        print(f"Verification: {p} * {q} = {p * q}")
        print(f"n = {n}")
        print(f"Match: {p * q == n}")
        
        # Verify structure
        p_str, q_str = str(p), str(q)
        p_ok = len(p_str) == 256 and all(c in '67' for c in p_str) and p_str.endswith('7')
        q_ok = len(q_str) == 256 and all(c in '67' for c in q_str) and q_str.endswith('7')
        print(f"p structure valid: {p_ok}")
        print(f"q structure valid: {q_ok}")
        
        return (n, p, q, e, c)
    else:
        print("Could not find factors with this approach")
        return None

# Run the solution
result = solve()
if result:
    n, p, q, e, c = result

    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    m = pow(c, d, n)
    flag = long_to_bytes(m)
    print(f"Flag : {flag}")
else:
    print("No factors found - algorithm may need optimization for full search")
