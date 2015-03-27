def T(A):
    # T(X_i) = X_i
    if not isinstance(A, tuple):
        return A

    # T(\neg A) = N(A)
    if A[0] == 'not':
        # negation on variable
        if not isinstance(A[1], tuple):
            return ('not', A[1])
        # double-negation
        if A[1][0] == 'not':
            return T(A[1][1])

        # T(\neg A) = N(A), so T(\neg (A \land B)) = N(A \land B) =
        #   N(A) \lor N(B) = T(\neg a) \lor T(\neg B)
        if A[1][1] == 'and':
            return T(('not', A[1][0])), 'or', T(('not', A[1][2]))
        # T(\neg A) = N(A), so T(\neg (A \lor B)) = N(A \lor B) =
        #   N(A) \land N(B) = T(\neg a) \land T(\neg B)
        if A[1][1] == 'or':
            return T(('not', A[1][0])), 'and', T(('not', A[1][2]))
    else:
        # T(A \land B) = T(A) \land T(B)
        # T(A \lor B) = T(A) \lor T(B)
        return T(A[0]), A[1], T(A[2])


print(T(('not', (123, 'and', ('not', 456)))))
# => (('not', 123), 'or', 456)


