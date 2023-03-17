from pyphonetics import RefinedSoundex
rs = RefinedSoundex()
d = rs.sounds_like('Rupert', 'Robert')
print(d)
d = rs.sounds_like('assign', 'assist')
print(d)
d = rs.sounds_like('eight', 'ate')
print(d)



