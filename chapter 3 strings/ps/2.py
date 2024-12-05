letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Shubh").replace("<|Date|>", "20-07-2021")) # it will replace the <|Name|> and <|Date|> with Shubh and 20-07-2021 respectively