"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

#It's an instance of the class Brand. It's also an object.  


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# When we model data we don't want to repeat information. An association table is a table that
# prevents the repetition of data by linking two tables based on their relationship with each other. 
# For example, We wouldn't want a table that combines inventory and customers because there is no direct 
# relationship between and inventory and customers, until a customer makes a purchase. 
# The purchase would be the association table. Association tables usually manage many to many relationships.






# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = "ram_id = Brand.query.filter_by(brand_id='ram').one()"
     "ram_id.name"

# Get all models with the name "Corvette" and the brand_id "che."
q2 = "corv_che = Model.query.filter_by(name='Corvette', brand_id='che').all()"

# Get all models that are older than 1960.
q3 = ">>> older_than_1960 = Model.query.filter(Model.year < 1960).all()"
    ">>> older_than_1960"

# Get all brands that were founded after 1920.
q4 = ">>> founded_after_1920 = Brand.query.filter(Brand.founded > 1920).all()"
     ">>> founded_after_1920"

# Get all models with names that begin with "Cor."
q5 = ">>> begin_with_cor = Model.query.filter(Model.name.like('Cor%')).all()"
     ">>> begin_with_cor"

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = ">>> fd1903_notdisc = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()"
     ">>> fd1903_notdisc"

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = ">>> brand_disc_1950 = Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued != None)).all()"
">>> brand_disc_1950"

# Get any model whose brand_id is not "for."
q8 = ">>> not_for = Model.query.filter(Model.brand_id != 'for').all()"
     ">>> not_for"



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    info_year = Model.query.filter_by(year=Model.year).all()

    for item in info_year:

        print "Model name: %s, \nBrand name: %s, \nBrand headquarters: %s" % (item.name, item.brand.name, item.brand.headquarters)



def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    brand_sum = Brand.query.join(Model).order_by(Model.brand).all()

    for item in brand_sum: 

        print "Brand name: %s ,\nModel name: %s, \nModel year: %s" % (item.name, item.model.name, item.model.year)



def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brand_mystr = Brand.query.filter(Brand.name.ilike('%' + mystr + '%')).all()

    return brand_mystr

def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    models_bet = Model.query.filter(Model.year < end_year, Model.year >= start_year).all()

    return models_bet

