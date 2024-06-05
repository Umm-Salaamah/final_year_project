import requests
from . import headers as HEADERS

def scan_headers(url):
    try:
        # Send a GET request to the target URL
        response = requests.get(url)
        
        # Extract headers from the response
        headers = response.headers

        # Check if each security header is present in the response
        results = {}
        for (header, description) in HEADERS.HEADERS.items():

            """
            Uncomment the block below for the CLI version of the script
            """
            
            # if header in headers:
            #     print(f'{header} is enabled for URL: {url}')
            # else:
            #     print(f'{header} is disabled for URL: {url}')
            #     print('<=========================>\n')
            #     print(f'Definition\n---------------- \n{description["definition"]}')
            #     print(f'Solution\n---------------- \n{description["fix"]}')
            #     print(f'Solution Steps\n----------------\n')
            #     for index, step in enumerate(description['fix-steps'], start=1):
            #         print(f'{index}. {step}')
            #     print('<=========================>\n')

            """
            Uncomment the block below for the JSON version of the script
            """
            if header in headers:
                results[header] = {'status': 'Present', 'value': headers[header]}
            else:
                results[header] = {'status': 'Missing', 'suggestion': description}
        
        return results
    except requests.RequestException as e:
        return {'error': str(e)}
