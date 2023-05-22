from uvicorn import run
from page_generator import env
from constants import URLS, RENDER_ARGS


async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/html'],
        ]
    })

    path = scope["path"][1:]  # remove leading /
    try:
        code = env.get_template(URLS[path]).render(RENDER_ARGS)
        await send({
            'type': 'http.response.body',
            'body': code.encode("utf-8")
        })
    except KeyError:
        await send({
            'type': 'http.response.body',
            'body': '404 Not Found ({})'.format(path).encode("utf-8")
        })


if __name__ == '__main__':
    URLS[""] = URLS["index.html"]

    run(app, host="localhost", port=8080)
    print("http://localhost:8080")
