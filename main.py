import asyncio
import httpx

URL = "https://camo.githubusercontent.com/055aed9c60b22cc3e0d0497021691c7f0983535a7770eb1e49b531b1f61c5ec5/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d736179616e74616e636f646578266c6162656c3d50726f66696c65253230766965777326636f6c6f723d306537356236267374796c653d666c6174"

async def curl_forever():
    async with httpx.AsyncClient(timeout=5.0) as client:
        while True:
            try:
                response = await client.get(URL)
                print(f"[✓] Status: {response.status_code}")
            except Exception as e:
                print(f"[✗] Error: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(curl_forever())
