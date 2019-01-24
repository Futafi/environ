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

Installation
-------------

利用したいディレクトリでgit clone https://github.com/Futafi/environ.git してください。
その後

    >>> import environ

を行ってください。

.envファイルはpythonを実行するフォルダに置きます。

.. _`the repository`: https://github.com/Futafi/environ.git
