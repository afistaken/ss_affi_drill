from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

import requests

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=300)
user_agents = user_agent_rotator.get_user_agents()

for element in user_agents:

    url = 'https://steelseries.com/gg/sonar/download'

    headers = {
        #referer: Your affi download URL
        "referer": "",
        "user-agent": element["user_agent"]
    }

    response = requests.get(url=url,headers=headers)

resd = response.content.decode()
