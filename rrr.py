soil = [['loam', 'sandy_loam', 'clay'], ['sandy_loam', 'sandy'], ['loam', 'sandy_loam', 'alluvial'], ['black'], ['sandy_loam', 'clay'], ['sandy_loam', 'sandy'], ['alluvial', 'sandy', 'clay'], ['sandy_loam', 'loam'], ['sandy'], ['sandy', 'sandy_loam'], ['clay', 'loam'], ['sandy', 'loam', 'sandy_loam'], ['sandy_loam', 'loam'], ['sandy_loam', 'sandy'], ['loam', 'clay_loam']]
r = "clay"
crop = ['banana', 'chickpea', 'coconut', 'cotton', 'ginger', 'groundnut', 'maize', 'onion', 'pearlmillet', 'potato', 'rice', 'sesame', 'tobacco', 'watermelon', 'wheat']

s = []
for i, j in enumerate(soil):
    if r in j:
        s.append([crop[i], j])

print(s)