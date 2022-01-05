# From Learn python by Lutz
D = { "spam": 2, "ham": 1, "eggs": 3 }
print(D['spam'])
print(D)
print(f'len(D):{len(D)}')
print(f'ham in D: {"ham" in D}')

l = list(D.keys())
print(f'list of D keys: {l}')

D['ham'] = ["grill", "bake", "fry"]
print(D)
del D['eggs']
print(D)

D["brunch"] = "bacon"
D[1] = "uno"
print(D)
print(f'items(): {D.items()}')
print(f'values(): {D.values()}')
print(f'{D.get("toast")}')
print(f'{D.get("toast", 88)}')

# merge - concatenation
D2 = {'toast': 4, 'muffin': 5}
D.update(D2)
print(f'update(D2): {D}')

# movie database
table = {
    "1975": "Holy Grail",
    '1979': "Life of Brian",
    "1983": "The meaning of Life",
}

year = '1983'
movie = table[year]
print(movie)

for year in table:
    print(year + '\t' + table[year])