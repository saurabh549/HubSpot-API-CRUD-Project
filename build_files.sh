echo "BUILD START"
apt-get install -y libsqlite3-dev
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD FINISH"