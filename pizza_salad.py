# Converted for the recipe https://www.kokaihop.se/recept/pizzasallad-5

import sys

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

def getReceipe(weight, concentration):
    cabbageInGrams = BaseAmount.CABBAGE_IN_GRAMS if weight is None else int(weight)
    concentrationInPercent=int(BaseAmount.VINEGAR_ESSENCE_CONCENTRATION*100)  if concentration is None else int(concentration)
    vinegarEssenceConcentration=concentrationInPercent/100

    proportion= cabbageInGrams/ BaseAmount.CABBAGE_IN_GRAMS
    # Ättiksyra
    aceticAcid=BaseAmount.getAmountOfAceticAcid()*proportion
    vinegarEssenceInGrams=int(aceticAcid/vinegarEssenceConcentration)
    waterInGrams=int(proportion*BaseAmount.VINEGAR_ESSENCE_IN_GRAMS+proportion*BaseAmount.WATER_IN_GRAMS-vinegarEssenceInGrams)
    ingredients={}
    ingredients["vitkål"]=str(cabbageInGrams) + " gr"
    ingredients["salt"]=str(int(proportion*BaseAmount.SALT_IN_ML)) + " ml"
    ingredients["socker"]=str(int(proportion*BaseAmount.SUGER_IN_ML)) + " ml"
    ingredients["ättika " + str(concentrationInPercent) +"% "]=str(vinegarEssenceInGrams) + " gr (= " + str(vinegarEssenceInGrams) + " ml)"
    ingredients["vatten"]=str(waterInGrams)+ " gr vatten"
    ingredients["olja"]=str(int(proportion*BaseAmount.OIL_IN_GRAMS)) + " gr (≈ " + str(int(proportion*BaseAmount.OIL_IN_GRAMS*0.9)) + " ml)"
    ingredients["italienska salladskrydda"]=str(proportion*BaseAmount.ITALIAN_SPICE_MIX_IN_ML) + " ml"
    ingredients["grovmalen svartpeppar"]=str(int(proportion*BaseAmount.PEPPER_IN_PINCHES))+ " nypor"
    
#    amount=Measurements.convert_amount(proportion*BaseAmount.SALT_IN_ML)
#    print(str(amount[0]) + amount[1] + " salt")

    return ingredients
    
if __name__ == "__main__":
    getReceipe()
