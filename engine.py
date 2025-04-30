import requests
import argparse
from apikey import APIKEY


def inputs():
    parser = argparse.ArgumentParser(description="parser for recipes ")
    parser.add_argument("--ingredients", nargs="+", type=str,
                        help="ingredients of the recipes")
    parser.add_argument("--num", type=int, default=5,
                        help="the num of recieps you want ")

    args = parser.parse_args()

    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ",".join(args.ingredients),
        "number": args.num,
        "apiKey": APIKEY
    }
    return {"u": url, "p": params}


def showCase(recipes):
    for recipe in recipes:
        print(recipe["title"])


def getRecipes(url, params):
    response = requests.get(url, params=params)
    recipes = response.json()
    showCase(recipes)


getRecipes(inputs()["u"], inputs()["p"])
