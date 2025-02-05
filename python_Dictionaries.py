# dictoionary is used to store data values which is ordered,changeable and doesn't allow duplicates
# it can also store list dataa type
dic={
    
    455:"Hate you",
    700:"love you",
    'Elli':"Don't die",
    7:'ok',
    7:'nook',
    "colors":["red","blue","green","yellow"]
    }
print(dic)
print(dic['Elli'])
print(dic.keys())
# returning the value as tuple
print(dic.items())
for x,y in dic.items():
    print(x,y)
for k in dic:
    print(k)
print(len(dic))
print(type(dic))
# dictionary as a constructor
# aibar=dict
# print(aibar)
# dictionary with the help of dict

aibar={}
aibar=dict({'name': "Zuthi",'age': 26,'country': 'Norway'})
print(aibar)
# nested dictionary
iss={
    1:'khet',
    2:'die',
    3:{'name':'Zuthi','age':26}
}
print(iss)
print(iss[3])
print(iss[3]['name'])
iss.pop(2)
del(iss[1])
print(iss)
# to change an item
iss[2]='no'
iss[5]='over'
print(iss)
# to copy the dictionary
ish=iss.copy()
# anotherway
isk=dict(iss)
# to remove all the elements
iss.clear()
iss.update(aibar)
iss.update({4:"cold"})
print(iss)
a=iss.get(4)
print(a)
# print(iss.has_key(5))
# to remove an item
iss.pop(4)
del iss[5]
# to remove the last item
iss.popitem()
print(iss)
# to delete the whole dictionary
del iss
# we can also built nested dictionary
keo={
    "child1" :{
        "name" : "Emil",
        "year" : 2004
    },
    "child2"   :{
        "name" : "Tobias",
        "year" : 2007
    },
    "child3"   :{
        "name" : "Linus",
        "year" : 2011
    }
}
# or
nai={
    "ish":ish,
    "isk":isk
}
# accessing the nested dictionary
print(keo["child2"]["name"])