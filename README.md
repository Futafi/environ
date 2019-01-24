environ:
==================================================================
.envファイルから何か取得します。


使い方的な
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

こんな感じの構成で使います。

    src/
    ├ environ/
    │    └ __init__.py
    ├ main.py
    └ .env
    
srcディレクトリでgit clone https://github.com/Futafi/environ.git してください。
その後

    main.py
    >>> import environ

を行ってください。

.envファイルはpythonを実行するフォルダに置きます。

.. _`the repository`: https://github.com/Futafi/environ.git
