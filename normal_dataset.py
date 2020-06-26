from imutils import paths
import argparse
import random
import os
import shutil

ap = argparse.ArgumentParser()
ap.add_argument('-n','--normal', required = True,
                help = 'path to the base directory of normal xray dataset')
ap.add_argument('-o','--output', required = True,
                help = 'path to the direcctory where images of normal xray will be stored')
ap.add_argument('-s','--sample',type=int, default=206,
                help='number of samples selected')
args = vars(ap.parse_args())

# grabbing all the training paths from the kaggle chest x-ray dataset
basePath = os.path.sep.join([args['normal'],'train','NORMAL'])
imagePaths = list(paths.list_images(basePath))

random.seed(42)
random.shuffle(imagePaths)
imagePaths = imagePaths[:args['sample']]

for i,imagePath in enumerate(imagePaths):
    filename = imagePath.split(os.path.sep)[-1]
    outputPath = os.path.sep.join([args['output'],filename])

    shutil.copy2(imagePath,outputPath)

