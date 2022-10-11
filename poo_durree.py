from xml.sax.handler import property_interning_dict


class Duree:
    ''' la classe definissnt une durée caracterisée par:
        - l'heure;
        - la minute
        - la seconde '''
    
    def __init__ (self,heure,minute,seconde):
        # Constucteur de notre classe
        self._heure = heure
        self.minute = minute
        self.seconde = seconde
    def __str__(self):
        # definition d'une methode qui nos objets dele classe durée en une bonne forme 
        # 1) pour le reglage de l'heure dans son format
        if self.seconde >= 60:
            self.minute += self.seconde // 60
            self.seconde = self.seconde % 60
            
        if self.minute >= 60:
            self._heure += self.minute // 60
            self.minute = self.minute % 60
       
        if self._heure >= 24:
            self._heure = self._heure % 24
            
        # 2) pour l'apparution du zeros pour les duree <9 : ex si seconde = 9 ,on va afficher seconde = 09sec        
        if self.seconde <= 9:
            self.seconde = '0' + str(self.seconde)
        else:
            self.seconde = self.seconde       
        if self.minute <= 9:
            self.minute = '0' + str(self.minute)
        else:
            self.minute = self.minute
        if self._heure <= 9:
            self._heure = '0' + str(self._heure)
        else:
            self._heure = self._heure
        return "{0}h {1}min :{2}sec".format(self._heure, self.minute, self.seconde)
        
    def __add__(self,objet_a_ajouter):
       #definition d'une methode qui permet d'additioner deux objet du type Duree 
        nouvelle_duree = Duree (0,0,0)
        nouvelle_duree.seconde += objet_a_ajouter.seconde + self.seconde
        nouvelle_duree.minute += objet_a_ajouter.minute + self.minute
        nouvelle_duree ._heure += objet_a_ajouter._heure + self._heure
        return nouvelle_duree
    
    def __len__(self):
        #methode qui nous retourne la longueur d'un objet de la classe Duree
        return len(dict(self.__dict__).items())
    
    #definition de l'heure comme proprieté
    def _get_heure(self):
        return self._heure
    def _set_heure(self,v):
        print("Attension!!! vous ne pouvez pas modifier l'heure") 
    heure= property(_get_heure,_set_heure)
        


d1 = Duree(6,35,45)
print(d1)
print("\n")

d2 = Duree (26,125,85)
print(d2)
print("\n")

d3 = Duree(12,30,30)
d4 = Duree(12,30,30)
d5 = d4+d3
print(d5)
print("\n")

print(len(d1))
print("\n")

print(len(d1))
print("\n")
