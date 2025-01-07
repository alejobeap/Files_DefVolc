#!/usr/bin/env python 
# Save r4 format to Defvolc from tif files 
import numpy as np
import os
import matplotlib.pyplot as plt
import sys
from PIL import Image
directorio= os.getcwd()


def load_r4(path, length=None, width=None):
    """ Load a ROI_PAC r4 format file """
    data = np.fromfile(path, dtype='f4')
    #data = np.flipud(data.reshape((length,width))) # N-up, W-left orientation
    return data



def save_r4(name, array, nanvalue=0):
    """save numpy array to ROI_PAC .r4 format """
    array[np.isnan(array)] = 0
    array[array==0] = np.nan
    #array = np.flipud(array)
    #array = np.rot90((np.fliplr(array)),1)
    #array = np.rot90((array),k=1, axes=(1, 2))
    array = array.flatten()
    array = array.astype('f4')
    array.tofile(name)
    #print(name)
    return array


#### Name outputs from UTM files

## Descending file
saveutmD=directorio+'/DESC_utm.r4'

## Ascending file
saveutmA=directorio+'/ASC_utm.r4'

### DEM file
saveutmhgt=directorio+'/hgt_utm.r4'


### Open UTM files Acsending and Descending and change to meter from mm
imA = Image.open(directorio+'/121A_090_UTM.tif')
imarrayA = (np.array(imA))/1000


imd = Image.open(directorio+'/040D_088_UTM.tif')
imarrayd = (np.array(imd))/1000

### Open UTM files Descending

imd = Image.open(directorio+'/DEM.tif')
imarraydem = (np.array(imd))/1000


### Save r4 format Descending
dataUTMD=save_r4(saveutmD, imarrayd, nanvalue=0 )
#print("Ascendente",dataUTMD)

### Save r4 format Ascending

dataUTMA=save_r4(saveutmA, imarrayA, nanvalue=0 )
#print("DEscendente",dataUTMA)

### Save r4 format DEM

dataUTMhgt=save_r4(saveutmhgt, imarraydem, nanvalue=0 )
#print("hgt",dataUTMhgt)

    
#datau=load_r4(utm)

