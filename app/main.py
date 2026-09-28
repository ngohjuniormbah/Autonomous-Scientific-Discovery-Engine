from fastapi import FastAPI

app = FastAPI(
    title='SCIENTIA',
    description='Autonomous Scientific Discovery Engine',
    version='0.1.0',
)


@app.get('/health')
def health_check():

    print('we are taking over the world with science and research \n we are the developer of the time')
    return {
        'status': 'ok',
        'service': 'scientia',
        'version': '0.1.0'
    }
