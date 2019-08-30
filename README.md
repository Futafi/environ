environ:
==================================================================
.envファイルから何か取得します。


Usage
-------------

    .env
    USER=hoge
    PASS=password
    komoji=oomoji

みたいなファイルがあったとき

    >>> import environ
    >>> environ.PASS
    password
    >>> environ.USER
    hoge
    >>> environ.KOMOJI
    oomoji

みたいな感じです。

keyの小文字は大文字に変わります。

Installation
-------------


    $ pip install https://github.com/Futafi/environ.git


.. _`the repository`: https://github.com/Futafi/environ.git
