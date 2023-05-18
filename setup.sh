

git add --all
git commit -am "Add py files"

python3 -m venv venv
source venv/bin/activate
echo $VIRTUAL_ENV
deactivate

pip3 install pytest==5.1.2
pip3 install -r requirements.txt

python3 -m package.class
python3 -m pytest tests/folder

git remote show origin