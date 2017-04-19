#!/usr/bin/python

import os
from services.BBCPollenService import BBCPollenService

pollenService = BBCPollenService()
pollen = pollenService.getPollenFlag()
print pollen

if (pollen == "Very High" or pollen == "High"):
	pass
	