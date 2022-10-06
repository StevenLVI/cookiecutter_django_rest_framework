OPTION=$1
MESSAGE_COLOR='\033[1;34m \033[47m'
MESSAGE_COLOR_2='\033[1;35m \033[47m'
NC='\033[0m'

export ENVIRONMENT=localhost

if [ "$OPTION" == "worker" ]; then
    echo "${MESSAGE_COLOR}=============> Start worker <============${NC}"
    cd .. && celery -A {{cookiecutter.app_name}}.tasks worker -B -l info --heartbeat-interval 5
elif [ "$OPTION" == "stop" ]; then
    echo "${MESSAGE_COLOR}==============> Stop celery <=============${NC}"
    cd .. && celery -A {{cookiecutter.app_name}}.tasks control shutdown
else
    echo "${MESSAGE_COLOR}===========> Option not found <==========${NC}"
fi