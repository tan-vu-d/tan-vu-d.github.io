import shutil, os, random
cwd = os.getcwd()
random_folder = ['column1','column2', 'column3', 'column4', 'column5']
image_folder = os.path.join(cwd, 'images\photos')
print(os.path.join(cwd, random.choice(random_folder)))

for image in os.listdir(image_folder):
    shutil.move(os.path.join(image_folder, image), os.path.join(os.path.join(cwd, 'images'), random.choice(random_folder)))
