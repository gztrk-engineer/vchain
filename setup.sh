

git add --all
git commit -am "Add py files"

pip3 install pytest==5.1.2
pip3 install -r requirements.txt

python3 -m package.class
python3 -m pytest test/folder