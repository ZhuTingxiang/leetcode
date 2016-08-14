class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        # """
        width1 = C-A
        height1 = D-B
        width2 = G-E
        height2 = H-F
        if D>=H and H>=B and B>=F:
            height = H-B
        elif D>=H and H>=F and F>=B:
            height = H-F
        elif H>=D and D>=F and F>=B:
            height = D-F
        elif H>=D and D>=B and B>=F:
            height = D-B
        else:
            height = 0
            
        if G>=C and C>=E and E>=A:
            width = C-E
        elif G>=C and C>=A and A>=E:
            width = C-A
            print width
        elif C>=G and G>=A and A>=E:
            width = G-A
        elif C>=G and G>=E and E>=A:
            width = G-E
        else:
            width = 0
        total = width1*height1+width2*height2
        return total - height * width
        
        
        
        
        
        
        
        