from fastapi import FastAPI
from pet import Pet
import sys
import uvicorn

web_app = FastAPI(title="Pet Demo")

Vasya = Pet('cat', '4')
Rax = Pet('dinosaur', '2')

Vasya.type = 'dog'


@web_app.get('/platform')
def platform():
    return sys.platform


@web_app.get('/pets/')
def pets():
    return 'Pet Vasya is ' + Vasya.type + ' and has ' + Vasya.legs + ' legs and ' + 'Pet Rax is ' + Rax.type + ' and has ' + Rax.legs + ' legs'


@web_app.get('/pets/vasya/pogladit')
def pogladit_via_http():
    return Vasya.pogladit()


if __name__ == '__main__':
    if sys.argv[1] == 'service':
        uvicorn.run(web_app, host='127.0.0.1', port='9999')
    else:
        print('Pet Vasya is ' + Vasya.type + ' and has ' + Vasya.legs)
        print('Pet Rax is ' + Rax.type + ' and has ' + Rax.legs)
