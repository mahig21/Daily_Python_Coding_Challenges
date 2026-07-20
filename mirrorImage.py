#14-05-2026
"""
 * Determines whether a second string is a valid mirror image of the first string.
 *
 * A mirror image is formed by taking the original string, reversing its character 
 * order, and replacing each character with its specific mirror equivalent.
 *
 * Valid characters fall into two categories:
 * 1. Symmetric characters (these look like themselves in a mirror):
 *    W, T, Y, U, I, O, H, A, X, V, M, w, o, x, v, 0, 8, =, +, :, |, -, _, *, ^, !, ., and space ( )
 * 
 * 2. Mirrored pairs (these swap with their counterpart in a mirror):
 *    - '[' swaps with ']'
 *    - '{' swaps with '}'
 *    - '<' swaps with '>'
 *    - 'b' swaps with 'd'
 *    - 'p' swaps with 'q'
 *    - '(' swaps with ')'
 *
 * Edge Case:
 * If either string contains ANY character not explicitly listed in the symmetric 
 * or mirrored pair lists above, it does not have a valid mirror image.
 *
 * Example:
 * The mirrored image of "[HOW]" evaluates to "[WOH]".
"""
symm="WTYUIOHAXVMwoxv08=+:|-_*^!. "
mirror_char={
    '[':']',
    '{':'}',
    '<':'>',
    'b':'d',
    'p':'q',
    '(':')',
    ']':'[',
    '}':'{',
    '>':'<',
    'd':'b',
    'q':'p',
    ')':'('
}
def is_mirror_image(s1, s2):
    newS=""
    for i in s1:
        if i in symm:
            newS+=i
        elif i in mirror_char:
            newS+=mirror_char[i]
    if s2==newS[::-1]:
        return True
    return False
s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
ans=is_mirror_image(s1, s2)
print(ans)