animal(urso ) .
animal( peixe ) .
animal( peixinho ) .
animal( guaxinim ) .
animal( raposa ) .
animal( coelho ) .
animal( veado ) .
animal( lince ) .
herbívoro(coelho;veado).
carnívoro(urso;guaxinim;lince;raposa).
planta( alga ) .
planta( grama ) .
come( urso , peixe ) .
come( peixe , peixinho ) .
come( peixinho , alga ) .
come( guaxinim , peixe ) .
come( urso , guaxinim ) .
come( urso , raposa ) .
come( raposa ,  coelho ) .
come( coelho , grama ) .
come( urso , veado ) .
come( veado , grama ) .
come( lince , veado ) .
presa(X) :- come(_, X) , animal(X) .
presa(X) :- come(_, X) , herbívoro(X) .
presa(X) :- come(_, X) , carnívoro(X) .
herbivoro(X,y) :- come(_, X) , come(_, y) .
