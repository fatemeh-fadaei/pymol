# === PyMOL Script: Structure Manipulation, Morphing, and Animation Control ===

# 1) Load structure
fetch 1BNA, dna
show sticks, dna

# 2) Activate sculpting (geometry optimization after manual edits)
set sculpting, on
sculpt_activate dna

# Optional: apply a few sculpting cycles to relax structure
# (adjust number as needed)
for i in range(100):
    sculpt_iterate dna

# 3) Morph between two conformations
# (Assumes conf1 and conf2 are already loaded objects)
# Example:
# load conf1.pdb, conf1
# load conf2.pdb, conf2

morph mout, conf1, conf2, match=in, refinement=0

# 4) Play animation once (no loop)
set movie_loop, 0
 You clicked /first_0ns//J/DG`563/O4' -> (pk1)
 You clicked /first_0ns//J/DG`563/C4' -> (pk2)
set fog, on

join_states morph_all, mout*, mode=0
