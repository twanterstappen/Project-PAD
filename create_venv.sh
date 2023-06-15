## To run start git bash from here and type ./create_venv.sh
#create a venv
py -m venv venv

# Install requirements
venv/Scripts/python -m pip install -r ./central-website/requirements.txt

# Upgrade pip
venv/Scripts/python -m pip install --upgrade pip