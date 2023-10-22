import asyncio
from scrapli.driver.core import AsyncIOSXEDriver, AsyncIOSXRDriver, AsyncNXOSDriver

csr1000v1 = {
    'host': 'sandbox-iosxe-recomm-1.cisco.com',
    'auth_username': 'developer',
    'auth_password': 'C1sco12345',
    "auth_strict_key": False,
    "transport": "asyncssh",
	  "driver": AsyncIOSXEDriver
}
iosxrv9000 = {
    'host': 'sandbox-iosxr-1.cisco.com',
    'auth_username': 'admin',
    'auth_password': 'C1sco12345',
    "auth_strict_key": False,
    "transport": "asyncssh",
	  "driver": AsyncIOSXRDriver
}
nxosv9000 = {
    'device_type': 'cisco_nxos',
    'host':   'sandbox-nxos-1.cisco.com',
    'username': 'admin',
    'password': 'Admin_1234!',
    'port' : 22,
    'secret': 'Admin_1234!',
     "transport": "asyncssh",
	  "driver": AsyncNXOSDriver
}

async def fetch_data(device):
    driver = device.pop("driver")
    async with driver(**device) as conn:
        responses = await conn.send_commands(["show ip int brief", "show version"])
        return responses

DEVICES = [csr1000v1, nxosv9000]

async def main():
    coroutines = [fetch_data(device) for device in DEVICES]
    results = await asyncio.gather(*coroutines)
    for result in results:
        print(result.result)

if __name__ == "__main__":
    asyncio.run(main())
    # asyncio.get_event_loop().run_until_complete(main())