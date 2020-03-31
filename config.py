import logging

# File path of contacts.xlsx
contacts_filePath   = r"assets/data/contacts.xlsx"

# File path of parameters.xlsx
parameters_filePath = r"assets/data/parameters.xlsx"

# File path of gift.png
imagepath           = r"/home/pushpa/Documents/PY/Python/Rap-Project-New/assets/images/gift.png"

# File path of ss.png under screenshots folder
sspath              = r"/home/pushpa/Documents/PY/Python/Rap-Project-New/assets/images/screenshots/ss.png"

log_filePath = r"logs/"
logname = log_filePath + 'rap-logs.log'

logging.basicConfig(level=logging.INFO,
                   # format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   format='%(asctime)s,%(msecs)d %(levelname)-5s [%(filename)s:%(lineno)d] %(message)s',
                   datefmt='%Y-%m-%d %H:%M:%S',
                   filemode='a+',
                   filename=logname)

logging = logging.getLogger()
