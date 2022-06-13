
# By default, 0: use DOW_30_TICKER (US), 1: use CSI_300_TICKER (CHINA),
# except that users provide explicit tickers
SELECT_REGION = 0

# directory
DATA_SAVE_DIR = "datasets"
TRAINED_MODEL_DIR = "trained_models"
TENSORBOARD_LOG_DIR = "tensorboard_log"
RESULTS_DIR = "results"

# DEFAULT FINRL DATES
#TRAIN_START_DATE = "2014-01-01"
#TRAIN_END_DATE = "2020-07-31"
#TEST_START_DATE = "2020-08-01"
#TEST_END_DATE = "2021-10-01"
#TRADE_START_DATE = "2021-11-01"
#TRADE_END_DATE = "2021-12-01"

#IRON DATES
#TRAIN_START_DATE = "2007-09-18"
#TRAIN_END_DATE = "2014-03-24"
#TEST_START_DATE = "2014-03-25"
#TEST_END_DATE = "2016-10-24"
#TRADE_START_DATE = "2021-10-25"
#TRADE_END_DATE = "2022-11-03"

#SILVER DATES
#TRAIN_START_DATE = "2006-01-16"
#TRAIN_END_DATE = "2012-09-24"
#TEST_START_DATE = "2012-09-25"
#TEST_END_DATE = "2016-07-11"
#TRADE_START_DATE = "2016-07-12"
#TRADE_END_DATE = "2020-11-09"

#LITHIUM DATES
# date format: '%Y-%m-%d'
#TRAIN_START_DATE = "2017-05-16"
#TRAIN_END_DATE = "2021-11-10"
#TEST_START_DATE = "2020-11-11"
#TEST_END_DATE = "2021-06-01"
#TRADE_START_DATE = "2021-11-05"
#TRADE_END_DATE = "2022-05-10"

#COAL DATES
TRAIN_START_DATE = "2008-12-05"
TRAIN_END_DATE = "2013-12-09"
TEST_START_DATE = "2013-12-10"
TEST_END_DATE = "2017-08-14"
TRADE_START_DATE = "2017-08-15"
TRADE_END_DATE = "2021-09-21"

# stockstats technical indicator column names
# check https://pypi.org/project/stockstats/ for different names
INDICATORS = [
    "macd",
    "boll_ub",
    "boll_lb",
    "rsi_30",
    "cci_30",
    "dx_30",
    "close_30_sma",
    "close_60_sma",
]


# Model Parameters ARE ADDED TO MAIN TRADING FILE
A2C_PARAMS = {"n_steps": 5, "ent_coef": 0.01, "learning_rate": 0.0007}
PPO_PARAMS = {
    "n_steps": 2048,
    "ent_coef": 0.01,
    "learning_rate": 0.00025,
    "batch_size": 64,
}
DDPG_PARAMS = {"batch_size": 128, "buffer_size": 50000, "learning_rate": 0.001}
TD3_PARAMS = {"batch_size": 100, "buffer_size": 1000000, "learning_rate": 0.001}
SAC_PARAMS = {
    "batch_size": 64,
    "buffer_size": 100000,
    "learning_rate": 0.0001,
    "learning_starts": 100,
    "ent_coef": "auto_0.1",
}
ERL_PARAMS = {
    "learning_rate": 3e-5,
    "batch_size": 2048,
    "gamma": 0.985,
    "seed": 312,
    "net_dimension": 512,
    "target_step": 5000,
    "eval_gap": 30
}
RLlib_PARAMS = {"lr": 5e-5, "train_batch_size": 500, "gamma": 0.99}


# Possible time zones
TIME_ZONE_SHANGHAI = 'Asia/Shanghai'  # Hang Seng HSI, SSE, CSI
TIME_ZONE_USEASTERN = 'US/Eastern'  # Dow, Nasdaq, SP
TIME_ZONE_PARIS = 'Europe/Paris'  # CAC,
TIME_ZONE_BERLIN = 'Europe/Berlin'  # DAX, TECDAX, MDAX, SDAX
TIME_ZONE_JAKARTA = 'Asia/Jakarta'  # LQ45
TIME_ZONE_SELFDEFINED = 'xxx'  # If neither of the above is your time zone, you should define it, and set USE_TIME_ZONE_SELFDEFINED 1.
USE_TIME_ZONE_SELFDEFINED = 0  # 0 (default) or 1 (use the self defined)

# parameters for data sources
ALPACA_API_KEY = "xxx"  # your ALPACA_API_KEY
ALPACA_API_SECRET = "xxx"  # your ALPACA_API_SECRET
ALPACA_API_BASE_URL = 'https://paper-api.alpaca.markets'  # alpaca url
BINANCE_BASE_URL = 'https://data.binance.vision/'  # binance url




