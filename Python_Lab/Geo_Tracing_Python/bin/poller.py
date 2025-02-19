#/usr/bin/env python

# Modules 
import asyncio
import aiohttp
import ssl

# Variables
base_url = 'https://ipapi.co'
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


# User-Defined Functions
async def single_request(session, ip_address):
    url = f'{base_url}/{ip_address}/json'

    async with session.get(url, ssl=ssl_context) as response:
        result = await response.json()

    return result


async def GetIP(ip_addresses):
    tasks = []
    
    async with aiohttp.ClientSession() as session:
        for entry in ip_addresses:
            tasks.append(asyncio.ensure_future(single_request(session=session, ip_address=entry)))

        await asyncio.gather(*tasks)

    results = [entry._result for entry in tasks]
    return results


