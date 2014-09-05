pymarketo
==============

pymarketo is a python query client that wraps the Marketo SOAP API. For sending data to Marketo.  Largely based on segment.io's library; however, it is different in that it is meant to be used more for creating integrations between marketo and other things like an FTP.

## Get Started

```
pip install git+http://github.com/kr4ng/pymarketo
```

```python
import pymarketo
from pymarketo import mktoclasses
client = pymarketo.Client(soap_endpoint='https://na-q.marketo.com/soap/mktows/2_0',
                        user_id='bigcorp1_461839624B16E06BA2D663',
                        encryption_key='899756834129871744AAEE88DDCC77CDEEDEC1AAAD66')
```

## Sync Custom Objects

This generates the XML and syncs a custom object to Marketo.

```python
mktoCustomObject=mktoclasses.MktoCustomObject(client)
'''
Then you would use the MktoCustomObject methods to finish this example
'''
```

## License

```
WWWWWW||WWWWWW
 W W W||W W W
      ||
    ( OO )__________
     /  |           \
    /o o|    MIT     \
    \___/||_||__||_|| *
         || ||  || ||
        _||_|| _||_||
       (__|__|(__|__|
```

(The MIT License)

Copyright (c) 2014 rightstack.io Inc. <ben@rightstack.io>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.