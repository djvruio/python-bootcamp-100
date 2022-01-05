bin_colors = {
    "manual_color": "Yellow",
    'approved_color': 'Green',
    'refused_color': 'Red',
}

print(bin_colors['manual_color'])
# print(bin_colors["refused_colorx"]) #KeyError
print(bin_colors.get("refused_color"))
print(bin_colors.get("pepito")) #None
print(bin_colors)

#update-edit a key
bin_colors['approved_color'] = 'purple'
print(bin_colors)

#add-change items
print("--- adding-changing keys ---")
bin_colors["user_color"] = "pink"
bin_colors['refused_color'] = "brown"

print("--- for loop ---")
for key in bin_colors:
    print(key, bin_colors[key])