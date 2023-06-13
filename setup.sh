

git add --all
git commit -am "Add py files"


echo $VIRTUAL_ENV
deactivate

pip3 install pytest==5.1.2
pip3 install Flask==1.1.1
pip3 install pubnub==4.1.6
pip3 install -r requirements.txt
pip3 freeze

python3 -m package.class
python3 -m pytest tests/folder

git remote show origin