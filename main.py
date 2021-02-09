# from DMCDaemon.Server.serve import run_server
import config
from DMCServiceDaemon.Server.serve import run_server

run_server(config.DAEMON_PORT)