from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base ,Categories,  User, CatItems

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes  you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista" ,email="tinnyTim@udacity.com" 
             ,picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for soccer
categorie1 = Categories(name="soccer" ,user_id=1)

session.add(categorie1)
session.commit()

catItem1 = CatItems(title="Ball" 
     ,description="The football dates to ancient times.Sculls pig's bladder and round objects made from animal skins all served to be kicked in competitive often violent and even ritualistic ways." 
                      ,category_id=1 ,user_id=1)

session.add(catItem1)
session.commit()


catItem2 = CatItems( title="Cleats" 
        ,description="Football requires as much traction as possible  the likes of which cannot be gained with ordinary footwear. In addition to providing ankle protection  football cleats have specially grooved soles for utmost traction on the playing field." 
        ,category_id= 1,user_id=1)

session.add(catItem2)
session.commit()






# Menu for Basketball
categorie2 = Categories(name="Basketball" ,user_id=1)

session.add(categorie2)
session.commit()

catItem1 = CatItems(title="Uniform"  
       ,description="The basketball uniform generally consists of a tank top and shorts. You also need socks and some good basketball type sneakers." 
       ,category_id=2,user_id=1)

session.add(catItem1)
session.commit()


catItem2 = CatItems(title="Basket" 
 ,description="The basket is made up of the backboard  rim  and net. The rim is 18 inches in diameter. A regulation backboard is 72 inches wide by 48 inches tall  although you will find backboards can vary in size." 
 ,category_id=2,user_id=1)

session.add(catItem2)
session.commit()


# Menu for Snowboarding
categorie3 = Categories(name="Snowboarding" ,user_id=1)

session.add(categorie3)
session.commit()

catItem1 = CatItems(title="Snowboard"
         ,description="Modern snowboarding began in 1965 when Sherman Poppen  an engineer in Muskegon  Michigan  invented a toy for his daughter by fastening two skis together and attaching a rope to one end so she would have some control as she stood on the board and glided downhill." 
                      ,category_id=3,user_id=1)

session.add(catItem1)
session.commit()



# Menu for baseball
categorie4 = Categories( name="Baseball" ,user_id=1)

session.add(categorie4)
session.commit()

catItem1 = CatItems(title="Bat" 
 ,description="A rounded  solid wooden or hollow aluminum bat. Wooden bats are traditionally made from ash wood  though maple and bamboo is also sometimes used. Aluminum bats are not permitted in professional leagues  but are frequently used in amateur leagues. Composite bats are also available  essentially wooden bats with a metal rod inside. Bamboo bats are also becoming popular." 
                      ,category_id=4,user_id=1)

session.add(catItem1)
session.commit()


catItem2 = CatItems(title="Golve" 
 ,description="Leather gloves worn by players in the field. Long fingers and a webbed 'KKK' between the thumb and first finger allows the fielder to catch the ball more easily." 
                      ,category_id=4,user_id=1)

session.add(catItem2)
session.commit()





# Menu for hockey
categorie5 = Categories( name="Hockey" ,user_id=1)

session.add(categorie5)
session.commit()

catItem1 = CatItems(title="Hockey pants" 
 ,description="These specially designed pants provide cushioning for the thighs and legs and include stiff plastic inserts for impact protection. Most models also provide kidney protection and are somewhat loose fitting for freedom of movement. " 
                      ,category_id=5,user_id=1)

session.add(catItem1)
session.commit()


catItem2 = CatItems(title="Stick" 
 ,description="Originally made of wood (ash  birch and willow)  sticks are now primarily made of carbon fibers and graphite. These materials provide added flexibility and durability. When you're standing in shoes  your stick should come at least to your nose. Always be ready with two sticks as hockey sticks sometimes break. " 
                      ,category_id=5,user_id=1)

session.add(catItem2)
session.commit()





# Menu for frisbee
categorie6 = Categories(name="Frisbee" ,user_id=1)

session.add(categorie6)
session.commit()

catItem1 = CatItems(title="Frisbee" 
 ,description="you can play Ultimate Frisbee with any kind of Frisbee  though it's typically easier and more recommended to play with a slightly heavier version of the classic recreational disc" 
                      ,category_id=6,user_id=1)

session.add(catItem1)
session.commit()


print "added menu items!"