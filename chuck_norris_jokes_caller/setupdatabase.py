from app import db

from app import \
    Joke, \
    JokeVersion

from app import app

from sqlalchemy.exc import SQLAlchemyError


print(" ")

with app.app_context(): 
        
    db.create_all()
    # create all tables defined via models, uding db variable


    # add test data

    try:
        joke_1 =  Joke(1)

        joke_version_1_content = """At various times during the making of Star Wars movies, Chuck Norris was considered for the parts of Han Solo, Luke Skywalker, Darth Vader, the Emperor, Chewbacca, Lando and Yoda. In each case he would be wearing his regular clothes and speak in his Texan drawl."""

        joke_version_1 = JokeVersion(
            id=2,
            joke_id=1,
            content=joke_version_1_content
        )

        db.session.add(joke_1)
        db.session.add(joke_version_1)
        db.session.commit()

    except SQLAlchemyError as e:
        print(f"Managed database error: \n{e}\n")
        db.session.rollback() 

    except Exception as e:
        print(f"An unexpected error occurred: \n{e}\n")
    

    try:
        joke_2 =  Joke(2)


        joke_version_2_content = """as a kid Chuck Norris carried out over 11 sucsessful scuicide bombing missions for the u.s. millitary... the most well known was his attack hiroshima"""

        joke_version_2 = JokeVersion(
            id=4,
            joke_id=2,
            content=joke_version_2_content
        )

        db.session.add(joke_2)
        db.session.add(joke_version_2)
        db.session.commit()

    except SQLAlchemyError as e:
        print(f"Managed database error: \n{e}\n")
        db.session.rollback() 

    except Exception as e:
        print(f"An unexpected error occurred: \n{e}\n")


    try:
        joke_3 =  Joke(3)


        joke_version_3_content = """Many a class 5 Oklahoma tornado were started when Chuck Norris was preparing to lasso a steer."""

        joke_version_3 = JokeVersion(
            id=6,
            joke_id=3,
            content=joke_version_3_content
        )

        db.session.add(joke_3)
        db.session.add(joke_version_3)
        db.session.commit()

    except SQLAlchemyError as e:
        print(f"Managed database error: \n{e}\n")
        db.session.rollback() 

    except Exception as e:
        print(f"An unexpected error occurred: \n{e}\n")



    # created_objects_list = [
    #     joke_1, joke_version_1,
    #     joke_2, joke_version_2,
    #     joke_3, joke_version_3
    # ]

    # db.session.add_all(created_objects_list)

    # db.session.commit()