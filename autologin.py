from bs4 import BeautifulSoup
import requests, logging, os

#REUSABLE PATHS
site_path = 'https://www.yoursitehere.org'
file_path = os.path.dirname(os.path.realpath(__file__))

#REQUEST NUMBER
log_id = 0
with open(f'{file_path}/history.log') as log:
    for last_line in log:
        pass
if "#" in last_line:
    log_id = last_line.split("#")[1]
    log_id = int(log_id.split("---")[0])
log_id += 1

#LOGIN INFO
logging.basicConfig(filename=f'{file_path}/history.log', format="[%(asctime)s] %(message)s", filemode="a", level=logging.DEBUG)
username = 'youruserhere'
password = 'yourpasshere'
data = {'username': username,'password': password,'remember_me': 'on','login': 'submit'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

with requests.session() as sess:
    logging.info('')
    post_data = sess.get(f'{site_path}')
    html = BeautifulSoup(post_data.text, 'html.parser')

    #Login
    res = sess.post(f'{site_path}/user/account/login', data=data, headers=headers)

    #Check login
    res = sess.get(f'{site_path}/profile/{username}/view')
    try:
        found = BeautifulSoup(res.text, 'html.parser').find(username)
    except:
        logging.warning(f'Your username or password is incorrect')
    else:
        logging.info(f'You have successfully logged in {site_path} as {username}')
    logging.info(f'--- End of Request #{log_id} ---')
