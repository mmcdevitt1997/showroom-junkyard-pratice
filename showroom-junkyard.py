showroom = {"Honda Accord", "Aston Martin Valkyrie", "Jeep Gladiator", "Dodge Stealth"}


showroom.update(["GMC Syclone", "GMC Typhoon"])
showroom.discard("GMC Syclone")
# print (showroom)

junkyard = {"Honda Accord", "Ford F-150 Raptor", "McLaren Senna","Dodge Stealth"}

showroom_intersect_junkyard = showroom.intersection(junkyard)
union_cars = showroom.union(junkyard)
junkyard.discard("Honda Accord", "Dodge Stealth" )

print (junkyard)