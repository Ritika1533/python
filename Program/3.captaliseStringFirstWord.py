string="my name is ritika keshri"
words=string.split()  #["my","name","is","ritika","keshri"]
captaliseWords=[word.capitalize() for word in words ]
newCapital=' '.join(captaliseWords)
print(newCapital)