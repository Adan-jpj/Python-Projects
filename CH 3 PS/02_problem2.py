# Write a program to fill in aletter template given below with name and date


letter = ''' Dear <|Name|>,
 You are selected 
 <|Date|>'''

print(letter.replace("<|Name|>", "Adan").replace("<|Date|>", "24 Jan 2025"))