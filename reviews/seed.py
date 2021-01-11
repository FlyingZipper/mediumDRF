from typing import List
from .models import Product, Category, Compagny, ProductSize, ProductSite, Comment

def seed():
    items = "Sedan, Hatchback, Coupe, Crossover, Micro, Full Size, Compact, Mid Size, Large, Extra Large"
    itemsList = items.split(', ')

    for item in itemsList:
        Category(name=item).save()

    Category.objects.filter()

    products = [
        {
        "Name" : "Mercedes-Benz E-Class",
        "Content" : "Mercedes-Benz began revamping its sedan lineup in 2013, when the current-generation S-Class went on sale. In early 2014, the new C-Class went in production as a shrunken S-Class, with a stylish yet sporty exterior and numerous cues borrowed from Stuttgart’s full-size limo. After more than a year of speculation and months of teasers, the brand-new, tenth-generation E-Class has finally been unveiled at the 2016 Detroit Auto Show.",
        "Category" : "Sedan, Full Size"
        },
        {
        "Name" : "BMW 7 Series",
        "Content" : "The BMW 7 Series is the mid-cycle update of the sixth-generation sedan, first introduced for the 2016 model year. The facelift brings substantial upgrades inside and out, as well as revised engines under the hood. BMW also upgraded the vehicle’s technology package in order to bring it in line with competitors like the Audi A8 and the Mercedes-Benz S-Class.",
        "Category" : "Sedan, Full Size"
        },
        {
        "Name" : "Mercedes-Benz CLA",
        "Content" : "The second-generation Mercedes-Benz CLA was unveiled at 2019 Consumer Electronics Show.The revised four-door coupe replaces the highly successful first-generation CLA, introduced all the way back in 2013.",
        "Category" : "Sedan, Compact"
        },
        {
        "Name" : "Audi A1",
        "Content" : "The second-generation Audi A1 is finally here. Initially launched as a small-sized, three-door, entry-level ‘Sportback’ in 2010, Audi then went on to give it five doors in 2011.",
        "Category" : "Crossover, Compact"
        }
    ]

    for product in products:
        a_product = Product()
        a_product.name = product['Name']
        a_product.content = product['Content']

        a_product.save()

        product_categories = product['Category'].split(', ')
        for product_category in product_categories:
            a_product.category.add(Category.objects.filter(name=product_category).get().id)

        a_product.save()


