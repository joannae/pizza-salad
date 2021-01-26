# Converted for the recipe https://www.kokaihop.se/recept/pizzasallad-5

# Running with flask
# $ python3 -m venv pizza_env
# $ source pizza_env/bin/activate   
# $ export FLASK_APP=pizza-salad
# $ export FLASK_ENV=development
# $ flask run
# example URL for running with flask locally: http://127.0.0.1:5000/?weight=1000&concentration=0.07

import sys
from flask import Flask
from flask import request

app = Flask(__name__)

class BaseAmount:
   CABBAGE_IN_GRAMS=100
   SALT_IN_ML=5
   SUGER_IN_ML=15
   VINEGAR_ESSENCE_IN_GRAMS=15
   VINEGAR_ESSENCE_CONCENTRATION=0.12
   WATER_IN_GRAMS=285
   OIL_IN_GRAMS=8
   ITALIAN_SPICE_MIX_IN_ML=0.5
   PEPPER_IN_PINCHES=1

   def getAmountOfAceticAcid():
      return BaseAmount.VINEGAR_ESSENCE_IN_GRAMS*BaseAmount.VINEGAR_ESSENCE_CONCENTRATION
   

class Measurements:
    TSK=(5, "tsk")
    MSK=(15, "msk")
    def convert_amount(amountInMl):
      if(amountInMl<5):
         return (amountInMl, "krm")
      if(amountInMl<15):
          return (amountInMl/Measurements.TSK[1], Measurements.TSK[2])
      return (amountInMl/Measurements.MSK[0], Measurements.MSK[1])

@app.route('/')
def main():
    weight = request.args.get('weight')
    concentration = request.args.get('concentration')
    cabbageInGrams=int(weight)
    vinegarEssenceConcentration=float(concentration)

    proportion= cabbageInGrams/ BaseAmount.CABBAGE_IN_GRAMS
    # Ättiksyra
    aceticAcid=BaseAmount.getAmountOfAceticAcid()*proportion
    vinegarEssenceInGrams=int(aceticAcid/vinegarEssenceConcentration)
    waterInGrams=int(proportion*BaseAmount.VINEGAR_ESSENCE_IN_GRAMS+proportion*BaseAmount.WATER_IN_GRAMS-vinegarEssenceInGrams)
    
    print(str(proportion*BaseAmount.SALT_IN_ML) + " ml salt")
#    amount=Measurements.convert_amount(proportion*BaseAmount.SALT_IN_ML)
#    print(str(amount[0]) + amount[1] + " salt")
    print(str(proportion*BaseAmount.SUGER_IN_ML) + " ml socker")
    print(str(vinegarEssenceInGrams) + " gr ättika")
    print(str(waterInGrams) + " gr vatten")
    print(str(proportion*BaseAmount.OIL_IN_GRAMS) + " gr olja")
    print(str(proportion*BaseAmount.ITALIAN_SPICE_MIX_IN_ML) + " ml italiensk kryddmix") 
    print(str(proportion*BaseAmount.PEPPER_IN_PINCHES) + " nypor peppar")
    return ''
    
if __name__ == "__main__":
    main()
