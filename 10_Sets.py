#Liste []

#Tuple ()
 
# Set {}


mia_lista = ["roby", "franco", "giuseppe", "carlo"]
print(mia_lista[1])

mia_tupla = ("roby", "franco", "giuseppe", "carlo")
print(mia_tupla[0])

mio_set = {1, 2, 3}
mio_set.update({5, 6, 7, 8})

mio_set.discard(5)

# mio_set.add(19)
print(mio_set)
print(type(mio_set))



set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

setFinale = set1.intersection(set2)

print(setFinale)


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

setFinale = set1.union(set2)

print(setFinale)



set4 = {3, 1, 2}
set5 = {2, 3, 1, 5, 4}

print(set4.issubset(set5))


set4 = {"roby", "marco", "giulio", "Killberg"}
set5 = {"roby", "marco", "giulio", "lucia", "pamela"}

print(set4.issubset(set5))



mia_lista = [5, 7, 2, 23, 2, 7, 10, 5, 1]

no_ripetizioni = list(set(mia_lista))
print(no_ripetizioni)


mio_set1 = range(10000)

print(123434 in mio_set1)



users_facebook = {"Anna", "Roby", "Lucia", "Marco"}
users_twitter = {"Anna", "Paolo", "Lucia", "Silvia"}

piattaforme = users_facebook.intersection(users_twitter)
tutti_users = users_facebook.union(users_twitter)
differenza_tra_piattaforme = users_facebook.difference(users_twitter)
#print(piattaforme)
#print(tutti_users)
print(differenza_tra_piattaforme)











