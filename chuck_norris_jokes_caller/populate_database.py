from app import db

from models import \
    Joke, \
    JokeVersion

from app import app

from sqlalchemy.exc import SQLAlchemyError

from time import sleep

DROP_TABLES_MODE = False


print(" ")

with app.app_context(): 

    if DROP_TABLES_MODE:

        db.drop_all() 

        # Joke.__table__.drop(db.engine)
        # JokeVersion.__table__.drop(db.engine)

        
    db.create_all()
    # create all tables defined via models, uding db variable


    # add test data
    ##################

    try:
        joke_1 =  Joke(1)
        db.session.add(joke_1)
        db.session.commit()

    except SQLAlchemyError as e:
        print(f"Managed database error: \n{e}\n")
        db.session.rollback() 

    except Exception as e:
        print(f"An unexpected error occurred: \n{e}\n")


    sleep(1)


    try:
        joke_version_1_1_content = """At various times during the making of Star Wars movies, Chuck Norris was considered for the parts of Han Solo, Luke Skywalker, Darth Vader, the Emperor, Chewbacca, Lando and Yoda. In each case he would be wearing his regular clothes and speak in his Texan drawl."""

        joke_version_1_1 = JokeVersion(
            id=1,
            joke_id=1,
            content=joke_version_1_1_content
        )

        db.session.add(joke_version_1_1)
        db.session.commit()

    except SQLAlchemyError as e:
        print(f"Managed database error: \n{e}\n")
        db.session.rollback() 

    except Exception as e:
        print(f"An unexpected error occurred: \n{e}\n")


    sleep(1)

    try:

        joke_version_2_1_content = """ V2 At various times during the making of."""

        joke_version_2_1 = JokeVersion(
            id=2,
            joke_id=1,
            content=joke_version_2_1_content
        )

        db.session.add(joke_version_2_1)
        db.session.commit()

    except SQLAlchemyError as e:
        print(f"Managed database error: \n{e}\n")
        db.session.rollback() 

    except Exception as e:
        print(f"An unexpected error occurred: \n{e}\n")


    sleep(1)

    try:
        joke_2 =  Joke(2)
        db.session.add(joke_2)
        db.session.commit()

    except SQLAlchemyError as e:
        print(f"Managed database error: \n{e}\n")
        db.session.rollback() 

    except Exception as e:
        print(f"An unexpected error occurred: \n{e}\n")


    sleep(1)

    try:

        joke_version_3_2_content = """as a kid Chuck Norris carried out over 11 sucsessful scuicide bombing missions for the u.s. millitary... the most well known was his attack hiroshima"""

        joke_version_3_2 = JokeVersion(
            id=3,
            joke_id=2,
            content=joke_version_3_2_content
        )

        db.session.add(joke_version_3_2)
        db.session.commit()

    except SQLAlchemyError as e:
        print(f"Managed database error: \n{e}\n")
        db.session.rollback() 

    except Exception as e:
        print(f"An unexpected error occurred: \n{e}\n")


    sleep(1)

    try:
        joke_version_4_2_content = """ v2 as a kid Chuck Norris carried out over 11 sucsessful """

        joke_version_4_2 = JokeVersion(
            id=4,
            joke_id=2,
            content=joke_version_4_2_content
        )

        db.session.add(joke_version_4_2)
        db.session.commit()

    except SQLAlchemyError as e:
        print(f"Managed database error: \n{e}\n")
        db.session.rollback() 

    except Exception as e:
        print(f"An unexpected error occurred: \n{e}\n")


    sleep(1)

    try:
        joke_3 =  Joke(3)
        db.session.add(joke_3)
        db.session.commit()

    except SQLAlchemyError as e:
        print(f"Managed database error: \n{e}\n")
        db.session.rollback() 

    except Exception as e:
        print(f"An unexpected error occurred: \n{e}\n")


    sleep(1)

    try:

        joke_version_5_3_content = """Many a class 5 Oklahoma tornado were started when Chuck Norris was preparing to lasso a steer."""

        joke_version_5_3 = JokeVersion(
            id=5,
            joke_id=3,
            content=joke_version_5_3_content
        )

        db.session.add(joke_version_5_3)
        db.session.commit()

    except SQLAlchemyError as e:
        print(f"Managed database error: \n{e}\n")
        db.session.rollback() 

    except Exception as e:
        print(f"An unexpected error occurred: \n{e}\n")


    sleep(1)

    try:
        joke_version_3_2_content = """ v2 Chuck Norris Many a class 5 Oklahoma tornado were started """

        joke_version_3_2 = JokeVersion(
            id=6,
            joke_id=3,
            content=joke_version_3_2_content
        )

        db.session.add(joke_version_3_2)
        db.session.commit()

    except SQLAlchemyError as e:
        print(f"Managed database error: \n{e}\n")
        db.session.rollback() 

    except Exception as e:
        print(f"An unexpected error occurred: \n{e}\n")



    # created_objects_list = [
    #     joke_1, joke_version_1_1,
    #     joke_2, joke_version_3_2,
    #     joke_3, joke_version_5_3
    # ]

    # db.session.add_all(created_objects_list)

    # db.session.commit()


    # test model methods
    ##########################
