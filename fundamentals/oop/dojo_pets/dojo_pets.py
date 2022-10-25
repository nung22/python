import ninja
import pet

ninja_1 = ninja.Ninja("Naruto","Uzumaki",1,"Ramen",pet.Toad())
ninja_2 = ninja.Ninja("Sakura","Haruno",5,"Cookies",pet.Slug())
ninja_3 = ninja.Ninja("Sasuke","Uchiha",3,"Eggs",pet.Snake())

ninja_1.feed().walk().bathe().feed()
ninja_2.feed().walk().bathe()
ninja_3.feed().walk().bathe().feed().feed().feed()